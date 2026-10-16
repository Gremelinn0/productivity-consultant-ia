"""Contrôle du pack consultant-ia : forme des compétences, copie embarquée du routeur de stratégie,
compétences complémentaires (COMPLEMENTAIRES.md et ses renvois), versions des manifestes, liens publics.

Usage :
  python scripts/verifier_pack.py                      contrôle tout (0 = aucun écart)
  python scripts/verifier_pack.py --embarquer <source>  régénère la copie embarquée depuis sa source
  python scripts/verifier_pack.py --source <source>     contrôle aussi que la copie suit sa source

<source> est le SKILL.md de `router-consulting-strategy` dans la bibliothèque de l'auteur. Par défaut,
le contrôle le cherche dans ~/.claude/skills/router-consulting-strategy/SKILL.md ; absent, il le dit
et ne contrôle que la forme de la copie.
"""
import json
import os
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
COMPLEMENTAIRES = "COMPLEMENTAIRES.md"
ENTETE_COMPLEMENTAIRES = ["Étape", "Compétence", "À quoi elle sert dans une mission", "Installation",
                          "Auteur · licence"]
ETAPES_COMPLEMENTAIRES = ("concevoir-solution", "construire-solution")
LICENCES_ADMISES = {"MIT", "Apache-2.0"}
PLACE_INTEGREE = "claude-plugins-official"  # connue de Claude Code sans `marketplace add`
PHRASE_ROUTEUR = "Une autre compétence installée a répondu à la place de l'étape"
DEPOTS_PUBLICS_AUTEUR = {"productivity-consultant-ia", "claude-skill-hub"}  # les seuls dépôts de l'auteur que le pack peut citer
NOMS_DEPRECIES = ("bmad-create-architecture",)  # renvoi vers bmad-architecture dans la version stable de BMad, absent de la suivante
COMMANDE = re.compile(r"`((?:/plugin|npx) [^`]+)`")
FORME_COMMANDE = re.compile(r"/plugin marketplace add [\w.-]+/[\w.-]+|/plugin install [\w-]+@[\w-]+|npx [\w-]+ install")
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


def lire(chemin):
    return chemin.read_text(encoding="utf-8")


def cellules(ligne):
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def controler_complementaires(noms):
    """COMPLEMENTAIRES.md : une table complète et tenue, et les renvois qui y mènent."""
    chemin = RACINE / COMPLEMENTAIRES
    if not chemin.exists():
        ecart(f"{COMPLEMENTAIRES} absent")
        return
    texte = lire(chemin)
    table = [cellules(ligne) for ligne in texte.splitlines() if ligne.startswith("|")]
    entete, lignes = (table[0], table[2:]) if len(table) >= 3 else (None, [])
    commandes_table, vues = set(), set()
    if entete != ENTETE_COMPLEMENTAIRES:
        ecart(f"{COMPLEMENTAIRES} : en-tête de la table inattendu ({entete})")
        lignes = []
    for ligne in lignes:
        if len(ligne) != len(ENTETE_COMPLEMENTAIRES):
            ecart(f"{COMPLEMENTAIRES} : une ligne a {len(ligne)} cellules au lieu de 5 ({ligne[:2]})")
            continue
        etape, competence, _, installation, auteur = ligne
        m_etape = re.fullmatch(r"`([a-z-]+)`", etape)
        if not m_etape or m_etape.group(1) not in ETAPES_COMPLEMENTAIRES or m_etape.group(1) not in noms:
            ecart(f"{COMPLEMENTAIRES} : étape inconnue « {etape} »")
            continue
        m_lien = re.match(r"\[`([a-z0-9-]+)`\]\((https://github\.com/[^/\s)]+/[^/\s)]+/blob/[0-9a-f]{40}/\S+)\)",
                          competence)
        if not m_lien or not m_lien.group(2).endswith(f"/{m_lien.group(1)}/SKILL.md"):
            ecart(f"{COMPLEMENTAIRES} : « {competence[:50]} » sans lien vers son SKILL.md à un commit fixé")
            continue
        nom = m_lien.group(1)
        if (m_etape.group(1), nom) in vues:
            ecart(f"{COMPLEMENTAIRES} : {nom} deux fois pour {m_etape.group(1)}")
        vues.add((m_etape.group(1), nom))
        commandes = COMMANDE.findall(installation)
        if not any(c.startswith(("/plugin install ", "npx ")) for c in commandes):
            ecart(f"{nom} : aucune commande d'installation")
        for commande in commandes:
            if not FORME_COMMANDE.fullmatch(commande):
                ecart(f"{nom} : commande d'installation mal formée « {commande} »")
            m_place = re.fullmatch(r"/plugin install [\w-]+@([\w-]+)", commande)
            if m_place and m_place.group(1) != PLACE_INTEGREE and not any(
                    c.startswith("/plugin marketplace add ") for c in commandes):
                ecart(f"{nom} : installe depuis {m_place.group(1)} sans la commande qui ajoute cette place de marché")
        commandes_table.update(commandes)
        m_auteur = re.fullmatch(r"(.+) · (\S+)", auteur)
        if not m_auteur or m_auteur.group(2) not in LICENCES_ADMISES:
            ecart(f"{nom} : licence absente ou hors de {sorted(LICENCES_ADMISES)} (« {auteur} »)")
    print(f"{COMPLEMENTAIRES}: {len(vues)} compétences, {len(commandes_table)} commandes")
    for etape in ETAPES_COMPLEMENTAIRES:
        if not any(e == etape for e, _ in vues):
            ecart(f"{COMPLEMENTAIRES} : aucune compétence pour {etape}")
    if PHRASE_ROUTEUR not in texte:
        ecart(f"{COMPLEMENTAIRES} : le renvoi à router-mission-ia (« {PHRASE_ROUTEUR} ») manque")
    if PHRASE_ROUTEUR not in lire(RACINE / "skills" / "router-mission-ia" / "SKILL.md"):
        ecart(f"router-mission-ia ne dit plus « {PHRASE_ROUTEUR} » : le renvoi de {COMPLEMENTAIRES} ne mène nulle part")
    for etape in ETAPES_COMPLEMENTAIRES:
        competence = lire(RACINE / "skills" / etape / "SKILL.md")
        entree = re.search(r"^- Compétences complémentaires[^\n]*(?:\n  [^\n]*)*", competence, re.M)
        if not entree or COMPLEMENTAIRES not in entree.group(0):
            ecart(f"{etape} : l'entrée « Compétences complémentaires » qui renvoie à {COMPLEMENTAIRES} manque")
        if "| Installation |" in competence:
            ecart(f"{etape} : la table de {COMPLEMENTAIRES} est recopiée dans la compétence")
    for chemin in (COMPLEMENTAIRES, "README.md", "ARCHITECTURE.md", "skills/concevoir-solution/SKILL.md",
                   "skills/construire-solution/SKILL.md"):
        for ancien in NOMS_DEPRECIES:
            if ancien in lire(RACINE / chemin):
                ecart(f"{chemin} : cite « {ancien} », nom déprécié par son auteur")
    if COMPLEMENTAIRES not in lire(RACINE / "ARCHITECTURE.md"):
        ecart(f"ARCHITECTURE.md ne cite pas {COMPLEMENTAIRES}")
    section = re.search(r"^## Compétences complémentaires \(à installer à part\)\n(.*?)(?=^## |\Z)",
                        lire(RACINE / "README.md"), re.M | re.S)
    if not section:
        ecart("README : la section « Compétences complémentaires (à installer à part) » manque")
        return
    if COMPLEMENTAIRES not in section.group(1):
        ecart(f"README : la section ne renvoie pas à {COMPLEMENTAIRES}")
    commandes_readme = {ligne.strip() for ligne in section.group(1).splitlines()
                        if ligne.strip().startswith(("/plugin ", "npx "))}
    if commandes_table - commandes_readme:
        ecart(f"README : commandes de {COMPLEMENTAIRES} absentes de la section : {sorted(commandes_table - commandes_readme)}")
    if commandes_readme - commandes_table:
        ecart(f"README : commandes absentes de {COMPLEMENTAIRES} : {sorted(commandes_readme - commandes_table)}")


def controler_versions():
    """Les deux manifestes portent la même version, de la forme x.y.z."""
    plugin = json.loads(lire(RACINE / ".claude-plugin" / "plugin.json"))
    place = json.loads(lire(RACINE / ".claude-plugin" / "marketplace.json"))
    v_plugin, v_place = plugin.get("version"), place.get("metadata", {}).get("version")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(v_plugin)):
        ecart(f"plugin.json : version illisible ({v_plugin})")
    elif v_plugin != v_place:
        ecart(f"versions différentes : plugin.json {v_plugin}, marketplace.json {v_place}")
    else:
        print(f"version: {v_plugin} (plugin.json et marketplace.json)")


def controler_liens():
    """Ce dépôt est public : pas de lien vers un autre dépôt de l'auteur que la liste, pas de chemin de poste.

    Un fichier qu'on ne peut pas lire n'est pas contrôlé : c'est un écart, jamais un silence (sous Windows,
    un dépôt posé dans un dossier au chemin trop long en fait partie, comme pour l'exemple).
    """
    illisibles = []
    for dossier, sous_dossiers, fichiers in os.walk(RACINE, onerror=lambda e: illisibles.append(str(e.filename))):
        sous_dossiers[:] = [d for d in sous_dossiers if d not in (".git", "__pycache__")]
        for fichier in sorted(fichiers):
            if not fichier.endswith((".md", ".json")):
                continue
            chemin = pathlib.Path(dossier) / fichier
            nom = chemin.relative_to(RACINE).as_posix()
            try:
                texte = lire(chemin)
            except (OSError, UnicodeDecodeError):
                illisibles.append(nom)
                continue
            for depot in sorted(set(re.findall(r"github\.com/Gremelinn0/([A-Za-z0-9._-]+)", texte))):
                if re.sub(r"\.git$", "", depot) not in DEPOTS_PUBLICS_AUTEUR:
                    ecart(f"{nom} : lien vers un dépôt de l'auteur hors de la liste des dépôts publics ({depot})")
            if re.search(r"[A-Za-z]:\\Users\\|/Users/[A-Za-z]|/home/[a-z]", texte):
                ecart(f"{nom} : chemin d'un poste personnel")
    if illisibles:
        ecart(f"{len(illisibles)} fichier(s) illisibles, non contrôlés (le premier : {illisibles[0]}) ; "
              "chemin trop long sous Windows ? placer le dépôt dans un dossier au chemin court")


def main(arguments):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # « ✗ » et les accents passent aussi dans un tuyau Windows
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

    controler_complementaires(noms)
    controler_versions()
    controler_liens()

    print("Écarts :", ecarts)
    return 1 if ecarts else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
