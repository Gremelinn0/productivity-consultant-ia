"""Contrôle de forme des livrables d'une mission : le dossier `mission/` suit-il les modèles du pack consultant-ia ?

Un contrôle déterministe, sans IA, pour juger les livrables d'un agent sans lui faire confiance. Il constate la
forme ; il ne juge ni le fond ni la justesse d'un chiffre.

Usage :
  python scripts/verifier_livrables.py <dossier mission> [--attendus 10,20,30] [--json]

<dossier mission> est le dossier `mission/` : 00 à 04 à sa racine, 10 à 70 dans chaque `cas-<slug>/`, et, pour le module
CRM, `20-diagnostic/audit-crm.md` et `30-exigences/annexes-crm.md` d'un cas. Un livrable présent est contrôlé ; un
livrable absent ne fait écart que s'il est attendu : `--attendus` donne ses codes (10, 20… ou `audit-crm`,
`annexes-crm`) et vaut pour chaque dossier `cas-<slug>/`. 80, 85, 90 et 95 (construction, recette, mise en service,
mesure) ne sont pas contrôlés : ils sont listés, jamais déclarés conformes, et les attendre est un contrôle impossible.
Même sort pour `35-optimisation.md` (optimiser le processus), facultatif : listé s'il existe, jamais un écart s'il manque.
Un livrable rangé au mauvais niveau est un écart. Sortie : un verdict OK ou KO par fichier avec ce qui manque, ou `--json`.
Code de sortie : 0 tout ce qui est présent et attendu est conforme · 1 au moins un écart · 2 contrôle impossible
(dossier introuvable ou sans livrable du pack, modèle introuvable).

Pour chaque livrable :
  - titre et en-tête : un titre de niveau 1 ; ce que l'en-tête du modèle porte (date, demandeur, valideur ; pour un
    plan, le décideur du plan) ; une version ajoutée à l'en-tête est datée (`Version 1.1, précisée le 2026-10-12`) ;
  - rubriques : chaque titre de section du modèle, comparé sans casse, accents, numérotation ni ponctuation ; une
    rubrique n'est pas vide (un tableau de cellules vides ne dit rien) ;
  - « Décision attendue » quand le modèle la porte : présente, non vide, dernière rubrique (`ARCHITECTURE.md`, règle 3) ;
  - statuts : au moins un `[F]`, `[H]` ou `[E]` quand le modèle en porte, lui ou les règles de remplissage de son fichier ;
  - identifiants (`EF`, `ENF`, `CA`, `T`, `R`, `IND`, `Q`, `D`, `A`, `EV`) : écrits `EF-01` (deux chiffres au moins), et
    jamais deux fois en tête de ligne d'un tableau d'une même rubrique. Hors du contrôle : un numéro réutilisé d'un
    livrable à l'autre, car la même question se relit légitimement de 30 à 95 (`ARCHITECTURE.md`, « Les identifiants »).

Les rubriques ne sont écrites nulle part ici : elles se lisent à chaque exécution dans le modèle de chaque compétence
(`skills/<compétence>/references/modeles.md`, ou `SKILL.md`), au premier bloc ```markdown qui suit le titre du modèle
(`LIVRABLES`). Un modèle introuvable est un contrôle impossible, jamais un livrable conforme. Le test
`scripts/tests/test_verifier_livrables.py` épingle les titres de chaque modèle : si l'un change, il échoue.
Bibliothèque standard seulement.
"""
import argparse
import json
import pathlib
import re
import sys
import unicodedata
from typing import NamedTuple

RACINE = pathlib.Path(__file__).resolve().parent.parent
DECISION = "decision attendue"  # « Décision attendue », normalisée (`normaliser`)


class Livrable(NamedTuple):
    code: str      # le numéro du livrable (« 10 »), ou son nom pour le module CRM (« audit-crm »)
    nom: str       # le nom du fichier
    ou: str        # « mission » : racine du dossier mission/ · « cas » : chaque dossier cas-<slug>/
    dossier: str   # sous-dossier du cas, s'il y en a un (module CRM)
    modele: str    # le fichier qui porte le modèle, sous skills/
    ancre: str     # le titre de ce fichier qui annonce le modèle (expression régulière, un seul titre doit y répondre)


DECOUVRIR = "decouvrir-cas-usage/references/modeles.md"
CHIFFRER = "chiffrer-rentabilite/references/modeles.md"
PLANIFIER = "planifier-deploiement/references/modeles.md"
REDIGER = "rediger-cahier-des-charges/references/modeles.md"
LIVRABLES = (
    Livrable("00", "00-contexte.md", "mission", "", DECOUVRIR, r"00-contexte\.md"),
    Livrable("01", "01-cartographie-taches.md", "mission", "", DECOUVRIR, r"01-cartographie-taches\.md"),
    Livrable("02", "02-portefeuille.md", "mission", "", DECOUVRIR, r"02-portefeuille\.md"),
    Livrable("03", "03-chiffrage.md", "mission", "", CHIFFRER, r"03-chiffrage\.md"),
    Livrable("04", "04-feuille-de-route.md", "mission", "", PLANIFIER, r"04-feuille-de-route\.md"),
    Livrable("10", "10-besoin.md", "cas", "", "cadrer-besoin/SKILL.md", r"^Le livrable$"),
    Livrable("20", "20-diagnostic.md", "cas", "", "auditer-processus/references/modeles.md", r"^Le modèle$"),
    Livrable("audit-crm", "audit-crm.md", "cas", "20-diagnostic", "auditer-crm/SKILL.md", r"^Le livrable$"),
    Livrable("30", "30-exigences.md", "cas", "", REDIGER, r"30-exigences\.md"),
    Livrable("annexes-crm", "annexes-crm.md", "cas", "30-exigences",
             "auditer-crm/references/trame-cahier-des-charges.md", r"annexes-crm\.md"),
    Livrable("40", "40-solutions.md", "cas", "", "concevoir-solution/references/modeles.md", r"^Le modèle$"),
    Livrable("50", "50-rentabilite.md", "cas", "", CHIFFRER, r"50-rentabilite\.md"),
    Livrable("60", "60-specification.md", "cas", "", REDIGER, r"60-specification\.md"),
    Livrable("70", "70-plan.md", "cas", "", PLANIFIER, r"70-plan\.md"),
)
# Les étapes 8 à 11 (construire, tester, mettre en service, mesurer) ont leurs modèles, que ce contrôle ne lit pas encore.
# 35 (optimiser le processus, décision du 09/11/2026) est facultatif et n'a pas de modèle dans le pack : le compagnon
# `operations:process-optimization` l'écrit. Présent, il est listé, jamais déclaré conforme ; absent, ce n'est pas un écart ;
# l'attendre est un contrôle impossible.
FACULTATIFS = ("35-optimisation.md",)
HORS_CONTROLE = ("80-construction.md", "85-recette.md", "90-mise-en-service.md", "95-mesure.md")

TITRE = re.compile(r" {0,3}(#{1,6})[ \t]+(.*?)(?:[ \t]+#+)?[ \t]*")
BARRIERE = re.compile(r" {0,3}(`{3,}|~{3,})(.*)")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
STATUT = re.compile(r"\[[FHE]\]")
TIRETS = "_\\-" + chr(0x2010) + "-" + chr(0x2015)  # trait d'union, tiret bas, puis les tirets typographiques U+2010 à U+2015
SERIES = "ENF|EF|CA|IND|EV|T|R|Q|D|A"
CANONIQUE = re.compile(rf"(?:{SERIES})-\d{{2,}}")
# Ce qui ressemble à un identifiant. EF, ENF, IND et EV ne se confondent avec rien : le trait d'union est facultatif.
# CA (chiffre d'affaires), T1 (trimestre), A1 (cellule d'un tableur) : le trait d'union est nécessaire.
TENTATIVE = rf"(?:(?:ENF|EF|IND|EV)[ {TIRETS}]?|(?:CA|T|R|Q|D|A)[{TIRETS}])(?:\d+|xx)(?![\w\-])"
TENTATIVE_EN_TETE = re.compile(TENTATIVE, re.I)  # tête d'une ligne de tableau : une casse fautive est aussi une faute
TENTATIVE_EN_TEXTE = re.compile(rf"\b(?:(?:ENF|EF|IND|EV)[ {TIRETS}]?\d+|CA[{TIRETS}]\d+)(?![\w\-])")
VERSION = re.compile(r"version\s+(\d+(?:\.\d+)*)")


class ControleImpossible(Exception):
    """Le contrôle ne peut pas rendre de verdict : dossier ou modèle introuvable."""


class Ecart(NamedTuple):
    controle: str   # titre · entete · version · rubriques · contenu · decision · statuts · identifiants · place · absent · lecture
    message: str
    ligne: object = None  # le numéro de ligne dans le livrable, quand l'écart en a une


class Titre(NamedTuple):
    niveau: int
    texte: str
    ligne: int  # à partir de 1


def normaliser(titre):
    """Un titre comparable : sans numérotation (« 3. », « A. »), casse, accents ni ponctuation."""
    t = re.sub(r"^(?:\d+(?:\.\d+)*[ \t]*[.):]?|[A-Za-z][.)])[ \t]+", "", titre.strip())
    t = unicodedata.normalize("NFKD", t.replace("œ", "oe").replace("Œ", "OE").replace("æ", "ae"))
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())


def sans_accents(texte):
    return "".join(c for c in unicodedata.normalize("NFKD", texte) if not unicodedata.combining(c)).lower()


def cellules(ligne):
    corps = ligne.strip()
    corps = corps[1:] if corps.startswith("|") else corps
    corps = corps[:-1] if corps.endswith("|") and not corps.endswith("\\|") else corps
    return [c.strip() for c in re.split(r"(?<!\\)\|", corps)]


def est_separateur(ligne):
    c = cellules(ligne)
    return bool(c) and all(re.fullmatch(r":?-+:?", x) for x in c)


def dit_quelque_chose(texte):
    return bool(re.search(r"[^\W_]", texte))


class Document:
    """Un livrable ou un modèle lu ligne à ligne : ses titres (hors blocs de code), ses blocs de code et ses tableaux."""

    def __init__(self, texte):
        self.lignes = texte.splitlines()
        self.en_code = []
        self.titres = []
        self.blocs = []  # (indice de la ligne qui ouvre un bloc de code, indice de celle qui le ferme), à partir de 0
        ouvert = debut = None
        for n, ligne in enumerate(self.lignes, 1):
            m = BARRIERE.match(ligne)
            if ouvert is not None:
                self.en_code.append(True)
                if m and m.group(1)[0] == ouvert[0] and len(m.group(1)) >= len(ouvert) and not m.group(2).strip():
                    self.blocs.append((debut, n - 1))
                    ouvert = None
            elif m and not (m.group(1)[0] == "`" and "`" in m.group(2)):
                ouvert, debut = m.group(1), n - 1
                self.en_code.append(True)
            else:
                self.en_code.append(False)
                t = TITRE.fullmatch(ligne)
                if t:
                    self.titres.append(Titre(len(t.group(1)), t.group(2), n))
        if ouvert is not None:
            self.blocs.append((debut, len(self.lignes)))  # un bloc jamais refermé court jusqu'à la fin
        # pour chaque ligne, la rubrique (titre de niveau 1 ou 2) qui la contient : 0 avant le premier titre
        self.rubrique_de = []
        courante = 0
        reste = iter(sorted(t.ligne for t in self.titres if t.niveau <= 2))
        prochaine = next(reste, None)
        for n in range(1, len(self.lignes) + 1):
            if n == prochaine:
                courante = n
                prochaine = next(reste, None)
            self.rubrique_de.append(courante)

    def corps(self, k):
        """Les indices des lignes de la section du k-ième titre, sous-sections comprises."""
        t = self.titres[k]
        fin = next((s.ligne - 1 for s in self.titres[k + 1:] if s.niveau <= t.niveau), len(self.lignes))
        return range(t.ligne, fin)

    def a_du_contenu(self, indices):
        """Une section dit-elle quelque chose ? Ni un titre, ni un en-tête de tableau, ni une ligne de cellules vides."""
        i = indices.start
        while i < indices.stop:
            ligne = self.lignes[i]
            if not self.en_code[i] and ligne.strip().startswith("|"):
                bloc = self.bloc_de_tableau(i, indices.stop)
                donnees = bloc[2:] if len(bloc) > 1 and est_separateur(self.lignes[bloc[1]]) else bloc[1:]
                if any(dit_quelque_chose(c) for j in donnees for c in cellules(self.lignes[j])):
                    return True
                i = bloc[-1] + 1
                continue
            titre = not self.en_code[i] and TITRE.fullmatch(ligne)
            barriere = self.en_code[i] and BARRIERE.match(ligne)
            if dit_quelque_chose(ligne) and not titre and not barriere:
                return True
            i += 1
        return False

    def bloc_de_tableau(self, debut, fin):
        j = debut
        while j < fin and self.lignes[j].strip().startswith("|") and not self.en_code[j]:
            j += 1
        return list(range(debut, j))

    def tableaux(self):
        """Chaque tableau hors bloc de code : les indices de ses lignes de données (l'en-tête et le séparateur exclus)."""
        i = 0
        while i < len(self.lignes):
            if self.lignes[i].strip().startswith("|") and not self.en_code[i]:
                bloc = self.bloc_de_tableau(i, len(self.lignes))
                yield bloc[2:] if len(bloc) > 1 and est_separateur(self.lignes[bloc[1]]) else bloc[1:]
                i = bloc[-1] + 1
            else:
                i += 1


class Modele(NamedTuple):
    titres: list    # [(titre tel que le modèle l'écrit, titre normalisé, ligne dans le fichier du modèle)]
    entete: set     # ce que l'en-tête du modèle porte : date · demandeur · valideur · decideur du plan
    decision: bool  # le modèle finit par « Décision attendue »
    statuts: bool   # le modèle, ou les règles de son fichier, portent des statuts [F] [H] [E]
    source: str     # fichier:ligne où il commence


def lire_modele(livrable, racine=RACINE):
    """Le modèle d'un livrable, lu dans la compétence qui le possède."""
    chemin = racine / "skills" / livrable.modele
    try:
        fichier = Document(chemin.read_text(encoding="utf-8-sig"))
    except OSError as e:
        raise ControleImpossible(f"modèle de {livrable.nom} introuvable : {chemin} ({e.strerror})")
    ancres = [k for k, t in enumerate(fichier.titres) if re.search(livrable.ancre, t.texte)]
    if len(ancres) != 1:
        raise ControleImpossible(f"modèle de {livrable.nom} introuvable : {len(ancres)} titre(s) de skills/{livrable.modele} "
                                 f"répondent à « {livrable.ancre} » (un seul est attendu)")
    ancre = fichier.titres[ancres[0]]
    section = fichier.corps(ancres[0])
    bloc = next(((o, c) for o, c in fichier.blocs if o in section), None)
    if bloc:
        # le modèle est le bloc ```markdown qui suit le titre ; ses rubriques sont ses titres de niveau 2
        ouverture, cloture = bloc
        modele = Document("\n".join(fichier.lignes[ouverture + 1:cloture]))
        decalage = ouverture + 1  # ligne du bloc + decalage = ligne du fichier
        rubriques = [t for t in modele.titres if t.niveau == 2]
        premiere = rubriques[0].ligne - 1 if rubriques else len(modele.lignes)
        entete, texte = "\n".join(modele.lignes[:premiere]), "\n".join(modele.lignes)
        depart = ouverture + 1
    else:
        # pas de bloc : le modèle est la section elle-même, ses sous-titres sont les rubriques (annexes du module CRM)
        decalage = 0
        rubriques = [t for t in fichier.titres if t.niveau == ancre.niveau + 1 and t.ligne - 1 in section]
        entete, texte = "", "\n".join(fichier.lignes[section.start:section.stop])
        depart = ancre.ligne
    if not rubriques:
        raise ControleImpossible(f"modèle de {livrable.nom} illisible : aucune rubrique à partir de "
                                 f"skills/{livrable.modele}:{depart}")
    # Les règles de remplissage d'un fichier de modèles, ou le lien Dev / Test / QA d'une compétence, précèdent son
    # premier titre de niveau 2 : ce qu'elles disent des statuts vaut pour les modèles du fichier.
    h2 = next((t.ligne - 1 for t in fichier.titres if t.niveau == 2), len(fichier.lignes))
    regles = "\n".join(fichier.lignes[:h2])
    titres = [(t.texte, normaliser(t.texte), t.ligne + decalage) for t in rubriques]
    z = sans_accents(entete)
    portes = {nom for nom, motif in (("date", r"\bdate\b"), ("demandeur", r"\bdemandeur\b"), ("valideur", r"\bvalideur\b"))
              if re.search(motif, z)}
    if "valideur" not in portes and re.search(r"decideur du plan", z):
        portes.add("decideur du plan")  # le plan n'a pas de « valideur » : son décideur est le rôle qui le valide
    return Modele(titres, portes, any(n == DECISION for _, n, _ in titres), bool(STATUT.search(regles + texte)),
                  f"skills/{livrable.modele}:{depart}")


def controler_entete(doc, modele):
    ecarts = []
    h1 = next((t for t in doc.titres if t.niveau == 1), None)
    if h1 is None:
        ecarts.append(Ecart("titre", "titre de niveau 1 absent (« # … » : le modèle commence par lui)"))
    debut = h1.ligne - 1 if h1 else 0
    rubrique = next((t for t in doc.titres if t.niveau >= 2 and (h1 is None or t.ligne > h1.ligne)), None)
    zone = "\n".join(doc.lignes[debut:(rubrique.ligne - 1) if rubrique else len(doc.lignes)])
    z = sans_accents(zone)
    if "date" in modele.entete and not DATE.search(zone):
        ecarts.append(Ecart("entete", "aucune date AAAA-MM-JJ dans l'en-tête"))
    if "demandeur" in modele.entete and not re.search(r"\bdemandeur\b", z):
        ecarts.append(Ecart("entete", "le demandeur manque à l'en-tête"))
    if "valideur" in modele.entete and not re.search(r"\bvalideur\b", z):
        ecarts.append(Ecart("entete", "le valideur manque à l'en-tête"))
    if "decideur du plan" in modele.entete and not re.search(r"\bvalideur\b|\bdecideur du plan\b", z):
        ecarts.append(Ecart("entete", "le décideur du plan (le rôle qui le valide) manque à l'en-tête"))
    # une version qui s'ajoute à l'en-tête est datée, avec son motif (ARCHITECTURE.md, « Corriger un livrable déjà validé »)
    for n, ligne in enumerate(zone.splitlines(), h1.ligne if h1 else 1):
        for segment in ligne.split(" · "):
            m = VERSION.match(sans_accents(segment).strip())
            if m and m.group(1) not in ("1", "1.0") and not DATE.search(segment):
                ecarts.append(Ecart("version", f"la version {m.group(1)} n'est pas datée "
                                    "(« Version x.y, précisée le AAAA-MM-JJ : motif »)", n))
    return ecarts


def controler_rubriques(doc, modele):
    ecarts = []
    presentes = {}
    for k, t in enumerate(doc.titres):
        if t.niveau >= 2:
            presentes.setdefault(normaliser(t.texte), k)
    for ecrit, norme, ligne in modele.titres:
        if norme == DECISION and modele.decision:
            continue  # contrôlée à part
        if norme not in presentes:
            fichier = modele.source.rsplit(":", 1)[0]
            ecarts.append(Ecart("rubriques", f"rubrique absente : « {ecrit} » (modèle : {fichier}:{ligne})"))
        elif not doc.a_du_contenu(doc.corps(presentes[norme])):
            t = doc.titres[presentes[norme]]
            ecarts.append(Ecart("contenu", f"rubrique vide : « {t.texte} »", t.ligne))
    return ecarts


def controler_decision(doc, modele):
    if not modele.decision:
        return []
    ks = [k for k, t in enumerate(doc.titres) if t.niveau >= 2 and normaliser(t.texte) == DECISION]
    if not ks:
        return [Ecart("decision", "« Décision attendue » absente : chaque livrable finit par elle (ARCHITECTURE.md, règle 3)")]
    t = doc.titres[ks[-1]]
    ecarts = []
    suivant = next((s for s in doc.titres[ks[-1] + 1:] if s.niveau <= t.niveau), None)
    if suivant:
        ecarts.append(Ecart("decision", f"« Décision attendue » n'est pas la dernière rubrique : « {suivant.texte} » "
                            "la suit (chaque livrable finit par elle)", suivant.ligne))
    if not doc.a_du_contenu(doc.corps(ks[-1])):
        ecarts.append(Ecart("decision", "« Décision attendue » est vide : elle dit ce que le valideur doit trancher", t.ligne))
    return ecarts


def controler_statuts(doc, modele):
    if modele.statuts and not any(STATUT.search(l) for l, c in zip(doc.lignes, doc.en_code) if not c):
        return [Ecart("statuts", "aucun statut [F], [H] ou [E] : le modèle en porte (ARCHITECTURE.md, « Les trois statuts »)")]
    return []


def attendu_pour(jeton):
    m = re.match(r"[A-Za-z]+", jeton)
    return f"{m.group(0).upper()}-01, deux chiffres au moins" if m else "PREFIXE-01"


def controler_identifiants(doc):
    ecarts, vus, signales = [], {}, set()
    for donnees in doc.tableaux():
        for i in donnees:
            tete = TENTATIVE_EN_TETE.match(re.sub(r"^[`*_\s]+", "", cellules(doc.lignes[i])[0]))
            if not tete:
                continue
            jeton = tete.group(0)
            if not CANONIQUE.fullmatch(jeton):
                signales.add((i + 1, jeton))
                if jeton.lower().endswith("xx"):
                    ecarts.append(Ecart("identifiants", f"identifiant non renseigné « {jeton} » : "
                                        "le modèle est resté tel quel", i + 1))
                else:
                    ecarts.append(Ecart("identifiants", f"identifiant mal formé « {jeton} » "
                                        f"(attendu : {attendu_pour(jeton)})", i + 1))
                continue
            cle = (doc.rubrique_de[i], jeton)
            if cle in vus:
                ecarts.append(Ecart("identifiants", f"doublon : {jeton} ouvre deux lignes de tableau de la même rubrique "
                                    f"(lignes {vus[cle]} et {i + 1}) ; un numéro n'est jamais réutilisé", i + 1))
            else:
                vus[cle] = i + 1
    for n, (ligne, en_code) in enumerate(zip(doc.lignes, doc.en_code), 1):
        if en_code:
            continue
        for m in TENTATIVE_EN_TEXTE.finditer(ligne):
            if not CANONIQUE.fullmatch(m.group(0)) and (n, m.group(0)) not in signales:
                ecarts.append(Ecart("identifiants", f"identifiant mal formé « {m.group(0)} » "
                                    f"(attendu : {attendu_pour(m.group(0))})", n))
    return sorted(ecarts, key=lambda e: e.ligne)


def controler(modele, chemin):
    """Les écarts d'un livrable présent à son modèle."""
    try:
        doc = Document(chemin.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeDecodeError) as e:
        return [Ecart("lecture", f"illisible : {e}")]
    return (controler_entete(doc, modele) + controler_rubriques(doc, modele) + controler_decision(doc, modele)
            + controler_statuts(doc, modele) + controler_identifiants(doc))


class Resultat(NamedTuple):
    fichier: str    # chemin relatif à la mission, avec des /
    code: str
    cas: object     # le slug du cas, ou None pour la racine
    present: bool
    attendu: bool
    ecarts: list

    @property
    def ok(self):
        return not self.ecarts


class Rapport(NamedTuple):
    dossier: str
    attendus: list
    resultats: list
    non_controles: list

    @property
    def conforme(self):
        return all(r.ok for r in self.resultats)


def verifier(dossier, attendus=(), racine=RACINE):
    """Contrôle un dossier mission/ : chaque livrable présent, et chaque livrable attendu."""
    dossier = pathlib.Path(dossier)
    if not dossier.is_dir():
        raise ControleImpossible(f"dossier introuvable : {dossier}")
    attendus = list(dict.fromkeys(attendus))
    hors = [a for a in attendus if a in {n[:2] for n in HORS_CONTROLE + FACULTATIFS}]
    if hors:
        raise ControleImpossible(f"livrable attendu non contrôlé : {', '.join(hors)} "
                                 "(les étapes 8 à 11 et l'étape facultative 35 sont hors de ce contrôle)")
    inconnus = [a for a in attendus if a not in {l.code for l in LIVRABLES}]
    if inconnus:
        raise ControleImpossible(f"livrable attendu inconnu : {', '.join(inconnus)} "
                                 f"(connus : {', '.join(l.code for l in LIVRABLES)})")
    modeles = {l.code: lire_modele(l, racine) for l in LIVRABLES}
    cas = sorted(d for d in dossier.iterdir() if d.is_dir() and d.name.startswith("cas-"))
    emplacements = [(dossier, None, "mission")] + [(d, d.name[4:], "cas") for d in cas]
    resultats, non_controles = [], []
    for base, slug, nature in emplacements:
        prefixe = "" if slug is None else f"cas-{slug}/"
        for livrable in LIVRABLES:
            if livrable.ou != nature:
                continue
            chemin = base / livrable.dossier / livrable.nom
            fichier = prefixe + (f"{livrable.dossier}/" if livrable.dossier else "") + livrable.nom
            attendu = livrable.code in attendus
            if chemin.is_file():
                resultats.append(Resultat(fichier, livrable.code, slug, True, attendu,
                                          controler(modeles[livrable.code], chemin)))
            elif attendu:
                resultats.append(Resultat(fichier, livrable.code, slug, False, True,
                                          [Ecart("absent", "livrable attendu, absent du dossier")]))
        # un livrable rangé à l'autre niveau n'est lu par personne : c'est un écart, pas un silence
        for livrable in LIVRABLES:
            if livrable.ou != nature and not livrable.dossier and (base / livrable.nom).is_file():
                ou = "à la racine de mission/" if livrable.ou == "mission" else "dans mission/cas-<slug>/"
                resultats.append(Resultat(prefixe + livrable.nom, livrable.code, slug, True, False,
                                          [Ecart("place", f"{livrable.nom} est rangé au mauvais niveau : il va {ou}")]))
        non_controles += [prefixe + nom for nom in FACULTATIFS + HORS_CONTROLE if (base / nom).is_file()]
    if not cas:
        for livrable in LIVRABLES:
            if livrable.ou == "cas" and livrable.code in attendus:
                resultats.append(Resultat(f"cas-<slug>/{livrable.nom}", livrable.code, None, False, True,
                                          [Ecart("absent", "livrable attendu : la mission n'a aucun dossier cas-<slug>/")]))
    if not resultats:
        raise ControleImpossible(f"aucun livrable du pack dans {dossier} : le dossier à donner est mission/, "
                                 "qui contient 00-contexte.md… et les dossiers cas-<slug>/")
    return Rapport(str(dossier), attendus, resultats, non_controles)


def rendre_texte(rapport):
    sortie = [f"mission : {rapport.dossier}"]
    for r in rapport.resultats:
        sortie.append(f"{'OK' if r.ok else 'KO'}  {r.fichier}")
        for e in r.ecarts:
            sortie.append(f"      {e.controle} : {e.message}" + (f" [ligne {e.ligne}]" if e.ligne else ""))
    if rapport.non_controles:
        sortie.append("Non contrôlés (étape facultative 35 et étapes 8 à 11, hors de ce contrôle) : " + ", ".join(rapport.non_controles))
    ko = [r for r in rapport.resultats if not r.ok]
    if ko:
        sortie.append(f"Verdict : KO ({len(ko)} fichier(s) en écart sur {len(rapport.resultats)})")
    else:
        sortie.append(f"Verdict : OK ({len(rapport.resultats)} fichier(s) conformes)")
    return "\n".join(sortie)


def rendre_json(rapport):
    return json.dumps({
        "dossier": rapport.dossier,
        "conforme": rapport.conforme,
        "attendus": rapport.attendus,
        "livrables": [{"fichier": r.fichier, "code": r.code, "cas": r.cas, "present": r.present, "attendu": r.attendu,
                       "ok": r.ok, "ecarts": [{"controle": e.controle, "message": e.message, "ligne": e.ligne}
                                              for e in r.ecarts]} for r in rapport.resultats],
        "non_controles": rapport.non_controles,
    }, ensure_ascii=False, indent=2)


def lire_attendus(texte):
    """« 10, 20-diagnostic,audit-crm » → ['10', '20', 'audit-crm']."""
    codes = []
    for jeton in re.split(r"[,\s]+", texte.strip()):
        m = re.fullmatch(r"(\d\d)(?:-[a-z-]+)?(?:\.md)?", jeton)
        codes.append(m.group(1) if m else re.sub(r"\.md$", "", jeton))
    return [c for c in codes if c]


def main(argv):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("dossier", help="le dossier mission/ à contrôler")
    p.add_argument("--attendus", default="", help="les livrables qui doivent exister : 10,20,30 (00 à 04, 10 à 70, "
                   "audit-crm, annexes-crm) ; un code de cas vaut pour chaque dossier cas-<slug>/")
    p.add_argument("--json", action="store_true", help="le verdict en JSON")
    a = p.parse_args(argv)
    try:
        rapport = verifier(a.dossier, lire_attendus(a.attendus))
    except ControleImpossible as e:
        if a.json:
            print(json.dumps({"conforme": False, "erreur": str(e)}, ensure_ascii=False, indent=2))
        print(f"contrôle impossible : {e}", file=sys.stderr)
        return 2
    print(rendre_json(rapport) if a.json else rendre_texte(rapport))
    return 0 if rapport.conforme else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
