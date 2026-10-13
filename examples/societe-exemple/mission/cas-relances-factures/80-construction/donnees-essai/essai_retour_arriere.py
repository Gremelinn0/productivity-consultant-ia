"""Essai du retour arrière : restaurer une version archivée dans un dossier neuf, la contrôler, la faire tourner.

Un retour arrière jamais essayé n'en est pas un (`construire-solution`, étape 9 et `references/garde-fous.md`
partie 1). Ce script restaure l'archive d'une version gelée (`livraison/archives/flux-relances-v<x.y>.zip`) dans
un dossier temporaire, vérifie son manifeste, rejoue la séance du 2026-09-07 avec cette version-là et relève la
durée totale. C'est la durée `[F]` pour l'essai ; sur la plateforme, la durée de production reste `[H]`.

Commande : `python -X utf8 essai_retour_arriere.py <version>` (par exemple 1.0). Code de sortie 0 si la version
restaurée est conforme à son manifeste et rejoue la séance sans écart.
"""
from __future__ import annotations

import csv
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
LIVRAISON = ICI.parent / "livraison"
sys.path.insert(0, str(ICI))

import jeux  # noqa: E402


def main(version: str) -> int:
    archive = LIVRAISON / "archives" / f"flux-relances-v{version}.zip"
    if not archive.exists():
        print(f"archive introuvable : {archive.name}")
        return 2
    debut = time.perf_counter()
    racine = Path(tempfile.mkdtemp(prefix="retour-arriere-"))
    try:
        restauree = racine / "livraison"
        with zipfile.ZipFile(archive) as z:
            z.extractall(restauree)
        etape1 = time.perf_counter()
        controle = subprocess.run([sys.executable, "-X", "utf8", str(restauree / "flux_relances.py"),
                                   "verifier-livraison"], capture_output=True, text=True, encoding="utf-8")
        version_lue = subprocess.run([sys.executable, "-X", "utf8", str(restauree / "flux_relances.py"), "version"],
                                     capture_output=True, text=True, encoding="utf-8").stdout.strip()
        espace = racine / "espace"
        jeux.ecrire_espace_modele(espace, restauree)
        rejeu = subprocess.run([sys.executable, "-X", "utf8", str(restauree / "flux_relances.py"), "executer",
                                "--espace", str(espace), "--maintenant", "2026-09-07T09:30:00"],
                               capture_output=True, text=True, encoding="utf-8")
        fin = time.perf_counter()
        with open(espace / "dispositif" / "propositions.csv", encoding="utf-8", newline="") as f:
            propositions = list(csv.DictReader(f))
        print(f"restauration de l'archive {archive.name} : {etape1 - debut:.2f} s")
        print(f"version restaurée : {version_lue}")
        print(f"contrôle du manifeste : {controle.stdout.strip().splitlines()[-1]} (code {controle.returncode})")
        print(f"rejeu de la séance par la version restaurée : {rejeu.stdout.strip().splitlines()[0]} ; "
              f"{len(propositions)} propositions")
        print(f"durée totale du retour arrière essayé : {fin - debut:.2f} s")
        ok = controle.returncode == 0 and rejeu.returncode == 0 and len(propositions) == 42
        print("RETOUR ARRIÈRE ESSAYÉ : conforme" if ok else "RETOUR ARRIÈRE : ÉCART")
        return 0 if ok else 1
    finally:
        shutil.rmtree(racine, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "1.0"))
