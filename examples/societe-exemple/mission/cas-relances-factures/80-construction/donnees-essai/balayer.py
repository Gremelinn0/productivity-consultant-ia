"""Balayage de ce qui est rangé dans `80-construction/` : secrets et données personnelles.

Méthode (`construire-solution`, `references/garde-fous.md` partie 7) : une recherche de texte sur chaque
fichier, puis la relecture des lignes trouvées. Le balayage ne prouve pas l'absence, il réduit le risque.

Ce que le script cherche :
- secrets : un des mots « key », « token », « secret », « password », « bearer », « authorization » suivi d'une
  valeur (« mot = valeur », « mot : valeur ») ; les chaînes de 32 caractères ou plus faites de lettres et de
  chiffres mélangés, sans tiret ni soulignement (une empreinte SHA-256 de 64 caractères hexadécimaux est
  reconnue et écartée) ; les fichiers d'environnement et les clés privées. Les simples mentions du mot (« aucun
  secret dans le code ») sont comptées, pas listées ;
- données personnelles : adresses électroniques hors du domaine réservé `.invalid`, numéros de téléphone,
  adresses postales (numéro et rue).

Les lignes qui citent le NOM d'un des trois secrets de `60-specification.md` §9 (accès-listes, accès-messagerie,
accès-alerte) sont comptées à part : un nom de secret n'est pas un secret.

Aucune valeur n'est affichée en entier, ni dans la sortie, ni dans les résultats rendus à un test : un début de
valeur (préfixe, 4 caractères, « … ») suffit pour retrouver la ligne et ne permet pas de reconstituer un secret.

Commande : `python -X utf8 balayer.py [dossier ...]` (par défaut : `80-construction/` entier). Code de sortie 0 s'il
ne reste rien à relire, 1 sinon.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent
NOMS_DE_SECRETS = ("accès-listes", "accès-messagerie", "accès-alerte")
SUFFIXES_TEXTE = {".py", ".csv", ".txt", ".md", ".sha256", ".json", ".yaml", ".yml"}
FICHIERS_A_RISQUE = {".env", "id_rsa"}
SUFFIXES_A_RISQUE = {".pem", ".key", ".p12"}

MOTS = r"(?:api[_-]?key|access[_-]?key|secret|token|password|passwd|bearer|authorization)"
MENTION_SECRET = re.compile(r"\b" + MOTS + r"\b", re.I)
SECRET_AFFECTE = re.compile(r"\b" + MOTS + r"\b\s*[:=]\s*[\"']?([^\s\"',;)]{6,})", re.I)
CHAINE_LONGUE = re.compile(r"[A-Za-z0-9+/]{32,}")
EMPREINTE_SHA256 = re.compile(r"^[0-9a-f]{64}$")
COURRIEL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
TELEPHONE = re.compile(r"(?<![\w-])(?:\+33|0)\s?[1-9](?:[ .-]?\d{2}){4}(?![\w-])")
ADRESSE_POSTALE = re.compile(
    r"\b\d{1,3},? (?:bis |ter )?(?:[Rr]ue|[Aa]venue|[Bb]oulevard|[Cc]hemin|[Ii]mpasse|[Pp]lace|[Aa]llée)\s+"
    r"(?:(?:de la |de l'|de |du |des |d'|l')\s*)?[A-ZÉÈ]\w+")


def masquer(valeur: str) -> str:
    """Un début de valeur, jamais la valeur entière : le préfixe (jusqu'au dernier « _ » ou « - » des douze premiers
    caractères), 4 caractères, puis « … »."""
    coupe = max(valeur[:12].rfind("_"), valeur[:12].rfind("-")) + 1
    return valeur[:coupe + 4] + "…"


def masquer_ligne(ligne: str) -> str:
    return SECRET_AFFECTE.sub(lambda m: m.group(0).replace(m.group(1), masquer(m.group(1))), ligne)


def a_risque(chemin: Path) -> bool:
    return chemin.name in FICHIERS_A_RISQUE or chemin.suffix in SUFFIXES_A_RISQUE


def fichiers(dossiers: list) -> list:
    sortie = []
    for dossier in dossiers:
        for chemin in sorted(Path(dossier).rglob("*")):
            if not chemin.is_file() or "__pycache__" in chemin.parts:
                continue
            if chemin.suffix.lower() in SUFFIXES_TEXTE or a_risque(chemin):
                sortie.append(chemin)
    return sortie


def balayer(dossiers: list) -> dict:
    trouvailles = {"secret": [], "chaine": [], "courriel": [], "telephone": [], "adresse": [], "fichier": []}
    noms_de_secrets = 0
    mentions = 0
    liste = fichiers(dossiers)
    for chemin in liste:
        if a_risque(chemin):
            trouvailles["fichier"].append((chemin, 0, chemin.name))
            continue
        texte = chemin.read_text(encoding="utf-8", errors="replace")
        for numero, ligne in enumerate(texte.splitlines(), start=1):
            sans_noms = ligne
            if any(nom in ligne for nom in NOMS_DE_SECRETS):
                noms_de_secrets += 1
                for nom in NOMS_DE_SECRETS:
                    sans_noms = sans_noms.replace(nom, "")
            if MENTION_SECRET.search(sans_noms):
                mentions += 1
            if SECRET_AFFECTE.search(sans_noms):
                trouvailles["secret"].append((chemin, numero, masquer_ligne(ligne.strip()[:140])))
            for chaine in CHAINE_LONGUE.findall(ligne):
                if EMPREINTE_SHA256.match(chaine):
                    continue
                if any(c.isdigit() for c in chaine) and any(c.isalpha() for c in chaine):
                    trouvailles["chaine"].append((chemin, numero, masquer(chaine)))
            for courriel in COURRIEL.findall(ligne):
                if not courriel.lower().endswith(".invalid"):
                    trouvailles["courriel"].append((chemin, numero, courriel))
            for tel in TELEPHONE.findall(ligne):
                trouvailles["telephone"].append((chemin, numero, tel))
            if ADRESSE_POSTALE.search(ligne):
                trouvailles["adresse"].append((chemin, numero, ligne.strip()[:100]))
    return {"fichiers": liste, "trouvailles": trouvailles, "noms_de_secrets": noms_de_secrets, "mentions": mentions}


def main(argv: list) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    dossiers = [Path(a) for a in argv] or [RACINE]
    r = balayer(dossiers)
    print(f"balayer.py · {len(r['fichiers'])} fichiers lus dans {', '.join(d.name for d in dossiers)}")
    total = 0
    for genre, lignes in r["trouvailles"].items():
        total += len(lignes)
        print(f"  {genre:9s} : {len(lignes)} ligne(s) à relire")
        for chemin, numero, extrait in lignes[:20]:
            print(f"      {chemin.relative_to(RACINE) if RACINE in chemin.parents else chemin}:{numero}: {extrait}")
    print(f"  noms de secrets cités (écartés) : {r['noms_de_secrets']} ligne(s) ; "
          f"mentions du mot sans valeur : {r['mentions']} ligne(s)")
    print("RIEN À RELIRE" if total == 0 else f"{total} ligne(s) à relire")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
