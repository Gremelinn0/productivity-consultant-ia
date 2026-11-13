#!/usr/bin/env python3
"""Un Word (.docx) ou un Excel (.xlsx) joint par la personne devient du texte, sans aucun paquet à installer.

Le poste de l'agent en ligne n'a pas de réseau et le Lecteur de documents ne lit que du texte ou des PDF : ces deux formats,
qui sont des archives de XML, se lisent ici avec la seule bibliothèque standard de Python.

    python3 lire_document.py <fichier.docx|fichier.xlsx> <sortie.md>

Sort avec le code 2 si le fichier est illisible, sans rien écrire : l'agent le dit à la personne, il n'invente pas le contenu.
"""
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
S = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PR = "{http://schemas.openxmlformats.org/package/2006/relationships}"
LIGNES_MAX = 5000  # par feuille : au-delà, le texte le dit


def texte_paragraphe(p) -> str:
    morceaux = []
    for e in p.iter():
        if e.tag == W + "t":
            morceaux.append(e.text or "")
        elif e.tag == W + "tab":
            morceaux.append("\t")
        elif e.tag == W + "br":
            morceaux.append("\n")
    return "".join(morceaux)


def lire_docx(archive: zipfile.ZipFile) -> str:
    racine = ET.fromstring(archive.read("word/document.xml"))
    corps = racine.find(W + "body")
    sortie = []
    for bloc in corps if corps is not None else []:
        if bloc.tag == W + "p":
            texte = texte_paragraphe(bloc).strip()
            if texte:
                sortie.append(texte)
        elif bloc.tag == W + "tbl":
            for ligne in bloc.findall(W + "tr"):
                cellules = [" ".join(texte_paragraphe(p).strip() for p in c.findall(W + "p")).strip() for c in ligne.findall(W + "tc")]
                sortie.append("| " + " | ".join(c.replace("|", "/") for c in cellules) + " |")
    return "\n\n".join(sortie)


def chaines_partagees(archive: zipfile.ZipFile) -> list:
    if "xl/sharedStrings.xml" not in archive.namelist():
        return []
    racine = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    return ["".join(t.text or "" for t in si.iter(S + "t")) for si in racine.findall(S + "si")]


def colonne(reference: str) -> int:
    n = 0
    for lettre in re.sub(r"[^A-Z]", "", reference):
        n = n * 26 + ord(lettre) - 64
    return n - 1


def valeur(cellule, chaines: list) -> str:
    sorte = cellule.get("t")
    if sorte == "inlineStr":
        return "".join(t.text or "" for t in cellule.iter(S + "t"))
    v = cellule.find(S + "v")
    if v is None or v.text is None:
        return ""
    if sorte == "s":
        i = int(v.text)
        return chaines[i] if 0 <= i < len(chaines) else ""
    return v.text


def lire_xlsx(archive: zipfile.ZipFile) -> str:
    classeur = ET.fromstring(archive.read("xl/workbook.xml"))
    liens = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    cibles = {r.get("Id"): r.get("Target") for r in liens.findall(PR + "Relationship")}
    chaines = chaines_partagees(archive)
    sortie = []
    for feuille in classeur.find(S + "sheets"):
        cible = cibles.get(feuille.get(R + "id"), "")
        chemin = cible.lstrip("/") if cible.startswith("/") else "xl/" + cible
        sortie.append("## " + (feuille.get("name") or "Feuille"))
        lignes = ET.fromstring(archive.read(chemin)).find(S + "sheetData")
        vues = 0
        for ligne in lignes if lignes is not None else []:
            if vues >= LIGNES_MAX:
                sortie.append(f"(feuille coupée à {LIGNES_MAX} lignes)")
                break
            cellules = {colonne(c.get("r", "A1")): valeur(c, chaines) for c in ligne.findall(S + "c")}
            if not any(str(v).strip() for v in cellules.values()):
                continue
            largeur = max(cellules) + 1
            sortie.append("| " + " | ".join(str(cellules.get(i, "")).replace("|", "/").replace("\n", " ") for i in range(largeur)) + " |")
            vues += 1
    return "\n".join(sortie)


def lire(chemin: Path) -> str:
    extension = chemin.suffix.lower()
    if extension not in (".docx", ".xlsx"):
        raise ValueError("format non pris en charge")
    with zipfile.ZipFile(chemin) as archive:
        return lire_docx(archive) if extension == ".docx" else lire_xlsx(archive)


def main(arguments: list) -> int:
    if len(arguments) != 2:
        print("usage : lire_document.py <fichier.docx|fichier.xlsx> <sortie.md>", file=sys.stderr)
        return 2
    source, cible = Path(arguments[0]), Path(arguments[1])
    try:
        texte = lire(source)
    except (OSError, KeyError, ValueError, zipfile.BadZipFile, ET.ParseError) as e:
        print(f"illisible : {source.name} ({type(e).__name__})", file=sys.stderr)
        return 2
    if not texte.strip():
        print(f"vide : {source.name}", file=sys.stderr)
        return 2
    cible.parent.mkdir(parents=True, exist_ok=True)
    cible.write_text(texte + "\n", encoding="utf-8")
    print(f"{cible} : {len(texte)} caractères")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
