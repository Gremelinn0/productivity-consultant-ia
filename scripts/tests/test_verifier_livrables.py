"""Essais de scripts/verifier_livrables.py : python -m unittest discover -s scripts/tests

Le témoin positif est la mission fictive de examples/societe-exemple/mission : elle passe en entier. Les sabotages en
cassent une copie, une règle à la fois : chacun doit faire échouer le contrôle et dire ce qui manque.
"""
import contextlib
import io
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ICI = pathlib.Path(__file__).resolve().parent
SCRIPTS = ICI.parent
RACINE = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))
import verifier_livrables as vl  # noqa: E402

TEMOIN = RACINE / "examples" / "societe-exemple" / "mission"
CAS = "cas-relances-factures"
NBSP, APOSTROPHE_TYPOGRAPHIQUE, TRAIT_D_UNION_INSECABLE, DEMI_CADRATIN = chr(0xA0), chr(0x2019), chr(0x2011), chr(0x2013)
DECISION = "Décision attendue"

# Les titres de chaque modèle, tels que la compétence qui le possède les écrit. Le contrôle lit les modèles à chaque
# exécution : si l'un d'eux perd une rubrique, il en exige une de moins sans le dire, et un livrable que ce contrôle
# refusait hier passe aujourd'hui. Ce test est la garde : il échoue dès qu'un titre change. Mettre alors à jour la
# table, puis l'exemple et les livrables concernés.
TITRES = {
    # decouvrir-cas-usage/references/modeles.md, parties A, B et C
    "00": ["1. Fiche entreprise", "2. Sources branchées et autorisations obtenues", "3. Sources manquantes", DECISION],
    "01": ["1. Les tâches", "2. Écarts gardés et tâches non observées", "3. Le tri", DECISION],
    "02": ["1. Vue d'ensemble", "2. Fiches", "3. Recommandation", DECISION],
    # chiffrer-rentabilite/references/modeles.md, parties A et B
    "03": ["1. Paramètres communs", "2. Un cas par ligne, en fourchettes bas" + DEMI_CADRATIN + "haut", "3. Classement",
           "4. Hypothèses à confirmer", "5. Hors chiffrage", DECISION],
    "50": ["1. Situation de référence", "2. Hypothèses et mesure", "3. Calcul par option",
           "4. Trois scénarios et point mort", "5. Temps libéré et adoption", "6. Valeur non financière",
           "7. Recommandation", DECISION],
    # planifier-deploiement/references/modeles.md, parties A et B
    "04": ["1. Les cas, notés", "2. La séquence", "3. Socle commun et prérequis à lever d'abord",
           "4. Ce qu'on ne fait pas maintenant", "5. Pré-mortem", DECISION],
    "70": ["1. Objectif et critères de réussite", "2. Lots", "3. Porte, pilote, recette et mise en production",
           "4. Adoption", "5. Exploitation", "6. Protocole de mesure", "7. Communication", "8. Pré-mortem", DECISION],
    # cadrer-besoin/SKILL.md, « Le livrable »
    "10": ["1. La demande, telle qu'exprimée", "2. Reformulation", "3. Symptôme, problème, solution demandée",
           "4. Décision à prendre", "5. Parties prenantes", "6. Périmètre", "7. Contraintes", "8. Critères de succès",
           "9. Ce qu'on sait, ce qu'on suppose, ce qu'on ignore", "10. Est-ce le bon problème ?", DECISION],
    # auditer-processus/references/modeles.md, « Le modèle »
    "20": ["1. Le processus tel qu'il se fait", "2. Mesures", "3. Goulets et gaspillages", "4. Causes", "5. Stabilité",
           "6. Tri des étapes", "7. À simplifier et à standardiser d'abord", "8. Les huit questions d'automatisation",
           "9. Opportunités classées", DECISION],
    # auditer-crm/SKILL.md, « Le livrable »
    "audit-crm": ["Bilan, à lire d'abord", "1. Vue d'usage", "2. Automatisations, intégrations et outils",
                  "3. Données", "4. Ventes", "5. Tableaux de bord", "Ce qui reste à vérifier", DECISION],
    # rediger-cahier-des-charges/references/modeles.md, parties A et B
    "30": ["1. Contexte et objectifs", "2. Utilisateurs et rôles", "3. Processus cible", "4. Exigences fonctionnelles",
           "5. Données", "6. Intégrations", "7. Exigences non fonctionnelles", "8. Contraintes",
           "9. Critères d'acceptation", "10. Indicateurs", "11. Hors périmètre", "12. Questions ouvertes", DECISION],
    "60": ["1. Problème et objectif", "2. Non-objectifs", "3. Utilisateurs et scénarios",
           "4. Comportement étape par étape", "5. Flux de données", "6. Intégrations et droits",
           "7. Gestion des erreurs", "8. Dédoublonnage", "9. Secrets", "10. Observabilité",
           "11. Environnements et versions", "12. Plan de test et recette", "13. Pilote", "14. Indicateurs",
           "15. Risques", "16. Questions ouvertes", "17. Propriétaire de la maintenance", DECISION],
    # auditer-crm/references/trame-cahier-des-charges.md, « Annexes : gabarit de annexes-crm.md » (sous-titres)
    "annexes-crm": ["A. Pipelines et étapes", "B. Droits et visibilité", "C. Catalogue", "D. Raisons de perte",
                    "E. Automatisations souhaitées", "F. Messagerie et rendez-vous"],
    # concevoir-solution/references/modeles.md, « Le modèle »
    "40": ["1. Recommandation", "2. Faut-il automatiser ?", "3. Le chemin le plus simple",
           "4. Où l'humain reste dans la boucle", "5. Les options examinées", "6. Matrice", "7. L'option de repli",
           "8. Plateforme ou code", "9. À vérifier avant de signer", "10. Porte", "11. Questions ouvertes", DECISION],
}
CODES_DU_TEMOIN = ["00", "01", "02", "03", "04", "10", "20", "30", "40", "50", "60", "70"]  # les deux modules CRM : à part


def livrable(code):
    return next(l for l in vl.LIVRABLES if l.code == code)


def chemin_du_temoin(code):
    l = livrable(code)
    return (TEMOIN if l.ou == "mission" else TEMOIN / CAS) / l.dossier / l.nom


def lancer(*arguments):
    """Le contrôle en ligne de commande : (code de sortie, sortie standard, sortie d'erreur)."""
    sortie, erreur = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreur):
        code = vl.main([str(a) for a in arguments])
    return code, sortie.getvalue(), erreur.getvalue()


def doc_conforme(code, niveau="##"):
    """Un livrable fabriqué sur son modèle : toutes ses rubriques, dans chacune une phrase et un statut."""
    lignes = ["# Titre du livrable", "",
              "2026-10-30 · Demandeur : direction générale · Valideur : responsable financier · Rédigé par : essai", ""]
    for ecrit, _, _ in vl.lire_modele(livrable(code)).titres:
        lignes += [f"{niveau} {ecrit}", "", "Une phrase, avec un statut `[H]` (à confirmer par la direction).", ""]
    return "\n".join(lignes)


class Normalisation(unittest.TestCase):
    def test_deux_ecritures_du_meme_titre_se_valent(self):
        for a, b in [("3. Symptôme, problème, solution demandée", "SYMPTOME  PROBLEME : solution demandée"),
                     ("10. Est-ce le bon problème ?", "Est ce le bon probleme"),
                     ("A. Pipelines et étapes", "pipelines et etapes"),
                     ("Décision attendue", "11. décision" + NBSP + "attendue :"),
                     ("L'option de repli", "7) L" + APOSTROPHE_TYPOGRAPHIQUE + "option de repli"),
                     ("Un cas par ligne, en fourchettes bas" + DEMI_CADRATIN + "haut", "un cas par ligne en fourchettes bas-haut"),
                     ("Le cœur", "Le coeur")]:
            with self.subTest(a=a):
                self.assertEqual(vl.normaliser(a), vl.normaliser(b))

    def test_deux_titres_differents_restent_differents(self):
        self.assertNotEqual(vl.normaliser("4. Causes"), vl.normaliser("4. Causes racines"))
        self.assertNotEqual(vl.normaliser("2. Mesures"), vl.normaliser("2. Mesure"))
        self.assertNotEqual(vl.normaliser("Questions ouvertes"), vl.normaliser("Questions"))


class ModelesDeLaCompetence(unittest.TestCase):
    def test_les_titres_de_chaque_modele_sont_epingles(self):
        self.assertEqual(sorted(TITRES), sorted(l.code for l in vl.LIVRABLES))
        for l in vl.LIVRABLES:
            with self.subTest(livrable=l.code):
                self.assertEqual([t[0] for t in vl.lire_modele(l).titres], TITRES[l.code])

    def test_ce_que_chaque_modele_porte(self):
        for l in vl.LIVRABLES:
            m = vl.lire_modele(l)
            with self.subTest(livrable=l.code):
                self.assertTrue(m.statuts, "tous les modèles portent des statuts, lui ou ses règles de remplissage")
                self.assertEqual(m.decision, l.code != "annexes-crm", "toutes les fiches finissent par la décision attendue")
                attendu = ({"date", "demandeur", "decideur du plan"} if l.code == "70" else
                           set() if l.code == "annexes-crm" else {"date", "demandeur", "valideur"})
                self.assertEqual(m.entete, attendu)

    def test_chaque_erreur_dit_ou_est_le_modele(self):
        m = vl.lire_modele(livrable("20"))
        self.assertRegex(m.source, r"^skills/auditer-processus/references/modeles\.md:\d+$")
        ecrit, _, ligne = m.titres[3]
        fichier = RACINE / "skills" / "auditer-processus" / "references" / "modeles.md"
        self.assertEqual(fichier.read_text(encoding="utf-8").splitlines()[ligne - 1], f"## {ecrit}")

    def _racine_avec_modeles(self, retoucher=None):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        racine = pathlib.Path(tmp.name)
        for l in vl.LIVRABLES:
            cible = racine / "skills" / l.modele
            if not cible.exists():
                cible.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(RACINE / "skills" / l.modele, cible)
        if retoucher:
            retoucher(racine)
        return racine

    def test_le_controle_suit_le_modele_sans_table_a_part(self):
        def ajouter_une_rubrique(racine):
            f = racine / "skills" / "auditer-processus" / "references" / "modeles.md"
            texte = f.read_text(encoding="utf-8")
            self.assertIn("## 9. Opportunités classées", texte)
            f.write_text(texte.replace("## 9. Opportunités classées", "## 9bis. Une rubrique de plus\n\n"
                                       "## 9. Opportunités classées", 1), encoding="utf-8", newline="\n")
        racine = self._racine_avec_modeles(ajouter_une_rubrique)
        rapport = vl.verifier(TEMOIN, racine=racine)
        ko = [r for r in rapport.resultats if not r.ok]
        self.assertEqual([r.fichier for r in ko], [f"{CAS}/20-diagnostic.md"])
        self.assertIn("9bis. Une rubrique de plus", ko[0].ecarts[0].message)

    def test_un_modele_introuvable_n_est_jamais_un_livrable_conforme(self):
        with tempfile.TemporaryDirectory() as vide:
            with self.assertRaises(vl.ControleImpossible):
                vl.verifier(TEMOIN, racine=pathlib.Path(vide))

        def renommer_le_titre(racine):  # le titre qui annonce le modèle disparaît : plus d'ancre
            f = racine / "skills" / "cadrer-besoin" / "SKILL.md"
            f.write_text(f.read_text(encoding="utf-8").replace("## Le livrable", "## Le résultat", 1),
                         encoding="utf-8", newline="\n")
        with self.assertRaisesRegex(vl.ControleImpossible, "10-besoin.md introuvable"):
            vl.verifier(TEMOIN, racine=self._racine_avec_modeles(renommer_le_titre))

        def doubler_le_titre(racine):  # deux titres répondent à l'ancre : lequel est le modèle ? on ne choisit pas en silence
            f = racine / "skills" / "cadrer-besoin" / "SKILL.md"
            f.write_text(f.read_text(encoding="utf-8").replace("## Le livrable", "## Le livrable\n\n## Le livrable", 1),
                         encoding="utf-8", newline="\n")
        with self.assertRaisesRegex(vl.ControleImpossible, r"10-besoin.md introuvable : 2 titre\(s\)"):
            vl.verifier(TEMOIN, racine=self._racine_avec_modeles(doubler_le_titre))

        def vider_le_modele(racine):  # le titre reste, le bloc et ses rubriques non
            f = racine / "skills" / "planifier-deploiement" / "references" / "modeles.md"
            texte = f.read_text(encoding="utf-8")
            f.write_text(re.sub(r"(## A\. Feuille de route[^\n]*\n).*?(\n## B\.)", r"\1\2", texte, flags=re.S),
                         encoding="utf-8", newline="\n")
        with self.assertRaisesRegex(vl.ControleImpossible, "04-feuille-de-route.md illisible"):
            vl.verifier(TEMOIN, racine=self._racine_avec_modeles(vider_le_modele))

    def test_tout_livrable_fabrique_sur_son_modele_passe(self):
        with tempfile.TemporaryDirectory() as d:
            for l in vl.LIVRABLES:
                for niveau in ("##", "###"):  # les annexes du gabarit CRM sont des sous-titres, un agent les écrit en ##
                    f = pathlib.Path(d) / "livrable.md"
                    f.write_text(doc_conforme(l.code, niveau), encoding="utf-8", newline="\n")
                    with self.subTest(livrable=l.code, niveau=niveau):
                        self.assertEqual(vl.controler(vl.lire_modele(l), f), [])


class Temoin(unittest.TestCase):
    def test_le_temoin_passe_en_entier(self):
        rapport = vl.verifier(TEMOIN, CODES_DU_TEMOIN)
        self.assertEqual(sorted(r.code for r in rapport.resultats), sorted(CODES_DU_TEMOIN))
        for r in rapport.resultats:
            with self.subTest(fichier=r.fichier):
                self.assertEqual(r.ecarts, [])
                self.assertTrue(r.present)
        self.assertTrue(rapport.conforme)

    def test_le_temoin_a_douze_livrables_et_les_etapes_8_a_11_sont_listees_sans_etre_controlees(self):
        rapport = vl.verifier(TEMOIN)
        self.assertEqual(len(rapport.resultats), 12)
        self.assertEqual(rapport.non_controles, [f"{CAS}/{n}" for n in vl.HORS_CONTROLE])

    def test_la_ligne_de_commande_rend_zero_et_un_verdict_par_fichier(self):
        code, sortie, erreur = lancer(TEMOIN)
        self.assertEqual((code, erreur), (0, ""))
        lignes = sortie.splitlines()
        self.assertEqual(sum(1 for l in lignes if l.startswith("OK  ")), 12)
        self.assertFalse(any(l.startswith("KO") for l in lignes))
        self.assertIn(f"OK  {CAS}/60-specification.md", lignes)
        self.assertTrue(any(l.startswith("Non contrôlés") and "85-recette.md" in l for l in lignes))
        self.assertEqual(lignes[-1], "Verdict : OK (12 fichier(s) conformes)")

    def test_le_json_porte_le_meme_verdict(self):
        code, sortie, _ = lancer(TEMOIN, "--json", "--attendus", "10,20,30")
        donnees = json.loads(sortie)
        self.assertEqual(code, 0)
        self.assertTrue(donnees["conforme"])
        self.assertEqual(donnees["attendus"], ["10", "20", "30"])
        self.assertEqual([l["code"] for l in donnees["livrables"]], CODES_DU_TEMOIN)
        self.assertTrue(all(l["ok"] and l["present"] and l["ecarts"] == [] for l in donnees["livrables"]))
        self.assertTrue(next(l for l in donnees["livrables"] if l["code"] == "20")["attendu"])
        self.assertFalse(next(l for l in donnees["livrables"] if l["code"] == "40")["attendu"])
        self.assertEqual(donnees["livrables"][0]["cas"], None)
        self.assertEqual(donnees["livrables"][5]["cas"], "relances-factures")

    def test_le_script_se_lance_comme_un_programme(self):
        script = SCRIPTS / "verifier_livrables.py"
        fait = subprocess.run([sys.executable, "-X", "utf8", str(script), str(TEMOIN), "--attendus", "10,70"],
                              capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(fait.returncode, 0, fait.stdout + fait.stderr)
        self.assertIn("Verdict : OK", fait.stdout)
        introuvable = subprocess.run([sys.executable, "-X", "utf8", str(script), str(TEMOIN / "nulle-part")],
                                     capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(introuvable.returncode, 2)
        self.assertIn("contrôle impossible", introuvable.stderr)


class SurUneCopie(unittest.TestCase):
    """Une copie du témoin dans un dossier temporaire, que chaque essai casse à sa façon."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.mission = pathlib.Path(tmp.name) / "mission"
        self.cas = self.mission / CAS
        self.cas.mkdir(parents=True)
        for f in TEMOIN.glob("*.md"):
            if f.name != "journal.md":
                shutil.copyfile(f, self.mission / f.name)
        for f in (TEMOIN / CAS).glob("*.md"):
            shutil.copyfile(f, self.cas / f.name)

    def chemin(self, code):
        l = livrable(code)
        return (self.mission if l.ou == "mission" else self.cas) / l.dossier / l.nom

    def lire(self, code):
        return self.chemin(code).read_text(encoding="utf-8")

    def ecrire(self, code, texte):
        self.chemin(code).parent.mkdir(parents=True, exist_ok=True)
        self.chemin(code).write_text(texte, encoding="utf-8", newline="\n")

    def remplacer(self, code, ancien, nouveau, nombre=1):
        texte = self.lire(code)
        self.assertIn(ancien, texte, f"le témoin ne contient plus {ancien!r} : l'essai est à réécrire")
        self.ecrire(code, texte.replace(ancien, nouveau, nombre))

    def ecarts(self, code, attendus=()):
        """Les écarts du livrable `code` : [(contrôle, message)] ; la mission entière est contrôlée."""
        rapport = vl.verifier(self.mission, attendus)
        r = next(r for r in rapport.resultats if r.code == code)
        return [(e.controle, e.message) for e in r.ecarts]

    def autres_ko(self, code):
        return [r.fichier for r in vl.verifier(self.mission).resultats if not r.ok and r.code != code]


class Rubriques(SurUneCopie):
    def test_chaque_rubrique_retiree_fait_echouer_son_livrable(self):
        modeles = {l.code: vl.lire_modele(l) for l in vl.LIVRABLES}
        essais = 0
        for code in CODES_DU_TEMOIN:
            lignes = self.lire(code).splitlines()
            requis = {norme for _, norme, _ in modeles[code].titres}
            for i, ligne in enumerate(lignes):
                if not ligne.startswith("## "):
                    continue
                self.ecrire(code, "\n".join(lignes[:i] + lignes[i + 1:]))
                ecarts = vl.controler(modeles[code], self.chemin(code))
                titre = ligne[3:]
                with self.subTest(livrable=code, retiree=titre):
                    if vl.normaliser(titre) in requis:
                        self.assertTrue(any(titre in e.message for e in ecarts), f"{titre!r} : {ecarts}")
                    else:
                        self.assertEqual(ecarts, [], "une rubrique de plus que le modèle n'est pas exigée")
                essais += 1
            self.ecrire(code, "\n".join(lignes) + "\n")
        self.assertGreater(essais, 100)

    def test_une_rubrique_retiree_est_nommee_avec_la_ligne_de_son_modele(self):
        self.remplacer("20", "## 4. Causes\n", "")
        ecarts = self.ecarts("20")
        self.assertEqual(len(ecarts), 1)
        self.assertEqual(ecarts[0][0], "rubriques")
        self.assertRegex(ecarts[0][1], r"rubrique absente : « 4\. Causes » \(modèle : skills/auditer-processus/"
                                       r"references/modeles\.md:\d+\)")
        self.assertEqual(self.autres_ko("20"), [])

    def test_le_titre_se_lit_sans_casse_accents_ni_numerotation(self):
        self.remplacer("20", "## 4. Causes\n", "### CAUSES :\n")
        self.remplacer("20", "## 5. Stabilité\n", "## Stabilite\n")
        self.assertEqual(self.ecarts("20"), [])

    def test_une_rubrique_vide_est_un_ecart(self):
        texte = self.lire("00")
        self.ecrire("00", re.sub(r"(## 3\. Sources manquantes\n).*?(\n## Décision attendue)", r"\1\2", texte, flags=re.S))
        self.assertEqual([c for c, _ in self.ecarts("00")], ["contenu"])
        self.assertIn("rubrique vide : « 3. Sources manquantes »", self.ecarts("00")[0][1])

    def test_un_tableau_de_cellules_vides_ne_dit_rien(self):
        texte = self.lire("00")
        vide = ("## 2. Sources branchées et autorisations obtenues\n\n"
                "| Source | Nature | Date | Autorisation |\n|---|---|---|---|\n| | | | |\n\n## 3.")
        self.ecrire("00", re.sub(r"## 2\. Sources branchées.*?\n## 3\.", lambda m: vide, texte, flags=re.S))
        self.assertEqual([c for c, _ in self.ecarts("00")], ["contenu"])

    def test_une_rubrique_qui_n_a_que_des_titres_de_sous_section_est_vide(self):
        self.ecrire("70", re.sub(r"## 2\. Lots\n.*?\n## 3\.", lambda m: "## 2. Lots\n\n### Lot 1\n\n### Lot 2\n\n## 3.",
                                 self.lire("70"), flags=re.S))
        self.assertEqual([c for c, _ in self.ecarts("70")], ["contenu"])

    def test_un_titre_de_niveau_un_est_exige(self):
        texte = self.lire("10")
        self.assertTrue(texte.startswith("# "))
        self.ecrire("10", texte.split("\n", 1)[1])
        self.assertEqual([c for c, _ in self.ecarts("10")], ["titre"])

    def test_une_rubrique_n_est_pas_le_titre_du_livrable(self):
        self.remplacer("20", "## 4. Causes\n", "# 4. Causes\n")  # le niveau un est le titre, pas une rubrique
        ecarts = self.ecarts("20")
        self.assertEqual([c for c, _ in ecarts], ["rubriques"])
        self.assertIn("rubrique absente : « 4. Causes »", ecarts[0][1])


class DecisionAttendue(SurUneCopie):
    def test_chaque_livrable_perd_sa_decision_attendue(self):
        for code in CODES_DU_TEMOIN:
            texte = self.lire(code)
            self.ecrire(code, texte[:texte.index("## Décision attendue")])
            with self.subTest(livrable=code):
                ecarts = self.ecarts(code)
                self.assertEqual([c for c, _ in ecarts], ["decision"])
                self.assertIn("« Décision attendue » absente", ecarts[0][1])
            self.ecrire(code, texte)

    def test_elle_est_la_derniere_rubrique(self):
        self.ecrire("02", self.lire("02") + "\n## Annexes\n\nUn texte.\n")
        ecarts = self.ecarts("02")
        self.assertEqual([c for c, _ in ecarts], ["decision"])
        self.assertIn("n'est pas la dernière rubrique : « Annexes » la suit", ecarts[0][1])

    def test_une_sous_section_apres_elle_reste_dans_elle(self):
        self.ecrire("02", self.lire("02") + "\n### Détail\n\nUn texte.\n")
        self.assertEqual(self.ecarts("02"), [])

    def test_elle_n_est_pas_vide(self):
        texte = self.lire("03")
        self.ecrire("03", texte[:texte.index("## Décision attendue")] + "## Décision attendue\n\n")
        self.assertEqual([c for c, _ in self.ecarts("03")], ["decision"])
        self.assertIn("est vide", self.ecarts("03")[0][1])

    def test_les_annexes_crm_n_ont_pas_de_decision_attendue(self):
        self.assertFalse(vl.lire_modele(livrable("annexes-crm")).decision)


class EnTete(SurUneCopie):
    def test_le_demandeur_le_valideur_et_la_date_sont_exiges(self):
        self.remplacer("10", "Demandeur, valideur et décideur", "Valideur et décideur")
        self.assertEqual(self.ecarts("10"), [("entete", "le demandeur manque à l'en-tête")])
        self.remplacer("10", "Valideur et décideur", "Demandeur et décideur")
        self.assertEqual(self.ecarts("10"), [("entete", "le valideur manque à l'en-tête")])
        self.remplacer("00", "2026-08-31 · ", "")
        self.assertEqual(self.ecarts("00"), [("entete", "aucune date AAAA-MM-JJ dans l'en-tête")])

    def test_un_seul_role_pour_les_trois_suffit(self):
        self.assertEqual(self.ecarts("10"), [])  # « Demandeur, valideur et décideur : direction générale »

    def test_un_plan_demande_son_decideur_ou_son_valideur(self):
        self.remplacer("70", "Décideur du plan : direction générale", "Décideur : direction générale")
        self.assertEqual(self.ecarts("70"), [("entete", "le décideur du plan (le rôle qui le valide) manque à l'en-tête")])
        self.remplacer("70", "Décideur : direction générale", "Valideur du plan : direction générale")
        self.assertEqual(self.ecarts("70"), [])

    def test_l_en_tete_peut_s_ecrire_en_lignes_et_en_gras(self):
        self.remplacer("10", "2026-09-24 · Demandeur, valideur et décideur : direction générale",
                       "**Date** : 2026-09-24\n**Demandeur** : DG\n**Valideur** : DAF")
        self.assertEqual(self.ecarts("10"), [])

    def test_une_version_ajoutee_est_datee(self):
        self.remplacer("03", "Version 1.1, précisée le 2026-09-30 :", "Version 1.1 :")
        ecarts = self.ecarts("03")
        self.assertEqual([c for c, _ in ecarts], ["version"])
        self.assertIn("la version 1.1 n'est pas datée", ecarts[0][1])

    def test_la_version_un_n_a_pas_besoin_de_date_ni_une_version_lue(self):
        self.remplacer("40", "Rédigé par : consultant IA", "Rédigé par : consultant IA · Version 1")
        self.assertEqual(self.ecarts("40"), [])  # la date de l'en-tête est celle de la version 1
        # « Exigences lues : … version 1.1 » désigne le livrable lu, pas celui-ci
        self.remplacer("40", "Rédigé par : consultant IA", "Rédigé par : consultant IA · Exigences lues : 30, version 1.2")
        self.assertEqual(self.ecarts("40"), [])


class Statuts(SurUneCopie):
    def test_un_livrable_sans_aucun_statut_est_un_ecart(self):
        for code in ("50", "70", "02"):
            texte = self.lire(code)
            self.ecrire(code, re.sub(r"\[[FHE]\]", "", texte))
            with self.subTest(livrable=code):
                self.assertEqual([c for c, _ in self.ecarts(code)], ["statuts"])
            self.ecrire(code, texte)

    def test_un_seul_statut_suffit(self):
        self.ecrire("50", re.sub(r"\[[FHE]\]", "", self.lire("50")) + "\nUn chiffre `[E]`.\n")
        self.assertEqual(self.ecarts("50"), [])

    def test_un_statut_dans_un_bloc_de_code_n_est_pas_un_statut(self):
        self.ecrire("50", re.sub(r"\[[FHE]\]", "", self.lire("50")) + "\n```\nUn chiffre [E]\n```\n")
        self.assertEqual([c for c, _ in self.ecarts("50")], ["statuts"])


class Identifiants(SurUneCopie):
    def test_un_identifiant_en_double_dans_une_rubrique_est_un_ecart(self):
        for code, ancien, nouveau, serie in [("30", "| EF-02 |", "| EF-01 |", "EF-01"),
                                              ("30", "| Q-03 |", "| Q-02 |", "Q-02"),
                                              ("30", "| CA-05 |", "| CA-04 |", "CA-04"),
                                              ("40", "| Q-04 |", "| Q-01 |", "Q-01"),
                                              ("60", "| T-05 |", "| T-04 |", "T-04"),
                                              ("70", "| IND-03 ", "| IND-02 ", "IND-02")]:
            texte = self.lire(code)
            self.remplacer(code, ancien, nouveau)
            with self.subTest(livrable=code, double=serie):
                ecarts = self.ecarts(code)
                self.assertEqual([c for c, _ in ecarts], ["identifiants"], ecarts)
                self.assertRegex(ecarts[0][1], rf"doublon : {serie} ouvre deux lignes")
                self.assertEqual(self.autres_ko(code), [])
            self.ecrire(code, texte)

    def test_la_ligne_du_doublon_est_donnee(self):
        self.remplacer("30", "| EF-02 |", "| EF-01 |")
        rapport = vl.verifier(self.mission)
        e = next(r for r in rapport.resultats if r.code == "30").ecarts[0]
        self.assertTrue(self.lire("30").splitlines()[e.ligne - 1].startswith("| EF-01 |"))
        self.assertIn(f"lignes {e.ligne - 1} et {e.ligne}", e.message)

    def test_un_identifiant_mal_forme_est_un_ecart(self):
        for ancien, nouveau, mal_forme in [("| EF-03 |", "| EF3 |", "EF3"), ("| EF-03 |", "| EF-3 |", "EF-3"),
                                           ("| EF-03 |", "| EF 03 |", "EF 03"), ("| EF-03 |", "| ef-03 |", "ef-03"),
                                           ("| EF-03 |", "| EF_03 |", "EF_03"), ("| EF-03 |", f"| EF{TRAIT_D_UNION_INSECABLE}03 |", f"EF{TRAIT_D_UNION_INSECABLE}03"),
                                           ("| EF-03 |", "| `EF-3` |", "EF-3"), ("| EF-03 |", "| **EF-3** |", "EF-3")]:
            texte = self.lire("30")
            self.remplacer("30", ancien, nouveau)
            with self.subTest(ecrit=mal_forme):
                ecarts = self.ecarts("30")
                self.assertEqual([c for c, _ in ecarts], ["identifiants"], ecarts)
                self.assertIn(f"identifiant mal formé « {mal_forme} »", ecarts[0][1])
            self.ecrire("30", texte)

    def test_un_modele_laisse_tel_quel_est_un_ecart(self):
        self.remplacer("40", "| Q-04 |", "| Q-xx |")
        ecarts = self.ecarts("40")
        self.assertEqual([c for c, _ in ecarts], ["identifiants"])
        self.assertIn("identifiant non renseigné « Q-xx »", ecarts[0][1])

    def test_un_renvoi_mal_ecrit_est_un_ecart_meme_hors_d_un_tableau_d_identifiants(self):
        self.remplacer("30", "| CA-01 | EF-01 |", "| CA-01 | EF-1 |")  # la colonne « exigence » du tableau des critères
        ecarts = self.ecarts("30")
        self.assertEqual([c for c, _ in ecarts], ["identifiants"])
        self.assertIn("identifiant mal formé « EF-1 »", ecarts[0][1])
        self.remplacer("30", "| CA-01 | EF-1 |", "| CA-01 | EF-01 |")
        self.remplacer("60", "(EF-01 à EF-04", "(EF01 à EF-04")
        self.assertIn("identifiant mal formé « EF01 »", self.ecarts("60")[0][1])

    def test_ce_qui_ressemble_a_un_identifiant_sans_en_etre_un_passe(self):
        # CA = chiffre d'affaires, T1 = trimestre, A1 = cellule d'un tableur : sans trait d'union, ce ne sont pas des identifiants
        self.remplacer("30", "## 11. Hors périmètre\n",
                       "## 11. Hors périmètre\n\nLe CA 2026 `[H]` du T1, la cellule A1, le test T1 et R2D2.\n\n"
                       "| Cellule | Valeur |\n|---|---|\n| A1 | 3 |\n| T1 | 4 |\n| CA 2026 | 5 |\n")
        self.assertEqual(self.ecarts("30"), [])

    def test_un_meme_identifiant_dans_deux_rubriques_n_est_pas_un_doublon(self):
        # la même question se relit d'une rubrique à l'autre (60 reprend les IND de 30) : le doublon est celui d'une rubrique
        tableau = "\n| ? | Question |\n|---|---|\n| Q-01 | Une question |\n"
        phrase = "\nUne phrase, avec un statut `[H]`"
        base = doc_conforme("40").replace("## 1. Recommandation\n" + phrase, "## 1. Recommandation\n" + tableau + phrase, 1)
        question = "## 11. Questions ouvertes\n" + phrase
        self.assertIn(question, base)
        self.ecrire("40", base.replace(question, "## 11. Questions ouvertes\n" + tableau + phrase, 1))
        self.assertEqual(self.ecarts("40"), [])  # Q-01 ouvre une ligne dans la rubrique 1 et une dans la rubrique 11
        self.ecrire("40", base.replace(question, "## 11. Questions ouvertes\n" + tableau + tableau + phrase, 1))
        self.assertEqual([c for c, _ in self.ecarts("40")], ["identifiants"])  # deux fois dans la rubrique 11

    def test_un_identifiant_dans_un_bloc_de_code_n_est_pas_lu(self):
        self.remplacer("30", "## 11. Hors périmètre\n", "## 11. Hors périmètre\n\n```\n| EF1 | x |\nEF-1\n```\n\nTexte.\n")
        self.assertEqual(self.ecarts("30"), [])


class LivrablesAttendusEtPlaces(SurUneCopie):
    def test_un_livrable_attendu_et_absent_est_un_ecart(self):
        self.chemin("40").unlink()
        self.assertEqual(self.ecarts("50", attendus=("10", "20", "30", "50")), [])
        rapport = vl.verifier(self.mission, ["10", "20", "30", "40"])
        absent = [r for r in rapport.resultats if not r.ok]
        self.assertEqual([(r.fichier, r.present, r.attendu) for r in absent], [(f"{CAS}/40-solutions.md", False, True)])
        self.assertEqual(absent[0].ecarts[0].controle, "absent")
        self.assertFalse(rapport.conforme)

    def test_un_livrable_absent_mais_non_attendu_n_est_pas_un_ecart(self):
        self.chemin("40").unlink()
        self.assertTrue(vl.verifier(self.mission).conforme)
        self.assertEqual(lancer(self.mission)[0], 0)

    def test_la_ligne_de_commande_rend_un_quand_un_livrable_attendu_manque(self):
        self.chemin("40").unlink()
        code, sortie, _ = lancer(self.mission, "--attendus", "10,20,30,40,50")
        self.assertEqual(code, 1)
        self.assertIn(f"KO  {CAS}/40-solutions.md", sortie.splitlines())
        self.assertIn("      absent : livrable attendu, absent du dossier", sortie.splitlines())
        self.assertEqual(sortie.splitlines()[-1], "Verdict : KO (1 fichier(s) en écart sur 12)")
        code, sortie, _ = lancer(self.mission, "--json", "--attendus", "40")
        donnees = json.loads(sortie)
        self.assertEqual((code, donnees["conforme"]), (1, False))
        ko = [l for l in donnees["livrables"] if not l["ok"]]
        self.assertEqual([(l["fichier"], l["present"], l["attendu"]) for l in ko], [(f"{CAS}/40-solutions.md", False, True)])

    def test_seuls_les_dossiers_cas_sont_des_cas(self):
        for dossier in ("sources", "notes", "archive"):
            (self.mission / dossier).mkdir()
            (self.mission / dossier / "note.md").write_text("# Une note\n", encoding="utf-8")
        (self.mission / "cas-sans-dossier.md").write_text("# Un fichier, pas un dossier\n", encoding="utf-8")
        rapport = vl.verifier(self.mission, ["10"])
        self.assertTrue(rapport.conforme)
        self.assertEqual(len(rapport.resultats), 12)
        self.assertEqual({r.cas for r in rapport.resultats}, {None, "relances-factures"})

    def test_un_livrable_de_porte_deux_attendu_sans_etre_la(self):
        for f in ("00-contexte.md", "04-feuille-de-route.md"):
            (self.mission / f).unlink()
        rapport = vl.verifier(self.mission, ["00", "04"])
        self.assertEqual([r.fichier for r in rapport.resultats if not r.ok], ["00-contexte.md", "04-feuille-de-route.md"])

    def test_un_besoin_sans_dossier_de_cas_est_un_ecart(self):
        shutil.rmtree(self.cas)
        rapport = vl.verifier(self.mission, ["10"])
        ko = [r for r in rapport.resultats if not r.ok]
        self.assertEqual([r.fichier for r in ko], ["cas-<slug>/10-besoin.md"])
        self.assertIn("aucun dossier cas-<slug>/", ko[0].ecarts[0].message)

    def test_chaque_dossier_de_cas_porte_les_livrables_attendus(self):
        autre = self.mission / "cas-tri-tickets"
        autre.mkdir()
        shutil.copyfile(self.cas / "10-besoin.md", autre / "10-besoin.md")
        rapport = vl.verifier(self.mission, ["10", "20"])
        self.assertEqual([r.fichier for r in rapport.resultats if not r.ok], ["cas-tri-tickets/20-diagnostic.md"])

    def test_un_livrable_de_cas_range_a_la_racine_est_un_ecart(self):
        shutil.copyfile(self.cas / "10-besoin.md", self.mission / "10-besoin.md")
        rapport = vl.verifier(self.mission)
        ko = [r for r in rapport.resultats if not r.ok]
        self.assertEqual([r.fichier for r in ko], ["10-besoin.md"])
        self.assertEqual(ko[0].ecarts[0].controle, "place")
        self.assertIn("dans mission/cas-<slug>/", ko[0].ecarts[0].message)

    def test_un_livrable_de_porte_deux_range_dans_un_cas_est_un_ecart(self):
        shutil.copyfile(self.mission / "00-contexte.md", self.cas / "00-contexte.md")
        ko = [r for r in vl.verifier(self.mission).resultats if not r.ok]
        self.assertEqual([r.fichier for r in ko], [f"{CAS}/00-contexte.md"])
        self.assertIn("à la racine de mission/", ko[0].ecarts[0].message)

    def test_un_fichier_illisible_est_un_ecart_pas_un_plantage(self):
        self.chemin("20").write_bytes(b"# Diagnostic\n\xff\xfe\x00\x00 pas de l'UTF-8\n")
        ecarts = self.ecarts("20")
        self.assertEqual([c for c, _ in ecarts], ["lecture"])

    def test_une_etape_hors_controle_est_listee_jamais_declaree_conforme(self):
        (self.cas / "85-recette.md").write_text("n'importe quoi", encoding="utf-8")
        rapport = vl.verifier(self.mission)
        self.assertTrue(rapport.conforme)
        self.assertIn(f"{CAS}/85-recette.md", rapport.non_controles)
        self.assertEqual(sorted(rapport.non_controles), sorted(f"{CAS}/{n}" for n in vl.HORS_CONTROLE))
        self.assertTrue(set(vl.HORS_CONTROLE).isdisjoint({l.nom for l in vl.LIVRABLES}))
        self.assertEqual(len(rapport.resultats), 12)


class ModuleCrm(SurUneCopie):
    def test_un_audit_et_des_annexes_conformes_passent(self):
        self.ecrire("audit-crm", doc_conforme("audit-crm"))
        self.ecrire("annexes-crm", doc_conforme("annexes-crm"))
        rapport = vl.verifier(self.mission, ["audit-crm", "annexes-crm"])
        crm = [r for r in rapport.resultats if r.code in ("audit-crm", "annexes-crm")]
        self.assertEqual([(r.fichier, r.ecarts) for r in crm],
                         [(f"{CAS}/20-diagnostic/audit-crm.md", []), (f"{CAS}/30-exigences/annexes-crm.md", [])])
        self.assertTrue(rapport.conforme)

    def test_le_dossier_20_diagnostic_n_empeche_pas_le_fichier_20_diagnostic(self):
        self.ecrire("audit-crm", doc_conforme("audit-crm"))
        self.assertTrue((self.cas / "20-diagnostic").is_dir() and (self.cas / "20-diagnostic.md").is_file())
        self.assertEqual([r.fichier for r in vl.verifier(self.mission).resultats if r.code == "20"], [f"{CAS}/20-diagnostic.md"])

    def test_un_audit_sans_son_volet_ventes_echoue(self):
        self.ecrire("audit-crm", doc_conforme("audit-crm").replace("## 4. Ventes", "## 4. Autre chose"))
        ecarts = self.ecarts("audit-crm")
        self.assertEqual([c for c, _ in ecarts], ["rubriques"])
        self.assertIn("rubrique absente : « 4. Ventes » (modèle : skills/auditer-crm/SKILL.md:", ecarts[0][1])

    def test_des_annexes_sans_les_raisons_de_perte_echouent(self):
        self.ecrire("annexes-crm", doc_conforme("annexes-crm").replace("D. Raisons de perte", "D. Autre"))
        ecarts = self.ecarts("annexes-crm")
        self.assertEqual([c for c, _ in ecarts], ["rubriques"])
        self.assertIn("« D. Raisons de perte »", ecarts[0][1])

    def test_un_audit_sans_decision_attendue_echoue(self):
        texte = doc_conforme("audit-crm")
        self.ecrire("audit-crm", texte[:texte.index("## Décision attendue")])
        self.assertEqual([c for c, _ in self.ecarts("audit-crm")], ["decision"])

    def test_un_module_crm_attendu_et_absent_echoue(self):
        rapport = vl.verifier(self.mission, ["audit-crm"])
        self.assertEqual([(r.fichier, r.ecarts[0].controle) for r in rapport.resultats if not r.ok],
                         [(f"{CAS}/20-diagnostic/audit-crm.md", "absent")])


class LigneDeCommande(SurUneCopie):
    def test_les_codes_de_sortie(self):
        self.assertEqual(lancer(self.mission)[0], 0)
        self.remplacer("20", "## 4. Causes\n", "")
        code, sortie, _ = lancer(self.mission)
        self.assertEqual(code, 1)
        self.assertIn(f"KO  {CAS}/20-diagnostic.md", sortie.splitlines())
        self.assertTrue(any("rubrique absente : « 4. Causes »" in l for l in sortie.splitlines()))

    def test_un_dossier_introuvable_ou_sans_livrable_est_un_controle_impossible(self):
        code, sortie, erreur = lancer(self.mission / "absent")
        self.assertEqual((code, sortie), (2, ""))
        self.assertIn("contrôle impossible : dossier introuvable", erreur)
        vide = self.mission.parent / "vide"
        vide.mkdir()
        code, _, erreur = lancer(vide)
        self.assertEqual(code, 2)
        self.assertIn("aucun livrable du pack", erreur)
        self.assertIn("le dossier à donner est mission/", erreur)

    def test_en_json_un_controle_impossible_reste_un_json(self):
        code, sortie, _ = lancer(self.mission / "absent", "--json")
        self.assertEqual(code, 2)
        donnees = json.loads(sortie)
        self.assertFalse(donnees["conforme"])
        self.assertIn("dossier introuvable", donnees["erreur"])

    def test_un_code_attendu_inconnu_est_un_controle_impossible(self):
        code, _, erreur = lancer(self.mission, "--attendus", "10,99")
        self.assertEqual(code, 2)
        self.assertIn("livrable attendu inconnu : 99", erreur)
        code, _, erreur = lancer(self.mission, "--attendus", "10,85")  # la recette n'est pas contrôlée : on ne le tait pas
        self.assertEqual(code, 2)
        self.assertIn("livrable attendu non contrôlé : 85", erreur)

    def test_les_codes_attendus_s_ecrivent_de_plusieurs_facons(self):
        self.assertEqual(vl.lire_attendus("10, 20-diagnostic,audit-crm 30-exigences.md"), ["10", "20", "audit-crm", "30"])
        self.assertEqual(vl.lire_attendus("annexes-crm.md"), ["annexes-crm"])
        self.assertEqual(vl.lire_attendus(""), [])
        self.assertEqual(lancer(self.mission, "--attendus", "10-besoin.md, 20-diagnostic")[0], 0)

    def test_la_sortie_dit_ce_qui_manque_sans_planter_sur_un_dossier_presque_vide(self):
        for f in list(self.cas.glob("*.md")) + list(self.mission.glob("0*.md")):
            f.unlink()
        self.ecrire("10", "")
        code, sortie, _ = lancer(self.mission)
        self.assertEqual(code, 1)
        self.assertIn(f"KO  {CAS}/10-besoin.md", sortie.splitlines())
        self.assertIn("titre : titre de niveau 1 absent", sortie)
        self.assertIn("rubriques : rubrique absente : « 1. La demande, telle qu'exprimée »", sortie)
        self.assertIn("decision : « Décision attendue » absente", sortie)


class Fichiers(SurUneCopie):
    def test_un_fichier_avec_bom_et_fins_de_ligne_windows_se_lit_pareil(self):
        for f in self.mission.rglob("*.md"):
            texte = f.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\n", "\r\n")
            f.write_bytes(b"\xef\xbb\xbf" + texte.encode("utf-8"))
        self.assertTrue(self.chemin("20").read_bytes().startswith(b"\xef\xbb\xbf"))
        rapport = vl.verifier(self.mission, CODES_DU_TEMOIN)
        self.assertEqual([r.ecarts for r in rapport.resultats], [[] for _ in CODES_DU_TEMOIN])

    def test_des_espaces_en_fin_de_titre_ne_changent_rien(self):
        self.ecrire("20", re.sub(r"^(## .*)$", r"\1   ", self.lire("20"), flags=re.M))
        self.assertEqual(self.ecarts("20"), [])


if __name__ == "__main__":
    unittest.main()
