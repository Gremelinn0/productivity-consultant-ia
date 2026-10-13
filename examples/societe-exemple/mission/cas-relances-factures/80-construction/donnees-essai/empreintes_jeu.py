"""Empreintes du jeu d'essai : prouver que le jeu rejoué en recette est celui que la construction a utilisé.

`espace-modele/` est produit par `jeux.py` (graine fixe) ; son empreinte est celle de l'ensemble de ses fichiers
(chemin et SHA-256 de chaque fichier, fins de ligne normalisées), puis celle de cette liste. Un générateur qui
change, ou un fichier retouché à la main, change l'empreinte.

Commande : `python -X utf8 empreintes_jeu.py` ; `--verifier` régénère le jeu dans un dossier temporaire et
compare à `espace-modele/` rangé (code de sortie 1 en cas d'écart).
"""
from __future__ import annotations

import hashlib
import shutil
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
LIVRAISON = ICI.parent / "livraison"
sys.path.insert(0, str(ICI))

import jeux  # noqa: E402


def sha256_lf(octets: bytes) -> str:
    return hashlib.sha256(octets.replace(b"\r\n", b"\n")).hexdigest()


def empreinte_arbre(racine: Path) -> tuple:
    lignes = [f"{sha256_lf(p.read_bytes())}  {p.relative_to(racine).as_posix()}"
              for p in sorted(racine.rglob("*")) if p.is_file()]
    return hashlib.sha256("\n".join(lignes).encode("utf-8")).hexdigest(), lignes


def main(argv: list) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    rangee, lignes = empreinte_arbre(ICI / "espace-modele")
    print(f"jeux.py : SHA-256 {sha256_lf((ICI / 'jeux.py').read_bytes())}")
    print(f"espace-modele/ rangé : {len(lignes)} fichiers · SHA-256 de l'arbre {rangee}")
    if "--verifier" in argv:
        temporaire = Path(tempfile.mkdtemp(prefix="jeu-"))
        try:
            jeux.ecrire_espace_modele(temporaire / "espace-modele", LIVRAISON)
            regenere, _ = empreinte_arbre(temporaire / "espace-modele")
        finally:
            shutil.rmtree(temporaire, ignore_errors=True)
        print(f"espace-modele/ régénéré par jeux.py : SHA-256 de l'arbre {regenere}")
        if regenere != rangee:
            print("ÉCART : le jeu rangé n'est pas celui que produit jeux.py")
            return 1
        print("le jeu rangé est exactement celui que produit jeux.py")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
