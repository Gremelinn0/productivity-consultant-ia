"""Gèle une version de la livraison : manifeste des empreintes, archive exportée, empreinte de l'archive.

Une version gelée se reconnaît à son manifeste (`livraison/MANIFESTE.sha256`, une empreinte SHA-256 par fichier
livré) et à son archive (`livraison/archives/flux-relances-v<x.y>.zip`, fabriquée de façon reproductible : mêmes
octets pour les mêmes fichiers). Toute modification d'un fichier livré après le gel se voit par
`python flux_relances.py verifier-livraison` : c'est une nouvelle version, avec ses tests rejoués.

Commande : `python -X utf8 geler_version.py` (depuis ce dossier). Écrit le manifeste, fabrique l'archive de la
version lue dans `flux_relances.VERSION`, affiche les empreintes à recopier dans `journal-versions.md`.
"""
from __future__ import annotations

import hashlib
import sys
import zipfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
LIVRAISON = ICI.parent / "livraison"
sys.path.insert(0, str(LIVRAISON))

import flux_relances as fr  # noqa: E402


def archive(version: str) -> Path:
    dossier = LIVRAISON / "archives"
    dossier.mkdir(exist_ok=True)
    cible = dossier / f"flux-relances-v{version}.zip"
    fichiers = fr.fichiers_livres(LIVRAISON) + [LIVRAISON / "MANIFESTE.sha256"]
    with zipfile.ZipFile(cible, "w", zipfile.ZIP_DEFLATED) as z:
        for chemin in sorted(fichiers, key=lambda p: p.relative_to(LIVRAISON).as_posix()):
            info = zipfile.ZipInfo(chemin.relative_to(LIVRAISON).as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, chemin.read_bytes().replace(b"\r\n", b"\n") if chemin.suffix in (".py", ".csv", ".txt", ".sha256") else chemin.read_bytes())
    return cible


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    empreinte_manifeste = fr.ecrire_manifeste(LIVRAISON)
    cible = archive(fr.VERSION)
    empreinte_archive = hashlib.sha256(cible.read_bytes()).hexdigest()
    print(f"version gelée : {fr.VERSION}")
    print(f"  manifeste  : livraison/MANIFESTE.sha256 · SHA-256 {empreinte_manifeste}")
    print(f"  archive    : livraison/archives/{cible.name} · SHA-256 {empreinte_archive}")
    for ligne in (LIVRAISON / "MANIFESTE.sha256").read_text(encoding="utf-8").splitlines():
        print("   ", ligne)
    ecarts = fr.verifier_livraison(LIVRAISON)
    print("contrôle de la livraison :", "conforme au manifeste" if not ecarts else ecarts)
    return 0 if not ecarts else 1


if __name__ == "__main__":
    sys.exit(main())
