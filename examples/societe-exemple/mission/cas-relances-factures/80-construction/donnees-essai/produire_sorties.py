"""Produit `sorties-simulees/rejeu-2026-09-07/` : ce que la maquette écrit à la place des effets réels.

Rejeu de la séance du lundi 2026-09-07 (61 factures fictives) par la ligne de commande du flux, en mode
simulation, sur un espace d'essai neuf. Les brouillons créés dans la boîte simulée, les messages d'avertissement,
le journal et les compteurs sont copiés tels quels : ce sont les pièces de la tranche 3 et du balayage. Rien n'est
envoyé, rien n'est écrit hors de l'espace d'essai (aucun droit d'envoi n'existe dans l'essai).

Commande : `python -X utf8 produire_sorties.py`.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent
LIVRAISON = RACINE / "livraison"
SORTIE = RACINE / "sorties-simulees" / "rejeu-2026-09-07"
sys.path.insert(0, str(ICI))

import jeux  # noqa: E402


def main() -> int:
    espace = Path(tempfile.mkdtemp(prefix="essai-relances-"))
    try:
        jeux.ecrire_espace_modele(espace, LIVRAISON)
        commande = [sys.executable, "-X", "utf8", str(LIVRAISON / "flux_relances.py"), "executer",
                    "--espace", "<espace d'essai>", "--maintenant", "2026-09-07T09:30:00"]
        reel = [str(espace) if c == "<espace d'essai>" else c for c in commande]
        sortie = subprocess.run(reel, capture_output=True, text=True, encoding="utf-8")
        if SORTIE.exists():
            shutil.rmtree(SORTIE)
        SORTIE.mkdir(parents=True)
        for source, cible in (("boite/Relances du lundi", "brouillons/relances-du-lundi"),
                              ("boite/Comptes clés à valider", "brouillons/comptes-cles-a-valider"),
                              ("boite/messages", "messages"), ("dispositif", "dispositif"),
                              ("plateforme", "plateforme")):
            shutil.copytree(espace / source, SORTIE / cible)
        shutil.copyfile(espace / "boite" / "journal-boite.csv", SORTIE / "journal-boite.csv")
        (SORTIE / "resume.txt").write_text(
            "Rejeu de la séance du lundi 2026-09-07 en mode simulation (horloge de test 09:30).\n"
            "Commande : python -X utf8 livraison/flux_relances.py executer --espace <espace d'essai> "
            "--maintenant 2026-09-07T09:30:00\n"
            f"Code de sortie : {sortie.returncode}\n{sortie.stdout}{sortie.stderr}", encoding="utf-8")
        print((SORTIE / "resume.txt").read_text(encoding="utf-8"))
        nombre = sum(1 for _ in (SORTIE / "brouillons").rglob("*.txt"))
        print(f"{nombre} brouillons copiés dans {SORTIE.relative_to(RACINE)}")
        return sortie.returncode
    finally:
        shutil.rmtree(espace, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
