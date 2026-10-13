"""Contrôle du pack consultant-ia : forme des compétences et copie embarquée du routeur de stratégie.

Usage :
  python scripts/verifier_pack.py                      contrôle tout (0 = aucun écart)
  python scripts/verifier_pack.py --embarquer <source>  régénère la copie embarquée depuis sa source
  python scripts/verifier_pack.py --source <source>     contrôle aussi que la copie suit sa source

<source> est le SKILL.md de `router-consulting-strategy` dans la bibliothèque de l'auteur. Par défaut,
le contrôle le cherche dans ~/.claude/skills/router-consulting-strategy/SKILL.md ; absent, il le dit
et ne contrôle que la forme de la copie.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
EMBARQUEE = "router-consulting-strategy"
SOURCE_PAR_DEFAUT = pathlib.Path.home() / ".claude" / "skills" / EMBARQUEE / "SKILL.md"
ENTETE_COPIE = (
    "<!-- Copie embarquée de `router-consulting-strategy`, tenue identique à sa source dans la "
    "bibliothèque de l'auteur du pack. Ne pas l'éditer ici : `python scripts/verifier_pack.py "
    "--embarquer <source>` la régénère. -->"
)
SECTIONS = ["## Ce que cette compétence résout", "## Stratégie", "## Étapes", "## Le livrable",
            "## Décisions et rejets", "## Frontières", "## Preuves restantes"]
MARQUEURS = ["<!-- capitaliser:squelette-v1 -->", "<!-- dev-qa-link -->"]
LIVRABLES = {
    "00-contexte.md", "01-cartographie-taches.md", "02-portefeuille.md", "03-chiffrage.md",
    "04-feuille-de-route.md", "10-besoin.md", "20-diagnostic.md", "30-exigences.md",
    "40-solutions.md", "50-rentabilite.md", "60-specification.md", "70-plan.md",
    "80-construction.md", "85-recette.md", "90-mise-en-service.md", "95-mesure.md",
}
MAX_LIGNES = 260
ecarts = 0


def ecart(message):
    global ecarts
    ecarts += 1
    print("  ✗", message)


def frontmatter(texte):
    m = re.match(r"---\n(.*?)\n---\n", texte, re.S)
    return m.group(1) if m else None


def copie_attendue(source_texte):
    """Frontmatter + titre + corps public (à partir de « ## Purpose »), sans la tête locale."""
    fm = frontmatter(source_texte)
    debut = source_texte.find("\n## Purpose")
    if fm is None or debut == -1:
        raise ValueError("source illisible : frontmatter ou « ## Purpose » introuvable")
    return f"---\n{fm}\n---\n\n# Consulting Strategy Router\n\n{ENTETE_COPIE}\n{source_texte[debut:]}"


def controler_competence(dossier, noms):
    chemin = dossier / "SKILL.md"
    texte = chemin.read_text(encoding="utf-8")
    lignes = texte.count("\n")
    print(f"{dossier.name}: {lignes} lignes")
    fm = frontmatter(texte)
    if fm is None:
        ecart("frontmatter absent")
        return
    nom = re.search(r"^name:\s*(\S+)", fm, re.M)
    if not nom or nom.group(1) != dossier.name:
        ecart(f"name différent du dossier ({nom.group(1) if nom else 'absent'})")
    if not re.search(r"^description:", fm, re.M):
        ecart("description absente")
    if dossier.name == EMBARQUEE:
        if ENTETE_COPIE not in texte:
            ecart("copie embarquée sans son en-tête")
        return
    for cle in ("scope", "owns", "consumes"):
        if not re.search(rf"^\s+{cle}:", fm, re.M):
            ecart(f"metadata.{cle} absent")
    for marqueur in MARQUEURS:
        if marqueur not in texte:
            ecart(f"marqueur {marqueur} absent")
    positions = [texte.find(s) for s in SECTIONS]
    if -1 in positions:
        ecart("sections absentes : " + ", ".join(s for s, p in zip(SECTIONS, positions) if p == -1))
    elif positions != sorted(positions):
        ecart("sections dans le désordre")
    if lignes > MAX_LIGNES:
        ecart(f"plus de {MAX_LIGNES} lignes")
    textes = [("SKILL.md", texte)]
    for ref in sorted((dossier / "references").glob("*.md")):
        if ref.name not in texte:
            ecart(f"références/{ref.name} jamais citée par SKILL.md")
        textes.append((ref.name, ref.read_text(encoding="utf-8")))
    for nom_fichier, contenu in textes:
        for livrable in re.findall(r"\b(\d\d-[a-z-]+\.md)", contenu):
            if livrable not in LIVRABLES:
                ecart(f"{nom_fichier} : livrable inconnu {livrable}")
        for cite in re.findall(r"`/?([a-z]+(?:-[a-z]+)+)`", contenu):
            semble_competence = cite.endswith(("-ia", "-usage", "-besoin", "-processus", "-charges",
                                                "-solution", "-rentabilite", "-deploiement",
                                                "-service", "-gains", "-strategy"))
            if semble_competence and cite not in noms and not cite.startswith("cas-"):
                ecart(f"{nom_fichier} : compétence inconnue `{cite}`")


def main(arguments):
    source = SOURCE_PAR_DEFAUT
    if "--embarquer" in arguments:
        source = pathlib.Path(arguments[arguments.index("--embarquer") + 1])
        cible = RACINE / "skills" / EMBARQUEE / "SKILL.md"
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_text(copie_attendue(source.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
        print(f"copie embarquée régénérée : {cible.relative_to(RACINE)}")
    if "--source" in arguments:
        source = pathlib.Path(arguments[arguments.index("--source") + 1])

    dossiers = sorted(d for d in (RACINE / "skills").iterdir() if (d / "SKILL.md").exists())
    noms = {d.name for d in dossiers}
    for dossier in dossiers:
        controler_competence(dossier, noms)

    copie = RACINE / "skills" / EMBARQUEE / "SKILL.md"
    if not copie.exists():
        ecart(f"copie embarquée absente : skills/{EMBARQUEE}/SKILL.md")
    elif source.exists():
        attendue = copie_attendue(source.read_text(encoding="utf-8"))
        if copie.read_text(encoding="utf-8") != attendue:
            ecart(f"la copie embarquée ne suit plus sa source ({source}) : --embarquer la régénère")
        else:
            print(f"{EMBARQUEE}: identique à sa source")
    else:
        print(f"{EMBARQUEE}: source absente sur ce poste, seule la forme de la copie est contrôlée")

    print("Écarts :", ecarts)
    return 1 if ecarts else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
