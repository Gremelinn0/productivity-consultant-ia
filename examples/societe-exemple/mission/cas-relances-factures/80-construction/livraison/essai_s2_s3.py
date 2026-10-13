"""Doubles d'essai de S2 (classeurs) et de S3 (messagerie partagée de la finance), sur fichiers locaux.

Ils ne remplacent aucun outil réel : la plateforme sans code les remplacera par ses connecteurs. Ils
portent les propriétés que la spécification exige de ces deux systèmes (60 §6) :

- S2 : le classeur de pilotage et le dépôt sont en lecture seule ; le flux n'écrit que dans les onglets de
  son classeur du dispositif ; un verrou garantit une exécution à la fois ;
- S3 : le compte de service crée des brouillons et lit « Envoyés », mais n'a aucun droit d'envoi ; un
  brouillon porte un identifiant de relance qui ne survit pas à l'envoi (réponse à Q-11) ; les messages
  d'alerte partent par un compte distinct.

Chaque double sait tomber en panne pour les tests de reprise : `panne_jusqua` (indisponible jusqu'à cette heure
de l'horloge) et `crochet` (une fonction appelée avant chaque opération, qui peut déclencher une panne à un rang
précis). `plantage_possible` arrête le processus net, comme une coupure.
"""
from __future__ import annotations

import csv
import io
import os
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from flux_relances import (
    COMPTABLE, DOSSIER_COMPTES_CLES, DOSSIER_ENVOYES, DOSSIER_NORMAL, GESTIONNAIRE,
    RESPONSABLE_FINANCIER, SERVICE_ALERTE, SERVICE_MESSAGERIE, DroitRefuse, ErreurDefinitive,
    ErreurPassagere, iso,
)

ENTETES = {
    "propositions": ["cle", "numero_facture", "id_client", "niveau", "etat", "dossier", "id_brouillon",
                     "id_envoi", "horodatage", "execution"],
    "historique": ["numero_facture", "niveau", "date_envoi", "expediteur"],
    "echecs": ["cle", "etape", "erreur", "heure", "execution", "rejouer", "etat"],
    "commande": ["parametre", "valeur"],
    "journal": ["horodatage", "execution", "cle", "etape", "resultat", "detail", "version_flux", "version_regles"],
    "compteurs": ["date", "execution", "statut", "propositions", "creees", "comptes_cles", "payee",
                  "deja_relancee", "litige", "au_dela_j60", "a_la_main", "en_echec", "deja_fait"],
    "a-traiter-a-la-main": ["numero_facture", "motif", "date", "execution"],
    "envois-traites": ["id_message", "cle", "resultat", "horodatage"],
}


_COMPTE_PLANTAGE: Counter = Counter()


def plantage_possible(evenement: str) -> None:
    """Panne franche pour les essais de reprise : si `FLUX_PLANTAGE=<événement>:<rang>` est posé, le processus
    s'arrête net au rang voulu de cet événement, comme une coupure, sans rien nettoyer (ni verrou ni journal)."""
    nom, _, rang = os.environ.get("FLUX_PLANTAGE", "").partition(":")
    if nom != evenement:
        return
    _COMPTE_PLANTAGE[evenement] += 1
    if _COMPTE_PLANTAGE[evenement] >= int(rang or 1):
        os._exit(137)


# --------------------------------------------------------------------------------------------------
# S2 : classeurs de fichiers
# --------------------------------------------------------------------------------------------------
class ClasseurFichiers:
    """Zones : `depot` et `pilotage` en lecture seule, `dispositif` en lecture et écriture limitée aux
    onglets de `ENTETES`."""

    def __init__(self, racine, horloge):
        self.racine = Path(racine)
        self.horloge = horloge
        self.panne_jusqua: datetime | None = None
        self.crochet = None  # fonction(double) appelée avant chaque opération : essais de panne à un rang précis
        self.ecritures: list = []  # (onglet) : où le flux a écrit, pour les contrôles
        self.operations: Counter = Counter()  # un appel à ce double = une opération de la plateforme

    def _verifier_panne(self) -> None:
        if self.crochet is not None:
            self.crochet(self)
        if self.panne_jusqua is not None and self.horloge.maintenant() < self.panne_jusqua:
            raise ErreurPassagere("S2 indisponible")

    def _chemin(self, zone: str, nom: str) -> Path:
        return self.racine / zone / nom

    @staticmethod
    def _lire_csv(chemin: Path):
        try:
            texte = chemin.read_text(encoding="utf-8")
            lecteur = csv.DictReader(io.StringIO(texte, newline=""))
            lignes = [dict(l) for l in lecteur]
            return list(lecteur.fieldnames or []), lignes
        except (UnicodeDecodeError, csv.Error) as e:
            raise ErreurDefinitive(f"fichier illisible : {chemin.name}") from e

    # lecture --------------------------------------------------------------------------------------
    def lire(self, zone: str, onglet: str) -> list:
        self.operations["lecture"] += 1
        self._verifier_panne()
        chemin = self._chemin(zone, onglet + ".csv")
        if not chemin.exists():
            if zone == "dispositif" and onglet in ENTETES:
                return []
            raise ErreurPassagere(f"onglet illisible : {zone}/{onglet}")
        return self._lire_csv(chemin)[1]

    def lire_octets(self, zone: str, relatif: str) -> bytes:
        self.operations["lecture"] += 1
        self._verifier_panne()
        try:
            return self._chemin(zone, relatif).read_bytes()
        except OSError as e:
            raise ErreurPassagere(f"fichier illisible : {zone}/{relatif}") from e

    def existe_depot(self, nom: str) -> bool:
        self.operations["lecture"] += 1
        self._verifier_panne()
        return self._chemin("depot", nom).exists()

    def lire_depot(self, nom: str):
        """Rend (entêtes, lignes) ; fichier absent : erreur passagère (l'extraction n'est pas encore déposée)."""
        self.operations["lecture"] += 1
        self._verifier_panne()
        chemin = self._chemin("depot", nom)
        if not chemin.exists():
            raise ErreurPassagere(f"extraction absente : {nom}")
        return self._lire_csv(chemin)

    # écriture, limitée aux onglets du dispositif ---------------------------------------------------
    @staticmethod
    def _ecrire_csv(chemin: Path, entetes: list, lignes: list) -> None:
        chemin.parent.mkdir(parents=True, exist_ok=True)
        temporaire = chemin.with_name(chemin.name + ".tmp")
        with open(temporaire, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=entetes, lineterminator="\n")
            w.writeheader()
            for ligne in lignes:
                w.writerow({k: ligne.get(k, "") for k in entetes})
        os.replace(temporaire, chemin)

    def _onglet_ecrivable(self, onglet: str) -> list:
        if onglet not in ENTETES:
            raise DroitRefuse(f"écriture refusée hors des onglets du dispositif : {onglet}")
        return ENTETES[onglet]

    def ecrire_ligne(self, onglet: str, cle_champs: tuple, ligne: dict) -> None:
        """Mise à jour par clé ; insertion seulement si la clé n'existe pas (60 §8). Une opération."""
        self.ecrire_lignes(onglet, cle_champs, [ligne])

    def ecrire_lignes(self, onglet: str, cle_champs: tuple, lignes: list) -> None:
        """Mêmes règles pour un lot : une seule opération, quel que soit le nombre de lignes."""
        entetes = self._onglet_ecrivable(onglet)
        self.operations["ecriture"] += 1
        self._verifier_panne()
        chemin = self._chemin("dispositif", onglet + ".csv")
        existantes = self._lire_csv(chemin)[1] if chemin.exists() else []
        for ligne in lignes:
            neuve = {k: str(ligne.get(k, "")) for k in entetes}
            for i, existante in enumerate(existantes):
                if all(str(existante.get(c, "")) == neuve[c] for c in cle_champs):
                    existantes[i] = neuve
                    break
            else:
                existantes.append(neuve)
        self._ecrire_csv(chemin, entetes, existantes)
        self.ecritures.append(onglet)
        plantage_possible("ecriture-" + onglet)

    def ajouter(self, onglet: str, ligne: dict) -> None:
        self.ajouter_lot(onglet, [ligne])

    def ajouter_lot(self, onglet: str, lignes: list) -> None:
        """Ajoute des lignes à la suite : une seule opération pour le lot."""
        entetes = self._onglet_ecrivable(onglet)
        self.operations["ecriture"] += 1
        self._verifier_panne()
        chemin = self._chemin("dispositif", onglet + ".csv")
        chemin.parent.mkdir(parents=True, exist_ok=True)
        neuf = not chemin.exists()
        with open(chemin, "a", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=entetes, lineterminator="\n")
            if neuf:
                w.writeheader()
            for ligne in lignes:
                w.writerow({k: ligne.get(k, "") for k in entetes})
        self.ecritures.append(onglet)
        plantage_possible("ecriture-" + onglet)

    # verrou : une exécution à la fois (60 §7) ------------------------------------------------------
    def prendre_verrou(self, maintenant: datetime, perime_apres: int) -> bool:
        self.operations["verrou"] += 1
        chemin = self._chemin("dispositif", "verrou.txt")
        chemin.parent.mkdir(parents=True, exist_ok=True)
        try:
            fd = os.open(chemin, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            try:
                depuis = datetime.fromisoformat(chemin.read_text(encoding="utf-8").strip())
            except (ValueError, OSError):
                depuis = None
            if depuis is not None and (maintenant - depuis).total_seconds() <= perime_apres:
                return False
            chemin.write_text(iso(maintenant) + "\n", encoding="utf-8")  # verrou périmé : repris
            return True
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(iso(maintenant) + "\n")
        return True

    def liberer_verrou(self) -> None:
        self.operations["verrou"] += 1
        try:
            self._chemin("dispositif", "verrou.txt").unlink()
        except FileNotFoundError:
            pass

    # historique d'exécution de la plateforme : il existe même quand S2 est coupé --------------------
    def trace_plateforme(self, ligne: dict) -> None:
        chemin = self.racine / "plateforme" / "historique-execution.csv"
        chemin.parent.mkdir(parents=True, exist_ok=True)
        champs = ["horodatage", "execution", "cle", "etape", "resultat", "detail"]
        neuf = not chemin.exists()
        with open(chemin, "a", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=champs, lineterminator="\n")
            if neuf:
                w.writeheader()
            w.writerow({k: ligne.get(k, "") for k in champs})


# --------------------------------------------------------------------------------------------------
# S3 : boîte de messagerie simulée
# --------------------------------------------------------------------------------------------------
DROITS = {
    SERVICE_MESSAGERIE: {"creer_brouillon", "lire", "lister", "supprimer_brouillon"},
    SERVICE_ALERTE: {"poster_message"},
    GESTIONNAIRE: {"envoyer", "lire", "lister", "supprimer_brouillon"},
    COMPTABLE: {"envoyer", "lire", "lister", "supprimer_brouillon"},
    RESPONSABLE_FINANCIER: {"envoyer", "lire", "lister", "supprimer_brouillon"},
}
PREFIXES = {DOSSIER_NORMAL: "RL", DOSSIER_COMPTES_CLES: "CC", DOSSIER_ENVOYES: "EN", "messages": "MS"}
DOSSIERS_BROUILLONS = (DOSSIER_NORMAL, DOSSIER_COMPTES_CLES)


@dataclass
class Message:
    id: str
    dossier: str
    entetes: dict
    corps: str


class BoiteSimulee:
    """Les brouillons sont des fichiers de `boite/<dossier>/` ; rien ne part, jamais."""

    def __init__(self, racine, horloge):
        self.racine = Path(racine)
        self.horloge = horloge
        self.panne_jusqua: datetime | None = None
        self.crochet = None  # fonction(double) appelée avant chaque opération : essais de panne à un rang précis
        self.operations: Counter = Counter()  # appels des comptes de service : ce que la plateforme facturerait
        for dossier in PREFIXES:
            (self.racine / dossier).mkdir(parents=True, exist_ok=True)

    # ---- mécanique ------------------------------------------------------------------------------
    def _verifier_panne(self) -> None:
        if self.crochet is not None:
            self.crochet(self)
        if self.panne_jusqua is not None and self.horloge.maintenant() < self.panne_jusqua:
            raise ErreurPassagere("S3 indisponible")

    def _journaliser(self, operation: str, compte: str, dossier: str, id_message: str, detail: str = "") -> None:
        chemin = self.racine / "journal-boite.csv"
        neuf = not chemin.exists()
        with open(chemin, "a", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\n")
            if neuf:
                w.writerow(["horodatage", "operation", "compte", "dossier", "id", "detail"])
            w.writerow([iso(self.horloge.maintenant()), operation, compte, dossier, id_message, detail])

    def _droit(self, compte: str, droit: str) -> None:
        if compte in (SERVICE_MESSAGERIE, SERVICE_ALERTE):
            self.operations[compte] += 1
        if droit not in DROITS.get(compte, set()):
            self._journaliser("refus", compte, "", "", droit)
            raise DroitRefuse(f"le compte {compte} n'a pas le droit : {droit}")

    def _prochain_id(self, dossier: str) -> str:
        chemin = self.racine / "compteur.txt"
        n = int(chemin.read_text(encoding="utf-8").strip()) + 1 if chemin.exists() else 1
        chemin.write_text(str(n), encoding="utf-8")
        return f"{PREFIXES[dossier]}-{n:05d}"

    def _dossier_de(self, id_message: str) -> str:
        for dossier, prefixe in PREFIXES.items():
            if id_message.startswith(prefixe + "-"):
                return dossier
        raise ErreurDefinitive(f"identifiant de message inconnu : {id_message}")

    def _ecrire(self, dossier: str, id_message: str, entetes: dict, corps: str) -> None:
        lignes = [f"{k}: {v}" for k, v in entetes.items()]
        (self.racine / dossier / f"{id_message}.txt").write_text(
            "\n".join(lignes) + "\n\n" + corps, encoding="utf-8", newline="\n")

    def _relire(self, dossier: str, id_message: str) -> Message:
        chemin = self.racine / dossier / f"{id_message}.txt"
        try:
            texte = chemin.read_text(encoding="utf-8")
        except FileNotFoundError as e:
            raise ErreurDefinitive(f"message introuvable : {id_message}") from e
        tete, _, corps = texte.partition("\n\n")
        entetes = {}
        for ligne in tete.splitlines():
            cle, _, valeur = ligne.partition(": ")
            entetes[cle] = valeur
        return Message(id_message, dossier, entetes, corps)

    # ---- opérations du compte de service ----------------------------------------------------------
    def creer_brouillon(self, compte: str, dossier: str, destinataire: str, objet: str, corps: str, cle: str) -> str:
        self._droit(compte, "creer_brouillon")
        self._verifier_panne()
        if dossier not in DOSSIERS_BROUILLONS:
            raise ErreurDefinitive(f"dossier inconnu : {dossier}")
        id_message = self._prochain_id(dossier)
        self._ecrire(dossier, id_message, {
            "X-Relance-Id": cle, "A": destinataire, "Objet": objet, "Etat": "brouillon",
            "Cree-par": compte, "Cree-le": iso(self.horloge.maintenant())}, corps)
        self._journaliser("brouillon créé", compte, dossier, id_message, cle)
        plantage_possible("brouillon-cree")
        return id_message

    def chercher(self, compte: str, cle: str):
        """Cherche dans les dossiers de brouillons celui qui porte l'identifiant de relance."""
        self._droit(compte, "lister")
        self._verifier_panne()
        for dossier in DOSSIERS_BROUILLONS:
            for chemin in sorted((self.racine / dossier).glob("*.txt")):
                message = self._relire(dossier, chemin.stem)
                if message.entetes.get("X-Relance-Id") == cle:
                    return message
        return None

    def lire(self, compte: str, id_message: str) -> Message:
        self._droit(compte, "lire")
        self._verifier_panne()
        return self._relire(self._dossier_de(id_message), id_message)

    def lister(self, compte: str, dossier: str) -> list:
        self._droit(compte, "lister")
        self._verifier_panne()
        return [self._relire(dossier, p.stem) for p in sorted((self.racine / dossier).glob("*.txt"))]

    def supprimer(self, compte: str, id_message: str) -> None:
        self._droit(compte, "supprimer_brouillon")
        self._verifier_panne()
        dossier = self._dossier_de(id_message)
        if dossier not in DOSSIERS_BROUILLONS:
            raise DroitRefuse("seuls les brouillons se suppriment")
        chemin = self.racine / dossier / f"{id_message}.txt"
        if not chemin.exists():
            raise ErreurDefinitive(f"message introuvable : {id_message}")
        chemin.unlink()
        self._journaliser("brouillon supprimé", compte, dossier, id_message)

    # ---- opérations des personnes : le dispositif ne s'en sert jamais -------------------------------
    def envoyer(self, compte: str, id_message: str) -> str:
        """Une personne envoie un brouillon. Le compte de service n'en a pas le droit."""
        self._droit(compte, "envoyer")
        message = self._relire(self._dossier_de(id_message), id_message)
        nouveau = self._prochain_id(DOSSIER_ENVOYES)
        entetes = {k: v for k, v in message.entetes.items() if k not in ("X-Relance-Id", "Etat", "Cree-par")}
        entetes.update({"Etat": "envoyé", "Envoye-par": compte, "Envoye-le": iso(self.horloge.maintenant())})
        self._ecrire(DOSSIER_ENVOYES, nouveau, entetes, message.corps)
        (self.racine / message.dossier / f"{id_message}.txt").unlink()
        self._journaliser("envoyé", compte, message.dossier, nouveau, message.entetes.get("Objet", ""))
        return nouveau

    def deposer_envoye(self, compte: str, destinataire: str, objet: str, corps: str) -> str:
        """Une personne écrit et envoie un courriel sans passer par un brouillon du flux (lundi 1, en parallèle)."""
        self._droit(compte, "envoyer")
        nouveau = self._prochain_id(DOSSIER_ENVOYES)
        self._ecrire(DOSSIER_ENVOYES, nouveau, {
            "A": destinataire, "Objet": objet, "Etat": "envoyé", "Envoye-par": compte,
            "Envoye-le": iso(self.horloge.maintenant())}, corps)
        self._journaliser("envoyé à la main", compte, DOSSIER_ENVOYES, nouveau, objet)
        return nouveau

    # ---- messages d'alerte et d'information -------------------------------------------------------
    def poster_message(self, compte: str, role: str, objet: str, corps: str) -> str:
        """Les messages passent par le compte d'alerte, distinct de la boîte partagée : une panne de la boîte
        (`panne_jusqua`) ne les bloque pas, sans quoi l'alerte d'une panne de S3 ne partirait jamais."""
        self._droit(compte, "poster_message")
        id_message = self._prochain_id("messages")
        self._ecrire("messages", id_message, {
            "Pour": role, "Objet": objet, "Cree-le": iso(self.horloge.maintenant())}, corps)
        return id_message

    def messages(self, role: str | None = None) -> list:
        tous = [self._relire("messages", p.stem) for p in sorted((self.racine / "messages").glob("*.txt"))]
        return [m for m in tous if role is None or m.entetes.get("Pour") == role]
