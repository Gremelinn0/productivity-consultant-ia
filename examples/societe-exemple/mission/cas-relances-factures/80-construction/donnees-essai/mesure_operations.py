"""Mesure de la consommation de la maquette : combien d'opérations pour une semaine type (80, rubrique 9).

Une « opération » est un appel à l'un des deux doubles (lecture, écriture ou verrou du classeur ; création,
lecture, listage, suppression d'un brouillon ou envoi d'un message d'alerte dans la boîte). C'est la façon de
compter d'une plateforme à l'opération (page fictive de l'éditeur, `mission/sources/devis-et-page-editeur-2026-10-21.md`).
La maquette compte ses propres appels, pas ceux d'un connecteur réel : le relevé vaut `[F]` pour l'essai et
`[H]` pour la production.

Semaine type, calquée sur la séance du lundi 2026-09-07 :
- lundi 9 h 30 : exécution du flux (42 propositions) ;
- lundi de 9 h 40 à 12 h 00 : un passage de la veille (étapes 9 et 8) toutes les 10 minutes ;
  la gestionnaire clients envoie 2 brouillons par passage de 9 h 50 à 11 h 30 (24 relances, comme la séance) ;
  un litige est signalé à 10 h 35 ;
- lundi 10 h 00 : l'alerte sur silence regarde le journal ;
- mardi : le responsable financier envoie les 5 comptes clés, constatés au passage de 17 h ;
- mercredi, jeudi, vendredi : un passage de 17 h (étape 8 seule).

Commande : `python -X utf8 mesure_operations.py [--pas MINUTES]` ; code de sortie 0.
"""
from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
import time
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

ICI = Path(__file__).resolve().parent
LIVRAISON = ICI.parent / "livraison"
sys.path.insert(0, str(LIVRAISON))
sys.path.insert(0, str(ICI))

import flux_relances as fr  # noqa: E402
import jeux  # noqa: E402
from essai_s2_s3 import BoiteSimulee, ClasseurFichiers  # noqa: E402

MOIS_EN_SEMAINES = 52 / 12
QUOTA_PALIER_ENTREE = 1000  # opérations par mois incluses dans le palier de 20 € (page fictive de l'éditeur)


def total(classeur, boite) -> int:
    return sum(classeur.operations.values()) + sum(boite.operations.values())


def semaine(pas_minutes: int = 10) -> dict:
    racine = Path(tempfile.mkdtemp(prefix="mesure-"))
    try:
        jeux.ecrire_espace_modele(racine, LIVRAISON)
        lundi = datetime(2026, 9, 7, 9, 30)
        horloge = fr.HorlogeDeTest(lundi)
        classeur = ClasseurFichiers(racine, horloge)
        boite = BoiteSimulee(racine / "boite", horloge)
        flux = fr.Flux(racine, classeur, boite, horloge)
        postes: dict = {}

        def poste(nom: str, avant: int) -> None:
            postes[nom] = postes.get(nom, 0) + total(classeur, boite) - avant

        avant = total(classeur, boite)
        debut = time.perf_counter()
        res = flux.executer()
        duree = time.perf_counter() - debut
        poste("exécution du lundi (étapes 1 à 6)", avant)
        assert res.statut == "ok" and len(res.propositions) == 42, res.statut

        envois_restants = 24
        passages = 0
        passages_avec_travail = 0
        litige_pose = False
        silence_fait = False
        t = lundi
        fin = datetime(2026, 9, 7, 12, 0)
        while t < fin:
            t += timedelta(minutes=pas_minutes)
            horloge.t = t
            # la gestionnaire clients envoie 2 brouillons entre 9 h 50 et 11 h 30
            if envois_restants and datetime(2026, 9, 7, 9, 50) <= t <= datetime(2026, 9, 7, 11, 30):
                brouillons = boite.lister(fr.GESTIONNAIRE, fr.DOSSIER_NORMAL)
                for message in brouillons[:2]:
                    boite.envoyer(fr.GESTIONNAIRE, message.id)
                    envois_restants -= 1
            if not litige_pose and t >= datetime(2026, 9, 7, 10, 35):
                restants = [m for m in boite.lister(fr.GESTIONNAIRE, fr.DOSSIER_NORMAL)]
                numero = restants[-1].entetes["Objet"].split()[1]
                with open(racine / "pilotage" / "litiges.csv", "a", encoding="utf-8", newline="") as f:
                    f.write(f"{numero},2026-09-07\n")
                litige_pose = True
            avant = total(classeur, boite)
            bilan = flux.sonder()
            passages += 1
            ecart = total(classeur, boite) - avant
            if bilan:
                passages_avec_travail += 1
                postes["veille du lundi : passages avec travail"] = postes.get("veille du lundi : passages avec travail", 0) + ecart
            else:
                postes["veille du lundi : passages à vide"] = postes.get("veille du lundi : passages à vide", 0) + ecart
            if not silence_fait and t >= datetime(2026, 9, 7, 10, 0):
                avant = total(classeur, boite)
                flux.veiller()
                poste("alerte sur silence de 10 h", avant)
                silence_fait = True

        # mardi à vendredi : un passage à 17 h (étape 8 seule) ; mardi, les 5 comptes clés sont envoyés
        for jour in range(1, 5):
            horloge.t = datetime(2026, 9, 7 + jour, 17, 0)
            if jour == 1:
                for message in boite.lister(fr.RESPONSABLE_FINANCIER, fr.DOSSIER_COMPTES_CLES):
                    boite.envoyer(fr.RESPONSABLE_FINANCIER, message.id)
            avant = total(classeur, boite)
            flux.envois()
            poste("passage de 17 h, mardi à vendredi (étape 8)", avant)

        ops_semaine = total(classeur, boite)
        return {
            "postes": postes, "semaine": ops_semaine, "duree_lundi": duree, "passages_lundi": passages,
            "passages_avec_travail": passages_avec_travail, "par_type": Counter(classeur.operations) + Counter(boite.operations),
        }
    finally:
        shutil.rmtree(racine, ignore_errors=True)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser()
    p.add_argument("--pas", type=int, default=10, help="minutes entre deux passages de la veille (spécification : 10)")
    args = p.parse_args()
    r = semaine(args.pas)
    print(f"mesure_operations.py · maquette flux_relances {fr.VERSION} · pas de la veille {args.pas} min")
    for nom, valeur in r["postes"].items():
        print(f"  {valeur:4d}  {nom}")
    print(f"  ----\n  {r['semaine']:4d}  opérations pour la semaine type "
          f"({r['passages_lundi']} passages de la veille le lundi, dont {r['passages_avec_travail']} avec travail)")
    print(f"  durée de l'exécution du lundi par la maquette : {r['duree_lundi']:.2f} s (horloge réelle, 42 brouillons)")
    mois = r["semaine"] * MOIS_EN_SEMAINES
    print(f"  {mois:6.0f}  opérations par mois ({r['semaine']} × 52/12), quota du palier d'entrée : {QUOTA_PALIER_ENTREE}")
    print(f"  {100 * mois / QUOTA_PALIER_ENTREE:5.0f} %  du quota")
    return 0


if __name__ == "__main__":
    sys.exit(main())
