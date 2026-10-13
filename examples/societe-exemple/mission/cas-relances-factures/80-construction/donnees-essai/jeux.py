"""Jeux d'essai fictifs de l'environnement d'essai `essai-relances`.

Ce module fabrique l'espace de départ du rejeu de la séance du lundi 2026-09-07 (61 factures) et son
attendu. Il n'importe jamais le flux : l'attendu vient du décompte de la séance
(`mission/sources/seance-finance-2026-09-07.md`), pas de la sortie du programme. Tout est fictif :
clients, contacts et adresses sont des identifiants inventés (domaine réservé `.invalid`).

Bibliothèque standard seulement. Commande : `python -X utf8 jeux.py` (réécrit `espace-modele/`).
"""
from __future__ import annotations

import csv
import hashlib
import shutil
import sys
from datetime import date, timedelta
from pathlib import Path

ICI = Path(__file__).resolve().parent
SEANCE = date(2026, 9, 7)  # lundi
RAPPROCHEMENT_RECENT = date(2026, 9, 4)  # vendredi : un jour ouvré avant la séance
DELAIS = (7, 21, 35)

# Décompte de la séance du 2026-09-07 : catégorie, issue attendue, factures par niveau (n1, n2, n3).
# Somme : 61 factures ; 24 relances envoyées (14, 7, 3) ; 9 payées ; 4 déjà relancées ; 6 en litige ;
# 5 comptes clés ; 7 en attente du commercial ; 6 sous 15 €.
CATEGORIES = [
    ("envoyee", "proposee", (14, 7, 3)),
    ("payee", "payee", (5, 3, 1)),
    ("deja_relancee", "deja_relancee", (2, 1, 1)),
    ("litige", "litige", (4, 1, 1)),
    ("compte_cle", "mise_a_part", (3, 1, 1)),
    ("attente", "proposee", (5, 2, 0)),
    ("petite", "proposee", (4, 2, 0)),
]

# Âge en jours (plage) selon le niveau atteint ; les « déjà relancées » ont été relancées vendredi.
PLAGES = {1: (7, 13), 2: (21, 27), 3: (35, 41)}
PLAGES_DEJA = {1: (10, 13), 2: (24, 27), 3: (38, 41)}

ENTETES_EXTRACTION = [
    "numero_facture", "id_client", "nom_contact", "adresse_courriel",
    "montant_ht", "date_echeance", "etat_paiement",
]
ENTETES_HISTORIQUE = ["numero_facture", "niveau", "date_envoi", "expediteur"]


class Alea:
    """Générateur congruentiel linéaire : mêmes valeurs sur toutes les versions de Python."""

    def __init__(self, graine: int):
        self.etat = graine % (2 ** 64)

    def suivant(self) -> int:
        self.etat = (self.etat * 6364136223846793005 + 1442695040888963407) % (2 ** 64)
        return self.etat >> 33

    def entre(self, bas: int, haut: int) -> int:
        return bas + self.suivant() % (haut - bas + 1)

    def melanger(self, liste: list) -> list:
        liste = list(liste)
        for i in range(len(liste) - 1, 0, -1):
            j = self.suivant() % (i + 1)
            liste[i], liste[j] = liste[j], liste[i]
        return liste


def ecrire_csv(chemin: Path, entetes: list[str], lignes: list[dict]) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=entetes, lineterminator="\n")
        w.writeheader()
        for ligne in lignes:
            w.writerow({k: ligne.get(k, "") for k in entetes})


def sha256_lf(octets: bytes) -> str:
    return hashlib.sha256(octets.replace(b"\r\n", b"\n")).hexdigest()


def empreinte_modeles(dossier_modeles: Path) -> str:
    morceaux = [p.read_bytes().replace(b"\r\n", b"\n") for p in sorted(dossier_modeles.glob("niveau-*.txt"))]
    return hashlib.sha256(b"".join(morceaux)).hexdigest()


def ligne_facture(numero: str, age: int, jour: date = SEANCE, client: str = "C900",
                  montant: float = 250.0, paiement: str = "non rapprochée",
                  adresse: str | None = None, nom: str | None = None) -> dict:
    """Une ligne d'extraction fictive ; `age` en jours depuis l'échéance."""
    cl = client.lower()
    return {
        "numero_facture": numero,
        "id_client": client,
        "nom_contact": nom if nom is not None else f"Contact {client}",
        "adresse_courriel": adresse if adresse is not None else f"contact.{cl}@exemple-{cl}.invalid",
        "montant_ht": f"{montant:.2f}",
        "date_echeance": (jour - timedelta(days=age)).isoformat(),
        "etat_paiement": paiement,
    }


def rejeu() -> dict:
    """Les 61 factures de la séance du 2026-09-07 et tout ce qui les entoure."""
    a = Alea(20260907)
    paires = []
    for categorie, issue, par_niveau in CATEGORIES:
        for niveau, n in enumerate(par_niveau, start=1):
            paires.extend([(categorie, issue, niveau)] * n)
    assert len(paires) == 61
    paires = a.melanger(paires)

    cles_clients = ["C%03d" % n for n in range(1, 26)]  # 25 comptes clés (liste écrite)
    comptes_cles_utilises = a.melanger(cles_clients)[:5]

    extraction, historique, litiges, attendu = [], [], [], []
    for rang, (categorie, issue, niveau) in enumerate(paires):
        numero = "FA-2026-%04d" % (1200 + 3 * rang)
        plage = PLAGES_DEJA[niveau] if categorie == "deja_relancee" else PLAGES[niveau]
        age = a.entre(*plage)
        if categorie == "compte_cle":
            client = comptes_cles_utilises.pop()
        else:
            client = "C%03d" % (26 + (rang * 7) % 60)
        if categorie == "petite":
            montant = a.entre(620, 1490) / 100
        else:
            montant = a.entre(8000, 450000) / 100
        paiement = "rapprochée" if categorie == "payee" else "non rapprochée"
        extraction.append(ligne_facture(numero, age, client=client, montant=montant, paiement=paiement))
        echeance = SEANCE - timedelta(days=age)

        derniers = niveau if categorie == "deja_relancee" else niveau - 1
        for k in range(1, derniers + 1):
            if categorie == "deja_relancee" and k == niveau:
                envoi = RAPPROCHEMENT_RECENT  # relancée vendredi, notée dans l'historique
                qui = "comptable"
            else:
                envoi = echeance + timedelta(days=DELAIS[k - 1] + a.entre(0, 3))
                qui = "gestionnaire clients"
            historique.append({"numero_facture": numero, "niveau": k, "date_envoi": envoi.isoformat(), "expediteur": qui})
        if categorie == "litige":
            ouverture = SEANCE - timedelta(days=a.entre(3, 7))
            litiges.append({"numero_facture": numero, "date_ouverture": ouverture.isoformat()})

        attendu.append({
            "numero_facture": numero,
            "id_client": client,
            "categorie": categorie,
            "niveau": niveau,
            "issue": issue,
            "dossier": ("Comptes clés à valider" if issue == "mise_a_part"
                        else "Relances du lundi" if issue == "proposee" else ""),
        })

    # Bruit : anciennes relances et anciens litiges d'autres factures, absentes de l'extraction du jour.
    for i in range(30):
        numero = "FA-2026-%04d" % (700 + 5 * i)
        envoi = date(2026, 6, 1) + timedelta(days=a.entre(0, 60))
        historique.append({"numero_facture": numero, "niveau": a.entre(1, 3), "date_envoi": envoi.isoformat(),
                           "expediteur": "gestionnaire clients"})
    for i in range(4):
        numero = "FA-2026-%04d" % (650 + 9 * i)
        litiges.append({"numero_facture": numero, "date_ouverture": "2026-07-%02d" % (3 + 5 * i)})

    return {
        "extraction": extraction,
        "historique": historique,
        "litiges": litiges,
        "comptes_cles": cles_clients,
        "attendu": attendu,
    }


def extraction_volume(nombre: int, jour: date, graine: int = 7) -> list[dict]:
    """Une extraction de `nombre` factures toutes au niveau 1, pour la pointe de volume (T-17)."""
    a = Alea(graine)
    lignes = []
    for i in range(nombre):
        lignes.append(ligne_facture("FA-2026-%04d" % (5000 + i), a.entre(7, 13), jour=jour,
                                    client="C%03d" % (100 + i), montant=a.entre(8000, 450000) / 100))
    return lignes


def ecrire_espace_modele(dest: Path, livraison: Path) -> dict:
    """Écrit l'espace de départ du rejeu dans `dest` (remis à zéro). Rend le jeu et les empreintes."""
    if dest.exists():
        shutil.rmtree(dest)
    jeu = rejeu()
    jour = SEANCE
    ecrire_csv(dest / "depot" / f"extraction-{jour.isoformat()}.csv", ENTETES_EXTRACTION, jeu["extraction"])
    ecrire_csv(dest / "depot" / "rapprochement.csv", ["date_rapprochement", "role"],
               [{"date_rapprochement": RAPPROCHEMENT_RECENT.isoformat(), "role": "comptable"}])
    ecrire_csv(dest / "pilotage" / "litiges.csv", ["numero_facture", "date_ouverture"], jeu["litiges"])
    ecrire_csv(dest / "pilotage" / "litiges-maj.csv", ["date", "role"],
               [{"date": d, "role": "responsable du support"}
                for d in ("2026-08-31", "2026-09-01", "2026-09-02", "2026-09-03", "2026-09-04")])
    ecrire_csv(dest / "pilotage" / "comptes-cles.csv", ["id_client"], [{"id_client": c} for c in jeu["comptes_cles"]])
    shutil.copyfile(livraison / "regles-v1.0.csv", dest / "pilotage" / "regles.csv")
    (dest / "pilotage" / "modeles").mkdir(parents=True, exist_ok=True)
    for p in sorted((livraison / "modeles").glob("niveau-*.txt")):
        shutil.copyfile(p, dest / "pilotage" / "modeles" / p.name)
    ecrire_csv(dest / "pilotage" / "approbation.csv",
               ["version", "date", "empreinte_regles", "empreinte_modeles"],
               [{"version": "R1", "date": "2026-10-28",
                 "empreinte_regles": sha256_lf((dest / "pilotage" / "regles.csv").read_bytes()),
                 "empreinte_modeles": empreinte_modeles(dest / "pilotage" / "modeles")}])
    ecrire_csv(dest / "dispositif" / "historique.csv", ENTETES_HISTORIQUE, jeu["historique"])
    ecrire_csv(dest / "dispositif" / "commande.csv", ["parametre", "valeur"],
               [{"parametre": "suspendre", "valeur": "non"}, {"parametre": "etape8_active", "valeur": "oui"}])
    ecrire_csv(dest / "attendu" / "rejeu-2026-09-07.csv",
               ["numero_facture", "id_client", "categorie", "niveau", "issue", "dossier"], jeu["attendu"])
    return jeu


def main() -> int:
    livraison = ICI.parent / "livraison"
    jeu = ecrire_espace_modele(ICI / "espace-modele", livraison)
    par_issue: dict[str, int] = {}
    for ligne in jeu["attendu"]:
        par_issue[ligne["issue"]] = par_issue.get(ligne["issue"], 0) + 1
    print("espace-modele écrit :", len(jeu["extraction"]), "factures ;", par_issue)
    return 0


if __name__ == "__main__":
    sys.exit(main())
