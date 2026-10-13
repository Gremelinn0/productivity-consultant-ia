"""Contrôles de tranche de la maquette `essai-relances` (80-construction.md, rubrique 5).

Ce sont les contrôles du constructeur : ils vérifient qu'une tranche fait ce qu'elle doit pour passer à la
suivante. Ils ne déclarent aucun critère d'acceptation « réussi » : la recette (`85-recette/`) le fait, sur la
version gelée, avec des attendus tirés de `60-specification.md` et du décompte de la séance.

Commande : `python -X utf8 controles_tranches.py` (depuis ce dossier). Code de sortie 0 si tous les contrôles
passent, 1 sinon. Chaque contrôle écrit une ligne : tranche, résultat, ce qui a été constaté.
"""
from __future__ import annotations

import csv
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

ICI = Path(__file__).resolve().parent
LIVRAISON = ICI.parent / "livraison"
sys.path.insert(0, str(LIVRAISON))
sys.path.insert(0, str(ICI))

import flux_relances as fr  # noqa: E402
import jeux  # noqa: E402
from essai_s2_s3 import BoiteSimulee, ClasseurFichiers  # noqa: E402

LUNDI = datetime(2026, 9, 7, 9, 30)
RESULTATS: list = []


def controle(tranche: int, nom: str, condition: bool, constat: str) -> None:
    RESULTATS.append((tranche, nom, bool(condition), constat))
    print(f"[tranche {tranche}] {'OK    ' if condition else 'ÉCHEC '} {nom} : {constat}")


def monter(depart: datetime = LUNDI):
    """Un espace d'essai neuf, une horloge de test, le flux branché sur les doubles."""
    racine = Path(tempfile.mkdtemp(prefix="essai-relances-"))
    jeux.ecrire_espace_modele(racine, LIVRAISON)
    horloge = fr.HorlogeDeTest(depart)
    classeur = ClasseurFichiers(racine, horloge)
    boite = BoiteSimulee(racine / "boite", horloge)
    return racine, horloge, classeur, boite, fr.Flux(racine, classeur, boite, horloge)


def lire(racine: Path, zone: str, nom: str) -> list:
    chemin = racine / zone / (nom + ".csv")
    if not chemin.exists():
        return []
    with open(chemin, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def nombre_brouillons(racine: Path) -> int:
    return sum(len(list((racine / "boite" / d).glob("*.txt"))) for d in (fr.DOSSIER_NORMAL, fr.DOSSIER_COMPTES_CLES))


def tranche_0() -> None:
    racine, horloge, classeur, boite, flux = monter()
    # Lancement à vide : on vide la liste des factures, le flux doit tourner de bout en bout et le dire.
    jeux.ecrire_csv(racine / "depot" / "extraction-2026-09-07.csv", jeux.ENTETES_EXTRACTION, [])
    res = flux.executer()
    journal = lire(racine, "dispositif", "journal")
    etapes = [(l["etape"], l["resultat"]) for l in journal]
    controle(0, "lancement à vide", res.statut == "ok" and ("0", "début") in etapes and ("fin", "ok") in etapes,
             f"statut {res.statut}, {len(journal)} lignes au journal, début et fin présents")
    controle(0, "aucun brouillon, message d'avertissement posté", nombre_brouillons(racine) == 0
             and len(boite.messages(fr.GESTIONNAIRE)) == 1,
             f"{nombre_brouillons(racine)} brouillon, {len(boite.messages(fr.GESTIONNAIRE))} message à la gestionnaire clients")
    shutil.rmtree(racine)

    # Case « Suspendre » cochée : rien n'est créé.
    racine, horloge, classeur, boite, flux = monter()
    (racine / "dispositif" / "commande.csv").write_text("parametre,valeur\nsuspendre,oui\netape8_active,oui\n", encoding="utf-8")
    res = flux.executer()
    controle(0, "case « Suspendre » cochée", res.statut == "suspendu" and nombre_brouillons(racine) == 0,
             f"statut {res.statut}, {nombre_brouillons(racine)} brouillon")
    shutil.rmtree(racine)

    # Verrou : une seconde exécution pendant la première est refusée.
    racine, horloge, classeur, boite, flux = monter()
    classeur.prendre_verrou(horloge.maintenant(), 1800)
    res = flux.executer()
    controle(0, "verrou : une exécution à la fois", res.statut == "verrou" and nombre_brouillons(racine) == 0,
             f"statut {res.statut}, aucun brouillon")
    shutil.rmtree(racine)

    # Isolement : le compte de service n'envoie pas, n'écrit pas hors de ses onglets, n'a pas de mode réel.
    racine, horloge, classeur, boite, flux = monter()
    flux.executer()
    un_brouillon = boite.lister(fr.SERVICE_MESSAGERIE, fr.DOSSIER_NORMAL)[0]
    refus_envoi = refus_ecriture = False
    try:
        boite.envoyer(fr.SERVICE_MESSAGERIE, un_brouillon.id)
    except fr.DroitRefuse:
        refus_envoi = True
    try:
        classeur.ecrire_ligne("litiges", ("numero_facture",), {"numero_facture": "FA-X"})
    except fr.DroitRefuse:
        refus_ecriture = True
    sortie = subprocess.run([sys.executable, "-X", "utf8", str(LIVRAISON / "flux_relances.py"), "executer",
                             "--espace", str(racine), "--mode", "reel"], capture_output=True, text=True, encoding="utf-8")
    controle(0, "isolement : envoi refusé, écriture hors onglets refusée, mode réel refusé",
             refus_envoi and refus_ecriture and sortie.returncode == 2 and (racine / "boite" / "Envoyés").exists()
             and not list((racine / "boite" / "Envoyés").glob("*.txt")),
             f"envoi refusé {refus_envoi}, écriture refusée {refus_ecriture}, mode réel : code {sortie.returncode}, "
             f"« Envoyés » vide")
    refus = [l for l in open(racine / "boite" / "journal-boite.csv", encoding="utf-8") if "refus" in l]
    controle(0, "la tentative d'envoi est consignée", len(refus) >= 1, f"{len(refus)} ligne « refus » au journal de la boîte")
    shutil.rmtree(racine)


def tranche_1() -> None:
    racine, horloge, classeur, boite, flux = monter()
    res = flux.executer()
    total = len(res.propositions) + len(res.ecartees) + len(res.a_la_main)
    controle(1, "extraction du jour lue, liste candidate complète", total == 61 and res.statut == "ok",
             f"{len(res.propositions)} propositions + {len(res.ecartees)} écartées + {len(res.a_la_main)} à la main = {total}")
    niveaux = sorted({p.niveau for p in res.propositions})
    controle(1, "niveaux proposés dans 1 à 3", niveaux == [1, 2, 3], f"niveaux {niveaux}")
    shutil.rmtree(racine)

    # Rapprochement trop ancien : jeudi 2026-09-03 pour un lundi 2026-09-07.
    racine, horloge, classeur, boite, flux = monter()
    jeux.ecrire_csv(racine / "depot" / "rapprochement.csv", ["date_rapprochement", "role"],
                    [{"date_rapprochement": "2026-09-03", "role": "comptable"}])
    res = flux.executer()
    controle(1, "rapprochement trop ancien : aucune proposition", res.statut == "refus" and nombre_brouillons(racine) == 0
             and len(res.propositions) == 0, f"statut {res.statut}, {nombre_brouillons(racine)} brouillon")
    alertes = [m.entetes["Objet"] for m in boite.messages(fr.GESTIONNAIRE)]
    controle(1, "…et le motif est lisible par la gestionnaire clients", "[alerte] rapprochement trop ancien" in alertes,
             f"alerte reçue : {alertes}")
    shutil.rmtree(racine)

    # Vendredi → lundi : un jour ouvré, accepté.
    racine, horloge, classeur, boite, flux = monter()
    res = flux.executer()
    controle(1, "rapprochement du vendredi accepté un lundi", res.statut == "ok", f"statut {res.statut}")
    shutil.rmtree(racine)

    # Colonne obligatoire absente : erreur définitive, aucune reprise.
    racine, horloge, classeur, boite, flux = monter()
    (racine / "depot" / "extraction-2026-09-07.csv").write_text("numero_facture,id_client\nFA-1,C1\n", encoding="utf-8")
    res = flux.executer()
    controle(1, "colonne absente : arrêt sans reprise", res.statut == "echec" and not horloge.pauses,
             f"statut {res.statut}, pauses {horloge.pauses}")
    shutil.rmtree(racine)


def tranche_2() -> None:
    racine, horloge, classeur, boite, flux = monter()
    res = flux.executer()
    motifs = {}
    for _, _, motif in res.ecartees:
        motifs[motif] = motifs.get(motif, 0) + 1
    controle(2, "écarts par motif", motifs == {"payée": 9, "déjà relancée": 4, "litige": 6},
             f"{motifs}")
    cles = [p for p in res.propositions if p.compte_cle]
    controle(2, "comptes clés mis à part", len(cles) == 5, f"{len(cles)} propositions de compte clé")
    journal = lire(racine, "dispositif", "journal")
    avec_motif = [l for l in journal if l["etape"] == "4" and l["resultat"] == "écartée" and l["detail"]]
    controle(2, "motif de chaque écart au journal", len(avec_motif) == 19, f"{len(avec_motif)} lignes d'écart avec motif")
    shutil.rmtree(racine)


def tranche_3() -> None:
    racine, horloge, classeur, boite, flux = monter()
    res = flux.executer()
    normaux = len(list((racine / "boite" / fr.DOSSIER_NORMAL).glob("*.txt")))
    cles = len(list((racine / "boite" / fr.DOSSIER_COMPTES_CLES).glob("*.txt")))
    controle(3, "brouillons créés dans les deux dossiers", (normaux, cles) == (37, 5), f"{normaux} + {cles}")
    sorties = [m for m in boite.lister(fr.GESTIONNAIRE, fr.DOSSIER_NORMAL)]
    objet_ok = all(m.entetes["Objet"].startswith("Facture FA-2026-") for m in sorties)
    controle(3, "chaque brouillon porte son niveau dans l'objet", objet_ok, f"{len(sorties)} objets lus")
    propositions = lire(racine, "dispositif", "propositions")
    controle(3, "une proposition par brouillon, état relu", len(propositions) == 42
             and all(p["etat"] == "brouillon créé" for p in propositions), f"{len(propositions)} propositions")
    # Deuxième lancement : rien de nouveau.
    horloge.avancer(minutes=10)
    flux2 = fr.Flux(racine, classeur, boite, horloge)
    res2 = flux2.executer()
    controle(3, "flux lancé deux fois : aucun doublon", nombre_brouillons(racine) == 42 and res2.compteurs["creees"] == 0
             and res2.compteurs["deja_fait"] == 42, f"{nombre_brouillons(racine)} brouillons, {res2.compteurs['deja_fait']} déjà faits")
    shutil.rmtree(racine)

    # Arrêt net entre l'écriture du brouillon et celle de la proposition (processus tué), puis reprise.
    racine = Path(tempfile.mkdtemp(prefix="essai-relances-"))
    jeux.ecrire_espace_modele(racine, LIVRAISON)
    env = dict(os.environ, FLUX_PLANTAGE="brouillon-cree:10")
    sortie = subprocess.run([sys.executable, "-X", "utf8", str(LIVRAISON / "flux_relances.py"), "executer", "--espace",
                             str(racine), "--maintenant", "2026-09-07T09:30:00"], capture_output=True, text=True,
                            encoding="utf-8", env=env)
    avant_b, avant_p = nombre_brouillons(racine), len(lire(racine, "dispositif", "propositions"))
    horloge = fr.HorlogeDeTest(datetime(2026, 9, 7, 10, 15))
    classeur = ClasseurFichiers(racine, horloge)
    boite = BoiteSimulee(racine / "boite", horloge)
    res = fr.Flux(racine, classeur, boite, horloge).executer()
    cles_boite = [m.entetes.get("X-Relance-Id") for d in (fr.DOSSIER_NORMAL, fr.DOSSIER_COMPTES_CLES)
                  for m in boite.lister(fr.GESTIONNAIRE, d)]
    controle(3, "arrêt entre l'écriture et l'enregistrement, puis reprise sans doublon",
             sortie.returncode == 137 and (avant_b, avant_p) == (10, 9) and res.statut == "ok"
             and len(cles_boite) == 42 and len(set(cles_boite)) == 42,
             f"arrêt code {sortie.returncode} après 10 brouillons et 9 propositions ; reprise : {len(cles_boite)} brouillons, "
             f"{len(set(cles_boite))} clés distinctes")
    shutil.rmtree(racine)


def tranche_4() -> None:
    racine, horloge, classeur, boite, flux = monter()
    flux.executer()
    normaux = boite.lister(fr.GESTIONNAIRE, fr.DOSSIER_NORMAL)
    for m in normaux[:4]:
        boite.envoyer(fr.GESTIONNAIRE, m.id)
    horloge.avancer(minutes=10)
    bilan = flux.sonder()
    historique = lire(racine, "dispositif", "historique")
    nouvelles = [h for h in historique if h["date_envoi"] == "2026-09-07"]
    controle(4, "courriel envoyé par une personne : ligne d'historique", len(nouvelles) == 4 and bilan["envoyée"] == 4,
             f"{len(nouvelles)} lignes d'historique du jour, bilan {dict(bilan)}")
    # Litige saisi après la création des brouillons.
    restants = [p for p in lire(racine, "dispositif", "propositions") if p["etat"] == "brouillon créé"]
    cible = restants[0]
    with open(racine / "pilotage" / "litiges.csv", "a", encoding="utf-8", newline="") as f:
        f.write(f"{cible['numero_facture']},2026-09-07\n")
    horloge.avancer(minutes=10)
    bilan = flux.sonder()
    present = any(m.entetes.get("X-Relance-Id") == cible["cle"] for m in boite.lister(fr.GESTIONNAIRE, fr.DOSSIER_NORMAL)
                  + boite.lister(fr.GESTIONNAIRE, fr.DOSSIER_COMPTES_CLES))
    controle(4, "litige saisi : brouillon retiré au passage suivant", not present and bilan["retirees"] == 1,
             f"brouillon de {cible['cle']} {'toujours là' if present else 'retiré'}, bilan {dict(bilan)}")
    shutil.rmtree(racine)

    # Réglage du pilote : étape 8 désactivée.
    racine, horloge, classeur, boite, flux = monter()
    flux.executer()
    (racine / "dispositif" / "commande.csv").write_text("parametre,valeur\nsuspendre,non\netape8_active,non\n", encoding="utf-8")
    boite.deposer_envoye(fr.GESTIONNAIRE, "x@exemple.invalid", "Courriel écrit à la main", "texte")
    boite.envoyer(fr.GESTIONNAIRE, boite.lister(fr.GESTIONNAIRE, fr.DOSSIER_NORMAL)[0].id)
    horloge.avancer(minutes=10)
    bilan = flux.sonder()
    controle(4, "étape 8 désactivée le premier lundi du pilote", bilan["desactivee"] == 1 and not lire(racine, "dispositif", "echecs")
             and len([h for h in lire(racine, "dispositif", "historique") if h["date_envoi"] == "2026-09-07"]) == 0,
             f"bilan {dict(bilan)}, aucun échec, aucune ligne d'historique du jour")
    shutil.rmtree(racine)


def tranche_5() -> None:
    # Erreur passagère : S3 coupé 10 minutes, reprises espacées puis succès.
    racine, horloge, classeur, boite, flux = monter()
    boite.panne_jusqua = LUNDI + timedelta(minutes=10)
    res = flux.executer()
    controle(5, "S3 coupé 10 min : reprises puis succès", res.statut == "ok" and nombre_brouillons(racine) == 42
             and len(horloge.pauses) >= 1, f"statut {res.statut}, pauses {[round(p) for p in horloge.pauses]} s, "
             f"{nombre_brouillons(racine)} brouillons")
    shutil.rmtree(racine)

    # Panne longue de S3 : file des échecs et alerte.
    racine, horloge, classeur, boite, flux = monter()
    boite.panne_jusqua = LUNDI + timedelta(hours=4)
    res = flux.executer()
    echecs = lire(racine, "dispositif", "echecs")
    controle(5, "S3 coupé plusieurs heures : file des échecs", res.statut == "echec" and nombre_brouillons(racine) == 0
             and len(echecs) >= 1, f"statut {res.statut}, {len(echecs)} lignes dans la file")
    shutil.rmtree(racine)

    # Plafond.
    racine, horloge, classeur, boite, flux = monter()
    jeux.ecrire_csv(racine / "depot" / "extraction-2026-09-07.csv", jeux.ENTETES_EXTRACTION,
                    jeux.extraction_volume(150, jeux.SEANCE))
    res = flux.executer()
    alertes = [m.entetes["Objet"] for m in boite.messages(fr.RESPONSABLE_FINANCIER)]
    controle(5, "150 propositions : arrêt avant création et alerte", res.statut == "volume" and nombre_brouillons(racine) == 0
             and "[alerte] volume anormal" in alertes, f"statut {res.statut}, alertes {alertes}")
    shutil.rmtree(racine)

    # Alerte sur silence : rien lancé à 10 h.
    racine, horloge, classeur, boite, flux = monter(datetime(2026, 9, 7, 10, 0))
    etat = flux.veiller()
    alertes = [m.entetes["Objet"] for m in boite.messages(fr.RESPONSABLE_FINANCIER)]
    controle(5, "aucune exécution à 10 h : alerte", etat == "alerte" and "[alerte] aucune exécution" in alertes,
             f"état {etat}, alertes {alertes}")
    flux.executer()
    horloge.avancer(minutes=1)
    etat = flux.veiller()
    controle(5, "…et pas d'alerte quand l'exécution a eu lieu", etat == "ok", f"état {etat}")
    shutil.rmtree(racine)


def main() -> int:
    print(f"controles_tranches.py · maquette flux_relances {fr.VERSION} · Python {sys.version.split()[0]}")
    for tranche in (tranche_0, tranche_1, tranche_2, tranche_3, tranche_4, tranche_5):
        tranche()
    echecs = [r for r in RESULTATS if not r[2]]
    print(f"\n{len(RESULTATS) - len(echecs)} contrôles passés sur {len(RESULTATS)}.")
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
