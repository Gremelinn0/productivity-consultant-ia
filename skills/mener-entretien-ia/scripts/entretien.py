"""Entretien guidé par IA : questionnaire, consigne de l'intervieweur, note d'entretien.

Usage :
  python entretien.py questionnaire (--guide besoin | --questionnaire mission/sources/questionnaire-<objet>-<date>.md)
  python entretien.py consigne (--guide besoin | --questionnaire …) --role "dirigeante" --entreprise "Société Exemple"
                               [--langue en] [--contexte contexte.md] [--consultant "le consultant"]
  python entretien.py schema
  python entretien.py note --compte-rendu cr.json [--questionnaire …] [--transcription messages.json] --sortie mission/sources

Les questions ne sont écrites qu'à un endroit : `decouvrir-cas-usage/references/guides-entretien.md` (direction,
équipes, version courte), l'étape 3 de `cadrer-besoin` (besoin) et l'étape 9 d'`auditer-processus` (processus).
Ce script les lit là ; il n'en garde aucune copie. Un questionnaire préparé pour un objectif (guide `prepare`) est
un fichier de la mission, au modèle de `references/questionnaire-prepare.md`, validé avant l'entretien. `note`
refuse un compte rendu qui enfreint les règles du pack (statuts, données personnelles) et rend 1.
"""
import argparse
import json
import pathlib
import re
import sys
import unicodedata

ICI = pathlib.Path(__file__).resolve().parent
COMPETENCE = ICI.parent
SKILLS = COMPETENCE.parent
CONSIGNE = COMPETENCE / "references" / "consigne-intervieweur.md"
SCHEMA = COMPETENCE / "references" / "compte-rendu.schema.json"
GUIDES = SKILLS / "decouvrir-cas-usage" / "references" / "guides-entretien.md"
CADRER = SKILLS / "cadrer-besoin" / "SKILL.md"
AUDITER = SKILLS / "auditer-processus" / "SKILL.md"

GUIDES_CONNUS = ("direction", "equipes", "besoin", "processus", "court", "prepare")
PREFIXES = {"direction": "D", "equipes": "E", "besoin": "B", "processus": "P", "court": "C", "prepare": "Q"}
DUREES = {"direction": 30, "equipes": 35, "besoin": 20, "processus": 25, "court": 10}
# Un questionnaire préparé reste un entretien court : au-delà, la personne abandonne, et le reste attend l'audit.
MAX_PREPARE = 12
# La version courte de guides-entretien.md : « la semaine type, la tâche qu'on voudrait ne plus faire, les
# informations recopiées d'un outil à l'autre », soit les thèmes 1, 10 et 5 du guide équipes.
COURT = (1, 10, 5)


class Erreur(Exception):
    pass


def _lire(chemin):
    if not chemin.exists():
        raise Erreur(f"source introuvable : {chemin}")
    return chemin.read_text(encoding="utf-8")


def _tableau(texte, titre):
    """Les lignes `| n | Thème | Question | … |` de la section dont le titre commence par `titre`."""
    m = re.search(r"^## " + re.escape(titre) + r".*?$(.*?)(?=^## |\Z)", texte, re.M | re.S)
    if not m:
        raise Erreur(f"section absente de guides-entretien.md : « {titre} »")
    lignes = []
    for ligne in m.group(1).splitlines():
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cellules) >= 4 and cellules[0].isdigit():
            lignes.append({"numero": int(cellules[0]), "theme": cellules[1], "question": cellules[2],
                           "alimente": cellules[3]})
    if not lignes:
        raise Erreur(f"aucune question lue dans « {titre} »")
    return lignes


def _besoin():
    texte = _lire(CADRER)
    m = re.search(r"Le socle tient en\s+huit questions.*?:\n(.*?)\n\n", texte, re.S)
    if not m:
        raise Erreur("cadrer-besoin : la liste des huit questions (étape 3) est introuvable")
    lignes = []
    for brut in re.findall(r"^\s+- (.+?)\s*\((?:rubriques? )?([\d, ]+)\)\s*$", m.group(1), re.M):
        lignes.append({"numero": len(lignes) + 1, "theme": "", "question": brut[0],
                       "alimente": "10-besoin, rubriques " + brut[1].strip()})
    return lignes


def _processus():
    texte = _lire(AUDITER)
    m = re.search(r"Poser les huit questions d'automatisation.*?\n(.*?)\n\s*Une réponse manquante", texte, re.S)
    if not m:
        raise Erreur("auditer-processus : la liste des huit questions (étape 9) est introuvable")
    lignes = [{"numero": int(n), "theme": "", "question": q.strip(), "alimente": "20-diagnostic §8"}
              for n, q in re.findall(r"^\s+(\d)\. (.+)$", m.group(1), re.M)]
    return lignes


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
    return {"guide": "prepare", "source": chemin.name, "objectif": objectif.group(1), "valide_par": valide.group(1),
            "deja_etabli": deja, "duree_minutes": max(5, round(2.5 * len(lignes))),
            "questions": [{"id": f"Q{l['numero']}", "theme": l["theme"], "question": l["question"],
                           "deja_su": l["deja_su"], "alimente": l["alimente"]} for l in lignes]}


def questionnaire(guide, fichier=None):
    if guide not in GUIDES_CONNUS:
        raise Erreur(f"guide inconnu : {guide} (connus : {', '.join(GUIDES_CONNUS)})")
    if guide == "prepare":
        if not fichier:
            raise Erreur("guide prepare : donner le questionnaire préparé (--questionnaire <fichier>)")
        return _prepare(fichier)
    if guide == "direction":
        lignes, source = _tableau(_lire(GUIDES), "Guide direction"), "decouvrir-cas-usage/references/guides-entretien.md"
    elif guide == "equipes":
        lignes, source = _tableau(_lire(GUIDES), "Guide équipes"), "decouvrir-cas-usage/references/guides-entretien.md"
    elif guide == "court":
        equipes = {l["numero"]: l for l in _tableau(_lire(GUIDES), "Guide équipes")}
        lignes = [dict(equipes[n], numero=i + 1) for i, n in enumerate(COURT)]
        source = "decouvrir-cas-usage/references/guides-entretien.md (version courte)"
    elif guide == "besoin":
        lignes, source = _besoin(), "cadrer-besoin/SKILL.md, étape 3"
    else:
        lignes, source = _processus(), "auditer-processus/SKILL.md, étape 9"
    attendu = {"besoin": 8, "processus": 8, "court": 3}.get(guide)
    if attendu and len(lignes) != attendu:
        raise Erreur(f"guide {guide} : {len(lignes)} questions lues, {attendu} attendues ({source})")
    questions = [{"id": f"{PREFIXES[guide]}{l['numero']}", "theme": l["theme"], "question": l["question"],
                  "alimente": l["alimente"]} for l in lignes]
    return {"guide": guide, "source": source, "duree_minutes": DUREES[guide], "questions": questions}


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
        contexte = (contexte.strip() + "\n\n" if contexte.strip() else "") + "Déjà établi, à ne pas redemander :\n" \
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
    préparé de l'entretien (guide `prepare`), lu dans son fichier ou gardé par l'hôte."""
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
    return ecarts


def slug(texte):
    t = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:40] or "personne"


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
    complet = questionnaire_prepare or questionnaire(cr["guide"])
    q = {x["id"]: x for x in complet["questions"]}
    nom_guide = NOMS_GUIDES.get(cr["guide"]) or (
        f"questionnaire préparé pour : {complet['objectif']} (`{complet['source']}`, {len(q)} questions)")
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
        statut = f"[{t['statut']}]" + (f", {t['confirme_par']}" if t.get("confirme_par") else "")
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
    return "\n".join(l).rstrip() + "\n"


def rendre_transcription(cr, messages):
    l = [f"# Transcription — entretien {cr['role']} · {cr['date']}", "",
         "Entretien écrit guidé par IA. « Assistant » est l'IA ; « Personne » est la personne interrogée. "
         "Texte tel qu'échangé, dans la langue de l'échange ; adresses et numéros remplacés par [retiré].", ""]
    for m in messages:
        qui = "Assistant" if m.get("role") == "assistant" else "Personne"
        texte = DONNEE_PERSO.sub("[retiré]", str(m.get("texte", "")).strip())  # guides-entretien : données personnelles retirées
        l += [f"**{qui}**" + (f" · {m['le']}" if m.get("le") else ""), "", texte, ""]
    return "\n".join(l).rstrip() + "\n"


def ecrire_note(cr, sortie, messages=None, questionnaire_prepare=None):
    ecarts = controler(cr, q=questionnaire_prepare)
    if ecarts:
        raise Erreur("compte rendu refusé :\n  - " + "\n  - ".join(ecarts))
    sortie = pathlib.Path(sortie)
    sortie.mkdir(parents=True, exist_ok=True)
    base = f"entretien-{slug(cr['role'])}-{cr['date']}"
    nom_t = f"{base}.transcription.md" if messages else None
    note = sortie / f"{base}.md"
    note.write_text(rendre_note(cr, nom_t, questionnaire_prepare), encoding="utf-8")
    fichiers = [note]
    if messages:
        (sortie / nom_t).write_text(rendre_transcription(cr, messages), encoding="utf-8")
        fichiers.append(sortie / nom_t)
    return fichiers


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
    a.add_argument("--consultant", default="le consultant")
    a.add_argument("--objet")
    sp.add_parser("schema")
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
        elif args.commande == "schema":
            print(json.dumps(schema(), ensure_ascii=False, indent=2))
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
