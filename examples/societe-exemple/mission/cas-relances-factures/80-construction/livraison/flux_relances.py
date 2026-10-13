"""Flux des relances de factures échues : maquette exécutable de l'option 4.

Cette maquette reproduit sur des fichiers le comportement de `60-specification.md` (rubriques 4, 7, 8, 9
et 13) : elle lit une extraction déposée, prépare des brouillons dans une boîte de messagerie simulée et
ne peut rien envoyer. La plateforme sans code retenue en `40-solutions.md` reste la cible ; ce programme
est la maquette exécutable de sa logique, et `80-construction.md` le dit.

Bibliothèque standard seulement. Mode simulation seul : le passage au réel est une action de
`90-mise-en-service`, il n'existe pas dans l'essai. Aucun secret : seuls les noms des trois secrets de
la spécification (rubrique 9) figurent ici.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import sys
import time
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path

VERSION = "1.1"

# Noms des secrets (60 §9). Les valeurs vivent dans le coffre de la plateforme, jamais ici.
NOMS_DES_SECRETS = ("accès-listes", "accès-messagerie", "accès-alerte")

SERVICE_MESSAGERIE = "service-messagerie"
SERVICE_ALERTE = "service-alerte"
GESTIONNAIRE = "gestionnaire clients"
COMPTABLE = "comptable"
RESPONSABLE_FINANCIER = "responsable financier"
SUPPORT = "responsable du support"

DOSSIER_NORMAL = "Relances du lundi"
DOSSIER_COMPTES_CLES = "Comptes clés à valider"
DOSSIER_ENVOYES = "Envoyés"

ENTETES_EXTRACTION = [
    "numero_facture", "id_client", "nom_contact", "adresse_courriel",
    "montant_ht", "date_echeance", "etat_paiement",
]
ETATS_PAIEMENT = ("rapprochée", "non rapprochée")
REPRISES_PAR_DEFAUT = (60, 300, 900)
DUREE_VERROU_PERIME = 1800  # secondes : la durée totale des reprises (60 §7)


# --------------------------------------------------------------------------------------------------
# Erreurs
# --------------------------------------------------------------------------------------------------
class ErreurPassagere(Exception):
    """Service momentanément indisponible : on reprend (60 §7)."""


class ServiceIndisponible(ErreurPassagere):
    """Reprises épuisées : file des échecs et alerte."""


class ErreurDefinitive(Exception):
    """Donnée invalide, droit refusé, élément introuvable : aucune reprise."""


class DroitRefuse(ErreurDefinitive):
    """Le compte n'a pas le droit demandé."""


class Refus(ErreurDefinitive):
    """Cas de refus voulu (60 §4) : le motif est lisible, rien n'est écrit chez un tiers."""


class ChangementNonApprouve(Refus):
    """Règles ou modèles modifiés hors de la version approuvée par le responsable financier (60 §4, T-22)."""


# --------------------------------------------------------------------------------------------------
# Horloge
# --------------------------------------------------------------------------------------------------
class Horloge:
    def maintenant(self) -> datetime:
        raise NotImplementedError

    def dormir(self, secondes: float) -> None:
        raise NotImplementedError


class HorlogeReelle(Horloge):
    def maintenant(self) -> datetime:
        return datetime.now().replace(microsecond=0)

    def dormir(self, secondes: float) -> None:
        time.sleep(secondes)


class HorlogeDeTest(Horloge):
    """Horloge qui n'attend jamais : `dormir` avance simplement l'heure."""

    def __init__(self, depart: datetime):
        self.t = depart
        self.pauses: list[float] = []

    def maintenant(self) -> datetime:
        return self.t

    def avancer(self, **kw) -> None:
        self.t += timedelta(**kw)

    def dormir(self, secondes: float) -> None:
        self.pauses.append(secondes)
        self.t += timedelta(seconds=secondes)


def iso(t: datetime) -> str:
    return t.replace(microsecond=0).isoformat(sep=" ")


# --------------------------------------------------------------------------------------------------
# Calendrier
# --------------------------------------------------------------------------------------------------
def est_ouvre(jour: date, feries) -> bool:
    return jour.weekday() < 5 and jour not in feries


def jours_ouvres_entre(debut: date, fin: date, feries) -> int:
    """Jours ouvrés de l'intervalle ]debut, fin] : début exclu, fin incluse."""
    n, jour = 0, debut
    while jour < fin:
        jour += timedelta(days=1)
        if est_ouvre(jour, feries):
            n += 1
    return n


def niveau_atteint(age: int, delais) -> int:
    niveau = 0
    for i, delai in enumerate(delais, start=1):
        if age >= delai:
            niveau = i
    return niveau


def sha256_lf(octets: bytes) -> str:
    return hashlib.sha256(octets.replace(b"\r\n", b"\n")).hexdigest()


# --------------------------------------------------------------------------------------------------
# Règles (60 §6 : données datées, lues au début de chaque exécution)
# --------------------------------------------------------------------------------------------------
@dataclass(frozen=True)
class Regles:
    version: str
    date_version: str
    delais: tuple
    limite_age: int
    plafond: int
    fraicheur: int
    feries: frozenset
    reprises: tuple
    duree_max: int
    variation: float
    delai_alerte: int
    silence_heure: str
    litiges_jours: int
    age_liste_vide: int
    libelles: dict
    modeles: dict
    empreinte_regles: str
    empreinte_modeles: str


def charger_regles(classeur, avec_modeles: bool = True) -> Regles:
    octets = classeur.lire_octets("pilotage", "regles.csv")
    param = {}
    for ligne in csv.DictReader(octets.decode("utf-8").splitlines()):
        param[ligne["parametre"].strip()] = ligne["valeur"].strip()

    def exiger(nom: str) -> str:
        if not param.get(nom):
            raise ErreurDefinitive(f"règle absente ou sans valeur : {nom}")
        return param[nom]

    try:
        delais = tuple(int(exiger(f"delai_niveau_{n}")) for n in (1, 2, 3))
        feries = frozenset(date.fromisoformat(x) for x in exiger("jours_feries").split(";") if x)
        reprises = tuple(int(x) for x in exiger("reprises_secondes").split(";"))
        regles_valeurs = dict(
            version=exiger("version"),
            date_version=exiger("date_version"),
            delais=delais,
            limite_age=int(exiger("limite_age_jours")),
            plafond=int(exiger("plafond_propositions")),
            fraicheur=int(exiger("fraicheur_rapprochement_jours_ouvres")),
            feries=feries,
            reprises=reprises,
            duree_max=int(exiger("duree_max_reprises_secondes")),
            variation=float(exiger("variation_reprises")),
            delai_alerte=int(exiger("delai_alerte_secondes")),
            silence_heure=exiger("silence_heure"),
            litiges_jours=int(exiger("litiges_sans_maj_jours_ouvres")),
            age_liste_vide=int(exiger("liste_vide_age_jours")),
        )
    except ValueError as e:
        raise ErreurDefinitive(f"règle illisible : {e}") from e
    libelles, modeles, morceaux = {}, {}, []
    for n in (1, 2, 3):
        libelles[n] = exiger(f"libelle_niveau_{n}")
        if not avec_modeles:
            continue
        try:
            brut = classeur.lire_octets("pilotage", f"modeles/niveau-{n}.txt")
        except ErreurPassagere as e:
            raise ErreurDefinitive(f"modèle introuvable : niveau {n}") from e
        modeles[n] = brut.decode("utf-8")
        morceaux.append(brut.replace(b"\r\n", b"\n"))
    return Regles(libelles=libelles, modeles=modeles, empreinte_regles=sha256_lf(octets),
                  empreinte_modeles=hashlib.sha256(b"".join(morceaux)).hexdigest(), **regles_valeurs)


def approuver(espace: Path, version: str, jour: str) -> None:
    """Acte du responsable financier, hors du flux : note l'empreinte des règles et des modèles approuvés."""
    pilotage = Path(espace) / "pilotage"
    octets = (pilotage / "regles.csv").read_bytes()
    morceaux = [p.read_bytes().replace(b"\r\n", b"\n") for p in sorted((pilotage / "modeles").glob("niveau-*.txt"))]
    with open(pilotage / "approbation.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["version", "date", "empreinte_regles", "empreinte_modeles"])
        w.writerow([version, jour, sha256_lf(octets), hashlib.sha256(b"".join(morceaux)).hexdigest()])


# --------------------------------------------------------------------------------------------------
# Données du flux
# --------------------------------------------------------------------------------------------------
@dataclass
class Proposition:
    numero: str
    niveau: int
    id_client: str
    compte_cle: bool
    ligne: dict

    @property
    def cle(self) -> str:
        return f"{self.numero}|{self.niveau}"


@dataclass
class Resultat:
    statut: str = "ok"  # ok · refus · echec · suspendu · volume · verrou
    compteurs: Counter = field(default_factory=Counter)
    propositions: list = field(default_factory=list)
    ecartees: list = field(default_factory=list)  # (numero, niveau, motif)
    a_la_main: list = field(default_factory=list)  # (numero, motif)
    messages: list = field(default_factory=list)


def decimal_ou_none(texte: str):
    try:
        valeur = Decimal((texte or "").strip().replace(",", "."))
    except InvalidOperation:
        return None
    return valeur if valeur > 0 else None


def format_montant(valeur: Decimal) -> str:
    return f"{valeur:.2f}".replace(".", ",")


def format_date_fr(jour: date) -> str:
    return jour.strftime("%d/%m/%Y")


# --------------------------------------------------------------------------------------------------
# Le flux
# --------------------------------------------------------------------------------------------------
class Flux:
    def __init__(self, espace, classeur, boite, horloge: Horloge):
        self.espace = Path(espace)
        self.classeur = classeur
        self.boite = boite
        self.horloge = horloge
        self.regles: Regles | None = None
        self.id_execution = ""
        self._reprises = REPRISES_PAR_DEFAUT
        self._variation = 0.1
        self._duree_max = DUREE_VERROU_PERIME
        self._tampon: list = []  # lignes du journal en attente d'écriture groupée (une opération par lot)
        self._props: dict = {}  # onglet « propositions » lu une fois par exécution
        self._brouillons: dict = {}  # brouillons déjà présents dans la boîte, par identifiant de relance
        self._envoyes: set | None = None  # objets du dossier « Envoyés », lus au besoin une fois par exécution

    # ---- trace ----------------------------------------------------------------------------------
    def _journal(self, cle: str, etape: str, resultat: str, detail: str = "") -> None:
        """Une ligne par élément et par étape (60 §10) : ni nom ni adresse."""
        ligne = {
            "horodatage": iso(self.horloge.maintenant()), "execution": self.id_execution, "cle": cle,
            "etape": etape, "resultat": resultat, "detail": detail, "version_flux": VERSION,
            "version_regles": self.regles.version if self.regles else "",
        }
        self.classeur.trace_plateforme(ligne)  # l'historique d'exécution de la plateforme, hors classeur
        self._tampon.append(ligne)

    def _vider_journal(self) -> None:
        """Écrit le tampon en un seul lot. S2 coupé : les lignes restent dans l'historique de la plateforme."""
        if not self._tampon:
            return
        try:
            self.classeur.ajouter_lot("journal", self._tampon)
            self._tampon = []
        except ErreurPassagere:
            pass

    def _echec(self, cle: str, etape: str, erreur: str) -> None:
        try:
            self.classeur.ecrire_ligne("echecs", ("cle",), {
                "cle": cle, "etape": etape, "erreur": erreur, "heure": iso(self.horloge.maintenant()),
                "execution": self.id_execution, "rejouer": "non", "etat": "ouvert",
            })
        except ErreurPassagere:
            pass
        self._journal(cle, etape, "échec", erreur)

    def _alerter(self, roles, code: str, etape: str, cle: str, erreur: str) -> None:
        corps = f"étape : {etape}\nclé : {cle}\nerreur : {erreur}\nheure : {iso(self.horloge.maintenant())}"
        for role in roles:
            try:
                self.boite.poster_message(SERVICE_ALERTE, role, f"[alerte] {code}", corps)
            except ErreurPassagere:
                self.classeur.trace_plateforme({"horodatage": iso(self.horloge.maintenant()), "cle": cle,
                                                "etape": etape, "resultat": "alerte non partie", "detail": code})
        self._journal(cle, etape, "alerte", code)

    # ---- reprises (60 §7) -----------------------------------------------------------------------
    def _avec_reprises(self, fonction, cle: str = "", etape: str = ""):
        attentes = [0] + [self._varier(s, cle, i) for i, s in enumerate(self._reprises)]
        derniere = None
        ecoule = 0.0
        for essai, attente in enumerate(attentes, start=1):
            if attente:
                self.horloge.dormir(attente)
                ecoule += attente
            try:
                return fonction()
            except ErreurPassagere as e:
                derniere = e
                self._journal(cle, etape, "erreur passagère", f"tentative {essai}")
                if ecoule > self._duree_max:
                    break
        raise ServiceIndisponible(str(derniere))

    def _varier(self, secondes: int, cle: str, rang: int) -> float:
        h = int(hashlib.sha256(f"{cle}/{rang}".encode()).hexdigest()[:4], 16) / 0xFFFF  # 0..1, déterministe
        return round(secondes * (1 + self._variation * (2 * h - 1)), 1)

    # ---- verrou et interrupteur -----------------------------------------------------------------
    def _commande(self) -> dict:
        """L'onglet « commande » : la case « Suspendre » et le réglage de l'étape 8. Une opération."""
        lignes = self._avec_reprises(lambda: self.classeur.lire("dispositif", "commande"),
                                     cle="commande", etape="interrupteur")
        return {l["parametre"].strip(): l["valeur"].strip().lower() for l in lignes}

    def _suspendu(self) -> bool:
        return self._commande().get("suspendre") == "oui"

    # ---- exécution ------------------------------------------------------------------------------
    def executer(self, cles_filtre=None) -> Resultat:
        """Le lundi : étapes 1 à 6 de 60 §4. `cles_filtre` rejoue seulement ces clés (file des échecs)."""
        maintenant = self.horloge.maintenant()
        self.id_execution = maintenant.strftime("%Y-%m-%d-%H%M%S")
        res = Resultat()
        if not self.classeur.prendre_verrou(maintenant, self._duree_max):
            self._journal("", "0", "refus", "une exécution est déjà en cours")
            self._vider_journal()
            res.statut = "verrou"
            res.messages.append("une exécution est déjà en cours")
            return res
        try:
            self._executer(maintenant.date(), res, cles_filtre)
        finally:
            self._vider_journal()
            self.classeur.liberer_verrou()
        return res

    def _executer(self, jour: date, res: Resultat, cles_filtre) -> None:
        self._journal("", "0", "début", "")
        self._vider_journal()  # la trace de début sert l'alerte sur silence (60 §10) : elle part tout de suite
        try:
            self._derouler(jour, res, cles_filtre)
        except ChangementNonApprouve as e:
            res.statut = "refus"
            self._echec("approbation", "0", str(e))
            self._alerter([GESTIONNAIRE, RESPONSABLE_FINANCIER], str(e), "0", "approbation", str(e))
        except Refus as e:
            res.statut = "refus"
            self._echec("extraction", "1", str(e))
            self._alerter([GESTIONNAIRE], str(e), "1", "extraction", str(e))
        except ErreurDefinitive as e:
            res.statut = "echec"
            self._echec("execution", "?", str(e))
            self._alerter([GESTIONNAIRE], "erreur définitive", "?", "execution", str(e))
        except ServiceIndisponible as e:
            res.statut = "echec"
            self._echec("execution", "?", f"service indisponible : {e}")
            self._alerter([GESTIONNAIRE, RESPONSABLE_FINANCIER], "service indisponible", "?", "execution", str(e))
        self._compteurs(jour, res)
        self._journal("", "fin", res.statut, "")

    def _derouler(self, jour: date, res: Resultat, cles_filtre) -> None:
        self.regles = self._avec_reprises(lambda: charger_regles(self.classeur), etape="0")
        self._reprises, self._variation, self._duree_max = (
            self.regles.reprises, self.regles.variation, self.regles.duree_max)
        self._verifier_approbation()
        if self._suspendu():
            self._suspendre(res)
            return
        lignes = self._etape1(jour)
        donnees = self._etape2(jour)
        evaluation = self._etape3_et_4(jour, lignes, donnees, res)
        self._vider_journal()
        if cles_filtre is not None:
            evaluation = [p for p in evaluation if p.cle in cles_filtre]
        if len(evaluation) > self.regles.plafond:
            res.statut = "volume"
            self._echec("volume", "5", f"{len(evaluation)} propositions, plafond {self.regles.plafond}")
            self._alerter([GESTIONNAIRE, RESPONSABLE_FINANCIER], "volume anormal", "5", "volume",
                          f"{len(evaluation)} propositions au-delà du plafond de {self.regles.plafond}")
            return
        if self._suspendu():
            self._suspendre(res)
            return
        try:
            self._etape5(evaluation, res)
        finally:
            self._vider_journal()
        if res.statut == "ok":
            if self._suspendu():
                self._suspendre(res)
                return
            self._etape6(res)

    def _suspendre(self, res: Resultat) -> None:
        res.statut = "suspendu"
        self._journal("", "0", "suspendu", "la case « Suspendre » est cochée")
        self._retirer_brouillons("interrupteur")

    def _verifier_approbation(self) -> None:
        lignes = self._avec_reprises(lambda: self.classeur.lire("pilotage", "approbation"),
                                     cle="approbation", etape="0")
        for ligne in lignes:
            if (ligne["version"] == self.regles.version
                    and ligne["empreinte_regles"] == self.regles.empreinte_regles
                    and ligne["empreinte_modeles"] == self.regles.empreinte_modeles):
                return
        raise ChangementNonApprouve("règles ou modèles modifiés hors de la version approuvée")

    # ---- étape 1 --------------------------------------------------------------------------------
    def _etape1(self, jour: date) -> list:
        nom = f"extraction-{jour.isoformat()}.csv"
        entetes, lignes = self._avec_reprises(lambda: self.classeur.lire_depot(nom), cle=nom, etape="1")
        manquantes = [c for c in ENTETES_EXTRACTION if c not in entetes]
        if manquantes:
            raise ErreurDefinitive("extraction illisible : colonne absente " + ", ".join(manquantes))
        if not self.classeur.existe_depot("rapprochement.csv"):
            raise Refus("date du rapprochement absente")
        _, rapp = self.classeur.lire_depot("rapprochement.csv")
        try:
            dernier = date.fromisoformat(rapp[0]["date_rapprochement"].strip())
        except (IndexError, KeyError, ValueError):
            raise Refus("date du rapprochement absente") from None
        if jours_ouvres_entre(dernier, jour, self.regles.feries) > self.regles.fraicheur:
            raise Refus("rapprochement trop ancien")
        self._journal("extraction", "1", "ok", f"{len(lignes)} lignes")
        return lignes

    # ---- étape 2 --------------------------------------------------------------------------------
    def _etape2(self, jour: date) -> dict:
        def lire(zone, onglet):
            return self._avec_reprises(lambda: self.classeur.lire(zone, onglet), cle=onglet, etape="2")

        donnees = {
            "litiges": {l["numero_facture"].strip() for l in lire("pilotage", "litiges")},
            "comptes_cles": {l["id_client"].strip() for l in lire("pilotage", "comptes-cles")},
            "historique": lire("dispositif", "historique"),
            "maj_litiges": [l["date"] for l in lire("pilotage", "litiges-maj")],
        }
        self._controler_maj_litiges(jour, donnees["maj_litiges"])
        self._journal("pilotage", "2", "ok", "")
        return donnees

    def _controler_maj_litiges(self, jour: date, dates: list) -> None:
        dernieres = [date.fromisoformat(d) for d in dates if d]
        if not dernieres or jours_ouvres_entre(max(dernieres), jour, self.regles.feries) > self.regles.litiges_jours:
            self._alerter([RESPONSABLE_FINANCIER, SUPPORT], "liste des litiges sans mise à jour", "2", "litiges",
                          f"aucune mise à jour depuis plus de {self.regles.litiges_jours} jours ouvrés")

    # ---- étapes 3 et 4 --------------------------------------------------------------------------
    def _problemes_ligne(self, ligne: dict) -> list:
        problemes = []
        if not (ligne.get("numero_facture") or "").strip():
            problemes.append("numéro de facture vide")
        if not (ligne.get("id_client") or "").strip():
            problemes.append("identifiant du client vide")
        if not (ligne.get("nom_contact") or "").strip():
            problemes.append("nom du contact vide")
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", (ligne.get("adresse_courriel") or "").strip()):
            problemes.append("adresse non plausible")
        if decimal_ou_none(ligne.get("montant_ht", "")) is None:
            problemes.append("montant invalide")
        if not (ligne.get("date_echeance") or "").strip():
            problemes.append("échéance vide")
        else:
            try:
                date.fromisoformat(ligne["date_echeance"].strip())
            except ValueError:
                problemes.append("échéance illisible")
        if (ligne.get("etat_paiement") or "").strip() not in ETATS_PAIEMENT:
            problemes.append("état de paiement inconnu")
        return problemes

    def _etape3_et_4(self, jour: date, lignes: list, donnees: dict, res: Resultat) -> list:
        regles = self.regles
        compte = Counter(l["numero_facture"].strip() for l in lignes)
        derniers = {}
        for h in donnees["historique"]:
            try:
                n = int(h["niveau"])
            except (ValueError, KeyError):
                continue
            derniers[h["numero_facture"].strip()] = max(n, derniers.get(h["numero_facture"].strip(), 0))
        propositions = []
        for ligne in sorted(lignes, key=lambda l: l["numero_facture"]):
            numero = ligne["numero_facture"].strip()
            problemes = self._problemes_ligne(ligne)
            if numero and compte[numero] > 1:
                problemes.append("numéro en double")
            if problemes:
                res.a_la_main.append((numero, "; ".join(problemes)))
                self._journal(numero, "3", "à traiter à la main", "; ".join(problemes))
                continue
            age = (jour - date.fromisoformat(ligne["date_echeance"].strip())).days
            if age < 0:
                res.a_la_main.append((numero, "échéance dans le futur"))
                self._journal(numero, "3", "à traiter à la main", "échéance dans le futur")
                continue
            if age > regles.limite_age:
                res.ecartees.append((numero, 0, "au-delà de J+60"))
                self._journal(numero, "3", "écartée", "au-delà de J+60")
                continue
            atteint = niveau_atteint(age, regles.delais)
            if atteint == 0:
                self._journal(numero, "3", "ignorée", "aucun niveau atteint")
                continue
            dernier = derniers.get(numero, 0)
            if dernier > atteint:
                # une relance notée à un niveau que l'âge ne justifie pas : ligne sans doute mal placée
                res.a_la_main.append((numero, "historique contradictoire"))
                self._journal(numero, "3", "à traiter à la main", "historique contradictoire")
                continue
            niveau = dernier + 1
            self._journal(numero, "3", "candidate", f"niveau {niveau}")
            # étape 4 : écarts, dans l'ordre de 60 §4 (payée, déjà relancée, litige)
            if ligne["etat_paiement"].strip() == "rapprochée":
                motif = "payée"
            elif niveau > atteint:
                motif = "déjà relancée"
            elif numero in donnees["litiges"]:
                motif = "litige"
            else:
                motif = None
            if motif:
                res.ecartees.append((numero, atteint, motif))
                self._journal(f"{numero}|{atteint}", "4", "écartée", motif)
                continue
            prop = Proposition(numero, niveau, ligne["id_client"].strip(),
                               ligne["id_client"].strip() in donnees["comptes_cles"], ligne)
            propositions.append(prop)
            self._journal(prop.cle, "4", "mise à part" if prop.compte_cle else "retenue",
                          "compte clé" if prop.compte_cle else "")
        # liste vide suspecte (60 §10)
        avec_age = [l for l in lignes if self._age_ligne(l, jour) is not None
                    and self._age_ligne(l, jour) > regles.age_liste_vide]
        if avec_age and not propositions and not res.ecartees and not res.a_la_main:
            self._alerter([RESPONSABLE_FINANCIER, GESTIONNAIRE], "liste vide suspecte", "4", "extraction",
                          "factures échues sans proposition ni motif d'écart")
        res.propositions = propositions
        return propositions

    @staticmethod
    def _age_ligne(ligne: dict, jour: date):
        try:
            return (jour - date.fromisoformat(ligne["date_echeance"].strip())).days
        except (ValueError, KeyError, AttributeError):
            return None

    # ---- étape 5 --------------------------------------------------------------------------------
    def _composer(self, prop: Proposition):
        ligne = prop.ligne
        objet = f"Facture {prop.numero} — {self.regles.libelles[prop.niveau]}"
        corps = self.regles.modeles[prop.niveau].format(
            contact=ligne["nom_contact"].strip(), numero=prop.numero,
            montant=format_montant(decimal_ou_none(ligne["montant_ht"])),
            echeance=format_date_fr(date.fromisoformat(ligne["date_echeance"].strip())))
        return objet, corps

    def _ecrire_proposition(self, prop: Proposition, etat: str, dossier: str, id_brouillon: str) -> None:
        ligne = {
            "cle": prop.cle, "numero_facture": prop.numero, "id_client": prop.id_client,
            "niveau": prop.niveau, "etat": etat, "dossier": dossier, "id_brouillon": id_brouillon,
            "id_envoi": "", "horodatage": iso(self.horloge.maintenant()), "execution": self.id_execution,
        }
        self._avec_reprises(lambda: self.classeur.ecrire_ligne("propositions", ("cle",), ligne),
                            cle=prop.cle, etape="5")  # S2 coupé pendant l'écriture : reprises (D-05)
        self._props[prop.cle] = ligne

    def _charger_etape5(self) -> None:
        """Une lecture de l'onglet des propositions et un listage de chaque dossier de brouillons, une fois
        par exécution : le flux ne les relit pas pour chaque facture."""
        lignes = self._avec_reprises(lambda: self.classeur.lire("dispositif", "propositions"),
                                     cle="propositions", etape="5")
        self._props = {l["cle"]: l for l in lignes}
        self._envoyes = None
        self._brouillons = {}
        for dossier in (DOSSIER_NORMAL, DOSSIER_COMPTES_CLES):
            messages = self._avec_reprises(lambda d=dossier: self.boite.lister(SERVICE_MESSAGERIE, d),
                                           cle=dossier, etape="5")
            for message in messages:
                cle = message.entetes.get("X-Relance-Id", "")
                if cle:
                    self._brouillons[cle] = message

    def _etape5(self, propositions: list, res: Resultat) -> None:
        try:
            self._charger_etape5()
        except ServiceIndisponible as e:
            self._tout_en_echec(propositions, e, res)
            return
        for rang, prop in enumerate(propositions):
            try:
                self._creer_brouillon(prop, res)
            except ServiceIndisponible as e:
                self._tout_en_echec(propositions[rang:], e, res)
                return
            except ErreurDefinitive as e:
                self._echec(prop.cle, "5", str(e))
                res.compteurs["en_echec"] += 1
                # erreur définitive : file des échecs et alerte immédiate (60 §7) ; le responsable financier aussi si c'est
                # un compte clé (D-04)
                roles = [GESTIONNAIRE] + ([RESPONSABLE_FINANCIER] if prop.compte_cle else [])
                self._alerter(roles, "erreur définitive", "5", prop.cle, str(e))

    def _tout_en_echec(self, restantes: list, erreur: Exception, res: Resultat) -> None:
        """Un service reste coupé après toutes les reprises : le reste de la liste va dans la file des échecs."""
        res.statut = "echec"
        for reste in restantes:
            self._echec(reste.cle, "5", f"service indisponible : {erreur}")
            res.compteurs["en_echec"] += 1
        premiere = restantes[0].cle if restantes else ""
        # la gestionnaire clients ; le responsable financier si un compte clé est concerné (60 §7, panne de S3)
        roles = [GESTIONNAIRE] + ([RESPONSABLE_FINANCIER] if any(r.compte_cle for r in restantes) else [])
        self._alerter(roles, "service indisponible", "5", premiere, str(erreur))

    def _objets_envoyes(self) -> set:
        """Les objets du dossier « Envoyés », lus une fois par exécution et seulement quand il le faut."""
        if self._envoyes is None:
            messages = self._avec_reprises(lambda: self.boite.lister(SERVICE_MESSAGERIE, DOSSIER_ENVOYES),
                                           cle="envoyés", etape="5")
            self._envoyes = {m.entetes.get("Objet", "") for m in messages}
        return self._envoyes

    def _creer_brouillon(self, prop: Proposition, res: Resultat) -> None:
        cle = prop.cle
        dossier = DOSSIER_COMPTES_CLES if prop.compte_cle else DOSSIER_NORMAL
        objet, corps = self._composer(prop)
        etat = self._props.get(cle, {}).get("etat")
        if etat == "brouillon créé" and cle not in self._brouillons:
            # La proposition dit « brouillon créé » mais la boîte n'a plus ce brouillon : le courriel est parti (l'étape 8 le
            # consignera) ou une personne l'a supprimé. Dans ce second cas la facture n'a pas été relancée : elle revient
            # (EF-01 version 1.1) et une proposition supprimée ne bloque pas une nouvelle création (60 §8). D-03.
            if objet in self._objets_envoyes():
                self._journal(cle, "5", "déjà fait", "courriel parti, à consigner par l'étape 8")
                res.compteurs["deja_fait"] += 1
                return
            self._journal(cle, "5", "supprimée par une personne", "le brouillon n'est plus dans la boîte")
            etat = "supprimée"
        if etat in ("brouillon créé", "envoyée"):
            self._journal(cle, "5", "déjà fait", "")
            res.compteurs["deja_fait"] += 1
            return
        adresse = prop.ligne["adresse_courriel"].strip()
        existant = self._brouillons.get(cle)
        if existant is not None:
            # Un brouillon porte déjà cette clé sans proposition notée : l'exécution précédente s'est arrêtée
            # entre l'écriture du brouillon et celle de la proposition. On l'adopte, on n'en crée pas un second,
            # et on ne le supprime jamais : une personne a pu le retoucher depuis.
            if existant.entetes.get("A") != adresse:
                raise ErreurDefinitive("un brouillon existant porte cette clé avec une autre adresse : à vérifier à la main")
            id_message = existant.id
            self._journal(cle, "5", "réconcilié", dossier)
        else:
            id_message = self._avec_reprises(
                lambda: self.boite.creer_brouillon(SERVICE_MESSAGERIE, dossier, adresse, objet, corps, cle),
                cle=cle, etape="5")
            relu = self._avec_reprises(lambda: self.boite.lire(SERVICE_MESSAGERIE, id_message), cle=cle, etape="5")
            if (relu.entetes.get("A") != adresse or relu.entetes.get("Objet") != objet
                    or relu.corps != corps or relu.entetes.get("X-Relance-Id") != cle):
                self._avec_reprises(lambda: self.boite.supprimer(SERVICE_MESSAGERIE, id_message), cle=cle, etape="5")
                raise ErreurDefinitive("le brouillon relu diffère de ce qui devait être écrit")
            self._brouillons[cle] = relu
        self._ecrire_proposition(prop, "brouillon créé", dossier, id_message)
        self._journal(cle, "5", "brouillon créé", dossier)
        res.compteurs["creees"] += 1

    def _retirer_brouillons(self, motif: str) -> None:
        """Interrupteur : supprime les brouillons non envoyés ; l'étape 8 continue (60 §7)."""
        lignes = self._avec_reprises(lambda: self.classeur.lire("dispositif", "propositions"),
                                     cle="propositions", etape="interrupteur")
        for ligne in lignes:
            if ligne["etat"] != "brouillon créé":
                continue
            retire = True
            try:
                self._avec_reprises(lambda l=ligne: self.boite.supprimer(SERVICE_MESSAGERIE, l["id_brouillon"]),
                                    cle=ligne["cle"], etape="interrupteur")
            except DroitRefuse:
                raise
            except ErreurDefinitive:
                retire = False  # déjà supprimé, ou déjà envoyé par une personne : l'étape 8 le constatera
            self._avec_reprises(lambda l=ligne: self.classeur.ecrire_ligne("propositions", ("cle",), dict(l, etat="supprimée")),
                                cle=ligne["cle"], etape="interrupteur")
            self._journal(ligne["cle"], "interrupteur", "supprimée" if retire else "déjà absent", motif)

    # ---- étape 6 --------------------------------------------------------------------------------
    def _etape6(self, res: Resultat) -> None:
        creees = res.compteurs["creees"] + res.compteurs["deja_fait"]
        cles = sum(1 for p in res.propositions if p.compte_cle)
        corps = (f"propositions : {creees}\ncomptes clés à valider : {cles}\n"
                 f"factures à traiter à la main : {len(res.a_la_main)}")
        roles = [GESTIONNAIRE] + ([RESPONSABLE_FINANCIER] if cles else [])
        for role in roles:
            try:
                self.boite.poster_message(SERVICE_ALERTE, role, "Relances du lundi prêtes", corps)
            except ErreurPassagere:
                self._journal("", "6", "message non parti", "")
        self._journal("", "6", "message", corps.replace("\n", " ; "))

    def _compteurs(self, jour: date, res: Resultat) -> None:
        motifs = Counter(m for _, _, m in res.ecartees)
        ligne = {
            "date": jour.isoformat(), "execution": self.id_execution, "statut": res.statut,
            "propositions": len(res.propositions), "creees": res.compteurs["creees"],
            "comptes_cles": sum(1 for p in res.propositions if p.compte_cle),
            "payee": motifs["payée"], "deja_relancee": motifs["déjà relancée"], "litige": motifs["litige"],
            "au_dela_j60": motifs["au-delà de J+60"], "a_la_main": len(res.a_la_main),
            "en_echec": res.compteurs["en_echec"], "deja_fait": res.compteurs["deja_fait"],
        }
        try:
            self.classeur.ajouter("compteurs", ligne)
            if res.a_la_main:
                self.classeur.ecrire_lignes("a-traiter-a-la-main", ("numero_facture",), [
                    {"numero_facture": numero, "motif": motif, "date": jour.isoformat(),
                     "execution": self.id_execution} for numero, motif in res.a_la_main])
        except ErreurPassagere:
            pass

    # ---- veille : étapes 9 et 8 de 60 §4 ----------------------------------------------------------
    def sonder(self) -> Counter:
        """Un passage de la veille (toutes les 10 min le lundi, 60 §4 étape 9) : la case « Suspendre », les
        litiges (étape 9) et les courriels envoyés (étape 8). Chaque onglet est lu une fois par passage."""
        return self._veille(("9", "8"))

    def envois(self) -> Counter:
        """L'étape 8 seule : un courriel envoyé par une personne met sa proposition à « envoyée »."""
        return self._veille(("8",))

    def surveiller_litiges(self) -> int:
        """L'étape 9 seule : un litige nouveau retire le brouillon non envoyé de la facture."""
        return self._veille(("9",))["retirees"]

    def _veille(self, etapes: tuple) -> Counter:
        self.id_execution = self.horloge.maintenant().strftime("%Y-%m-%d-%H%M%S") + "-veille"
        bilan = Counter()
        try:
            self._passage(etapes, bilan)
        except ServiceIndisponible as e:
            bilan["echec"] += 1
            self._journal("veille", "9", "échec", f"service indisponible : {e}")
            self._alerter([GESTIONNAIRE, RESPONSABLE_FINANCIER], "service indisponible", "9", "veille", str(e))
        finally:
            self._vider_journal()
        return bilan

    def _lire_veille(self, zone: str, onglet: str) -> list:
        return self._avec_reprises(lambda: self.classeur.lire(zone, onglet), cle=onglet, etape="veille")

    def _passage(self, etapes: tuple, bilan: Counter) -> None:
        self.regles = None
        commande = self._commande()
        suspendu = commande.get("suspendre") == "oui"
        props = None
        a_supprimer: list = []
        if "9" in etapes:
            props = self._lire_veille("dispositif", "propositions")
            if suspendu:
                a_supprimer = [(l, "interrupteur") for l in props if l["etat"] == "brouillon créé"]
            else:
                litiges = {l["numero_facture"].strip() for l in self._lire_veille("pilotage", "litiges")}
                a_supprimer = [(l, "litige signalé") for l in props
                               if l["etat"] == "brouillon créé" and l["numero_facture"] in litiges]
        envoyes: list = []
        if "8" in etapes:
            if commande.get("etape8_active", "oui") == "non":
                self._journal("", "8", "désactivée", "réglage du pilote")
                bilan["desactivee"] += 1
            else:
                lues = self._avec_reprises(lambda: self.boite.lister(SERVICE_MESSAGERIE, DOSSIER_ENVOYES),
                                           cle="envoyés", etape="8")
                traites = {l["id_message"] for l in self._lire_veille("dispositif", "envois-traites")}
                envoyes = [m for m in lues if m.id not in traites]
        if not a_supprimer and not envoyes:
            return
        # Une écriture est à faire : une exécution à la fois (60 §7). Si le lundi tourne, ce passage attend le suivant.
        if not self.classeur.prendre_verrou(self.horloge.maintenant(), self._duree_max):
            self._journal("", "9", "reporté", "une exécution est déjà en cours")
            bilan["reporte"] += 1
            return
        try:
            for ligne, motif in a_supprimer:
                self._supprimer_brouillon_de(ligne, motif, bilan)
            if envoyes:
                self.regles = self._avec_reprises(lambda: charger_regles(self.classeur, avec_modeles=False),
                                                  etape="8")
                if props is None:
                    props = self._lire_veille("dispositif", "propositions")
                self._consigner_envois(envoyes, props, bilan)
        finally:
            self.classeur.liberer_verrou()

    def _supprimer_brouillon_de(self, ligne: dict, motif: str, bilan: Counter) -> None:
        retire = True
        try:
            self._avec_reprises(lambda: self.boite.supprimer(SERVICE_MESSAGERIE, ligne["id_brouillon"]),
                                cle=ligne["cle"], etape="9")
        except DroitRefuse:
            raise
        except ErreurDefinitive:
            retire = False  # le brouillon n'est plus là : courriel parti ou brouillon supprimé par une personne
        self._avec_reprises(lambda: self.classeur.ecrire_ligne("propositions", ("cle",), dict(ligne, etat="supprimée")),
                            cle=ligne["cle"], etape="9")
        if not retire:
            # Rien n'a été retiré : on ne le dit pas. Si le courriel est parti, l'étape 8 le consigne comme « envoyée ».
            self._journal(ligne["cle"], "9", "déjà absent", f"{motif} : le brouillon n'est plus dans la boîte")
            return
        self._journal(ligne["cle"], "9", "supprimée", motif)
        bilan["retirees"] += 1
        if motif == "litige signalé":
            self._alerter([GESTIONNAIRE], "brouillon retiré : litige signalé", "9", ligne["cle"],
                          "la facture vient d'entrer en litige")

    def _consigner_envois(self, envoyes: list, lignes_props: list, bilan: Counter) -> None:
        props = {l["cle"]: l for l in lignes_props}
        connus = {(l["numero_facture"], str(l["niveau"])) for l in self._lire_veille("dispositif", "historique")}
        modele_objet = re.compile(r"^Facture (\S+) — (.+)$")
        niveaux = {libelle: n for n, libelle in self.regles.libelles.items()}
        historique, propositions, lus = [], {}, []
        for message in envoyes:
            trouve = modele_objet.match(message.entetes.get("Objet", ""))
            expediteur = message.entetes.get("Envoye-par", "")
            if not trouve or trouve.group(2) not in niveaux:
                cle, resultat = message.id, "objet non reconnu"
                self._echec(cle, "8", "identifiant de relance introuvable : objet non reconnu")
                self._alerter([GESTIONNAIRE], "identifiant introuvable", "8", cle, "objet non reconnu")
            else:
                numero, niveau = trouve.group(1), niveaux[trouve.group(2)]
                cle = f"{numero}|{niveau}"
                prop = props.get(cle)
                if prop is None:
                    resultat = "aucune proposition"
                    self._echec(cle, "8", "identifiant de relance introuvable : aucune proposition")
                    self._alerter([GESTIONNAIRE], "identifiant introuvable", "8", cle, "aucune proposition")
                elif prop["etat"] == "envoyée" and prop.get("id_envoi") == message.id:
                    resultat = "déjà consigné"  # reprise après un arrêt entre les écritures groupées
                elif prop["etat"] == "envoyée":
                    resultat = "double envoi"
                    self._alerter([RESPONSABLE_FINANCIER], "double envoi", "8", cle,
                                  "une seconde copie a été envoyée avec la même clé")
                else:
                    resultat = "envoyée"
                    if (numero, str(niveau)) not in connus:
                        connus.add((numero, str(niveau)))
                        historique.append({"numero_facture": numero, "niveau": niveau,
                                           "date_envoi": message.entetes.get("Envoye-le", "")[:10],
                                           "expediteur": expediteur})
                    props[cle] = dict(prop, etat="envoyée", id_envoi=message.id)
                    propositions[cle] = props[cle]
                    if prop["dossier"] == DOSSIER_COMPTES_CLES and expediteur != RESPONSABLE_FINANCIER:
                        self._alerter([RESPONSABLE_FINANCIER], "envoi hors validation", "8", cle,
                                      "un compte clé a été envoyé par un autre rôle que le responsable financier")
            lus.append({"id_message": message.id, "cle": cle, "resultat": resultat,
                        "horodatage": iso(self.horloge.maintenant())})
            self._journal(message.id, "8", resultat, "")
            bilan[resultat] += 1
        # Trois écritures groupées, dans cet ordre : un arrêt entre deux se rattrape à la reprise.
        if historique:
            self._avec_reprises(lambda: self.classeur.ecrire_lignes("historique", ("numero_facture", "niveau"), historique),
                                cle="historique", etape="8")
        if propositions:
            self._avec_reprises(lambda: self.classeur.ecrire_lignes("propositions", ("cle",), list(propositions.values())),
                                cle="propositions", etape="8")
        self._avec_reprises(lambda: self.classeur.ecrire_lignes("envois-traites", ("id_message",), lus),
                            cle="envois-traites", etape="8")

    # ---- alerte sur silence (60 §10) ------------------------------------------------------------
    def veiller(self) -> str:
        maintenant = self.horloge.maintenant()
        self.id_execution = maintenant.strftime("%Y-%m-%d-%H%M%S") + "-silence"
        self.regles = self._avec_reprises(lambda: charger_regles(self.classeur, avec_modeles=False), etape="10")
        heure = datetime.strptime(self.regles.silence_heure, "%H:%M").time()
        if maintenant.time() < heure:
            return "trop tôt"
        jour = maintenant.date().isoformat()
        journal = self._avec_reprises(lambda: self.classeur.lire("dispositif", "journal"), cle="journal", etape="10")
        debuts = [l for l in journal
                  if l["etape"] == "0" and l["resultat"] == "début" and l["horodatage"].startswith(jour)]
        if not debuts:
            self._alerter([RESPONSABLE_FINANCIER], "aucune exécution", "10", "silence",
                          f"aucune exécution le {jour} à {self.regles.silence_heure}")
            self._vider_journal()
            return "alerte"
        return "ok"

    # ---- file des échecs --------------------------------------------------------------------------
    def rejouer(self) -> Resultat:
        """La gestionnaire clients coche « rejouer » ; le flux reprend seulement ces clés."""
        lues = self._avec_reprises(lambda: self.classeur.lire("dispositif", "echecs"), cle="echecs", etape="rejeu")
        cles = {l["cle"] for l in lues if l["rejouer"].strip().lower() == "oui" and l["etat"] == "ouvert"}
        if not cles:
            res = Resultat()
            res.messages.append("rien à rejouer : aucune ligne de la file des échecs n'est cochée « rejouer »")
            return res
        res = self.executer(cles_filtre=cles)
        if res.statut == "ok":
            for ligne in self._avec_reprises(lambda: self.classeur.lire("dispositif", "echecs"), cle="echecs", etape="rejeu"):
                if ligne["cle"] in cles and ligne["etat"] == "ouvert":
                    self._avec_reprises(lambda l=ligne: self.classeur.ecrire_ligne("echecs", ("cle",), dict(l, etat="rejoué")),
                                        cle=ligne["cle"], etape="rejeu")
        return res


# --------------------------------------------------------------------------------------------------
# Livraison : empreinte de la version approuvée
# --------------------------------------------------------------------------------------------------
def fichiers_livres(dossier: Path) -> list:
    """Les fichiers de la version livrée : ni le manifeste, ni le cache de Python, ni les archives des versions."""
    return sorted(p for p in dossier.rglob("*")
                  if p.is_file() and p.name != "MANIFESTE.sha256" and "__pycache__" not in p.parts
                  and "archives" not in p.relative_to(dossier).parts)


def ecrire_manifeste(dossier: Path) -> str:
    lignes = [f"{sha256_lf(p.read_bytes())}  {p.relative_to(dossier).as_posix()}" for p in fichiers_livres(dossier)]
    texte = "\n".join(lignes) + "\n"
    (dossier / "MANIFESTE.sha256").write_text(texte, encoding="utf-8", newline="\n")
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def verifier_livraison(dossier: Path) -> list:
    """Compare ce qui est livré au manifeste de la version approuvée : liste des écarts."""
    ecarts = []
    manifeste = dossier / "MANIFESTE.sha256"
    if not manifeste.exists():
        return ["MANIFESTE.sha256 absent"]
    attendus = {}
    for ligne in manifeste.read_text(encoding="utf-8").splitlines():
        empreinte, _, chemin = ligne.partition("  ")
        attendus[chemin] = empreinte
    presents = {p.relative_to(dossier).as_posix(): p for p in fichiers_livres(dossier)}
    for chemin, empreinte in attendus.items():
        if chemin not in presents:
            ecarts.append(f"absent : {chemin}")
        elif sha256_lf(presents[chemin].read_bytes()) != empreinte:
            ecarts.append(f"modifié : {chemin}")
    for chemin in presents:
        if chemin not in attendus:
            ecarts.append(f"en trop : {chemin}")
    return ecarts


# --------------------------------------------------------------------------------------------------
# Ligne de commande
# --------------------------------------------------------------------------------------------------
def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(prog="flux_relances", description=__doc__.split("\n")[0])
    p.add_argument("commande", choices=["executer", "sonder", "envois", "surveiller", "veiller", "rejouer",
                                        "approuver", "verifier-livraison", "version"])
    p.add_argument("--espace", help="dossier de l'espace d'essai (dépôt, pilotage, dispositif, boîte)")
    p.add_argument("--maintenant", help="heure de l'horloge de test, AAAA-MM-JJTHH:MM:SS (défaut : maintenant)")
    p.add_argument("--mode", default="simulation", help="seul « simulation » existe dans l'essai")
    p.add_argument("--version-regles", default="R1")
    args = p.parse_args(argv)
    if args.mode != "simulation":
        print("Refusé : le mode réel n'existe pas dans l'essai. Le passage au réel est une action de "
              "90-mise-en-service, faite par le client après validation.", file=sys.stderr)
        return 2
    if args.commande == "version":
        print(f"flux_relances {VERSION}")
        return 0
    if args.commande == "verifier-livraison":
        ecarts = verifier_livraison(Path(__file__).resolve().parent)
        for e in ecarts:
            print("ÉCART", e)
        print("livraison conforme au manifeste" if not ecarts else f"{len(ecarts)} écart(s)")
        return 1 if ecarts else 0
    if not args.espace:
        p.error("--espace est obligatoire")
    if args.commande == "approuver":
        approuver(Path(args.espace), args.version_regles, (args.maintenant or datetime.now().isoformat())[:10])
        print("empreintes des règles et des modèles écrites dans pilotage/approbation.csv")
        return 0
    from essai_s2_s3 import BoiteSimulee, ClasseurFichiers  # doubles d'essai (voir essai_s2_s3.py)
    horloge = (HorlogeDeTest(datetime.fromisoformat(args.maintenant)) if args.maintenant else HorlogeReelle())
    classeur = ClasseurFichiers(args.espace, horloge)
    boite = BoiteSimulee(Path(args.espace) / "boite", horloge)
    flux = Flux(args.espace, classeur, boite, horloge)
    code = 0
    if args.commande == "executer":
        res = flux.executer()
        print(f"exécution : {res.statut} ; propositions {len(res.propositions)} ; écartées {len(res.ecartees)} ; "
              f"à traiter à la main {len(res.a_la_main)} ; brouillons créés {res.compteurs['creees']}")
        code = 0 if res.statut == "ok" else 1
    elif args.commande == "sonder":
        print(dict(flux.sonder()))
    elif args.commande == "envois":
        print(dict(flux.envois()))
    elif args.commande == "surveiller":
        print(f"brouillons retirés : {flux.surveiller_litiges()}")
    elif args.commande == "veiller":
        print(flux.veiller())
    elif args.commande == "rejouer":
        res = flux.rejouer()
        print(f"rejeu : {res.statut} ; brouillons créés {res.compteurs['creees']}")
    print(f"opérations de la plateforme : {sum(classeur.operations.values()) + sum(boite.operations.values())} "
          f"(classeur {sum(classeur.operations.values())}, messagerie {sum(boite.operations.values())})")
    return code


if __name__ == "__main__":
    # Un seul jeu de classes : les doubles d'essai importent ce module, ils doivent y retrouver les mêmes
    # erreurs que celles que le flux attrape (lancé tel quel, `__main__` serait un second module).
    import flux_relances
    sys.exit(flux_relances.main())
