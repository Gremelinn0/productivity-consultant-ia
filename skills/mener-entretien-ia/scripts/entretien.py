"""Entretien guidé par IA : questionnaire, consigne de l'intervieweur, note d'entretien.

Usage :
  python entretien.py questionnaire (--guide besoin | --questionnaire mission/sources/questionnaire-<objet>-<date>.md)
  python entretien.py consigne (--guide besoin | --questionnaire …) --role "dirigeante" --entreprise "Société Exemple"
                               [--langue en] [--contexte contexte.md] [--consultant "le consultant"]
  python entretien.py base [--sujet support-client]
  python entretien.py preparer --base support-client --objectif "…" --role "dirigeante" [--entreprise "…"]
                               [--garder SC02,SC05,…] --sortie mission/sources/questionnaire-<objet>-<date>.md
  python entretien.py ajouter --sujet support-client --partie 4 --question "…" --decide "…" [--dabord "la personne"]
  python entretien.py creer-sujet --sujet facturation --prefixe FA --titre "la facturation" --quand "…" --partie "…"
                                  --question "…" --decide "…" [--groupe "Servir ses clients" [--creer-groupe]]
  python entretien.py verifier
  python entretien.py consigne-en-ligne [--sortie ligne.json]
  python entretien.py schema [--guide en-ligne]
  python entretien.py note --compte-rendu cr.json [--questionnaire …] [--transcription messages.json] --sortie mission/sources

Les questions ne sont écrites qu'à un endroit, la base de questions : `references/base-questions/<sujet>.md`, un
fichier par sujet, indexé par `references/base-questions/README.md` (deux familles de sujets, chacune en groupes).
Les guides fixes (direction, équipes, version courte, besoin, processus) en sont des blocs : ce script les lit là et
n'en garde aucune copie. `preparer` tire de la base le brouillon d'un questionnaire ; `ajouter` y range une question
nouvelle, `creer-sujet` un sujet qui manque, au groupe voulu de l'index ; `verifier` contrôle la base et rend 1 au
moindre écart. Un questionnaire préparé pour un objectif (guide
`prepare`) est un fichier de la mission, au modèle de `references/questionnaire-prepare.md`, validé avant
l'entretien. `note` refuse un compte rendu qui enfreint les règles du pack (statuts, données personnelles) et rend 1.

L'agent en ligne (un visiteur, sans consultant avant l'entretien) choisit ses questions dans la base, douze au plus,
jamais en dehors : `consigne-en-ligne` écrit la ligne que l'hôte garde (la consigne, le schéma du compte rendu, les
sujets) et affiche la taille de la consigne ; `note` accepte son compte rendu (guide `en-ligne`) et refuse une question
absente de la base. Méthode : `references/agent-en-ligne.md`.
"""
import argparse
import hashlib
import json
import os
import pathlib
import re
import sys
import unicodedata

ICI = pathlib.Path(__file__).resolve().parent
COMPETENCE = ICI.parent
SKILLS = COMPETENCE.parent
CONSIGNE = COMPETENCE / "references" / "consigne-intervieweur.md"
SCHEMA = COMPETENCE / "references" / "compte-rendu.schema.json"
BASE = COMPETENCE / "references" / "base-questions"

GUIDES_CONNUS = ("direction", "equipes", "besoin", "processus", "court", "prepare")
PREFIXES = {"direction": "D", "equipes": "E", "besoin": "B", "processus": "P", "court": "C", "prepare": "Q"}
DUREES = {"direction": 30, "equipes": 35, "besoin": 20, "processus": 25, "court": 10}
# Les guides fixes sont des blocs de la base : (sujet, numéros gardés dans l'ordre ; le thème de chaque question
# est-il le titre de sa partie ?). Un sujet qui s'enrichit ne rallonge pas son guide : le guide garde ses numéros.
# La version courte de guides-entretien.md : « la semaine type, la tâche qu'on voudrait ne plus faire, les
# informations recopiées d'un outil à l'autre ».
GUIDES_BASE = {
    "direction": ("decouverte-direction", tuple(f"DI{i:02d}" for i in range(1, 11)), True),
    "equipes": ("decouverte-equipes", tuple(f"EQ{i:02d}" for i in range(1, 12)), True),
    "court": ("decouverte-equipes", ("EQ01", "EQ10", "EQ05"), True),
    "besoin": ("cadrage", tuple(f"CA0{i}" for i in range(1, 9)), False),
    "processus": ("processus", tuple(f"AP0{i}" for i in range(1, 9)), False),
}
# Un questionnaire préparé reste un entretien court : au-delà, la personne abandonne, et le reste attend l'audit.
MAX_PREPARE = 12
# Où chercher la réponse avant de poser la question : l'outil se lit, un document se demande, la personne répond.
DABORD = ("l'outil", "un document", "la personne")
NUMERO = re.compile(r"([A-Z]{2,4})(\d{2,3})")
TITRE_SUJET = "# Base de questions : "

# L'agent d'entretien en ligne : un visiteur, sans consultant avant l'entretien. Il choisit ses questions dans la base,
# jamais en dehors (references/agent-en-ligne.md). Les limites des outils `afficher` et `terminer_entretien` sont dites
# au modèle par la consigne : une seule définition ici.
GUIDE_EN_LIGNE = "en-ligne"
SCHEMA_EN_LIGNE = COMPETENCE / "references" / "compte-rendu-en-ligne.schema.json"
CONSIGNE_EN_LIGNE = COMPETENCE / "references" / "consigne-en-ligne.md"
TITRE_EN_LIGNE = "Entretien en ligne"
BASE_EN_LIGNE = "premier-echange"   # le sujet de départ d'un visiteur, porté par la ligne de l'agent
MAX_EN_LIGNE = MAX_PREPARE   # douze questions au plus, comme un questionnaire préparé
CHOIX_EN_LIGNE = (2, 6)   # les réponses suggérées : de 2 à 6 choix
CHOIX_LONGUEUR = 60   # de 60 caractères au plus chacun
PLAN_EN_LIGNE = (3, 7)   # le plan de l'audit : de 3 à 7 étapes
LIMITE_CONSIGNE_EN_LIGNE = 60000   # le modèle relit la consigne à chaque tour : la base ne la fait pas grossir au-delà
# Où chercher la réponse d'une question qu'un visiteur ne peut pas lire lui-même : la consigne la marque.
MARQUES_DABORD = {"l'outil": " [outil]", "un document": " [document]"}


class Erreur(Exception):
    pass


def _lire(chemin):
    if not chemin.exists():
        raise Erreur(f"source introuvable : {chemin}")
    return chemin.read_text(encoding="utf-8")


def sujets(dossier=None):
    """Les sujets de la base de questions : un fichier par sujet dans `references/base-questions/` (le README est
    l'index, pas un sujet)."""
    dossier = pathlib.Path(dossier or BASE)
    return sorted(p.stem for p in pathlib.Path(dossier).glob("*.md") if re.fullmatch(r"[a-z0-9-]+", p.stem))


def base(sujet, dossier=None):
    """Les questions d'un sujet de la base, dans l'ordre du fichier : [{id, partie, question, decide, dabord}]."""
    dossier = pathlib.Path(dossier or BASE)
    chemin = pathlib.Path(dossier) / f"{sujet}.md"
    if not re.fullmatch(r"[a-z0-9-]+", sujet or "") or not chemin.exists():
        raise Erreur(f"sujet absent de la base : {sujet} (connus : {', '.join(sujets(dossier)) or 'aucun'})")
    partie, sortie = "", []
    for ligne in _lire(chemin).splitlines():
        t = re.match(r"^## \d+\.\s*(.+?)\s*$", ligne)
        if t:
            partie = t.group(1)
            continue
        c = [x.strip() for x in ligne.strip().strip("|").split("|")]
        if len(c) >= 4 and NUMERO.fullmatch(c[0]):
            sortie.append({"id": c[0], "partie": partie, "question": c[1], "decide": c[2], "dabord": c[3]})
    if not sortie:
        raise Erreur(f"{chemin.name} : aucune question lue (lignes « | SC01 | question | décision | d'abord | »)")
    ids = [q["id"] for q in sortie]
    doubles = sorted({i for i in ids if ids.count(i) > 1})
    if doubles:
        raise Erreur(f"{chemin.name} : numéro en double ({', '.join(doubles)})")
    return sortie


def _empreinte(question):
    """Une question sans accents, casse ni ponctuation : deux questions de même empreinte sont un doublon."""
    t = unicodedata.normalize("NFKD", question).encode("ascii", "ignore").decode().lower()
    return " ".join(re.findall(r"[a-z0-9]+", t))


RANGEE_SUJET = re.compile(r"^\| \[([^\]]+)\]\(([a-z0-9-]+)\.md\) \| ([A-Z]{2,4}) \|")
# L'index du README range les sujets en deux niveaux sous « ## Les sujets » : des familles (`### …`) qui portent des
# groupes (`#### …`), un tableau de sujets par groupe. Un sujet neuf va, par défaut, au dernier groupe de la famille
# « Ce que veut le client ».
FAMILLE_PAR_DEFAUT = "Ce que veut le client"
ENTETE_INDEX = ["| Sujet | Préfixe | Quand l'ouvrir |", "|---|---|---|"]


def _plan(lignes):
    """Où sont rangés les sujets dans le README (la liste de ses lignes). Rend {"familles", "groupes", "sujets"} : une
    famille {titre, rang, groupes}, un groupe {titre, famille, rang, sujets, dernier} (`dernier` : le rang de sa
    dernière ligne de sujet, None s'il n'en a pas), un sujet {sujet, prefixe, nom, quand, rang, famille, groupe}
    (famille et groupe valent None pour une ligne posée hors de l'index). `rang` : le numéro de la ligne, depuis 0."""
    familles, groupes, sujets = [], [], []
    famille = groupe = None
    dans = False
    for rang, ligne in enumerate(lignes):
        t = ligne.strip()
        if t.startswith("## "):
            dans, famille, groupe = t.startswith("## Les sujets"), None, None
        elif dans and t.startswith("### "):
            famille = {"titre": t[4:].strip(), "rang": rang, "groupes": []}
            familles.append(famille)
            groupe = None
        elif dans and t.startswith("#### "):
            groupe = {"titre": t[5:].strip(), "famille": famille, "rang": rang, "sujets": [], "dernier": None}
            groupes.append(groupe)
            if famille:
                famille["groupes"].append(groupe)
        else:
            m = RANGEE_SUJET.match(t)
            if m:
                cellules = [x.strip() for x in t.strip("|").split("|")]
                s = {"sujet": m.group(2), "prefixe": m.group(3), "nom": m.group(1), "rang": rang,
                     "famille": famille, "groupe": groupe, "quand": cellules[2] if len(cellules) > 2 else ""}
                sujets.append(s)
                if groupe:
                    groupe["sujets"].append(s)
                    groupe["dernier"] = rang
    return {"familles": familles, "groupes": groupes, "sujets": sujets}


def _readme(dossier=None):
    """Le README de la base : son plan (`_plan`), et les compétences qui partent de la base."""
    chemin = pathlib.Path(dossier or BASE) / "README.md"
    if not chemin.exists():
        raise Erreur("README.md absent de la base de questions : il en est l'index")
    texte = _lire(chemin)
    m = re.search(r"^## Qui part de la base.*?$(.*?)(?=^## |\Z)", texte, re.M | re.S)
    lecteurs = re.findall(r"^- `([a-z0-9-]+)`", m.group(1), re.M) if m else []
    return _plan(texte.splitlines()), lecteurs


def _par_sujet(plan):
    return {s["sujet"]: (s["prefixe"], s["nom"]) for s in plan["sujets"]}


def _index(dossier=None):
    """Les sujets du README : {sujet: (préfixe, nom)}, et les compétences qui partent de la base."""
    plan, lecteurs = _readme(dossier)
    return _par_sujet(plan), lecteurs


def rangement(dossier=None):
    """L'index en deux niveaux, dans l'ordre du README : [(famille, [(groupe, [sujet, …]), …]), …]."""
    plan, _ = _readme(dossier)
    return [(f["titre"], [(g["titre"], [s["sujet"] for s in g["sujets"]]) for g in f["groupes"]])
            for f in plan["familles"]]


def _ecarts_de_l_index(plan):
    """Le rangement des sujets dans le README : chacun une seule fois, dans un groupe (`#### …`) d'une famille
    (`### …`) ; aucune famille ni aucun groupe vide ; aucun nom de famille ou de groupe pris deux fois."""
    ecarts, vus = [], set()
    for s in plan["sujets"]:
        if s["sujet"] in vus:
            ecarts.append(f"README : le sujet {s['sujet']} est listé deux fois")
        vus.add(s["sujet"])
        if not s["groupe"] or not s["famille"]:
            ecarts.append(f"README : le sujet {s['sujet']} n'est pas rangé dans un groupe (#### …) d'une famille "
                          "(### …)")
    for genre, elements in (("famille", plan["familles"]), ("groupe", plan["groupes"])):
        noms = set()
        for e in elements:
            if _empreinte(e["titre"]) in noms:
                ecarts.append(f"README : deux {genre}s s'appellent « {e['titre']} »")
            noms.add(_empreinte(e["titre"]))
    ecarts += [f"README : la famille « {f['titre']} » n'a aucun groupe" for f in plan["familles"] if not f["groupes"]]
    ecarts += [f"README : le groupe « {g['titre']} » n'a aucun sujet" for g in plan["groupes"] if not g["sujets"]]
    return ecarts


def _nom(texte):
    """Le nom d'un sujet : le titre de son fichier sans « Base de questions : », la première lettre en capitale."""
    t = texte.splitlines()[0][len(TITRE_SUJET):].strip() if texte.startswith(TITRE_SUJET) else ""
    return t[:1].upper() + t[1:]


def verifier_base(dossier=None, skills=None):
    """Les écarts de la base de questions ; une liste vide veut dire qu'elle est saine. Contrôle : chaque sujet se
    lit, un préfixe par sujet et un sujet par préfixe, chaque ligne a sa question, sa décision et un « D'abord »
    connu, aucun tiret cadratin, aucune question en double dans toute la base, le README liste exactement les
    sujets, chacun une fois dans un groupe d'une famille, chaque compétence qu'il cite comme lectrice renvoie à la
    base en tête de son SKILL.md, et la consigne de l'agent en ligne, qui reprend toutes les questions, reste sous
    `LIMITE_CONSIGNE_EN_LIGNE` caractères."""
    dossier = pathlib.Path(dossier or BASE)
    skills = pathlib.Path(skills or SKILLS)
    ecarts, vus, prefixes = [], {}, {}
    try:
        plan, lecteurs = _readme(dossier)
    except Erreur as e:
        return [str(e)]
    index = _par_sujet(plan)
    presents = sujets(dossier)
    for s in sorted(set(presents) - set(index)):
        ecarts.append(f"{s}.md : absent du tableau des sujets du README")
    for s in sorted(set(index) - set(presents)):
        ecarts.append(f"README : le sujet {s} n'a pas de fichier")
    ecarts += _ecarts_de_l_index(plan)
    for s in presents:
        texte = _lire(pathlib.Path(dossier) / f"{s}.md")
        if not texte.startswith(TITRE_SUJET):
            ecarts.append(f"{s}.md : le titre « {TITRE_SUJET.strip('# ')}… » manque en première ligne")
        elif s in index and index[s][1] != _nom(texte):
            ecarts.append(f"README : le sujet {s} s'appelle « {index[s][1]} », son fichier « {_nom(texte)} »")
        if "—" in texte:
            ecarts.append(f"{s}.md : tiret cadratin, à remplacer par une virgule, deux-points ou parenthèses")
        try:
            questions = base(s, dossier)
        except Erreur as e:
            ecarts.append(str(e))
            continue
        lettres = sorted({NUMERO.fullmatch(q["id"]).group(1) for q in questions})
        if len(lettres) != 1:
            ecarts.append(f"{s}.md : un seul préfixe par sujet, trouvé {', '.join(lettres)}")
        elif s in index and index[s][0] != lettres[0]:
            ecarts.append(f"{s}.md : préfixe {lettres[0]}, le README annonce {index[s][0]}")
        for p in lettres:
            if p in prefixes and prefixes[p] != s:
                ecarts.append(f"préfixe {p} pris par deux sujets : {prefixes[p]} et {s}")
            prefixes.setdefault(p, s)
        for q in questions:
            if not q["question"].rstrip().endswith("?"):
                ecarts.append(f"{q['id']} : une question finit par « ? »")
            if not q["decide"]:
                ecarts.append(f"{q['id']} : « Ce qu'elle décide » est vide ; une question sans décision ne se pose pas")
            if q["dabord"] not in DABORD:
                ecarts.append(f"{q['id']} : « D'abord » vaut {q['dabord']!r}, attendu {', '.join(DABORD)}")
            e = _empreinte(q["question"])
            if e in vus:
                ecarts.append(f"{q['id']} : même question que {vus[e]}")
            vus.setdefault(e, q["id"])
    for nom in lecteurs:
        chemin = pathlib.Path(skills) / nom / "SKILL.md"
        if not chemin.exists():
            ecarts.append(f"README : la compétence {nom} n'existe pas dans le pack")
        elif "base-questions" not in "\n".join(_lire(chemin).splitlines()[:40]):
            ecarts.append(f"{nom} : son SKILL.md ne renvoie pas à la base de questions en tête (40 premières lignes)")
    if not ecarts:   # la consigne en ligne se bâtit sur une base saine
        try:
            taille = len(consigne_en_ligne(dossier))
        except Erreur as e:
            ecarts.append(f"consigne en ligne : {e}")
        else:
            if taille > LIMITE_CONSIGNE_EN_LIGNE:
                ecarts.append(f"consigne en ligne : {_milliers(taille)} caractères, plus que les "
                              f"{_milliers(LIMITE_CONSIGNE_EN_LIGNE)} visés ; le modèle la relit à chaque tour : "
                              "resserrer des questions de la base")
    return ecarts


ENTETE_TABLEAU = ["| # | Question | Ce qu'elle décide | D'abord |", "|---|---|---|---|"]


def _ligne(numero, question, decide, dabord):
    return f"| {numero} | {question} | {decide} | {dabord} |"


def _question_neuve(question, decide, dabord, dossier):
    """La question et sa décision, nettoyées ; refuse ce qui n'entre pas dans la base, doublon compris."""
    question, decide = " ".join(question.split()), " ".join(decide.split())
    if not question.endswith("?"):
        raise Erreur("une question finit par « ? »")
    if not decide:
        raise Erreur("« Ce qu'elle décide » est obligatoire : une question sans décision ne se pose pas")
    if dabord not in DABORD:
        raise Erreur(f"« D'abord » : {', '.join(DABORD)}")
    if "—" in question + decide or "|" in question + decide:
        raise Erreur("ni tiret cadratin ni barre verticale dans une question")
    e = _empreinte(question)
    for s in sujets(dossier):
        for q in base(s, dossier):
            if _empreinte(q["question"]) == e:
                raise Erreur(f"déjà dans la base : {q['id']} ({s}) ; la reformuler là, ne pas l'ajouter")
    return question, decide


def ajouter(sujet, partie, question, decide, dabord="la personne", creer_partie=False, dossier=None):
    """Range une question nouvelle à la fin d'une partie du sujet (son numéro ou son titre), avec le numéro suivant
    du sujet ; rend ce numéro. Refuse une question déjà présente dans toute la base (accents, casse et ponctuation
    mis à part), une décision vide, un « D'abord » inconnu, un tiret cadratin. Avec `creer_partie`, une partie
    absente s'ouvre après la dernière."""
    dossier = pathlib.Path(dossier or BASE)
    questions = base(sujet, dossier)
    question, decide = _question_neuve(question, decide, dabord, dossier)
    lettres = NUMERO.fullmatch(questions[0]["id"]).group(1)
    numero = f"{lettres}{max(int(NUMERO.fullmatch(q['id']).group(2)) for q in questions) + 1:02d}"
    chemin = pathlib.Path(dossier) / f"{sujet}.md"
    lignes = _lire(chemin).splitlines()
    titres = [(i, m.group(1), m.group(2)) for i, l in enumerate(lignes)
              for m in [re.match(r"^## (\d+)\.\s*(.+?)\s*$", l)] if m]
    cible = [t for t in titres if str(partie).strip() == t[1] or _empreinte(str(partie)) == _empreinte(t[2])]
    ligne = _ligne(numero, question, decide, dabord)
    if cible:
        debut = cible[0][0]
        fin = next((i for i in range(debut + 1, len(lignes)) if lignes[i].startswith("## ")), len(lignes))
        rangs = [i for i in range(debut + 1, fin) if lignes[i].startswith("|")]
        if not rangs:
            raise Erreur(f"la partie {partie} de {sujet} n'a pas de tableau")
        lignes.insert(rangs[-1] + 1, ligne)
    elif creer_partie:
        if "—" in str(partie):
            raise Erreur("pas de tiret cadratin")
        fin = next((i for i in range(titres[-1][0] + 1, len(lignes)) if re.match(r"^## (?!\d+\.)", lignes[i])),
                   len(lignes))
        while fin > 0 and not lignes[fin - 1].strip():
            fin -= 1
        bloc = ["", f"## {int(titres[-1][1]) + 1}. {str(partie).strip()}", ""] + ENTETE_TABLEAU + [ligne]
        lignes[fin:fin] = bloc + ([""] if fin < len(lignes) and lignes[fin].strip() else [])
    else:
        raise Erreur(f"partie absente de {sujet} : {partie} (parties : "
                     + ", ".join(f"{t[1]}. {t[2]}" for t in titres) + ") ; --creer-partie pour l'ouvrir")
    chemin.write_text("\n".join(lignes).rstrip() + "\n", encoding="utf-8")
    return numero


def _place_du_sujet(lignes, groupe=None, creer_groupe=False):
    """Où inscrire un sujet neuf dans le README (la liste de ses lignes) : (rang de la ligne après laquelle poser la
    sienne, lignes à poser avant elle). Sans nom de groupe : à la fin du dernier groupe de « Ce que veut le client ».
    Un groupe nommé s'écrit comme dans le README (accents et casse mis à part) ; s'il n'existe pas, il est refusé, ou
    ouvert à la fin de « Ce que veut le client » avec `creer_groupe`."""
    plan = _plan(lignes)
    if not plan["groupes"]:  # l'ancien tableau unique, sans groupes : à la suite de sa dernière ligne
        if groupe is not None:
            raise Erreur("README : l'index n'a pas de groupes (#### …) : --groupe n'a rien à nommer")
        if not plan["sujets"]:
            raise Erreur("README : le tableau des sujets est introuvable")
        return plan["sujets"][-1]["rang"], []
    famille = next((f for f in plan["familles"] if _empreinte(f["titre"]) == _empreinte(FAMILLE_PAR_DEFAUT)), None)
    dernier = famille["groupes"][-1] if famille and famille["groupes"] else None
    noms = ", ".join(g["titre"] for g in plan["groupes"])
    if groupe is None:
        cible = dernier
        if cible is None:
            raise Erreur(f"README : la famille « {FAMILLE_PAR_DEFAUT} » est introuvable ; --groupe nomme le groupe "
                         f"voulu (groupes : {noms})")
    else:
        cible = next((g for g in plan["groupes"] if _empreinte(g["titre"]) == _empreinte(groupe)), None)
        if cible is None:
            if not creer_groupe:
                raise Erreur(f"groupe absent du README : {groupe} (groupes : {noms}) ; --creer-groupe pour l'ouvrir à "
                             f"la fin de « {FAMILLE_PAR_DEFAUT} »")
            if dernier is None or dernier["dernier"] is None:
                raise Erreur(f"README : la famille « {FAMILLE_PAR_DEFAUT} » n'a pas de groupe rempli : le groupe "
                             f"{groupe} n'a pas où s'ouvrir")
            return dernier["dernier"], ["", f"#### {groupe.strip()}", ""] + ENTETE_INDEX
    if cible["dernier"] is None:
        raise Erreur(f"README : le groupe « {cible['titre']} » n'a aucun sujet ; le corriger à la main")
    return cible["dernier"], []


def creer_sujet(sujet, prefixe, titre, quand, partie, question, decide, dabord="la personne", intro="",
                dossier=None, groupe=None, creer_groupe=False):
    """Ouvre un sujet qui manque, avec la question qui le fait naître : son fichier, sa première partie, et sa ligne
    dans l'index des sujets du README, à la fin du groupe `groupe` (par défaut le dernier groupe de « Ce que veut le
    client » ; un groupe qui n'existe pas se refuse, sauf avec `creer_groupe`). Les questions suivantes s'y rangent
    avec `ajouter`."""
    dossier = pathlib.Path(dossier or BASE)
    if not re.fullmatch(r"[a-z0-9-]+", sujet):
        raise Erreur("le sujet s'écrit en minuscules, chiffres et tirets : facturation, ressources-humaines")
    if not re.fullmatch(r"[A-Z]{2,4}", prefixe):
        raise Erreur("le préfixe tient en deux à quatre capitales : FA")
    chemin = pathlib.Path(dossier) / f"{sujet}.md"
    index, _ = _index(dossier)
    if chemin.exists() or sujet in index:
        raise Erreur(f"le sujet {sujet} existe déjà")
    if prefixe in {p for p, _ in index.values()}:
        raise Erreur(f"le préfixe {prefixe} est pris par {next(s for s, (p, _) in index.items() if p == prefixe)}")
    if "—" in titre + quand + partie + intro + (groupe or "") or "|" in quand + (groupe or ""):
        raise Erreur("pas de tiret cadratin, ni de barre verticale dans « quand » ou dans le nom du groupe")
    if groupe is not None and not groupe.strip():
        raise Erreur("--groupe : le nom du groupe est vide")
    question, decide = _question_neuve(question, decide, dabord, dossier)
    texte = [f"{TITRE_SUJET}{titre}", "", (intro.strip() or f"Quand l'objectif touche à {titre}.") +
             " Un questionnaire préparé part d'ici et du cadrage (`cadrage`), garde les questions utiles, douze au "
             "plus, et n'adapte que ce qui change pour l'entreprise.", "", f"## 1. {partie.strip()}", ""] \
        + ENTETE_TABLEAU + [_ligne(f"{prefixe}01", question, decide, dabord)]
    readme = pathlib.Path(dossier) / "README.md"
    lignes = _lire(readme).splitlines()
    rang, avant = _place_du_sujet(lignes, groupe, creer_groupe)
    lignes[rang + 1:rang + 1] = avant + [f"| [{_nom(TITRE_SUJET + titre)}]({sujet}.md) | {prefixe} | {quand.strip()} |"]
    chemin.write_text("\n".join(texte) + "\n", encoding="utf-8")
    readme.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return chemin


def preparer(sujet, objectif, role, entreprise="", garder=None, date=None):
    """Le brouillon d'un questionnaire préparé, tiré de la base du sujet : les questions gardées (toutes, sans `garder`),
    chacune avec son numéro de base et la décision qu'elle sert dans « Alimente ». « Validé par » reste vide : le script
    refuse de l'ouvrir tant qu'on n'a pas gardé douze questions au plus, adapté leurs mots et validé."""
    questions = base(sujet)
    if garder:
        connues = {q["id"]: q for q in questions}
        inconnues = [g for g in garder if g not in connues]
        if inconnues:
            raise Erreur(f"absentes de la base {sujet} : {', '.join(inconnues)}")
        questions = [connues[g] for g in garder]
    import datetime
    jour = date or datetime.date.today().isoformat()
    l = [f"# Questionnaire préparé · {objectif}" + (f" · {entreprise}" if entreprise else ""), "",
         f"Objectif : {objectif}",
         f"Personne interrogée : {role} · Préparé le {jour} par le consultant, depuis la base {sujet}",
         "Validé par :",
         "Lu pour le préparer :",
         f"Base : {sujet} ({', '.join(q['id'] for q in questions)})", "",
         "## Déjà établi (on ne le redemande pas)", "",
         "## Questions", "",
         "| # | Thème | Question | Déjà su (à faire confirmer) | Alimente |",
         "|---|---|---|---|---|"]
    for i, q in enumerate(questions, 1):
        l.append(f"| {i} | {q['partie']} | {q['question']} | | {q['id']} · {q['decide']} |")
    l += ["", "## Pas dans cet entretien", ""]
    return "\n".join(l) + "\n"


def _prepare(fichier):
    """Le questionnaire préparé pour un objectif : `references/questionnaire-prepare.md` en donne le modèle."""
    chemin = pathlib.Path(fichier)
    texte = _lire(chemin)
    objectif = re.search(r"^Objectif\s*:\s*(.+?)\s*$", texte, re.M)
    if not objectif:
        raise Erreur(f"{chemin.name} : la ligne « Objectif : » manque ; les questions visent un objectif écrit")
    valide = re.search(r"^Validé par\s*:[ \t]*(.*?)\s*$", texte, re.M)
    if not valide or not valide.group(1) or "<" in valide.group(1):
        raise Erreur(f"{chemin.name} : questionnaire non validé ; la ligne « Validé par : » attend le rôle de qui "
                     "l'a relu, et la date")
    m = re.search(r"^## Questions.*?$(.*?)(?=^## |\Z)", texte, re.M | re.S)
    if not m:
        raise Erreur(f"{chemin.name} : la section « ## Questions » manque")
    lignes = []
    for ligne in m.group(1).splitlines():
        c = [x.strip() for x in ligne.strip().strip("|").split("|")]
        if len(c) >= 5 and c[0].isdigit():
            lignes.append({"numero": int(c[0]), "theme": c[1], "question": c[2], "deja_su": c[3],
                           "alimente": c[4]})
    if not lignes:
        raise Erreur(f"{chemin.name} : aucune question lue dans « ## Questions »")
    if [l["numero"] for l in lignes] != list(range(1, len(lignes) + 1)):
        raise Erreur(f"{chemin.name} : questions à numéroter de 1 à {len(lignes)}, dans l'ordre")
    if len(lignes) > MAX_PREPARE:
        raise Erreur(f"{chemin.name} : {len(lignes)} questions ; {MAX_PREPARE} au plus, les plus décisives d'abord "
                     "(le reste attend la séance d'observation ou l'audit)")
    vides = [str(l["numero"]) for l in lignes if not l["question"]]
    if vides:
        raise Erreur(f"{chemin.name} : question vide (ligne {', '.join(vides)})")
    etabli = re.search(r"^## Déjà établi.*?$(.*?)(?=^## |\Z)", texte, re.M | re.S)
    deja = re.findall(r"^\s*- (.+?)\s*$", etabli.group(1), re.M) if etabli else []
    depuis = re.search(r"^Base\s*:\s*([a-z0-9-]+)", texte, re.M)
    return {"guide": "prepare", "source": chemin.name, "objectif": objectif.group(1), "valide_par": valide.group(1),
            "base": depuis.group(1) if depuis else None, "deja_etabli": deja, "duree_minutes": max(5, round(2.5 * len(lignes))),
            "questions": [{"id": f"Q{l['numero']}", "theme": l["theme"], "question": l["question"],
                           "deja_su": l["deja_su"], "alimente": l["alimente"]} for l in lignes]}


def questionnaire(guide, fichier=None):
    if guide not in GUIDES_CONNUS:
        raise Erreur(f"guide inconnu : {guide} (connus : {', '.join(GUIDES_CONNUS)})")
    if guide == "prepare":
        if not fichier:
            raise Erreur("guide prepare : donner le questionnaire préparé (--questionnaire <fichier>)")
        return _prepare(fichier)
    sujet, garder, avec_theme = GUIDES_BASE[guide]
    lignes = base(sujet)
    if garder:
        connues = {q["id"]: q for q in lignes}
        manque = [g for g in garder if g not in connues]
        if manque:
            raise Erreur(f"guide {guide} : {', '.join(manque)} absent(s) de la base {sujet}")
        lignes = [connues[g] for g in garder]
    source = f"mener-entretien-ia/references/base-questions/{sujet}.md" + (" (version courte)" if guide == "court" else "")
    questions = [{"id": f"{PREFIXES[guide]}{i}", "base": l["id"], "theme": l["partie"] if avec_theme else "",
                  "question": l["question"], "alimente": l["decide"]} for i, l in enumerate(lignes, 1)]
    return {"guide": guide, "source": source, "base": sujet, "duree_minutes": DUREES[guide], "questions": questions}


def _minuscule(phrase):
    return phrase[0].lower() + phrase[1:] if len(phrase) > 1 and phrase[0].isupper() and phrase[1].islower() else phrase


def consigne(guide, role, entreprise, langue=None, contexte="", consultant="le consultant", objet=None,
             fichier=None):
    q = questionnaire(guide, fichier)
    gabarit = _lire(CONSIGNE).split("\n---\n", 1)
    if len(gabarit) != 2:
        raise Erreur("consigne-intervieweur.md : la ligne --- qui ouvre la consigne est absente")
    bloc = "\n".join(
        f"{x['id']}. " + (f"[{x['theme']}] " if x["theme"] else "") + x["question"]
        + (f" (Déjà su : {x['deja_su']})" if x.get("deja_su") else "") for x in q["questions"])
    if q.get("deja_etabli"):
        contexte = (contexte.strip() + "\n\n" if contexte.strip() else "") + "Déjà établi, à ne pas redemander ni faire confirmer :\n" \
            + "\n".join(f"- {x}" for x in q["deja_etabli"])
    objet_par_defaut = ("comprendre comment le travail se passe aujourd'hui, pour voir ce qui pourrait être "
                        "simplifié ; rien n'est décidé, et personne n'est jugé.")
    if q.get("objectif"):
        objet_par_defaut = (f"comprendre ce qu'il faut savoir pour {_minuscule(q['objectif']).rstrip('.')} ; rien "
                            "n'est décidé, et personne n'est jugé.")
    champs = {
        "CONSULTANT": consultant,
        "ENTREPRISE": entreprise,
        "ROLE": role,
        "OBJET": objet or objet_par_defaut,
        "LANGUE": (f"Mène l'entretien dans cette langue : {langue}." if langue else
                   "Mène l'entretien dans la langue de la personne ; avant sa première réponse, écris en français."),
        "DUREE": str(q["duree_minutes"]),
        "NB": str(len(q["questions"])),
        "CONTEXTE": contexte.strip() or "(rien de plus que ce qui précède)",
        "QUESTIONNAIRE": bloc,
    }
    texte = gabarit[1].strip() + "\n"
    for cle, valeur in champs.items():
        texte = texte.replace("{{" + cle + "}}", valeur)
    reste = re.findall(r"\{\{[A-Z]+\}\}", texte)
    if reste:
        raise Erreur(f"champs non remplis dans la consigne : {', '.join(sorted(set(reste)))}")
    return texte


def schema():
    return json.loads(_lire(SCHEMA))


DONNEE_PERSO = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+|(?:\+?\d[\s.-]?){9,}")


def controler(cr, guide_attendu=None, q=None):
    """Les écarts aux règles du pack ; une liste vide veut dire que la note peut s'écrire. `q` : le questionnaire
    préparé de l'entretien (guide `prepare`), lu dans son fichier ou gardé par l'hôte. Un compte rendu de l'agent en
    ligne (guide `en-ligne`) a son propre contrôle : il n'a pas de questionnaire, l'agent choisit dans la base."""
    if isinstance(cr, dict) and cr.get("guide") == GUIDE_EN_LIGNE:
        return controler_en_ligne(cr, q)
    ecarts = []
    s = schema()
    for cle in s["required"]:
        if cle not in cr:
            ecarts.append(f"champ manquant : {cle}")
    if ecarts:
        return ecarts
    if cr["guide"] not in GUIDES_CONNUS:
        ecarts.append(f"guide inconnu : {cr['guide']}")
        return ecarts
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(cr["date"])):
        ecarts.append("date : AAAA-MM-JJ attendu")
    if not cr["ouverture_dite"]:
        ecarts.append("l'objet de l'entretien n'a pas été dit en ouverture (guides-entretien, règles communes)")
    if cr["guide"] == "prepare" and q is None:
        ecarts.append("guide prepare : le questionnaire préparé de l'entretien est requis (--questionnaire)")
        return ecarts
    if q is not None and q.get("guide") != cr["guide"]:
        ecarts.append(f"le compte rendu suit le guide {cr['guide']}, le questionnaire donné est {q.get('guide')}")
        return ecarts
    ids = [x["id"] for x in (q or questionnaire(guide_attendu or cr["guide"]))["questions"]]
    vus = [r.get("id") for r in cr["reponses"]]
    if vus != ids:
        ecarts.append(f"réponses : une par question dans l'ordre {ids}, reçu {vus}")

    def chiffre(c, ou):
        st = c.get("statut")
        if st not in ("F", "H", "E"):
            ecarts.append(f"{ou} « {c.get('valeur')} » : statut {st!r}, attendu F, H ou E")
        elif st == "F" and c.get("fondement") not in ("regle-enoncee", "piece-remise"):
            ecarts.append(f"{ou} « {c.get('valeur')} » : [F] sans fondement (règle énoncée ou pièce remise) ; "
                          "dit de mémoire, c'est un [H]")
        elif st == "F" and c.get("fondement") == "piece-remise" and not cr["pieces"]:
            ecarts.append(f"{ou} « {c.get('valeur')} » : [F] par pièce remise, mais aucune pièce n'a été remise")
        elif st == "H" and not str(c.get("confirme_par", "")).strip():
            ecarts.append(f"{ou} « {c.get('valeur')} » : [H] sans le rôle qui peut confirmer")
        elif st == "E" and not str(c.get("calcul", "")).strip():
            ecarts.append(f"{ou} « {c.get('valeur')} » : [E] sans son calcul")

    for r in cr["reponses"]:
        for c in r.get("chiffres", []):
            chiffre(c, r.get("id"))
        for texte in [r.get("synthese", ""), r.get("exemple_reel", "")] + list(r.get("citations", [])):
            if DONNEE_PERSO.search(texte or ""):
                ecarts.append(f"{r.get('id')} : une adresse ou un numéro reste dans le texte, à retirer")
    for t in cr["taches"]:
        chiffre({"valeur": t.get("tache"), **t}, "tâche")
    for texte in cr.get("pour_la_base", []):
        if DONNEE_PERSO.search(texte or ""):
            ecarts.append("pour la base : une adresse ou un numéro reste dans le texte, à retirer")
    noms = _noms(cr)
    if noms:
        textes = [cr.get("equipe", "")] + cr["ecarts"] + cr["promis"] + cr["questions_ouvertes"] + cr.get("pour_la_base", [])
        for r in cr["reponses"]:
            textes += [r.get("synthese", ""), r.get("exemple_reel", "")] + list(r.get("citations", []))
        textes += [" ".join(str(v) for v in t.values()) for t in cr["taches"]]
        textes += [" ".join(str(v) for v in p.values()) for p in cr["pieces"]]
        if any(noms.search(x or "") for x in textes):
            ecarts.append("un nom écrit pendant l'entretien (noms_a_retirer) reste dans le compte rendu, à retirer")
    return ecarts


def _noms(cr):
    """Les noms que la personne a écrits (`noms_a_retirer`), en une expression ; None s'il n'y en a pas."""
    noms = sorted({n.strip() for n in cr.get("noms_a_retirer") or [] if isinstance(n, str) and len(n.strip()) >= 2},
                  key=len, reverse=True)
    if not noms:
        return None
    return re.compile(r"(?<!\w)(?:" + "|".join(re.escape(n) for n in noms) + r")(?!\w)", re.I)


def slug(texte):
    t = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:40] or "personne"


def _role(cr):
    """Le rôle qui nomme la note. Un compte rendu en ligne n'en a pas toujours (l'hôte peut le poser) : la note
    s'appelle alors « visiteur » et une empreinte courte du compte rendu, pour que deux visiteurs le même jour ne
    s'écrasent pas."""
    if cr.get("role") or cr.get("guide") != GUIDE_EN_LIGNE:
        return cr["role"]
    contenu = json.dumps({"demande": cr.get("demande"), "reponses": cr.get("reponses")}, sort_keys=True,
                         ensure_ascii=False)
    return "visiteur " + hashlib.sha1(contenu.encode("utf-8")).hexdigest()[:6]


def _statut(c):
    st = c["statut"]
    if st == "H":
        return f"`[H]` (à confirmer : {c['confirme_par']})"
    if st == "E":
        return f"`[E]` ({c['calcul']})"
    return "`[F]` (" + ("règle énoncée par son détenteur, source : l'entretien" if c["fondement"] == "regle-enoncee"
                       else "pièce remise") + ")"


NOMS_GUIDES = {"direction": "direction", "equipes": "équipes", "besoin": "besoin (cadrer-besoin, 8 questions)",
               "processus": "processus (auditer-processus, 8 questions)", "court": "version courte"}


def rendre_note(cr, nom_transcription=None, questionnaire_prepare=None):
    if cr.get("guide") == GUIDE_EN_LIGNE:
        return rendre_note_en_ligne(cr, nom_transcription)
    complet = questionnaire_prepare or questionnaire(cr["guide"])
    q = {x["id"]: x for x in complet["questions"]}
    nom_guide = NOMS_GUIDES.get(cr["guide"]) or (
        f"questionnaire préparé pour : {complet['objectif']} (`{complet['source']}`, {len(q)} questions"
        + (f", depuis la base {complet['base']}" if complet.get("base") else "") + ")")
    entete = f"# Entretien — {cr['role']}" + (f", {cr['equipe']}" if cr.get("equipe") else "")
    entete += f" · {cr['date']} · {cr['duree_minutes']} min"
    presents = ", ".join(cr.get("personnes") or [cr["role"]])
    l = [entete, "",
         f"Mené par : entretien guidé par IA (consultant-ia, `mener-entretien-ia`), sans le consultant · Guide utilisé : "
         f"{nom_guide} · Personnes présentes (rôles) : {presents} · Langue : {cr['langue']}",
         ""]
    if nom_transcription:
        l += [f"Transcription intégrale : `{nom_transcription}` (même dossier).", ""]
    l += ["## Ce qui a été dit", "",
          "Ouverture : l'objet de l'entretien, l'enregistrement pour le consultant et la règle « des rôles, jamais "
          "de noms » ont été dits dans le premier message.", ""]
    for r in cr["reponses"]:
        question = q[r["id"]]
        titre = f"### {r['id']}" + (f" · {question['theme']}" if question["theme"] else "")
        l += [titre, "", f"*{question['question']}*", ""]
        l.append(r["synthese"].strip() if r["repondue"] else "Pas de réponse. " + r["synthese"].strip())
        if r.get("exemple_reel"):
            l += ["", f"Dernière occurrence racontée : {r['exemple_reel'].strip()}"]
        for c in r.get("chiffres", []):
            l.append(f"- {c['valeur']} {_statut(c)}")
        for cit in r.get("citations", []):
            l += ["", f"> « {cit.strip()} »"]
        if r["relances"]:
            l += ["", f"Relances : {r['relances']}."]
        l.append("")
    l += ["## Tâches citées (à reporter dans 01)", "",
          "| Tâche | Fréquence | Durée | Volume | Outils | Statut, et qui confirme |",
          "|---|---|---|---|---|---|"]
    for t in cr["taches"]:
        statut = _statut(t).replace("`", "")
        l.append("| " + " | ".join([t["tache"], t.get("frequence", ""), t.get("duree", ""), t.get("volume", ""),
                                    t.get("outils", ""), statut]) + " |")
    if not cr["taches"]:
        l.append("| aucune | | | | | |")

    def liste(titre, items, vide):
        return [f"## {titre}", ""] + ([f"- {x}" for x in items] or [vide]) + [""]

    l.append("")
    l += liste("Pièces remises", [p["piece"] + (f" : rend `[F]` {p['rend_f']}" if p.get("rend_f") else "")
                                  for p in cr["pieces"]], "Aucune pendant l'entretien.")
    l += liste("Écarts avec d'autres sources", cr["ecarts"], "Aucun relevé.")
    l += liste("Documents ou accès promis", cr["promis"], "Aucun.")
    l += liste("Questions restées ouvertes", cr["questions_ouvertes"], "Aucune.")
    if cr.get("pour_la_base") or complet.get("base"):
        sujet = complet.get("base") or "du sujet"
        l += liste("Pour la base de questions", cr.get("pour_la_base", []),
                   "Rien à ajouter.") + [f"À relire par le consultant avant de l'ajouter à `references/base-questions/{sujet}.md`.", ""]
    return "\n".join(l).rstrip() + "\n"


def rendre_transcription(cr, messages):
    l = [f"# Transcription — entretien {_role(cr)} · {cr['date']}", "",
         "Entretien écrit guidé par IA. « Assistant » est l'IA ; « Personne » est la personne interrogée. "
         "Texte tel qu'échangé, dans la langue de l'échange ; adresses, numéros et noms cités remplacés par [retiré].", ""]
    noms = _noms(cr)
    for m in messages:
        qui = "Assistant" if m.get("role") == "assistant" else "Personne"
        texte = DONNEE_PERSO.sub("[retiré]", str(m.get("texte", "")).strip())  # guides-entretien : données personnelles retirées
        texte = noms.sub("[retiré]", texte) if noms else texte
        l += [f"**{qui}**" + (f" · {m['le']}" if m.get("le") else ""), "", texte, ""]
    return "\n".join(l).rstrip() + "\n"


def ecrire_note(cr, sortie, messages=None, questionnaire_prepare=None):
    ecarts = controler(cr, q=questionnaire_prepare)
    if ecarts:
        raise Erreur("compte rendu refusé :\n  - " + "\n  - ".join(ecarts))
    sortie = pathlib.Path(sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    base = f"entretien-{slug(_role(cr))}-{cr['date']}"
    nom_t = f"{base}.transcription.md" if messages else None
    note = sortie / f"{base}.md"
    note.write_text(rendre_note(cr, nom_t, questionnaire_prepare), encoding="utf-8")
    fichiers = [note]
    if messages:
        (sortie / nom_t).write_text(rendre_transcription(cr, messages), encoding="utf-8")
        fichiers.append(sortie / nom_t)
    return fichiers


# ----------------------------------------------------------------------------------- l'agent d'entretien en ligne
# Un visiteur, sans consultant avant l'entretien : personne ne prépare ni ne valide son questionnaire. L'agent choisit
# ses questions dans la base, douze au plus, jamais en dehors (references/agent-en-ligne.md).


def _barree(q):
    """Une question retirée de la base garde son numéro et s'y lit barrée (~~…~~) : l'agent ne la pose pas."""
    return "~~" in q["id"] + q["question"] + q["decide"]


def questions_en_ligne(dossier=None):
    """Les questions que l'agent en ligne peut poser : toute la base, sauf les questions barrées. {numéro: question}."""
    dossier = pathlib.Path(dossier or BASE)
    return {q["id"]: q for s in sujets(dossier) for q in base(s, dossier) if not _barree(q)}


def index_des_sujets(dossier=None):
    """Les sujets de la base dans l'ordre de l'index du README : [{sujet, prefixe, nom, quand}]. Refuse un index qui ne
    concorde pas avec les fichiers de la base (`verifier` dit lesquels)."""
    plan, _ = _readme(dossier)
    if sorted(s["sujet"] for s in plan["sujets"]) != sujets(dossier):
        raise Erreur("l'index du README et les fichiers de la base ne concordent pas (entretien.py verifier)")
    return [{cle: s[cle] for cle in ("sujet", "prefixe", "nom", "quand")} for s in plan["sujets"]]


def _milliers(n):
    return f"{n:,}".replace(",", " ")


def _bloc_questions_en_ligne(index, dossier):
    """Toutes les questions de la base, par sujet, une ligne chacune : « numéro question → ce qu'elle décide », marquée
    [outil] ou [document] quand sa réponse se cherche d'abord ailleurs que chez la personne. Les parties d'un sujet
    ne sont pas reprises : la décision de chaque question suffit, et la consigne reste courte."""
    lignes = []
    for s in index:
        questions = [q for q in base(s["sujet"], dossier) if not _barree(q)]
        if not questions:
            continue
        lignes.append(f"### {s['sujet']}")
        lignes += [f"{q['id']} {q['question']} → {q['decide']}{MARQUES_DABORD.get(q['dabord'], '')}" for q in questions]
        lignes.append("")
    return "\n".join(lignes).rstrip()


def consigne_en_ligne(dossier=None):
    """La consigne de l'agent en ligne : la méthode condensée (`consigne-en-ligne.md`), l'index des sujets de la base et,
    sous forme compacte, toutes ses questions (numéro, question, ce qu'elle décide), sauf les questions barrées."""
    dossier = pathlib.Path(dossier or BASE)
    gabarit = _lire(CONSIGNE_EN_LIGNE).split("\n---\n", 1)
    if len(gabarit) != 2:
        raise Erreur("consigne-en-ligne.md : la ligne --- qui ouvre la consigne est absente")
    index = index_des_sujets(dossier)
    champs = {"MAX": MAX_EN_LIGNE, "CHOIX_MIN": CHOIX_EN_LIGNE[0], "CHOIX_MAX": CHOIX_EN_LIGNE[1],
              "CHOIX_LONGUEUR": CHOIX_LONGUEUR, "PLAN_MIN": PLAN_EN_LIGNE[0], "PLAN_MAX": PLAN_EN_LIGNE[1],
              "INDEX": "\n".join(f"- {s['sujet']} ({s['prefixe']}) | {s['nom']} | {s['quand']}" for s in index),
              "QUESTIONS": _bloc_questions_en_ligne(index, dossier)}
    texte = gabarit[1].strip() + "\n"
    for cle, valeur in champs.items():
        texte = texte.replace("{{" + cle + "}}", str(valeur))
    reste = re.findall(r"\{\{[A-Z_]+\}\}", texte)
    if reste:
        raise Erreur(f"champs non remplis dans la consigne en ligne : {', '.join(sorted(set(reste)))}")
    return texte


def schema_en_ligne(dossier=None):
    """Le schéma du compte rendu de l'agent en ligne, avec les sujets de la base du jour : `sujet` n'en prend qu'un."""
    s = json.loads(_lire(SCHEMA_EN_LIGNE))
    s["properties"]["sujet"]["enum"] = [x["sujet"] for x in index_des_sujets(dossier)]
    return s


def ligne_en_ligne(dossier=None):
    """Ce que l'hôte garde pour l'agent en ligne : {titre, guide, consigne, schema_compte_rendu, questionnaire}. Le
    `questionnaire` n'est pas une liste de questions (l'agent les choisit) : il dit le sujet de départ, le mode et les
    sujets de la base que la consigne porte."""
    return {"titre": TITRE_EN_LIGNE, "guide": GUIDE_EN_LIGNE, "consigne": consigne_en_ligne(dossier),
            "schema_compte_rendu": schema_en_ligne(dossier),
            "questionnaire": {"base": BASE_EN_LIGNE, "mode": GUIDE_EN_LIGNE,
                              "sujets": [s["sujet"] for s in index_des_sujets(dossier)]}}


def mesure_consigne_en_ligne(ligne, dossier=None):
    """La taille de la consigne, à afficher : le modèle la relit à chaque tour, la base ne doit pas la faire grossir
    sans qu'on le voie."""
    n = len(ligne["consigne"])
    return (f"consigne en ligne : {_milliers(n)} caractères (visé : moins de {_milliers(LIMITE_CONSIGNE_EN_LIGNE)}), "
            f"{len(ligne['questionnaire']['sujets'])} sujets, {len(questions_en_ligne(dossier))} questions"
            + ("" if n <= LIMITE_CONSIGNE_EN_LIGNE else " : TROP LONGUE, resserrer la base"))


def ecrire_atomique(chemin, texte):
    """Le fichier est écrit en entier ou pas du tout : un arrêt en route ne laisse pas une ligne tronquée à l'hôte."""
    chemin = pathlib.Path(chemin)
    provisoire = chemin.with_name(chemin.name + ".tmp")
    try:
        chemin.parent.mkdir(parents=True, exist_ok=True)
        with open(provisoire, "w", encoding="utf-8", newline="\n") as f:   # les mêmes fins de ligne sur tout poste
            f.write(texte)
        os.replace(provisoire, chemin)
    except OSError as e:
        if provisoire.exists():
            provisoire.unlink()
        raise Erreur(f"écriture impossible : {chemin} ({e})") from None


# Un prix : un montant avec sa devise, ou une devise suivie d'un montant, ou un « HT » / « TTC ». Une piste n'en porte pas.
PRIX = re.compile(r"\d[\d\s.,]*k?\s?(?:€|\$|£|euros?\b|eur\b|usd\b|dollars?\b|gbp\b)|[€$£]\s?\d"
                  r"|\b(?:eur|euros?|usd|dollars?|gbp)\s?\d|\b(?:HT|TTC)\b", re.I)


def controler_en_ligne(cr, q=None, dossier=None):
    """Les écarts d'un compte rendu de l'agent en ligne ; une liste vide veut dire que la note peut s'écrire. `q` : le
    `questionnaire` de la ligne de l'agent (`consigne-en-ligne`), que l'hôte garde ; il ne sert qu'à vérifier le guide.
    Une question qui n'est pas dans la base, plus de douze réponses, une adresse ou un numéro, un prix dans une piste :
    la note est refusée."""
    ecarts = []
    for cle in json.loads(_lire(SCHEMA_EN_LIGNE))["required"] + ["date"]:
        if cle not in cr:
            ecarts.append(f"champ manquant : {cle}" + (" (l'hôte la pose)" if cle == "date" else ""))
    if ecarts:
        return ecarts
    if isinstance(q, dict) and q.get("guide", GUIDE_EN_LIGNE) != GUIDE_EN_LIGNE:
        ecarts.append(f"le compte rendu suit le guide {GUIDE_EN_LIGNE}, le questionnaire donné est {q.get('guide')}")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(cr["date"])):
        ecarts.append("date : AAAA-MM-JJ attendu")
    duree = cr.get("duree_minutes")
    if duree is not None and (not isinstance(duree, int) or isinstance(duree, bool) or duree < 0):
        ecarts.append("duree_minutes : un nombre entier de minutes attendu")
    textes = []   # (où, texte) : ce qui est lu pour les adresses, les numéros et les noms

    def texte(valeur, ou):
        if not isinstance(valeur, str) or not valeur.strip():
            ecarts.append(f"{ou} : un texte est attendu")
            return ""
        textes.append((ou, valeur))
        return valeur

    def liste(valeur, ou):
        if not isinstance(valeur, list) or not all(isinstance(x, str) for x in valeur):
            ecarts.append(f"{ou} : une liste de textes est attendue")
            return []
        textes.extend((ou, x) for x in valeur)
        return valeur

    texte(cr["demande"], "demande")
    contexte = cr["contexte"]
    if not isinstance(contexte, dict):
        ecarts.append("contexte : taille, metier et outils attendus")
    else:
        for cle in ("taille", "metier"):
            if not isinstance(contexte.get(cle), str):
                ecarts.append(f"contexte.{cle} : un texte est attendu (vide si la personne ne l'a pas dit)")
            else:
                textes.append((f"contexte.{cle}", contexte[cle]))
        liste(contexte.get("outils"), "contexte.outils")
    connus = sujets(dossier)
    if cr["sujet"] not in connus:
        ecarts.append(f"sujet : {cr['sujet']!r} n'est pas un sujet de la base (connus : {', '.join(connus)})")
    reponses = cr["reponses"]
    if not isinstance(reponses, list) or not reponses:
        ecarts.append("reponses : au moins une réponse est attendue")
        reponses = []
    if len(reponses) > MAX_EN_LIGNE:
        ecarts.append(f"reponses : {len(reponses)} réponses, {MAX_EN_LIGNE} au plus (l'entretien en ligne reste court)")
    actives = questions_en_ligne(dossier)
    vus = set()
    for i, r in enumerate(reponses, 1):
        ou = f"reponses[{i}]"
        if not isinstance(r, dict):
            ecarts.append(f"{ou} : id, question et reponse attendus")
            continue
        ident = r.get("id")
        if not isinstance(ident, str):
            ecarts.append(f"{ou}.id : le numéro de la question dans la base est attendu")
        else:
            if ident in vus:
                ecarts.append(f"{ou} : la question {ident} est déjà dans les réponses")
            vus.add(ident)
            if ident not in actives:
                ecarts.append(f"{ou} : {ident!r} n'est pas une question de la base (inventée, retirée ou mal recopiée) ; "
                              "l'agent en ligne ne pose que des questions de la base")
        texte(r.get("question"), f"{ou}.question")
        texte(r.get("reponse"), f"{ou}.reponse")
    pistes = cr["pistes"]
    if not isinstance(pistes, list):
        ecarts.append("pistes : une liste est attendue")
        pistes = []
    for i, p in enumerate(pistes, 1):
        if not isinstance(p, dict):
            ecarts.append(f"pistes[{i}] : constat et piste attendus")
            continue
        texte(p.get("constat"), f"pistes[{i}].constat")
        if PRIX.search(texte(p.get("piste"), f"pistes[{i}].piste") or ""):
            ecarts.append(f"pistes[{i}].piste : un prix ; l'agent en ligne n'en donne pas, il est pour le consultant")
    liste(cr["questions_ouvertes"], "questions_ouvertes")
    if PRIX.search(texte(cr["prochaine_etape"], "prochaine_etape") or ""):
        ecarts.append("prochaine_etape : un prix ; l'agent en ligne n'en donne pas, il est pour le consultant")
    if "pour_la_base" in cr:
        liste(cr["pour_la_base"], "pour_la_base")
    if "noms_a_retirer" in cr and not isinstance(cr["noms_a_retirer"], list):
        ecarts.append("noms_a_retirer : une liste de textes est attendue")
    for ou, t in textes:
        if DONNEE_PERSO.search(t):
            ecarts.append(f"{ou} : une adresse ou un numéro reste dans le texte, à remplacer par [retiré]")
    noms = _noms(cr) if isinstance(cr.get("noms_a_retirer"), list) else None
    if noms and any(noms.search(t) for _, t in textes):
        ecarts.append("un nom écrit pendant l'entretien (noms_a_retirer) reste dans le compte rendu, à retirer")
    return ecarts


def _citation(texte):
    """Le texte d'une personne en citation, sur autant de lignes qu'elle en a écrit."""
    return "> « " + texte.strip().replace("\n", "\n> ") + " »"


def _section(titre, items, vide):
    return [f"## {titre}", ""] + ([f"- {x}" for x in items] or [vide]) + [""]


def rendre_note_en_ligne(cr, nom_transcription=None, dossier=None):
    """La note d'un entretien en ligne, de même structure que celle des autres guides, avec en plus ses pistes et ce qui
    peut entrer dans la base de questions."""
    contexte = cr["contexte"]
    role = _role(cr)
    entete = f"# Entretien — {role}" + (f", {contexte['metier']}" if contexte["metier"] else "")
    entete += f" · {cr['date']}" + (f" · {cr['duree_minutes']} min" if cr.get("duree_minutes") is not None else "")
    nom_guide = f"agent en ligne, {len(cr['reponses'])} questions choisies dans la base (sujet : {cr['sujet']})"
    l = [entete, "",
         "Mené par : entretien guidé par IA (consultant-ia, `mener-entretien-ia`), en ligne, sans le consultant · Guide "
         f"utilisé : {nom_guide} · Personnes présentes (rôles) : {', '.join(cr.get('personnes') or [role])} · Langue : "
         f"{cr.get('langue') or 'non précisée'}", ""]
    if nom_transcription:
        l += [f"Transcription intégrale : `{nom_transcription}` (même dossier).", ""]
    ctx = [f"{nom} : {valeur}" for nom, valeur in (("métier", contexte["metier"]), ("taille", contexte["taille"]),
                                                   ("outils", ", ".join(contexte["outils"]))) if valeur]
    l += ["## Ce qui a été dit", "",
          "L'agent a choisi ses questions dans la base de questions, jamais en dehors. La personne a répondu de mémoire, "
          "en ligne, sans remettre de pièce : tout nombre ci-dessous est un `[H]`, à confirmer par elle.", "",
          "La demande, mot pour mot :", "", _citation(cr["demande"]), "",
          "Contexte : " + (" ; ".join(ctx) if ctx else "non précisé") + ".", ""]
    parties = {ident: q["partie"] for ident, q in questions_en_ligne(dossier).items()}
    for r in cr["reponses"]:
        l += [f"### {r['id']}" + (f" · {parties[r['id']]}" if r["id"] in parties else ""), "",
              f"*{' '.join(r['question'].split())}*", "", _citation(r["reponse"]), ""]
    l += ["## Tâches citées (à reporter dans 01)", "",
          "Non relevées par l'agent en ligne : à tirer des réponses ci-dessus.", ""]
    l += _section("Pièces remises", ["Aucune : l'agent en ligne ne reçoit pas de pièce."], "")
    l += _section("Écarts avec d'autres sources", [], "Aucun relevé.")
    l += _section("Documents ou accès promis", [], "Aucun relevé ici : voir les questions restées ouvertes.")
    l += _section("Questions restées ouvertes", cr["questions_ouvertes"], "Aucune.")
    l += ["## Pistes", ""] + ([f"- {p['constat'].strip()} → piste : {p['piste'].strip()}" for p in cr["pistes"]]
                              or ["Aucune piste relevée."]) + ["", f"Prochaine étape : {cr['prochaine_etape'].strip()}", ""]
    l += _section("Pour la base de questions", cr.get("pour_la_base") or [], "Rien à ajouter.")
    l += [f"À relire par le consultant avant de l'ajouter à `references/base-questions/{cr['sujet']}.md`.", ""]
    return "\n".join(l).rstrip() + "\n"


def main(argv):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sp = p.add_subparsers(dest="commande", required=True)
    a = sp.add_parser("questionnaire")
    a.add_argument("--guide", choices=GUIDES_CONNUS)
    a.add_argument("--questionnaire", help="questionnaire préparé pour un objectif (guide prepare)")
    a = sp.add_parser("consigne")
    a.add_argument("--guide", choices=GUIDES_CONNUS)
    a.add_argument("--questionnaire", help="questionnaire préparé pour un objectif (guide prepare)")
    a.add_argument("--role", required=True)
    a.add_argument("--entreprise", required=True)
    a.add_argument("--langue")
    a.add_argument("--contexte", help="fichier texte : ce que le consultant sait déjà")
    a.add_argument("--consultant", default="le consultant", help="nom affiché, par exemple « Florent »")
    a.add_argument("--objet")
    a = sp.add_parser("base")
    a.add_argument("--sujet", help="sans sujet : la liste des sujets de la base")
    a = sp.add_parser("preparer")
    a.add_argument("--base", required=True, help="le sujet de la base : support-client…")
    a.add_argument("--objectif", required=True)
    a.add_argument("--role", required=True)
    a.add_argument("--entreprise", default="")
    a.add_argument("--garder", help="numéros de la base à garder, dans l'ordre : SC02,SC05,…")
    a.add_argument("--sortie", required=True, help="le fichier du questionnaire, jamais écrasé")
    a = sp.add_parser("ajouter", help="ranger une question nouvelle dans la base")
    a.add_argument("--sujet", required=True)
    a.add_argument("--partie", required=True, help="le numéro de la partie, ou son titre")
    a.add_argument("--question", required=True)
    a.add_argument("--decide", required=True, help="ce que la réponse décide")
    a.add_argument("--dabord", default="la personne", choices=DABORD)
    a.add_argument("--creer-partie", action="store_true", help="ouvrir la partie si elle n'existe pas")
    a = sp.add_parser("creer-sujet", help="ouvrir un sujet qui manque, avec sa première question")
    a.add_argument("--sujet", required=True)
    a.add_argument("--prefixe", required=True)
    a.add_argument("--titre", required=True, help="après « Base de questions : », en minuscule : la facturation")
    a.add_argument("--quand", required=True, help="quand ouvrir ce sujet, pour le tableau du README")
    a.add_argument("--partie", required=True, help="le titre de la première partie")
    a.add_argument("--question", required=True)
    a.add_argument("--decide", required=True)
    a.add_argument("--dabord", default="la personne", choices=DABORD)
    a.add_argument("--intro", default="")
    a.add_argument("--groupe", help="le groupe (#### …) du README où ranger le sujet ; par défaut le dernier groupe de "
                                    "« Ce que veut le client »")
    a.add_argument("--creer-groupe", action="store_true",
                   help="ouvrir le groupe nommé s'il n'existe pas, à la fin de « Ce que veut le client »")
    sp.add_parser("verifier", help="contrôler la base de questions (rend 1 au moindre écart)")
    a = sp.add_parser("consigne-en-ligne", help="la ligne de l'agent d'entretien en ligne : consigne, schéma, sujets (JSON)")
    a.add_argument("--sortie", help="le fichier JSON à écrire ; sans lui, le JSON va sur la sortie standard")
    a = sp.add_parser("schema")
    a.add_argument("--guide", choices=(GUIDE_EN_LIGNE,),
                   help="le schéma du compte rendu de l'agent en ligne ; sans guide, celui des autres guides")
    a = sp.add_parser("note")
    a.add_argument("--compte-rendu", required=True)
    a.add_argument("--questionnaire", help="le questionnaire préparé de l'entretien (guide prepare)")
    a.add_argument("--transcription", help="fichier JSON : liste de {role, texte, le}")
    a.add_argument("--sortie", required=True)
    args = p.parse_args(argv)
    try:
        if args.commande in ("questionnaire", "consigne"):
            guide = "prepare" if args.questionnaire else args.guide
            if not guide:
                raise Erreur("donner --guide, ou --questionnaire pour un questionnaire préparé")
        if args.commande == "questionnaire":
            print(json.dumps(questionnaire(guide, args.questionnaire), ensure_ascii=False, indent=2))
        elif args.commande == "consigne":
            contexte = pathlib.Path(args.contexte).read_text(encoding="utf-8") if args.contexte else ""
            print(consigne(guide, args.role, args.entreprise, args.langue, contexte, args.consultant, args.objet,
                           args.questionnaire))
        elif args.commande == "base":
            print(json.dumps(base(args.sujet) if args.sujet else sujets(), ensure_ascii=False, indent=2))
        elif args.commande == "preparer":
            sortie = pathlib.Path(args.sortie)
            if sortie.exists():
                raise Erreur(f"{sortie} existe déjà : on ne l'écrase pas")
            garder = [g.strip() for g in args.garder.split(",") if g.strip()] if args.garder else None
            sortie.parent.mkdir(parents=True, exist_ok=True)
            sortie.write_text(preparer(args.base, args.objectif, args.role, args.entreprise, garder), encoding="utf-8")
            print(sortie)
        elif args.commande == "ajouter":
            print(ajouter(args.sujet, args.partie, args.question, args.decide, args.dabord, args.creer_partie))
        elif args.commande == "creer-sujet":
            print(creer_sujet(args.sujet, args.prefixe, args.titre, args.quand, args.partie, args.question,
                              args.decide, args.dabord, args.intro, groupe=args.groupe,
                              creer_groupe=args.creer_groupe))
        elif args.commande == "verifier":
            ecarts = verifier_base()
            for e in ecarts:
                print(f"  ✗ {e}")
            if ecarts:
                print(f"base de questions : {len(ecarts)} écart(s)")
            else:
                n = sum(len(base(s)) for s in sujets())
                print(f"base de questions : {len(sujets())} sujets, {n} questions, aucun écart "
                      f"(consigne en ligne : {_milliers(len(consigne_en_ligne()))} caractères sur "
                      f"{_milliers(LIMITE_CONSIGNE_EN_LIGNE)})")
            return 1 if ecarts else 0
        elif args.commande == "consigne-en-ligne":
            ligne = ligne_en_ligne()
            donnees = json.dumps(ligne, ensure_ascii=False, indent=2) + "\n"
            if args.sortie:
                ecrire_atomique(args.sortie, donnees)
                print(args.sortie)
                print(mesure_consigne_en_ligne(ligne))
            else:   # le JSON seul sur la sortie standard, la mesure sur l'autre
                sys.stdout.write(donnees)
                print(mesure_consigne_en_ligne(ligne), file=sys.stderr)
        elif args.commande == "schema":
            print(json.dumps(schema_en_ligne() if args.guide == GUIDE_EN_LIGNE else schema(), ensure_ascii=False,
                             indent=2))
        else:
            cr = json.loads(pathlib.Path(args.compte_rendu).read_text(encoding="utf-8"))
            messages = json.loads(pathlib.Path(args.transcription).read_text(encoding="utf-8")) if args.transcription else None
            prepare = _prepare(args.questionnaire) if args.questionnaire else None
            for f in ecrire_note(cr, args.sortie, messages, prepare):
                print(f)
    except Erreur as e:
        print(f"✗ {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
