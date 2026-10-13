"""Recette de la maquette `flux_relances` (85-recette.md) : tests T-01 à T-25 de 60-specification §12 et tests ajoutés (T-26 et suivants).

Qui a écrit quoi. Le consultant IA a construit la maquette (80-construction) et écrit ces tests : le constructeur et
le testeur sont le même acteur, et `85-recette.md` le dit en tête. Ce qui tient lieu d'indépendance :
- chaque attendu vient de `60-specification.md`, de `30-exigences.md` §9 ou du décompte de la séance du 2026-09-07
  (61 factures, 9 payées, 4 déjà relancées, 6 en litige, 5 comptes clés, 24 relances en 14/7/3, 42 propositions),
  jamais de la sortie du programme ; la source est citée dans chaque test ;
- l'attendu du rejeu est le fichier `attendu/rejeu-2026-09-07.csv`, fabriqué par `donnees-essai/jeux.py` qui
  n'importe jamais le flux ;
- les tests ne lisent que ce qu'une personne pourrait lire : brouillons de la boîte, messages, onglets du classeur
  du dispositif, journal ; ils n'interrogent pas les structures internes du flux ;
- chaque test part d'un espace d'essai neuf (remise à zéro) et d'une horloge de test : l'ordre est indifférent.

Commande (depuis ce dossier) : `python -X utf8 test_recette.py`. Pour tester une autre copie de la livraison (sabotage,
retour arrière) : variable d'environnement `FLUX_LIVRAISON=<dossier>`. Bibliothèque standard seulement.
"""
from __future__ import annotations

import csv
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
import zipfile
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from decimal import Decimal
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE_80 = ICI.parent / "80-construction"
LIVRAISON = Path(os.environ.get("FLUX_LIVRAISON") or (RACINE_80 / "livraison")).resolve()
DONNEES = RACINE_80 / "donnees-essai"
sys.path.insert(0, str(LIVRAISON))
sys.path.insert(0, str(DONNEES))

import balayer  # noqa: E402  (balayage des secrets et des données personnelles, construit en 80)
import essai_s2_s3  # noqa: E402
import flux_relances as fr  # noqa: E402
import jeux  # noqa: E402
from essai_s2_s3 import BoiteSimulee, ClasseurFichiers  # noqa: E402

# Témoin positif du balayage des secrets (T-33). Il se compose à l'exécution : le texte d'une forme de clé réelle
# n'est écrit dans aucun fichier du dépôt, et aucune sortie ne le montre en entier.
TEMOIN_CLE = "sk_" + "live_" + "9f8e7d6c5b4a3928" + "1706f5e4d3c2b1a0"

# ------------------------------------------------------------------------------------------------------------------
# Ce que la spécification dit, écrit ici une fois (60 §4, §5, §6 ; 30 §9)
# ------------------------------------------------------------------------------------------------------------------
LUNDI = datetime(2026, 9, 7, 9, 30)  # le lundi du rejeu ; 60 §11 : la séance du 2026-09-07
JOUR = LUNDI.date()
NORMAL = "Relances du lundi"  # 60 §4 étape 5
COMPTES_CLES = "Comptes clés à valider"
ENVOYES = "Envoyés"
GEST, COMPT, RESP, SUPPORT = "gestionnaire clients", "comptable", "responsable financier", "responsable du support"
SEANCE = {  # décompte `[F]` de la séance du 2026-09-07 (30 §9, 60 §12)
    "factures": 61, "payees": 9, "deja_relancees": 4, "litiges": 6, "comptes_cles": 5,
    "envoyees": 24, "niveaux": (14, 7, 3), "propositions": 42,
}
ONGLETS_ECRITS_PAR_LE_FLUX = {  # 60 §5 et §10 : l'écriture est limitée aux onglets du classeur du dispositif
    "propositions", "historique", "echecs", "journal", "compteurs", "a-traiter-a-la-main", "envois-traites",
}


# ------------------------------------------------------------------------------------------------------------------
# Outils de lecture : ce qu'une personne verrait
# ------------------------------------------------------------------------------------------------------------------
def lire_csv(chemin) -> list:
    chemin = Path(chemin)
    if not chemin.exists():
        return []
    with open(chemin, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def ecrire_csv(chemin, entetes, lignes) -> None:
    jeux.ecrire_csv(Path(chemin), list(entetes), lignes)


def lire_message(chemin):
    texte = Path(chemin).read_text(encoding="utf-8")
    tete, _, corps = texte.partition("\n\n")
    entetes = {}
    for ligne in tete.splitlines():
        cle, _, valeur = ligne.partition(": ")
        entetes[cle] = valeur
    return entetes, corps


def empreinte_arbre(dossier) -> str:
    dossier = Path(dossier)
    lignes = [f"{hashlib.sha256(p.read_bytes().replace(b'\r\n', b'\n')).hexdigest()}  {p.relative_to(dossier).as_posix()}"
              for p in sorted(dossier.rglob("*")) if p.is_file()]
    return hashlib.sha256("\n".join(lignes).encode("utf-8")).hexdigest()


def ligne(numero, age, jour=JOUR, **kw) -> dict:
    """Une ligne d'extraction fictive, `age` jours après l'échéance."""
    return jeux.ligne_facture(numero, age, jour=jour, **kw)


@dataclass
class Brouillon:
    id: str
    dossier: str
    entetes: dict
    corps: str


def sans_noms_ni_adresses(texte: str) -> bool:
    return "@" not in texte and not re.search(r"Contact C\d", texte)


# ------------------------------------------------------------------------------------------------------------------
# Doubles qui laissent le test intervenir pendant l'exécution (un incident à un rang précis)
# ------------------------------------------------------------------------------------------------------------------
class ClasseurObservateur(ClasseurFichiers):
    """Le classeur d'essai, plus un rappel appelé après chaque écriture groupée : `apres_ecriture(onglet, rang)`."""

    def __init__(self, racine, horloge):
        super().__init__(racine, horloge)
        self.apres_ecriture = None
        self._rang = Counter()

    def ecrire_lignes(self, onglet, cle_champs, lignes):
        super().ecrire_lignes(onglet, cle_champs, lignes)
        self._rang[onglet] += 1
        if self.apres_ecriture is not None:
            self.apres_ecriture(onglet, self._rang[onglet])


class BoiteQuiAbime(BoiteSimulee):
    """Une messagerie qui enregistre le troisième brouillon avec un autre corps que celui demandé."""

    def creer_brouillon(self, compte, dossier, destinataire, objet, corps, cle):
        self._rang_creation = getattr(self, "_rang_creation", 0) + 1
        if self._rang_creation == 3:
            corps = corps.replace("€ HT", "€ TTC")
        return super().creer_brouillon(compte, dossier, destinataire, objet, corps, cle)


# ------------------------------------------------------------------------------------------------------------------
# Un banc d'essai : espace neuf, horloge de test, flux branché sur les doubles
# ------------------------------------------------------------------------------------------------------------------
class Banc:
    def __init__(self, depart=LUNDI, classeur_cls=ClasseurFichiers, boite_cls=BoiteSimulee):
        self.racine = Path(tempfile.mkdtemp(prefix="recette-"))
        jeux.ecrire_espace_modele(self.racine, LIVRAISON)  # remise à zéro : le rejeu de la séance, approuvé (version R1)
        self.horloge = fr.HorlogeDeTest(depart)
        self.classeur = classeur_cls(self.racine, self.horloge)
        self.boite = boite_cls(self.racine / "boite", self.horloge)
        self.flux = fr.Flux(self.racine, self.classeur, self.boite, self.horloge)

    def p(self, *morceaux) -> Path:
        return self.racine.joinpath(*morceaux)

    # ---- mises en place ------------------------------------------------------------------------------
    def extraction(self, lignes, jour=JOUR) -> None:
        ecrire_csv(self.p("depot", f"extraction-{jour.isoformat()}.csv"), jeux.ENTETES_EXTRACTION, lignes)

    def rapprochement(self, jour_iso, role=COMPT) -> None:
        ecrire_csv(self.p("depot", "rapprochement.csv"), ["date_rapprochement", "role"],
                   [{"date_rapprochement": jour_iso, "role": role}])

    def litiges(self, numeros, ouverture="2026-09-07") -> None:
        ecrire_csv(self.p("pilotage", "litiges.csv"), ["numero_facture", "date_ouverture"],
                   [{"numero_facture": n, "date_ouverture": ouverture} for n in numeros])

    def ajouter_litige(self, numero, ouverture="2026-09-07") -> None:
        with open(self.p("pilotage", "litiges.csv"), "a", encoding="utf-8", newline="") as f:
            f.write(f"{numero},{ouverture}\n")

    def litiges_maj(self, dates) -> None:
        ecrire_csv(self.p("pilotage", "litiges-maj.csv"), ["date", "role"], [{"date": d, "role": SUPPORT} for d in dates])

    def historique(self, lignes) -> None:
        ecrire_csv(self.p("dispositif", "historique.csv"), jeux.ENTETES_HISTORIQUE, lignes)

    def comptes_cles(self, ids) -> None:
        ecrire_csv(self.p("pilotage", "comptes-cles.csv"), ["id_client"], [{"id_client": c} for c in ids])

    def commande(self, suspendre="non", etape8="oui") -> None:
        ecrire_csv(self.p("dispositif", "commande.csv"), ["parametre", "valeur"],
                   [{"parametre": "suspendre", "valeur": suspendre}, {"parametre": "etape8_active", "valeur": etape8}])

    def regles(self) -> dict:
        return {l["parametre"]: l["valeur"] for l in lire_csv(self.p("pilotage", "regles.csv"))}

    def modifier_regle(self, nom, valeur) -> None:
        lignes = lire_csv(self.p("pilotage", "regles.csv"))
        for l in lignes:
            if l["parametre"] == nom:
                l["valeur"] = valeur
        ecrire_csv(self.p("pilotage", "regles.csv"), ["parametre", "valeur"], lignes)

    def modifier_modele(self, niveau, ajout) -> None:
        chemin = self.p("pilotage", "modeles", f"niveau-{niveau}.txt")
        chemin.write_text(chemin.read_text(encoding="utf-8") + ajout, encoding="utf-8", newline="\n")

    def approuver(self, version, jour="2026-11-12") -> None:
        fr.approuver(self.racine, version, jour)  # l'acte du responsable financier, hors du flux (60 §17)

    # ---- lectures -------------------------------------------------------------------------------------
    def table(self, zone, onglet) -> list:
        return lire_csv(self.p(zone, onglet + ".csv"))

    def journal(self) -> list:
        return self.table("dispositif", "journal")

    def propositions(self) -> dict:
        return {l["cle"]: l for l in self.table("dispositif", "propositions")}

    def historique_lignes(self) -> list:
        return self.table("dispositif", "historique")

    def echecs(self) -> list:
        return self.table("dispositif", "echecs")

    def compteurs(self) -> list:
        return self.table("dispositif", "compteurs")

    def a_la_main(self) -> dict:
        return {l["numero_facture"]: l["motif"] for l in self.table("dispositif", "a-traiter-a-la-main")}

    def attendu(self) -> list:
        return lire_csv(self.p("attendu", "rejeu-2026-09-07.csv"))

    def decisions(self) -> dict:
        """Pour chaque facture, la ligne d'étape 4 du journal : niveau, résultat (retenue, mise à part, écartée), motif."""
        sortie = {}
        for l in self.journal():
            if l["etape"] == "4":
                numero, _, niveau = l["cle"].partition("|")
                sortie[numero] = {"niveau": int(niveau), "resultat": l["resultat"], "detail": l["detail"]}
        return sortie

    def motif_d_ecart(self, numero):
        """Le motif d'écart d'une facture, à l'étape 3 (au-delà de J+60) ou à l'étape 4 (payée, déjà relancée, litige)."""
        for l in self.journal():
            if l["cle"].split("|")[0] == numero and l["resultat"] == "écartée":
                return l["detail"]
        return None

    def brouillons(self, dossier=None) -> list:
        sortie = []
        for d in ([dossier] if dossier else [NORMAL, COMPTES_CLES]):
            for chemin in sorted(self.p("boite", d).glob("*.txt")):
                entetes, corps = lire_message(chemin)
                sortie.append(Brouillon(chemin.stem, d, entetes, corps))
        return sortie

    def brouillons_de(self, cle) -> list:
        return [x for x in self.brouillons() if x.entetes.get("X-Relance-Id") == cle]

    def brouillon_de(self, cle):
        trouves = self.brouillons_de(cle)
        assert len(trouves) <= 1, f"{len(trouves)} brouillons pour la clé {cle}"
        return trouves[0] if trouves else None

    def envoyes(self) -> list:
        return [lire_message(c) + (c.stem,) for c in sorted(self.p("boite", ENVOYES).glob("*.txt"))]

    def messages(self, role=None) -> list:
        sortie = []
        for chemin in sorted(self.p("boite", "messages").glob("*.txt")):
            entetes, corps = lire_message(chemin)
            if role is None or entetes.get("Pour") == role:
                sortie.append((entetes, corps))
        return sortie

    def alertes(self, role, fragment="") -> list:
        return [(e, c) for e, c in self.messages(role)
                if e.get("Objet", "").startswith("[alerte]") and fragment in e.get("Objet", "") + "\n" + c]

    def nb_alertes(self, role) -> int:
        return len([1 for e, _ in self.messages(role) if e.get("Objet", "").startswith("[alerte]")])

    # ---- gestes des personnes ---------------------------------------------------------------------------
    def envoyer(self, cle, par=GEST):
        brouillon = self.brouillon_de(cle)
        assert brouillon is not None, f"pas de brouillon pour {cle}"
        return self.boite.envoyer(par, brouillon.id)

    def sonder(self, minutes=10):
        self.horloge.avancer(minutes=minutes)
        return self.flux.sonder()

    def journal_boite(self) -> list:
        return lire_csv(self.p("boite", "journal-boite.csv"))


def cli(commande, racine, maintenant, env=None):
    """La ligne de commande de la livraison, dans un autre processus (plantage possible)."""
    e = {k: v for k, v in os.environ.items() if k != "FLUX_PLANTAGE"}
    e.update(env or {})
    return subprocess.run([sys.executable, "-X", "utf8", str(LIVRAISON / "flux_relances.py"), commande,
                           "--espace", str(racine), "--maintenant", maintenant],
                          capture_output=True, text=True, encoding="utf-8", env=e)


class RecetteCase(unittest.TestCase):
    """Garde l'état final d'un test échoué pour comprendre ; efface celui des tests réussis."""

    def banc(self, **kw) -> Banc:
        b = Banc(**kw)
        self.bancs.append(b)
        return b

    def run(self, result=None):
        self.bancs = []
        avant = (len(result.failures) + len(result.errors)) if result is not None else 0
        sortie = super().run(result)
        echec = result is not None and (len(result.failures) + len(result.errors)) > avant
        for b in self.bancs:
            if echec:
                print(f"    [état final conservé pour comprendre : {court(b.racine)}]", file=sys.stderr)
            else:
                shutil.rmtree(b.racine, ignore_errors=True)
        return sortie


# ==================================================================================================================
class Recette(RecetteCase):
    # ------------------------------------------------------------------ T-01 à T-05 : la liste du lundi
    def test_T01_rejeu_61_factures_au_bon_niveau(self):
        """T-01 · EF-01, CA-01 · rejeu de la séance du 2026-09-07 : les 61 factures sont traitées, chacune au bon niveau"""
        b = self.banc()
        att = b.attendu()
        self.assertEqual(len(att), SEANCE["factures"])
        envoyees = Counter(int(a["niveau"]) for a in att if a["categorie"] == "envoyee")
        self.assertEqual((envoyees[1], envoyees[2], envoyees[3]), SEANCE["niveaux"], "le jeu ne reproduit pas 14/7/3")
        res = b.flux.executer()
        self.assertEqual(res.statut, "ok", res.messages)
        dec = b.decisions()
        self.assertEqual(sorted(dec), sorted(a["numero_facture"] for a in att),
                         "la liste ne contient pas exactement les 61 factures de la séance")
        for a in att:
            self.assertEqual(dec[a["numero_facture"]]["niveau"], int(a["niveau"]), a["numero_facture"])
        c = b.compteurs()[-1]
        self.assertEqual(int(c["creees"]), SEANCE["propositions"])
        self.assertEqual((int(c["payee"]), int(c["deja_relancee"]), int(c["litige"]), int(c["comptes_cles"])),
                         (SEANCE["payees"], SEANCE["deja_relancees"], SEANCE["litiges"], SEANCE["comptes_cles"]))
        self.assertEqual((int(c["a_la_main"]), int(c["en_echec"])), (0, 0))

    def test_T02_niveaux_et_pas_de_saut(self):
        """T-02 · EF-01, règle de niveau, CA-01 v1.1 · J+6 absente, J+7 et J+8 niveau 1, J+25 niveau 1, litige levé : revient"""
        b = self.banc(depart=datetime(2026, 8, 31, 9, 30))
        lundi1, lundi2 = date(2026, 8, 31), date(2026, 9, 7)
        e = "FA-T02-LEVE"
        b.historique([])
        b.comptes_cles([])
        # lundi 1 : la facture E est en litige, elle est écartée
        b.rapprochement("2026-08-28")
        b.litiges([e], ouverture="2026-08-27")
        b.litiges_maj(["2026-08-28"])
        b.extraction([ligne(e, 10, lundi1, client="C905")], lundi1)
        self.assertEqual(b.flux.executer().statut, "ok")
        self.assertEqual(b.propositions(), {}, "une facture en litige a été proposée")
        # lundi 2 : le litige est levé ; quatre autres factures à J+6, J+7, J+8 et J+25 sans relance consignée
        b.horloge.t = datetime(2026, 9, 7, 9, 30)
        b.rapprochement("2026-09-04")
        b.litiges([])
        b.litiges_maj(["2026-09-04"])
        b.extraction([ligne("FA-T02-J6", 6, lundi2, client="C901"), ligne("FA-T02-J7", 7, lundi2, client="C902"),
                      ligne("FA-T02-J8", 8, lundi2, client="C903"), ligne("FA-T02-J25", 25, lundi2, client="C904"),
                      ligne(e, 17, lundi2, client="C905")], lundi2)
        self.assertEqual(b.flux.executer().statut, "ok")
        props = b.propositions()
        self.assertEqual(sorted(props), ["FA-T02-J25|1", "FA-T02-J7|1", "FA-T02-J8|1", "FA-T02-LEVE|1"],
                         "J+6 doit être absente ; J+25 doit rester au niveau 1 ; le litige levé doit revenir")
        self.assertEqual(len(b.brouillons()), 4)

    def _exclusion(self, issue, motif, compteur, nombre):
        b = self.banc()
        res = b.flux.executer()
        self.assertEqual(res.statut, "ok", res.messages)
        att = [a for a in b.attendu() if a["issue"] == issue]
        self.assertEqual(len(att), nombre, "le jeu ne reproduit pas le décompte de la séance")
        dec, props = b.decisions(), b.propositions()
        for a in att:
            n = a["numero_facture"]
            self.assertEqual((dec[n]["resultat"], dec[n]["detail"]), ("écartée", motif), n)
            self.assertNotIn(f"{n}|{a['niveau']}", props, f"{n} est proposée alors qu'elle doit être écartée ({motif})")
            self.assertEqual(b.brouillons_de(f"{n}|{a['niveau']}"), [], f"{n} a un brouillon")
        self.assertEqual(int(b.compteurs()[-1][compteur]), nombre)

    def test_T03_factures_payees_ecartees(self):
        """T-03 · EF-02, CA-02 · les 9 factures dont le paiement est rapproché ne sont pas proposées, motif « payée »"""
        self._exclusion("payee", "payée", "payee", SEANCE["payees"])

    def test_T04_factures_deja_relancees_ecartees(self):
        """T-04 · EF-03, CA-03 · les 4 factures déjà relancées à leur niveau ne sont pas proposées, motif « déjà relancée »"""
        self._exclusion("deja_relancee", "déjà relancée", "deja_relancee", SEANCE["deja_relancees"])

    def test_T05_factures_en_litige_ecartees(self):
        """T-05 · EF-04, CA-04 · les 6 factures en litige ne sont pas proposées, motif « litige »"""
        self._exclusion("litige", "litige", "litige", SEANCE["litiges"])

    def test_T06_litige_signale_apres_les_brouillons(self):
        """T-06 · EF-04, CA-04, étape 9 · un litige saisi après la création des brouillons retire le brouillon à la veille suivante"""
        b = self.banc()
        b.flux.executer()
        proposees = [a for a in b.attendu() if a["categorie"] == "envoyee"]
        cible = proposees[0]["numero_facture"]
        niveau = int(proposees[0]["niveau"])
        autre = proposees[1]["numero_facture"]
        self.assertIsNotNone(b.brouillon_de(f"{cible}|{niveau}"))
        avant = len(b.brouillons())
        b.ajouter_litige(cible, "2026-09-07")  # le support saisit le litige pendant la séance
        b.sonder(minutes=9)  # un passage de la veille, moins de 10 minutes après la saisie
        self.assertEqual(b.brouillons_de(f"{cible}|{niveau}"), [], "le brouillon du litige est resté")
        self.assertEqual(len(b.brouillons()), avant - 1, "d'autres brouillons ont été retirés")
        self.assertIsNotNone(b.brouillon_de(f"{autre}|{int(proposees[1]['niveau'])}"))
        self.assertEqual(b.propositions()[f"{cible}|{niveau}"]["etat"], "supprimée")
        self.assertTrue(b.alertes(GEST, cible) or [m for m in b.messages(GEST) if cible in m[1]],
                        "la gestionnaire clients n'est pas avertie")

    def test_T07_comptes_cles_a_valider_par_le_responsable_financier(self):
        """T-07 · EF-06, CA-06 · 5 comptes clés : brouillons à part, rien ne part ; envoi par un autre rôle : alerte"""
        b = self.banc()
        b.flux.executer()
        cc = [a for a in b.attendu() if a["issue"] == "mise_a_part"]
        self.assertEqual(len(cc), SEANCE["comptes_cles"])
        for a in cc:
            cle = f"{a['numero_facture']}|{a['niveau']}"
            self.assertEqual(b.brouillon_de(cle).dossier, COMPTES_CLES, cle)
        self.assertEqual(len(b.brouillons(COMPTES_CLES)), SEANCE["comptes_cles"],
                         "d'autres brouillons que les comptes clés sont dans leur dossier")
        self.assertEqual(b.envoyes(), [], "un courriel est parti avant toute validation")
        cles = [f"{a['numero_facture']}|{a['niveau']}" for a in cc]
        avant = b.nb_alertes(RESP)
        b.envoyer(cles[0], par=RESP)  # le responsable financier envoie : rien à signaler
        b.sonder()
        self.assertEqual(b.nb_alertes(RESP), avant, "alerte à tort : le responsable financier a le droit d'envoyer")
        b.envoyer(cles[1], par=GEST)  # un autre rôle envoie un compte clé
        b.sonder()
        self.assertTrue(b.alertes(RESP, "envoi hors validation"), "aucune alerte « envoi hors validation »")

    def test_T08_courriels_conformes_a_la_facture(self):
        """T-08 · EF-07, CA-07 · modèle du niveau, numéro, montant, échéance exacts : 0 écart sur les 42 brouillons (dont les 24 envoyés)"""
        b = self.banc()
        b.flux.executer()
        libelles = {n: b.regles()[f"libelle_niveau_{n}"] for n in (1, 2, 3)}
        modeles = {n: b.p("pilotage", "modeles", f"niveau-{n}.txt").read_text(encoding="utf-8") for n in (1, 2, 3)}
        source = {l["numero_facture"]: l for l in lire_csv(b.p("depot", f"extraction-{JOUR.isoformat()}.csv"))}
        ecarts, controles = [], 0
        for a in b.attendu():
            if a["issue"] not in ("proposee", "mise_a_part"):
                continue
            n, niv = a["numero_facture"], int(a["niveau"])
            d = b.brouillon_de(f"{n}|{niv}")
            if d is None:
                ecarts.append(f"{n} : pas de brouillon")
                continue
            controles += 1
            src = source[n]
            annee, mois, jour = src["date_echeance"].split("-")
            attendu_corps = (modeles[niv].replace("{contact}", src["nom_contact"]).replace("{numero}", n)
                             .replace("{montant}", src["montant_ht"].replace(".", ",")).replace("{echeance}", f"{jour}/{mois}/{annee}"))
            if d.dossier != a["dossier"]:
                ecarts.append(f"{n} : dossier {d.dossier}")
            if d.entetes.get("A") != src["adresse_courriel"]:
                ecarts.append(f"{n} : destinataire")
            if d.entetes.get("Objet") != f"Facture {n} — {libelles[niv]}":
                ecarts.append(f"{n} : objet {d.entetes.get('Objet')!r}")
            if d.corps != attendu_corps:
                ecarts.append(f"{n} : corps")
            montant = re.search(r"(\d+,\d{2}) € HT", d.corps)
            if not montant or Decimal(montant.group(1).replace(",", ".")) != Decimal(src["montant_ht"]):
                ecarts.append(f"{n} : montant")
            if "{" in d.corps or "}" in d.corps:
                ecarts.append(f"{n} : champ non remplacé")
        self.assertEqual(controles, SEANCE["propositions"])
        self.assertEqual(ecarts, [], "0 écart toléré (CA-07)")

    def test_T09_ouverture_de_la_seance(self):
        """T-09 · EF-08, CA-11 · chaque brouillon est lisible avec son niveau avant tout envoi ; la gestionnaire clients est avertie"""
        b = self.banc()
        b.flux.executer()
        libelles = {n: b.regles()[f"libelle_niveau_{n}"] for n in (1, 2, 3)}
        niveaux = {f"{a['numero_facture']}|{a['niveau']}": int(a["niveau"]) for a in b.attendu()
                   if a["issue"] in ("proposee", "mise_a_part")}
        self.assertEqual(len(b.brouillons()), SEANCE["propositions"])
        for cle, niv in niveaux.items():
            d = b.brouillon_de(cle)
            self.assertIn(libelles[niv], d.entetes["Objet"], f"{cle} : le niveau ne se lit pas dans l'objet")
            self.assertTrue(d.corps.strip(), f"{cle} : brouillon vide")
            self.assertEqual(d.entetes.get("Etat"), "brouillon", cle)
        self.assertEqual(b.envoyes(), [], "un courriel est parti avant la séance")
        # étape 6 : nombre de propositions, de comptes clés, de factures à traiter à la main
        for role in (GEST, RESP):  # le responsable financier aussi, parce qu'il y a des comptes clés
            avis = [c for e, c in b.messages(role) if not e["Objet"].startswith("[alerte]")]
            self.assertTrue(avis, f"{role} n'a reçu aucun avertissement")
            self.assertEqual([int(x) for x in re.findall(r"\d+", avis[0])], [SEANCE["propositions"], SEANCE["comptes_cles"], 0])

    def test_T10_le_compte_de_service_n_envoie_pas(self):
        """T-10 · EF-10, CA-08 · tentative d'envoi par le compte de service : refusée, aucun courriel, tentative au journal"""
        b = self.banc()
        b.flux.executer()
        un = b.brouillons()[0]
        with self.assertRaises(fr.DroitRefuse):
            b.boite.envoyer(fr.SERVICE_MESSAGERIE, un.id)
        with self.assertRaises(fr.DroitRefuse):
            b.boite.envoyer(fr.SERVICE_ALERTE, un.id)
        self.assertEqual(b.envoyes(), [], "un courriel est parti")
        self.assertIsNotNone(b.brouillon_de(un.entetes["X-Relance-Id"]), "le brouillon a disparu")
        refus = [l for l in b.journal_boite() if l["operation"] == "refus" and l["compte"] == fr.SERVICE_MESSAGERIE]
        self.assertEqual(len(refus), 1, "la tentative n'est pas consignée")
        source = (LIVRAISON / "flux_relances.py").read_text(encoding="utf-8")
        self.assertNotRegex(source, r"\.envoyer\(|deposer_envoye\(", "le flux contient un appel d'envoi")
        # la liste des droits réellement accordés aux comptes de service, comparée à 60 §6 (« droits strictement nécessaires »)
        self.assertEqual(essai_s2_s3.DROITS[fr.SERVICE_MESSAGERIE], {"creer_brouillon", "lire", "lister", "supprimer_brouillon"})
        self.assertEqual(essai_s2_s3.DROITS[fr.SERVICE_ALERTE], {"poster_message"})

    def test_T11_historique_des_envois(self):
        """T-11 · EF-11, CA-09 · 24 courriels envoyés par une personne : 24 lignes d'historique (facture, niveau, date, expéditeur)"""
        b = self.banc()
        b.flux.executer()
        avant = len(b.historique_lignes())
        envoyees = [a for a in b.attendu() if a["categorie"] == "envoyee"]
        self.assertEqual(len(envoyees), SEANCE["envoyees"])
        for a in envoyees:
            b.envoyer(f"{a['numero_facture']}|{a['niveau']}", par=GEST)
        b.sonder()
        nouvelles = [l for l in b.historique_lignes() if l["date_envoi"] == "2026-09-07"]
        self.assertEqual(len(b.historique_lignes()) - avant, SEANCE["envoyees"])
        self.assertEqual(sorted((l["numero_facture"], int(l["niveau"])) for l in nouvelles),
                         sorted((a["numero_facture"], int(a["niveau"])) for a in envoyees))
        self.assertEqual({l["expediteur"] for l in nouvelles}, {GEST})
        etats = Counter(l["etat"] for l in b.propositions().values())
        self.assertEqual((etats["envoyée"], etats["brouillon créé"]), (SEANCE["envoyees"], SEANCE["propositions"] - SEANCE["envoyees"]))

    def test_T12_pas_de_doublon(self):
        """T-12 · dédoublonnage, CA-09 · flux lancé deux fois ; courriel envoyé deux fois : ni brouillon ni ligne en double, alerte « double envoi »"""
        b = self.banc()
        b.flux.executer()
        ids = sorted(x.id for x in b.brouillons())
        res2 = b.flux.executer()  # le flux est lancé une seconde fois
        self.assertEqual(res2.statut, "ok")
        self.assertEqual(sorted(x.id for x in b.brouillons()), ids, "la seconde exécution a créé ou retiré des brouillons")
        self.assertEqual(len(b.table("dispositif", "propositions")), SEANCE["propositions"], "ligne de proposition en double")
        self.assertEqual(len(b.brouillons()), SEANCE["propositions"])
        # un courriel envoyé deux fois avec la même clé
        un = next(a for a in b.attendu() if a["categorie"] == "envoyee")
        cle = f"{un['numero_facture']}|{un['niveau']}"
        brouillon = b.brouillon_de(cle)
        b.boite.envoyer(GEST, brouillon.id)
        b.boite.deposer_envoye(GEST, brouillon.entetes["A"], brouillon.entetes["Objet"], brouillon.corps)  # la même chose, renvoyée
        avant = len(b.historique_lignes())
        b.sonder()
        self.assertEqual(len(b.historique_lignes()) - avant, 1, "deux lignes d'historique pour une clé")
        self.assertTrue(b.alertes(RESP, "double envoi"), "aucune alerte « double envoi »")
        b.sonder()  # un nouveau passage ne redit rien
        self.assertEqual(len(b.alertes(RESP, "double envoi")), 1)

    # ------------------------------------------------------------------ T-13 : le cas limite critique
    def test_T13_cas_limite_critique_rapprochement_trop_ancien(self):
        """T-13 · ENF-09, CA-10 (cas limite critique) · payé vendredi, non rapproché, rapprochement du jeudi : aucune relance, « rapprochement trop ancien »"""
        b = self.banc()
        b.extraction([ligne("FA-T13", 8, client="C900", paiement="non rapprochée")])  # a payé vendredi, pas encore lettré
        b.rapprochement("2026-09-03")  # jeudi : deux jours ouvrés avant le lundi
        res = b.flux.executer()
        self.assertEqual(res.statut, "refus")
        self.assertEqual(b.brouillons(), [], "un brouillon a été créé malgré le rapprochement trop ancien")
        self.assertEqual(b.propositions(), {})
        self.assertTrue(b.alertes(GEST, "rapprochement trop ancien"), "la gestionnaire clients ne lit pas « rapprochement trop ancien »")
        # témoin positif : le même fichier avec un rapprochement de vendredi est bien proposé (la facture est à J+8, niveau 1)
        t = self.banc()
        t.extraction([ligne("FA-T13", 8, client="C900", paiement="non rapprochée")])
        t.rapprochement("2026-09-04")
        self.assertEqual(t.flux.executer().statut, "ok")
        self.assertEqual(sorted(t.propositions()), ["FA-T13|1"], "le témoin positif ne produit pas la proposition attendue")

    def test_T13b_frontieres_de_la_fraicheur(self):
        """T-13b · ENF-09 · un jour ouvré passe, deux non ; jours fériés comptés ; date absente : refus (60 §4 cas de refus, §5 règles)"""
        cas = [  # (lundi ou jour de séance, rapprochement, accepté ?)
            (datetime(2026, 9, 7, 9, 30), "2026-09-04", True),    # vendredi -> lundi : 1 jour ouvré
            (datetime(2026, 9, 7, 9, 30), "2026-09-03", False),   # jeudi -> lundi : 2 jours ouvrés
            (datetime(2026, 11, 12, 9, 30), "2026-11-10", True),  # mardi -> jeudi, le mercredi 11 novembre est férié : 1 jour ouvré
            (datetime(2026, 11, 12, 9, 30), "2026-11-09", False), # lundi -> jeudi, férié exclu : 2 jours ouvrés
            (datetime(2027, 4, 6, 9, 30), "2027-04-02", True),    # vendredi -> mardi, le lundi de Pâques 2027-04-05 est férié
        ]
        for depart, rapprochement, accepte in cas:
            with self.subTest(jour=depart.date().isoformat(), rapprochement=rapprochement):
                b = self.banc(depart=depart)
                jour = depart.date()
                b.extraction([ligne("FA-T13B", 8, jour, client="C900")], jour)
                b.rapprochement(rapprochement)
                b.litiges_maj([(jour - timedelta(days=3)).isoformat()])
                res = b.flux.executer()
                if accepte:
                    self.assertEqual((res.statut, sorted(b.propositions())), ("ok", ["FA-T13B|1"]))
                else:
                    self.assertEqual((res.statut, b.propositions()), ("refus", {}))
        absent = self.banc()
        absent.p("depot", "rapprochement.csv").unlink()
        absent.extraction([ligne("FA-T13B", 8, client="C900")])
        self.assertEqual((absent.flux.executer().statut, absent.propositions()), ("refus", {}), "date absente : aucune proposition")
        self.assertTrue(absent.alertes(GEST, "rapprochement"), "date absente : pas d'alerte")

    def test_T14_factures_sans_adresse(self):
        """T-14 · ENF-08 · 3 factures sans adresse plausible : jamais proposées, listées « à traiter à la main », sans adresse dans la trace"""
        b = self.banc()
        b.extraction([ligne("FA-T14-1", 9, client="C901", adresse=""), ligne("FA-T14-2", 9, client="C902", adresse="pas-d-adresse"),
                      ligne("FA-T14-3", 9, client="C903", adresse="   "), ligne("FA-T14-OK", 9, client="C904")])
        res = b.flux.executer()
        self.assertEqual(res.statut, "ok")
        self.assertEqual(sorted(b.propositions()), ["FA-T14-OK|1"])
        self.assertEqual(sorted(b.a_la_main()), ["FA-T14-1", "FA-T14-2", "FA-T14-3"])
        self.assertEqual(len(b.brouillons()), 1)
        self.assertEqual([int(x) for x in re.findall(r"\d+", [c for e, c in b.messages(GEST) if not e["Objet"].startswith("[alerte]")][0])][2], 3,
                         "le message du lundi ne dit pas qu'il y en a 3 à traiter à la main")
        for chemin in list(b.p("dispositif").glob("*.csv")) + list(b.p("plateforme").glob("*.csv")):
            self.assertTrue(sans_noms_ni_adresses(chemin.read_text(encoding="utf-8")), f"nom ou adresse dans {chemin.name}")

    # ------------------------------------------------------------------ T-15 à T-20 : pannes
    def test_T15_s2_coupe_dix_minutes(self):
        """T-15 · erreur passagère · S2 coupé 10 min au lancement : reprises espacées de 1, 5 puis 15 min, puis succès (60 §7)"""
        b = self.banc()
        b.classeur.panne_jusqua = LUNDI + timedelta(minutes=10)
        res = b.flux.executer()
        self.assertEqual(res.statut, "ok", res.messages)
        pauses = b.horloge.pauses
        self.assertGreaterEqual(len(pauses), 3, "moins de trois reprises")
        for reelle, nominale in zip(pauses[:3], (60, 300, 900)):
            self.assertAlmostEqual(reelle / nominale, 1.0, delta=0.11, msg=f"reprise de {reelle} s au lieu de {nominale} s ±10 %")
        self.assertEqual(len(b.brouillons()), SEANCE["propositions"])
        self.assertEqual(len(b.table("dispositif", "propositions")), SEANCE["propositions"])

    def test_T15b_flux_interrompu_au_milieu_des_brouillons(self):
        """T-15b · reprise après panne · processus arrêté net après 10 propositions : la relance ne double rien et ne perd rien"""
        b = self.banc()
        mort = cli("executer", b.racine, "2026-09-07T09:30:00", env={"FLUX_PLANTAGE": "ecriture-propositions:10"})
        self.assertEqual(mort.returncode, 137, mort.stdout + mort.stderr)
        self.assertEqual(len(b.brouillons()), 10)
        reprise = cli("executer", b.racine, "2026-09-07T10:05:00")  # plus de 30 minutes après : le verrou du processus mort est périmé
        self.assertEqual(reprise.returncode, 0, reprise.stdout + reprise.stderr)
        cles = [x.entetes["X-Relance-Id"] for x in b.brouillons()]
        self.assertEqual(len(cles), SEANCE["propositions"])
        self.assertEqual(len(set(cles)), SEANCE["propositions"], "un brouillon en double après la reprise")
        self.assertEqual(sorted(b.propositions()), sorted(cles))

    def test_T16_erreur_definitive_extraction_illisible(self):
        """T-16 · erreur définitive · extraction illisible : aucune reprise, file des échecs, alerte en moins de 5 min (60 §7)"""
        b = self.banc()
        b.p("depot", f"extraction-{JOUR.isoformat()}.csv").write_bytes(b"\xff\xfe\x00 pas un fichier d'extraction \x80\x81")
        res = b.flux.executer()
        self.assertEqual(res.statut, "echec")
        self.assertEqual(b.horloge.pauses, [], "l'erreur définitive a été reprise")
        self.assertTrue(b.echecs(), "rien dans la file des échecs")
        alertes = b.alertes(GEST)
        self.assertTrue(alertes, "aucune alerte à la gestionnaire clients")
        envoyee = datetime.fromisoformat(alertes[0][0]["Cree-le"])
        self.assertLessEqual(envoyee - LUNDI, timedelta(minutes=5))
        self.assertEqual(b.brouillons(), [])

    def test_T17_pointe_de_volume_et_plafond(self):
        """T-17 · pointe de volume, ENF-05 · 150 factures dont 90 propositions : traitées ; plus de 100 propositions : arrêt et alerte « volume anormal »"""
        # jeu 1 : 150 factures, 90 propositions et 60 payées
        b = self.banc()
        lignes = jeux.extraction_volume(90, JOUR) + [
            ligne("FA-2026-%04d" % (7000 + i), 9, client="C%03d" % (300 + i), paiement="rapprochée") for i in range(60)]
        self.assertEqual(len(lignes), 150)
        b.extraction(lignes)
        debut = time.perf_counter()
        res = b.flux.executer()
        duree = time.perf_counter() - debut
        self.assertEqual((res.statut, len(b.brouillons())), ("ok", 90))
        self.assertLess(duree, 300, "plus de 5 minutes pour 150 factures")
        # jeu 2 : exactement 100, puis 101 propositions
        for n, statut, brouillons in ((100, "ok", 100), (101, "volume", 0)):
            with self.subTest(propositions=n):
                c = self.banc()
                c.extraction(jeux.extraction_volume(n, JOUR))
                r = c.flux.executer()
                self.assertEqual((r.statut, len(c.brouillons())), (statut, brouillons))
                if statut == "volume":
                    self.assertEqual(c.propositions(), {}, "des propositions écrites malgré le plafond")
                    for role in (RESP, GEST):
                        self.assertTrue(c.alertes(role, "volume anormal"), f"{role} n'est pas alerté")

    def test_T18_interrupteur_en_cours_de_seance(self):
        """T-18 · ENF-10 · case « Suspendre » cochée : brouillons non envoyés supprimés, aucun nouveau, historique juste"""
        # (a) cochée après la création : les brouillons non envoyés disparaissent à la veille suivante, les envois restent consignés
        b = self.banc()
        b.flux.executer()
        envoyes = [a for a in b.attendu() if a["categorie"] == "envoyee"][:3]
        for a in envoyes:
            b.envoyer(f"{a['numero_facture']}|{a['niveau']}")
        b.commande(suspendre="oui")
        b.sonder()
        self.assertEqual(b.brouillons(), [], "des brouillons non envoyés sont restés")
        self.assertEqual(len(b.envoyes()), 3)
        etats = Counter(l["etat"] for l in b.propositions().values())
        self.assertEqual((etats["envoyée"], etats["supprimée"]), (3, SEANCE["propositions"] - 3))
        self.assertEqual(len([l for l in b.historique_lignes() if l["date_envoi"] == "2026-09-07"]), 3, "l'historique n'est plus juste")
        # (b) puis le flux lancé : plus rien de neuf
        b.horloge.avancer(minutes=5)
        res = b.flux.executer()
        self.assertEqual(res.statut, "suspendu")
        self.assertEqual(b.brouillons(), [])
        # (c) cochée pendant la création des brouillons : elle prend effet au plus tard au passage suivant de la veille
        c = self.banc(classeur_cls=ClasseurObservateur)
        c.classeur.apres_ecriture = lambda onglet, rang: c.commande(suspendre="oui") if (onglet, rang) == ("propositions", 10) else None
        c.flux.executer()
        c.sonder()
        self.assertEqual(c.brouillons(), [], "l'interrupteur coché en cours d'exécution n'a pas été appliqué")
        # (d) alerte sur silence : flux non lancé à 10 h
        d = self.banc()
        d.horloge.t = datetime(2026, 9, 7, 9, 50)
        avant = d.nb_alertes(RESP)
        d.flux.veiller()
        self.assertEqual(d.nb_alertes(RESP), avant, "alerte avant 10 h")
        d.horloge.t = datetime(2026, 9, 7, 10, 5)
        d.flux.veiller()
        self.assertEqual(d.nb_alertes(RESP), avant + 1, "pas d'alerte au responsable financier à 10 h")
        e = self.banc()
        e.flux.executer()  # lancé à 9 h 30
        e.horloge.t = datetime(2026, 9, 7, 10, 5)
        avant = e.nb_alertes(RESP)
        e.flux.veiller()
        self.assertEqual(e.nb_alertes(RESP), avant, "alerte de silence alors que le flux a tourné")

    def test_T19_pilote_en_parallele_etape_8(self):
        """T-19 · pilote, lundi 1 · étape 8 désactivée : aucune alerte, aucune ligne d'historique du flux ; remise en route : l'envoi est consigné"""
        b = self.banc()
        b.commande(etape8="non")
        b.horloge.t = datetime(2026, 9, 7, 10, 15)  # le flux est lancé après 10 h (70-plan, étape 19)
        b.flux.executer()
        avant_hist = len(b.historique_lignes())
        # la gestionnaire clients écrit et envoie ses propres courriels, avec l'objet convenu
        for a in [x for x in b.attendu() if x["categorie"] == "envoyee"][:5]:
            niv = int(a["niveau"])
            b.boite.deposer_envoye(GEST, "x.invalid", f"Facture {a['numero_facture']} — {b.regles()[f'libelle_niveau_{niv}']}", "texte écrit à la main")
        b.sonder()
        self.assertEqual(b.alertes(GEST, "identifiant introuvable"), [], "alerte « identifiant introuvable » alors que l'étape 8 est désactivée")
        self.assertEqual(len(b.historique_lignes()), avant_hist, "le flux a écrit dans l'historique étape 8 désactivée")
        self.assertEqual(b.table("dispositif", "envois-traites"), [])
        # un litige nouveau est toujours traité (étape 9 reste active) : le brouillon d'une facture est retiré
        cible = next(x for x in b.attendu() if x["categorie"] == "attente")
        b.ajouter_litige(cible["numero_facture"])
        b.sonder()
        self.assertEqual(b.brouillons_de(f"{cible['numero_facture']}|{cible['niveau']}"), [])
        # remise en route : un courriel envoyé depuis un brouillon met à jour sa proposition
        autre = next(x for x in b.attendu() if x["categorie"] == "petite")
        cle = f"{autre['numero_facture']}|{autre['niveau']}"
        b.envoyer(cle)
        b.commande(etape8="oui")
        b.sonder()
        self.assertEqual(b.propositions()[cle]["etat"], "envoyée")
        self.assertIn(autre["numero_facture"], {l["numero_facture"] for l in b.historique_lignes() if l["date_envoi"] == "2026-09-07"})

    def test_T20_pannes_longues_puis_reprise_le_lendemain(self):
        """T-20 · ENF-04, panne longue · S2 puis S3 coupés plusieurs heures le lundi ; relance le lendemain : un brouillon par clé, aucune oubliée"""
        b = self.banc()
        # S2 coupé toute la matinée
        b.classeur.panne_jusqua = LUNDI + timedelta(hours=4)
        res = b.flux.executer()
        self.assertEqual(res.statut, "echec")
        self.assertEqual((b.brouillons(), b.propositions()), ([], {}), "des écritures pendant la panne de S2")
        self.assertTrue(b.alertes(GEST), "la gestionnaire clients n'est pas alertée (panne de S2)")
        # S3 coupé quelques heures plus tard, S2 revenu
        b.classeur.panne_jusqua = None
        b.boite.panne_jusqua = b.horloge.maintenant() + timedelta(hours=4)
        res = b.flux.executer()
        self.assertEqual(res.statut, "echec")
        self.assertEqual((b.brouillons(), b.propositions()), ([], {}), "des brouillons ou des propositions à moitié créés pendant la panne de S3")
        self.assertGreaterEqual(len(b.alertes(GEST)), 2)
        # le lendemain : l'extraction est redéposée avec la date du jour et le rapprochement est refait
        b.boite.panne_jusqua = None
        b.horloge.t = datetime(2026, 9, 8, 9, 30)
        shutil.copyfile(b.p("depot", "extraction-2026-09-07.csv"), b.p("depot", "extraction-2026-09-08.csv"))
        b.rapprochement("2026-09-07")
        res = b.flux.executer()
        self.assertEqual(res.statut, "ok", res.messages)
        cles = [x.entetes["X-Relance-Id"] for x in b.brouillons()]
        attendues = sorted(f"{a['numero_facture']}|{a['niveau']}" for a in b.attendu() if a["issue"] in ("proposee", "mise_a_part"))
        self.assertEqual(sorted(cles), attendues, "une facture oubliée ou un brouillon en double après la reprise")

    def test_T21_entrees_hors_contrat(self):
        """T-21 · cas de refus, entrée hors contrat · colonne absente : rien traité ; J+60 proposée, J+61 écartée ; échéance vide et doublon à la main"""
        # colonne obligatoire absente
        b = self.banc()
        entetes = [c for c in jeux.ENTETES_EXTRACTION if c != "etat_paiement"]
        ecrire_csv(b.p("depot", f"extraction-{JOUR.isoformat()}.csv"), entetes,
                   [{k: v for k, v in ligne("FA-T21-0", 9).items() if k in entetes}])
        res = b.flux.executer()
        self.assertEqual((res.statut, b.brouillons(), b.propositions()), ("echec", [], {}))
        self.assertTrue(b.echecs() and b.alertes(GEST), "pas de file des échecs ou d'alerte")
        # J+60, J+61, échéance vide, numéro en double
        c = self.banc()
        vide = ligne("FA-T21-VIDE", 20, client="C904")
        vide["date_echeance"] = ""
        c.extraction([ligne("FA-T21-J60", 60, client="C901"), ligne("FA-T21-J61", 61, client="C902"), vide,
                      ligne("FA-T21-DOUBLON", 20, client="C905"), ligne("FA-T21-DOUBLON", 20, client="C905")])
        res = c.flux.executer()
        self.assertEqual(res.statut, "ok")
        self.assertEqual(sorted(c.propositions()), ["FA-T21-J60|1"], "J+60 est proposée, J+61 non, ni l'échéance vide ni le doublon")
        self.assertEqual(sorted(c.a_la_main()), ["FA-T21-DOUBLON", "FA-T21-VIDE"])
        self.assertEqual(c.motif_d_ecart("FA-T21-J61"), "au-delà de J+60")
        self.assertEqual(int(c.compteurs()[-1]["au_dela_j60"]), 1)

    def test_T22_changement_non_approuve(self):
        """T-22 · garde-fou « changement non approuvé » · modèle modifié hors procédure : aucune exécution ; approuvé : appliqué ; règle changée en cours : sans effet"""
        # (a) un modèle est modifié sans approbation
        b = self.banc()
        b.modifier_modele(2, "\nP.-S. ajouté hors procédure.\n")
        res = b.flux.executer()
        self.assertEqual(res.statut, "refus")
        self.assertEqual((b.brouillons(), b.propositions()), ([], {}), "des propositions malgré le changement non approuvé")
        for role in (RESP, GEST):
            self.assertTrue(b.alertes(role, "hors de la version approuvée"), f"{role} n'est pas alerté")
        # (b) le responsable financier approuve la nouvelle version : elle s'applique à l'exécution suivante
        b.modifier_regle("version", "R2")
        b.modifier_regle("delai_niveau_1", "10")
        b.approuver("R2")
        res = b.flux.executer()
        self.assertEqual(res.statut, "ok", res.messages)
        self.assertEqual({l["version_regles"] for l in b.journal() if l["etape"] == "4"}, {"R2"})
        niveau1 = [a for a in b.attendu() if int(a["niveau"]) == 1 and a["issue"] in ("proposee", "mise_a_part")]
        source = {l["numero_facture"]: l for l in lire_csv(b.p("depot", f"extraction-{JOUR.isoformat()}.csv"))}
        trop_jeunes = [a["numero_facture"] for a in niveau1 if (JOUR - date.fromisoformat(source[a["numero_facture"]]["date_echeance"])).days < 10]
        self.assertTrue(trop_jeunes, "le jeu ne contient aucune facture de niveau 1 de moins de 10 jours : test sans portée")
        for n in trop_jeunes:
            self.assertNotIn(f"{n}|1", b.propositions(), f"{n} (moins de 10 jours) est proposée : l'ancien délai s'applique encore")
        for l in [x for x in b.brouillons() if x.entetes["X-Relance-Id"].endswith("|2")]:
            self.assertIn("P.-S. ajouté hors procédure.", l.corps)
        # (c) une règle et un modèle changent pendant l'exécution : l'exécution en cours garde ceux du début
        c = self.banc(classeur_cls=ClasseurObservateur)

        def incident(onglet, rang):
            if (onglet, rang) == ("propositions", 5):
                c.modifier_regle("libelle_niveau_1", "rappel urgent")
                c.modifier_modele(1, "\nP.-S. ajouté pendant l'exécution.\n")

        c.classeur.apres_ecriture = incident
        res = c.flux.executer()
        self.assertEqual(res.statut, "ok")
        niveau1 = [x for x in c.brouillons() if x.entetes["X-Relance-Id"].endswith("|1")]
        self.assertGreater(len(niveau1), 6)
        for x in niveau1:
            self.assertNotIn("urgent", x.entetes["Objet"], f"{x.entetes['X-Relance-Id']} : la règle changée en cours d'exécution s'applique")
            self.assertNotIn("pendant l'exécution", x.corps)
        self.assertEqual({l["version_regles"] for l in c.journal() if l["etape"] == "4"}, {"R1"})
        res = c.flux.executer()  # la suivante est refusée : la modification n'est pas approuvée
        self.assertEqual(res.statut, "refus")

    def test_T23_copie_envoyee_retrouvee_par_l_objet(self):
        """T-23 · EF-11, Q-11 · objet conforme : proposition « envoyée » et une ligne ; objet modifié ou sans proposition : file des échecs et alerte"""
        b = self.banc()
        b.flux.executer()
        envoyees = [a for a in b.attendu() if a["categorie"] == "envoyee"]
        bon, modifie = envoyees[0], envoyees[1]
        cle_bon = f"{bon['numero_facture']}|{bon['niveau']}"
        b.envoyer(cle_bon)
        d = b.brouillon_de(f"{modifie['numero_facture']}|{modifie['niveau']}")
        chemin = b.p("boite", d.dossier, d.id + ".txt")
        chemin.write_text(chemin.read_text(encoding="utf-8").replace(d.entetes["Objet"], "Relance de la facture (objet retapé)"), encoding="utf-8")
        b.boite.envoyer(GEST, d.id)
        b.boite.deposer_envoye(GEST, "z.invalid", "Facture FA-2026-9999 — rappel de paiement", "pas de proposition pour cette facture")
        avant = len(b.historique_lignes())
        b.sonder()
        self.assertEqual(b.propositions()[cle_bon]["etat"], "envoyée")
        self.assertEqual(len(b.historique_lignes()) - avant, 1, "une seule ligne d'historique attendue")
        self.assertEqual(len(b.alertes(GEST, "identifiant introuvable")), 2)
        self.assertEqual(len([l for l in b.echecs() if l["etape"] == "8"]), 2)
        b.sonder()  # le même relevé une seconde fois
        self.assertEqual(len(b.historique_lignes()) - avant, 1, "ligne en double au second relevé")
        self.assertEqual(len(b.alertes(GEST, "identifiant introuvable")), 2, "alerte répétée au second relevé")
        self.assertEqual(len([l for l in b.echecs() if l["etape"] == "8"]), 2)

    def test_T24_historique_contradictoire(self):
        """T-24 · ENF-08 · facture à J+8 dont l'historique note une relance de niveau 2 : non proposée, « à traiter à la main »"""
        b = self.banc()
        b.historique([{"numero_facture": "FA-T24", "niveau": "2", "date_envoi": "2026-08-30", "expediteur": GEST}])
        b.extraction([ligne("FA-T24", 8, client="C901"), ligne("FA-T24-OK", 8, client="C902")])
        res = b.flux.executer()
        self.assertEqual(res.statut, "ok")
        self.assertEqual(sorted(b.propositions()), ["FA-T24-OK|1"])
        self.assertIn("FA-T24", b.a_la_main())
        self.assertTrue(b.a_la_main()["FA-T24"].strip(), "pas de motif")

    def test_T25_extraction_qui_n_est_pas_du_jour(self):
        """T-25 · cas de refus · l'extraction de la veille est déposée, celle du jour manque : jamais traitée ; reprises, échecs, alerte sous 30 min"""
        b = self.banc()
        b.p("depot", "extraction-2026-09-07.csv").rename(b.p("depot", "extraction-2026-08-31.csv"))
        res = b.flux.executer()
        self.assertEqual(res.statut, "echec")
        self.assertEqual((b.brouillons(), b.propositions()), ([], {}), "l'extraction ancienne a été traitée")
        self.assertEqual(len(b.horloge.pauses), 3, "trois reprises attendues")
        alertes = b.alertes(GEST)
        self.assertTrue(alertes and b.echecs())
        self.assertLessEqual(datetime.fromisoformat(alertes[0][0]["Cree-le"]) - LUNDI, timedelta(minutes=30))
        # l'extraction du jour arrive pendant les reprises : le traitement se fait, sur elle
        t = self.banc()
        a_deposer = t.p("depot", "extraction-2026-09-07.csv")
        reserve = t.p("depot", "reserve.csv")
        a_deposer.rename(reserve)
        original = t.horloge.dormir

        def dormir_puis_deposer(secondes):
            original(secondes)
            if len(t.horloge.pauses) == 1 and reserve.exists():
                reserve.rename(a_deposer)

        t.horloge.dormir = dormir_puis_deposer
        self.assertEqual(t.flux.executer().statut, "ok")
        self.assertEqual(len(t.brouillons()), SEANCE["propositions"])

    # ------------------------------------------------------------------ T-26 et suivants : tests ajoutés par la recette
    def test_T26_brouillon_supprime_a_la_main_la_facture_revient(self):
        """T-26 · EF-01 v1.1, 60 §2 et §4 · un brouillon supprimé à la main (petite facture) ne bloque pas la séance suivante : la facture revient"""
        j1, j2 = date(2026, 9, 7), date(2026, 9, 14)
        a, c_, d_ = "FA-T26-A", "FA-T26-B", "FA-T26-C"
        b = self.banc()
        b.historique([])
        b.comptes_cles([])
        b.extraction([ligne(a, 8, j1, client="C901"), ligne(c_, 9, j1, client="C902"), ligne(d_, 10, j1, client="C903")], j1)
        b.flux.executer()
        self.assertEqual(len(b.brouillons()), 3)
        ancien = b.brouillon_de(f"{c_}|1").id
        b.envoyer(f"{a}|1")  # envoyée
        b.boite.supprimer(GEST, ancien)  # supprimée à la main (la première phase n'a pas de seuil de montant)
        b.sonder()
        # lundi suivant : mêmes factures, 7 jours plus tard
        b.horloge.t = datetime(2026, 9, 14, 9, 30)
        b.rapprochement("2026-09-11")
        b.litiges_maj(["2026-09-11"])
        b.extraction([ligne(a, 15, j2, client="C901"), ligne(c_, 16, j2, client="C902"), ligne(d_, 17, j2, client="C903")], j2)
        res = b.flux.executer()
        self.assertEqual(res.statut, "ok", res.messages)
        self.assertEqual(b.brouillons_de(f"{a}|1"), [], "la facture relancée revient")
        revenue = b.brouillons_de(f"{c_}|1")
        self.assertEqual(len(revenue), 1, "la facture dont le brouillon a été supprimé n'est pas revenue sur la liste")
        self.assertNotEqual(revenue[0].id, ancien)
        self.assertEqual(len(b.brouillons_de(f"{d_}|1")), 1, "le brouillon laissé en place a été doublé")
        self.assertEqual(b.propositions()[f"{c_}|1"]["etat"], "brouillon créé")

    def test_T27_lecture_apres_ecriture(self):
        """T-27 · lecture après écriture, 60 §5 et §7 · un brouillon enregistré différemment est supprimé, sa clé va en échecs, la gestionnaire est alertée"""
        b = self.banc(boite_cls=BoiteQuiAbime)
        res = b.flux.executer()
        attendues = {f"{a['numero_facture']}|{a['niveau']}" for a in b.attendu() if a["issue"] in ("proposee", "mise_a_part")}
        presentes = {x.entetes["X-Relance-Id"] for x in b.brouillons()}
        manquante = attendues - presentes
        self.assertEqual(len(manquante), 1, f"un brouillon corrompu est resté, ou trop de brouillons manquent : {sorted(manquante)}")
        cle = manquante.pop()
        self.assertNotIn(cle, b.propositions(), "une proposition « brouillon créé » existe pour un brouillon corrompu")
        self.assertIn(cle, {l["cle"] for l in b.echecs()}, "la clé n'est pas dans la file des échecs")
        self.assertEqual(len(b.brouillons()), SEANCE["propositions"] - 1)
        self.assertTrue([1 for e, c in b.alertes(GEST) if cle in c], "la gestionnaire clients n'est pas alertée (erreur définitive, 60 §7)")

    def test_T28_pannes_en_cours_d_execution(self):
        """T-28 · erreur passagère · S2 puis S3 coupés 10 min pendant la création des brouillons : reprises, un brouillon par clé, aucun orphelin"""
        for service in ("S2", "S3"):
            with self.subTest(service=service):
                b = self.banc(classeur_cls=ClasseurObservateur)

                def incident(onglet, rang, b=b, service=service):
                    if (onglet, rang) == ("propositions", 10):
                        fin = b.horloge.maintenant() + timedelta(minutes=10)
                        if service == "S2":
                            b.classeur.panne_jusqua = fin
                        else:
                            b.boite.panne_jusqua = fin

                b.classeur.apres_ecriture = incident
                res = b.flux.executer()
                self.assertEqual(res.statut, "ok", res.messages)
                cles = [x.entetes["X-Relance-Id"] for x in b.brouillons()]
                self.assertEqual(len(cles), SEANCE["propositions"])
                self.assertEqual(len(set(cles)), SEANCE["propositions"], "brouillon en double")
                self.assertEqual(sorted(b.propositions()), sorted(cles), "brouillon orphelin ou proposition sans brouillon")
        # la veille pendant une panne de S3 : reprises, puis alerte, sans exception ; le passage suivant rattrape
        c = self.banc()
        c.flux.executer()
        un = next(a for a in c.attendu() if a["categorie"] == "envoyee")
        c.envoyer(f"{un['numero_facture']}|{un['niveau']}")
        c.boite.panne_jusqua = c.horloge.maintenant() + timedelta(hours=2)
        c.sonder()
        self.assertTrue(c.alertes(GEST, "indisponible"), "la panne de S3 pendant la veille n'est pas signalée")
        c.boite.panne_jusqua = None
        c.sonder()
        self.assertEqual(c.propositions()[f"{un['numero_facture']}|{un['niveau']}"]["etat"], "envoyée")

    def test_T29_plantage_autour_de_l_ecriture_d_un_brouillon(self):
        """T-29 · reprise après plantage · arrêt net juste après la création d'un brouillon, avant sa clé : un seul brouillon à la fin, « réconcilié »"""
        b = self.banc()
        mort = cli("executer", b.racine, "2026-09-07T09:30:00", env={"FLUX_PLANTAGE": "brouillon-cree:10"})
        self.assertEqual(mort.returncode, 137, mort.stdout + mort.stderr)
        self.assertEqual((len(b.brouillons()), len(b.propositions())), (10, 9), "le plantage n'a pas eu lieu entre le brouillon et sa clé")
        reprise = cli("executer", b.racine, "2026-09-07T10:05:00")  # plus de 30 minutes après : voir T-40 pour le verrou du processus mort
        self.assertEqual(reprise.returncode, 0, reprise.stdout + reprise.stderr)
        cles = [x.entetes["X-Relance-Id"] for x in b.brouillons()]
        self.assertEqual((len(cles), len(set(cles))), (SEANCE["propositions"], SEANCE["propositions"]), "brouillon en double ou perdu")
        self.assertEqual(sorted(b.propositions()), sorted(cles))
        self.assertEqual(len([l for l in b.journal() if "réconcil" in l["resultat"]]), 1, "le journal ne dit pas que l'état a été réconcilié")

    def test_T30_deux_executions_en_meme_temps(self):
        """T-30 · dédoublonnage, appel reçu deux fois · une exécution à la fois : la seconde est refusée ; un verrou de plus de 30 min est repris"""
        b = self.banc(classeur_cls=ClasseurObservateur)
        seconde = {}

        def pendant(onglet, rang):
            if (onglet, rang) == ("propositions", 5) and not seconde:
                seconde["res"] = fr.Flux(b.racine, b.classeur, b.boite, b.horloge).executer()

        b.classeur.apres_ecriture = pendant
        res = b.flux.executer()
        self.assertEqual(res.statut, "ok")
        self.assertEqual(seconde["res"].statut, "verrou", "la seconde exécution n'a pas été refusée")
        self.assertIn("déjà en cours", " ".join(seconde["res"].messages))
        cles = [x.entetes["X-Relance-Id"] for x in b.brouillons()]
        self.assertEqual((len(cles), len(set(cles))), (SEANCE["propositions"], SEANCE["propositions"]))
        self.assertFalse(b.p("dispositif", "verrou.txt").exists(), "le verrou n'est pas libéré")
        # un verrou posé il y a plus de 30 min (durée des reprises, 60 §7) ne peut plus être celui d'une exécution vivante
        v = self.banc()
        v.p("dispositif", "verrou.txt").write_text(fr.iso(LUNDI - timedelta(minutes=40)) + "\n", encoding="utf-8")
        self.assertEqual(v.flux.executer().statut, "ok")
        w = self.banc()
        w.p("dispositif", "verrou.txt").write_text(fr.iso(LUNDI - timedelta(minutes=5)) + "\n", encoding="utf-8")
        self.assertEqual((w.flux.executer().statut, w.brouillons()), ("verrou", []))

    def test_T31_envoi_rejoue_apres_une_panne(self):
        """T-31 · CA-09, EF-11 · arrêt net pendant l'écriture de l'historique (étape 8), puis relevé rejoué : 24 lignes, aucun doublon, aucune alerte"""
        for evenement in ("ecriture-historique:1", "ecriture-propositions:1"):
            with self.subTest(arret_apres=evenement):
                b = self.banc()
                b.flux.executer()
                envoyees = [a for a in b.attendu() if a["categorie"] == "envoyee"]
                for a in envoyees:
                    b.envoyer(f"{a['numero_facture']}|{a['niveau']}")
                mort = cli("sonder", b.racine, "2026-09-07T10:00:00", env={"FLUX_PLANTAGE": evenement})
                self.assertEqual(mort.returncode, 137, mort.stdout + mort.stderr)
                reprise = cli("sonder", b.racine, "2026-09-07T10:40:00")  # le verrou du processus mort est périmé (plus de 30 min)
                self.assertEqual(reprise.returncode, 0, reprise.stdout + reprise.stderr)
                nouvelles = [l for l in b.historique_lignes() if l["date_envoi"] == "2026-09-07"]
                self.assertEqual(len(nouvelles), SEANCE["envoyees"], "ligne d'historique en double ou manquante")
                self.assertEqual(len({(l["numero_facture"], l["niveau"]) for l in nouvelles}), SEANCE["envoyees"])
                self.assertEqual(Counter(l["etat"] for l in b.propositions().values())["envoyée"], SEANCE["envoyees"])
                self.assertEqual(len(b.table("dispositif", "envois-traites")), SEANCE["envoyees"])
                self.assertEqual(b.alertes(RESP, "double envoi"), [], "alerte « double envoi » à tort après la reprise")
                self.assertEqual(len(b.envoyes()), SEANCE["envoyees"], "un courriel de plus est parti")

    def test_T32_aucun_nom_ni_adresse_dans_les_traces(self):
        """T-32 · ENF-06, 60 §5 et §10 · journal, propositions, échecs, compteurs, messages aux personnes : ni nom ni adresse de contact"""
        b = self.banc()
        extraction = lire_csv(b.p("depot", f"extraction-{JOUR.isoformat()}.csv"))
        extraction += [ligne("FA-T32-1", 9, client="C901", adresse="", nom="Contact Inconnu"),
                       ligne("FA-T32-2", 9, client="C902", adresse="nom.prenom@societe-reelle.invalid", nom="Madame Test")]
        extraction[-1]["date_echeance"] = ""  # une erreur de donnée qui cite la facture
        b.extraction(extraction)
        b.flux.executer()
        b.sonder()
        b.p("depot", "extraction-2026-09-08.csv").write_bytes(b"\xff\xfe")  # une erreur définitive, le lendemain
        b.horloge.t = datetime(2026, 9, 8, 9, 30)
        b.rapprochement("2026-09-07")
        b.flux.executer()
        fichiers = (list(b.p("dispositif").glob("*.csv")) + list(b.p("plateforme").glob("*.csv"))
                    + list(b.p("boite", "messages").glob("*.txt")))
        self.assertGreaterEqual(len(fichiers), 8)
        for chemin in fichiers:
            self.assertTrue(sans_noms_ni_adresses(chemin.read_text(encoding="utf-8")), f"nom ou adresse dans {chemin.name}")
        self.assertTrue(any("@" in x.entetes.get("A", "") for x in b.brouillons()), "témoin : les brouillons, eux, portent l'adresse")

    def test_T33_aucun_secret_dans_la_livraison(self):
        """T-33 · secrets et données personnelles, 60 §9 · balayage de la livraison : rien à relire ; une clé fictive glissée dans une copie est trouvée"""
        r = balayer.balayer([LIVRAISON])
        total = sum(len(v) for v in r["trouvailles"].values())
        self.assertGreater(len(r["fichiers"]), 5, "le balayage n'a rien lu")
        self.assertEqual(total, 0, {k: v[:3] for k, v in r["trouvailles"].items() if v})
        # témoin positif : le balayage sait trouver
        copie = Path(tempfile.mkdtemp(prefix="balayage-"))
        try:
            shutil.copytree(LIVRAISON, copie / "livraison", ignore=shutil.ignore_patterns("__pycache__", "archives"))
            with open(copie / "livraison" / "flux_relances.py", "a", encoding="utf-8", newline="\n") as f:
                f.write(f'\nAPI_KEY = "{TEMOIN_CLE}"\n')
            trouve = balayer.balayer([copie / "livraison"])
            self.assertGreater(sum(len(v) for v in trouve["trouvailles"].values()), 0, "le balayage ne voit pas une clé glissée")
        finally:
            shutil.rmtree(copie, ignore_errors=True)

    def test_T34_retour_arriere(self):
        """T-34 · retour arrière, 60 §11 · la version 1.0 restaurée depuis son archive reprend l'état laissé par la version testée, sans rien doubler ni perdre"""
        archive = LIVRAISON / "archives" / "flux-relances-v1.0.zip"
        self.assertTrue(archive.exists(), "l'export de la version précédente manque")
        b = self.banc()
        b.flux.executer()
        envoyees = [a for a in b.attendu() if a["categorie"] == "envoyee"]
        for a in envoyees:
            b.envoyer(f"{a['numero_facture']}|{a['niveau']}")
        b.sonder()
        etat = (sorted(x.id for x in b.brouillons()), len(b.historique_lignes()))
        debut = time.perf_counter()
        dossier = Path(tempfile.mkdtemp(prefix="retour-arriere-"))
        try:
            with zipfile.ZipFile(archive) as z:
                z.extractall(dossier)
            ancienne = dossier / "flux_relances.py"
            controle = subprocess.run([sys.executable, "-X", "utf8", str(ancienne), "verifier-livraison"], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(controle.returncode, 0, controle.stdout)
            version = subprocess.run([sys.executable, "-X", "utf8", str(ancienne), "version"], capture_output=True, text=True, encoding="utf-8").stdout.strip()
            self.assertEqual(version, "flux_relances 1.0")
            lancement = subprocess.run([sys.executable, "-X", "utf8", str(ancienne), "executer", "--espace", str(b.racine),
                                        "--maintenant", "2026-09-07T11:00:00"], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(lancement.returncode, 0, lancement.stdout + lancement.stderr)
            veille = subprocess.run([sys.executable, "-X", "utf8", str(ancienne), "sonder", "--espace", str(b.racine),
                                     "--maintenant", "2026-09-07T11:10:00"], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(veille.returncode, 0, veille.stdout + veille.stderr)
        finally:
            shutil.rmtree(dossier, ignore_errors=True)
        duree = time.perf_counter() - debut
        self.assertEqual((sorted(x.id for x in b.brouillons()), len(b.historique_lignes())), etat,
                         "l'ancienne version a doublé ou perdu quelque chose")
        self.assertEqual(Counter(l["etat"] for l in b.propositions().values())["envoyée"], SEANCE["envoyees"])
        print(f"    [retour arrière essayé : {duree:.2f} s, archive restaurée, contrôlée, relancée sur l'état courant]")

    def test_T35_depot_et_pilotage_en_lecture_seule(self):
        """T-35 · permissions, 60 §6 · le flux n'écrit ni dans le dépôt ni dans le classeur de pilotage, seulement dans ses onglets"""
        b = self.banc()

        def etat():
            return (empreinte_arbre(b.p("depot")), empreinte_arbre(b.p("pilotage")), b.p("dispositif", "commande.csv").read_bytes())

        avant = etat()
        b.flux.executer()
        for a in [x for x in b.attendu() if x["categorie"] == "envoyee"][:5]:
            b.envoyer(f"{a['numero_facture']}|{a['niveau']}")
        b.sonder()
        self.assertEqual(etat(), avant, "le flux a écrit dans le dépôt, le pilotage ou la case « Suspendre »")
        b.ajouter_litige(next(x for x in b.attendu() if x["categorie"] == "attente")["numero_facture"])  # geste du support
        avant = etat()
        b.sonder()  # le brouillon du litige est retiré
        b.commande(suspendre="oui")  # geste de la gestionnaire clients
        avant = etat()
        b.sonder()
        b.flux.rejouer()
        self.assertEqual(etat(), avant, "le flux a écrit dans le dépôt, le pilotage ou la case « Suspendre »")
        self.assertTrue(set(b.classeur.ecritures) <= ONGLETS_ECRITS_PAR_LE_FLUX, set(b.classeur.ecritures) - ONGLETS_ECRITS_PAR_LE_FLUX)
        for onglet in ("litiges", "regles", "comptes-cles", "extraction-2026-09-07"):
            with self.assertRaises(fr.DroitRefuse, msg=onglet):
                b.classeur.ecrire_ligne(onglet, ("x",), {"x": "y"})

    def test_T36_litiges_sans_mise_a_jour(self):
        """T-36 · alertes, 60 §10 et R-05 · liste des litiges sans mise à jour depuis plus de 3 jours ouvrés : alerte ; mise à jour de vendredi : aucune"""
        b = self.banc()  # le jeu porte une mise à jour du vendredi 2026-09-04
        b.flux.executer()
        self.assertEqual([m for m in b.alertes(RESP) if "litige" in m[0]["Objet"] + m[1]], [], "alerte alors que la liste est à jour")
        v = self.banc()
        v.litiges_maj(["2026-08-31", "2026-09-01"])  # dernière mise à jour : mardi, quatre jours ouvrés avant le lundi
        res = v.flux.executer()
        self.assertEqual(res.statut, "ok")
        self.assertTrue(v.alertes(RESP, "litiges"), "pas d'alerte « litiges sans mise à jour »")

    def test_T37_liste_vide_suspecte_et_liste_vide_dite_telle(self):
        """T-37 · alertes, 60 §10 et cas vides de 60 §3 · factures de plus de 7 jours sans proposition ni motif : alerte ; extraction vide : dite telle"""
        b = self.banc()
        b.modifier_regle("version", "R2")
        b.modifier_regle("delai_niveau_1", "10")  # une règle qui ne laisse rien passer
        b.approuver("R2")
        b.extraction([ligne("FA-T37-1", 8, client="C901"), ligne("FA-T37-2", 9, client="C902")])
        res = b.flux.executer()
        self.assertEqual((res.statut, b.propositions(), b.brouillons()), ("ok", {}, []))
        self.assertTrue(b.alertes(RESP, "liste vide suspecte"), "pas d'alerte de liste vide suspecte")
        v = self.banc()
        v.extraction([])
        res = v.flux.executer()
        self.assertEqual(res.statut, "ok")
        avis = [c for e, c in v.messages(GEST) if not e["Objet"].startswith("[alerte]")]
        self.assertTrue(avis, "la gestionnaire clients n'est pas avertie d'une liste vide")
        self.assertEqual([int(x) for x in re.findall(r"\d+", avis[0])], [0, 0, 0])
        self.assertEqual(v.nb_alertes(RESP), 0, "alerte de liste vide suspecte sans aucune facture")

    def test_T38_file_des_echecs_rejouee(self):
        """T-38 · 60 §7 file des échecs · les clés cochées « rejouer » sont reprises seules, une fois ; un second rejeu ne fait rien ; rien n'est doublé"""
        b = self.banc()
        b.boite.panne_jusqua = LUNDI + timedelta(hours=4)
        self.assertEqual(b.flux.executer().statut, "echec")
        self.assertEqual(len(b.echecs()), SEANCE["propositions"])
        b.boite.panne_jusqua = None
        cc = {f"{a['numero_facture']}|{a['niveau']}" for a in b.attendu() if a["issue"] == "mise_a_part"}
        lignes = b.echecs()
        for l in lignes:
            l["rejouer"] = "oui" if l["cle"] in cc else "non"
        ecrire_csv(b.p("dispositif", "echecs.csv"), ["cle", "etape", "erreur", "heure", "execution", "rejouer", "etat"], lignes)
        res = b.flux.rejouer()
        self.assertEqual(res.statut, "ok", res.messages)
        self.assertEqual({x.entetes["X-Relance-Id"] for x in b.brouillons()}, cc, "le rejeu a créé autre chose que les clés cochées")
        etats = Counter(l["etat"] for l in b.echecs())
        self.assertEqual((etats["rejoué"], etats["ouvert"]), (SEANCE["comptes_cles"], SEANCE["propositions"] - SEANCE["comptes_cles"]))
        avant = len(b.brouillons())
        res = b.flux.rejouer()  # rien n'est coché : rien à rejouer
        self.assertEqual(len(b.brouillons()), avant)
        self.assertTrue(res.messages and "rien à rejouer" in res.messages[0])
        b.horloge.avancer(minutes=30)
        self.assertEqual(b.flux.executer().statut, "ok")  # un lancement complet derrière : aucune clé en double
        cles = [x.entetes["X-Relance-Id"] for x in b.brouillons()]
        self.assertEqual((len(cles), len(set(cles))), (SEANCE["propositions"], SEANCE["propositions"]))

    def test_T39_litige_signale_apres_le_depart_du_courriel(self):
        """T-39 · EF-04, CA-04, étape 9 · litige signalé alors que le courriel est déjà parti : le flux ne prétend pas avoir retiré un brouillon"""
        b = self.banc()
        b.flux.executer()
        un = next(a for a in b.attendu() if a["categorie"] == "envoyee")
        cle = f"{un['numero_facture']}|{un['niveau']}"
        b.envoyer(cle)  # la gestionnaire clients envoie
        b.ajouter_litige(un["numero_facture"])  # le support signale le litige dans la même fenêtre de 10 minutes
        b.sonder()
        self.assertEqual(len(b.envoyes()), 1)
        self.assertEqual(b.propositions()[cle]["etat"], "envoyée", "l'état de la proposition n'est pas celui du courriel parti")
        faux = [(e["Objet"], c) for e, c in b.messages(GEST) if un["numero_facture"] in c and "retir" in e["Objet"] + c]
        self.assertEqual(faux, [], "le flux dit avoir retiré un brouillon qui était déjà parti")
        # un brouillon supprimé à la main avant le litige : rien à retirer non plus
        autre = [a for a in b.attendu() if a["categorie"] == "envoyee"][1]
        cle2 = f"{autre['numero_facture']}|{autre['niveau']}"
        b.boite.supprimer(GEST, b.brouillon_de(cle2).id)
        b.ajouter_litige(autre["numero_facture"])
        b.sonder()
        faux = [(e["Objet"], c) for e, c in b.messages(GEST) if autre["numero_facture"] in c and "retir" in e["Objet"] + c]
        self.assertEqual(faux, [], "le flux dit avoir retiré un brouillon que la personne avait déjà supprimé")

    def test_T40_verrou_d_un_processus_mort(self):
        """T-40 · caractérisation (D-02) · après un arrêt net, la relance est refusée « une exécution est déjà en cours » jusqu'à 30 min, puis passe"""
        # Ce test fixe un comportement que 60 §7 ne décrit pas (« une exécution à la fois, un verrou l'impose ») pour que la
        # fiche d'exploitation dise la même chose : ce n'est pas un test de conformité.
        b = self.banc()
        mort = cli("executer", b.racine, "2026-09-07T09:30:00", env={"FLUX_PLANTAGE": "ecriture-propositions:3"})
        self.assertEqual(mort.returncode, 137, mort.stdout + mort.stderr)
        for heure, code in (("09:31:00", 1), ("09:59:00", 1), ("10:01:00", 0)):
            r = cli("executer", b.racine, f"2026-09-07T{heure}")
            self.assertEqual(r.returncode, code, f"{heure} : {r.stdout}{r.stderr}")
            if code == 1:
                self.assertIn("verrou", r.stdout)
        cles = [x.entetes["X-Relance-Id"] for x in b.brouillons()]
        self.assertEqual((len(cles), len(set(cles))), (SEANCE["propositions"], SEANCE["propositions"]))

    def test_T41_formats_d_entree(self):
        """T-41 · formats d'entrée, 60 §5 · colonnes permutées, fins de ligne Windows, caractères spéciaux, champ long, virgule : lus ; montant nul, négatif, illisible ou date non ISO : à la main"""
        b = self.banc()
        longue = "Madame Très-Longue " + "x" * 1000
        speciale = 'Dupont & Fils <SA> "Le Bœuf" {x} é'
        lignes = [ligne("FA-T41-VIRGULE", 9, client="C901"), ligne("FA-T41-SPECIAL", 9, client="C902", nom=speciale),
                  ligne("FA-T41-LONG", 9, client="C903", nom=longue),
                  ligne("FA-T41-ESPACES", 9, client="C904", adresse="  contact.c904@exemple-c904.invalid  "),
                  ligne("FA-T41-NUL", 9, client="C905", montant=0.0), ligne("FA-T41-NEG", 9, client="C906", montant=-12.5),
                  ligne("FA-T41-TEXTE", 9, client="C907"), ligne("FA-T41-DATE", 9, client="C908")]
        lignes[0]["montant_ht"] = "250,50"
        lignes[6]["montant_ht"] = "abc"
        lignes[7]["date_echeance"] = "07/09/2026"
        ordre = list(reversed(jeux.ENTETES_EXTRACTION))  # colonnes dans un autre ordre
        with open(b.p("depot", f"extraction-{JOUR.isoformat()}.csv"), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=ordre, lineterminator="\r\n")  # fins de ligne Windows
            w.writeheader()
            w.writerows(lignes)
        res = b.flux.executer()
        self.assertEqual(res.statut, "ok", res.messages)
        self.assertEqual(sorted(b.propositions()), ["FA-T41-ESPACES|1", "FA-T41-LONG|1", "FA-T41-SPECIAL|1", "FA-T41-VIRGULE|1"])
        self.assertEqual(sorted(b.a_la_main()), ["FA-T41-DATE", "FA-T41-NEG", "FA-T41-NUL", "FA-T41-TEXTE"])
        self.assertIn("250,50 € HT", b.brouillon_de("FA-T41-VIRGULE|1").corps)
        self.assertIn(f"Bonjour {speciale},", b.brouillon_de("FA-T41-SPECIAL|1").corps)
        self.assertIn(f"Bonjour {longue},", b.brouillon_de("FA-T41-LONG|1").corps)
        self.assertEqual(b.brouillon_de("FA-T41-ESPACES|1").entetes["A"], "contact.c904@exemple-c904.invalid")


# ==================================================================================================================
class Resultat(unittest.TextTestResult):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.statuts = {}

    def getDescription(self, test):
        return test.shortDescription() or test.id()

    def addSuccess(self, test):
        super().addSuccess(test)
        self.statuts[test.id()] = "réussi"

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.statuts[test.id()] = "ÉCHOUÉ"

    def addError(self, test, err):
        super().addError(test, err)
        self.statuts[test.id()] = "ERREUR"

    def addSubTest(self, test, subtest, err):
        super().addSubTest(test, subtest, err)
        if err is not None and self.statuts.get(test.id()) != "ERREUR":
            self.statuts[test.id()] = "ERREUR" if not issubclass(err[0], AssertionError) else "ÉCHOUÉ"


def court(chemin) -> str:
    """Un chemin sans le dossier personnel de la machine (les preuves ne portent pas de nom d'utilisateur)."""
    texte = str(chemin)
    exemple = str(RACINE_80.parent.parent.parent)  # .../examples/societe-exemple
    texte = texte.replace(exemple, "examples/societe-exemple")
    for racine in (Path(tempfile.gettempdir()), Path.home()):
        texte = texte.replace(str(racine), "<temp>" if racine == Path(tempfile.gettempdir()) else "~")
    return texte


def sha(chemin) -> str:
    return hashlib.sha256(Path(chemin).read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def main() -> int:
    for flux in (sys.stdout, sys.stderr):
        if hasattr(flux, "reconfigure"):
            flux.reconfigure(encoding="utf-8")
    ecarts = fr.verifier_livraison(LIVRAISON)
    print("Recette de la maquette flux_relances · test_recette.py")
    print(f"  exécution réelle : {datetime.now().isoformat(timespec='seconds')} · Python {sys.version.split()[0]}")
    print(f"  livraison testée : {court(LIVRAISON)}")
    print(f"  version du flux  : {fr.VERSION}")
    print(f"  flux_relances.py : SHA-256 {sha(LIVRAISON / 'flux_relances.py')}")
    print(f"  essai_s2_s3.py   : SHA-256 {sha(LIVRAISON / 'essai_s2_s3.py')}")
    if (LIVRAISON / "MANIFESTE.sha256").exists():
        print(f"  MANIFESTE.sha256 : SHA-256 {sha(LIVRAISON / 'MANIFESTE.sha256')}")
    print("  contrôle de la livraison contre son manifeste : " + ("conforme" if not ecarts else f"{len(ecarts)} écart(s) : {ecarts[:3]}"))
    print(f"  test_recette.py  : SHA-256 {sha(__file__)}")
    print()
    if sys.argv[1:]:  # `python test_recette.py T13 T10` : seulement ces tests
        suite = unittest.TestSuite()
        for nom in unittest.defaultTestLoader.getTestCaseNames(Recette):
            if any(nom == f"test_{a}" or nom.startswith(f"test_{a}_") for a in sys.argv[1:]):
                suite.addTest(Recette(nom))
    else:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Recette)
    res = unittest.TextTestRunner(stream=sys.stdout, verbosity=2, resultclass=Resultat).run(suite)
    comptes = Counter(res.statuts.values())
    print()
    print(f"BILAN : {res.testsRun} tests joués · {comptes['réussi']} réussis · {comptes['ÉCHOUÉ']} échoués · {comptes['ERREUR']} en erreur")
    return 0 if res.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
