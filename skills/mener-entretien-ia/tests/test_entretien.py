"""Essais de scripts/entretien.py : python -m unittest discover -s skills/mener-entretien-ia/tests"""
import contextlib
import copy
import io
import json
import pathlib
import re
import shutil
import sys
import tempfile
import unittest

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / "scripts"))
import entretien  # noqa: E402

EXEMPLE = json.loads((ICI / "compte-rendu-fictif.json").read_text(encoding="utf-8"))
SECTIONS = ["## Ce qui a été dit", "## Tâches citées (à reporter dans 01)", "## Pièces remises",
            "## Écarts avec d'autres sources", "## Documents ou accès promis", "## Questions restées ouvertes"]


class Questionnaires(unittest.TestCase):
    def test_chaque_guide_se_lit_dans_le_pack(self):
        attendus = {"direction": 10, "equipes": 11, "besoin": 8, "processus": 8, "court": 3}
        for guide, n in attendus.items():  # le guide prepare a ses essais plus bas
            q = entretien.questionnaire(guide)
            self.assertEqual(len(q["questions"]), n, guide)
            self.assertTrue(all(x["question"].rstrip().endswith("?") for x in q["questions"]
                                if guide in ("besoin", "processus")), guide)

    def test_consigne_sans_champ_vide(self):
        texte = entretien.consigne("besoin", "dirigeante", "Exemple", "en", "Une boutique en ligne.")
        self.assertNotIn("{{", texte)
        self.assertIn("B8.", texte)
        self.assertIn("terminer_entretien", texte)
        self.assertIn("en.", texte)

    def test_le_schema_exige_une_reponse_par_question(self):
        s = entretien.schema()
        self.assertIn("reponses", s["required"])


class Note(unittest.TestCase):
    def test_compte_rendu_fictif_donne_la_note_au_format_du_pack(self):
        self.assertEqual(entretien.controler(EXEMPLE), [])
        with tempfile.TemporaryDirectory() as d:
            messages = [{"role": "assistant", "texte": "Hello"}, {"role": "user", "texte": "Hi"}]
            fichiers = entretien.ecrire_note(EXEMPLE, d, messages)
            self.assertEqual([f.name for f in fichiers],
                             ["entretien-dirigeante-2026-10-28.md", "entretien-dirigeante-2026-10-28.transcription.md"])
            note = fichiers[0].read_text(encoding="utf-8")
        self.assertTrue(note.startswith("# Entretien — dirigeante, service client · 2026-10-28 · "))
        positions = [note.index(s) for s in SECTIONS]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("`[H]` (à confirmer :", note)
        self.assertIn("`[F]` (règle énoncée par son détenteur", note)
        self.assertIn("> « ", note)

    def test_la_transcription_retire_adresses_et_numeros(self):
        texte = entretien.rendre_transcription(EXEMPLE, [{"role": "user", "texte": "jane.doe@gmail.com, +1 212 555 0100"}])
        self.assertNotIn("@", texte)
        self.assertNotIn("555", texte)
        self.assertEqual(texte.split("**Personne**")[1].count("[retiré]"), 2)

    def _refuse(self, modifier, attendu):
        cr = copy.deepcopy(EXEMPLE)
        modifier(cr)
        ecarts = entretien.controler(cr)
        self.assertTrue(any(attendu in e for e in ecarts), ecarts)
        with tempfile.TemporaryDirectory() as d, self.assertRaises(entretien.Erreur):
            entretien.ecrire_note(cr, d)

    # Sabotages : chaque règle du pack, cassée une fois, doit faire refuser la note.
    def test_un_chiffre_dit_de_memoire_ne_devient_pas_un_fait(self):
        def f(cr):
            c = cr["reponses"][1]["chiffres"][0]
            c["statut"] = "F"
            c.pop("fondement", None)
        self._refuse(f, "[F] sans fondement")

    def test_une_hypothese_porte_qui_confirme(self):
        self._refuse(lambda cr: cr["reponses"][1]["chiffres"][0].update(confirme_par=""), "sans le rôle")

    def test_une_piece_promise_ne_fonde_pas_un_fait(self):
        def f(cr):
            cr["pieces"] = []
            cr["reponses"][1]["chiffres"][0].update(statut="F", fondement="piece-remise")
        self._refuse(f, "aucune pièce n'a été remise")

    def test_aucune_adresse_dans_les_citations(self):
        self._refuse(lambda cr: cr["reponses"][0]["citations"].append("write to jane@example.com"), "adresse")

    def test_une_reponse_par_question_dans_l_ordre(self):
        self._refuse(lambda cr: cr["reponses"].pop(3), "une par question")

    def test_l_objet_dit_en_ouverture(self):
        self._refuse(lambda cr: cr.update(ouverture_dite=False), "ouverture")


PREPARE = ICI / "questionnaire-fictif.md"


def cr_prepare():
    """Le compte rendu fictif, ramené aux quatre questions du questionnaire préparé."""
    cr = copy.deepcopy(EXEMPLE)
    cr["guide"] = "prepare"
    cr["reponses"] = [dict(r, id=f"Q{i + 1}") for i, r in enumerate(cr["reponses"][:4])]
    return cr


class QuestionnairePrepare(unittest.TestCase):
    def test_il_se_lit_avec_ce_qui_est_deja_su(self):
        q = entretien.questionnaire("prepare", PREPARE)
        self.assertEqual([x["id"] for x in q["questions"]], ["Q1", "Q2", "Q3", "Q4"])
        self.assertIn("où est ma commande", q["questions"][1]["deja_su"])
        self.assertEqual(len(q["deja_etabli"]), 1)
        texte = entretien.consigne("prepare", "dirigeante", "Exemple", "en", fichier=PREPARE)
        self.assertNotIn("{{", texte)
        self.assertIn("Q4.", texte)
        self.assertIn("(Déjà su : Surtout", texte)
        self.assertIn("Déjà établi, à ne pas redemander ni faire confirmer :", texte)
        self.assertIn("savoir pour mettre en place un agent", texte)

    def test_la_note_cite_son_questionnaire(self):
        q = entretien.questionnaire("prepare", PREPARE)
        self.assertEqual(entretien.controler(cr_prepare(), q=q), [])
        with tempfile.TemporaryDirectory() as d:
            note = entretien.ecrire_note(cr_prepare(), d, None, q)[0].read_text(encoding="utf-8")
        self.assertIn("questionnaire préparé pour : Mettre en place un agent", note)
        self.assertIn("`questionnaire-fictif.md`", note)

    def _questionnaire_refuse(self, modifier, attendu):
        texte = modifier(PREPARE.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as d:
            chemin = pathlib.Path(d) / "questionnaire-sabote.md"
            chemin.write_text(texte, encoding="utf-8")
            with self.assertRaises(entretien.Erreur) as e:
                entretien.consigne("prepare", "dirigeante", "Exemple", fichier=chemin)
        self.assertIn(attendu, str(e.exception))

    # Sabotages : le questionnaire préparé, cassé une fois, doit être refusé avant l'entretien.
    def test_un_questionnaire_non_valide_ne_s_ouvre_pas(self):
        self._questionnaire_refuse(lambda t: t.replace("Validé par : consultant, le 2026-10-28", "Validé par :"),
                                   "non validé")

    def test_les_questions_visent_un_objectif_ecrit(self):
        self._questionnaire_refuse(lambda t: t.replace("Objectif :", "But :"), "Objectif")

    def test_douze_questions_au_plus(self):
        def f(t):
            lignes = "".join(f"| {n} | Thème | Question {n} ? | | 01 |\n" for n in range(5, 14))
            return t.replace("\n## Pas dans cet entretien", lignes + "\n## Pas dans cet entretien")
        self._questionnaire_refuse(f, "12 au plus")

    def test_le_compte_rendu_ne_se_controle_pas_sans_son_questionnaire(self):
        self.assertTrue(any("questionnaire préparé" in e for e in entretien.controler(cr_prepare())))
        with tempfile.TemporaryDirectory() as d, self.assertRaises(entretien.Erreur):
            entretien.ecrire_note(cr_prepare(), d)


class BaseDeQuestions(unittest.TestCase):
    def test_le_sujet_support_client_se_lit_avec_sa_decision(self):
        self.assertIn("support-client", entretien.sujets())
        q = entretien.base("support-client")
        self.assertTrue({f"SC{i:02d}" for i in range(1, 40)} <= {x["id"] for x in q})  # un numéro ne se perd pas
        self.assertEqual(len({x["id"] for x in q}), len(q))
        self.assertTrue(all(x["question"] and x["decide"] and x["partie"] for x in q))
        self.assertTrue(all(x["dabord"] in ("l'outil", "un document", "la personne") for x in q))

    def test_le_questionnaire_reprend_la_base_au_lieu_de_la_reecrire(self):
        brouillon = entretien.preparer("support-client", "Mettre en place un agent qui réponde aux clients",
                                       "dirigeante", "Exemple", ["SC02", "SC06", "SC24"], date="2026-10-28")
        base = {x["id"]: x for x in entretien.base("support-client")}
        with tempfile.TemporaryDirectory() as d:
            chemin = pathlib.Path(d) / "questionnaire-agent.md"
            chemin.write_text(brouillon, encoding="utf-8")
            with self.assertRaises(entretien.Erreur):  # pas encore validé : il ne s'ouvre pas
                entretien.questionnaire("prepare", chemin)
            chemin.write_text(brouillon.replace("Validé par :", "Validé par : consultant, le 2026-10-28"), encoding="utf-8")
            q = entretien.questionnaire("prepare", chemin)
        self.assertEqual(q["base"], "support-client")
        self.assertEqual([x["question"] for x in q["questions"]], [base[i]["question"] for i in ("SC02", "SC06", "SC24")])
        self.assertTrue(q["questions"][2]["alimente"].startswith("SC24 · "))

    def test_toute_la_base_depasse_douze_questions_et_se_reduit_avant_l_entretien(self):
        brouillon = entretien.preparer("support-client", "Un agent", "dirigeante").replace("Validé par :", "Validé par : c, le 2026-10-28")
        with tempfile.TemporaryDirectory() as d:
            chemin = pathlib.Path(d) / "q.md"
            chemin.write_text(brouillon, encoding="utf-8")
            with self.assertRaises(entretien.Erreur) as e:
                entretien.questionnaire("prepare", chemin)
        self.assertIn("12 au plus", str(e.exception))

    def test_un_numero_inconnu_est_refuse(self):
        with self.assertRaises(entretien.Erreur):
            entretien.preparer("support-client", "Un agent", "dirigeante", garder=["SC99"])
        with self.assertRaises(entretien.Erreur):
            entretien.base("sujet-qui-n-existe-pas")

    def test_la_note_propose_ce_qui_manquait_a_la_base(self):
        cr = cr_prepare()
        cr["pour_la_base"] = ["Les clients professionnels ont-ils un interlocuteur à part ?"]
        q = dict(entretien.questionnaire("prepare", PREPARE), base="support-client")
        with tempfile.TemporaryDirectory() as d:
            note = entretien.ecrire_note(cr, d, None, q)[0].read_text(encoding="utf-8")
        self.assertIn("## Pour la base de questions", note)
        self.assertIn("interlocuteur à part", note)
        self.assertIn("base-questions/support-client.md", note)
        self.assertIn("depuis la base support-client", note)


class DefautsDuTestLocal(unittest.TestCase):
    def test_une_tache_peut_etre_un_fait_avec_son_fondement(self):
        cr = copy.deepcopy(EXEMPLE)
        cr["pieces"] = [{"piece": "export"}]
        cr["taches"] = [{"tache": "Répondre aux emails", "statut": "F", "fondement": "piece-remise"}]
        self.assertEqual(entretien.controler(cr), [])
        self.assertIn("required", entretien.schema()["properties"]["taches"]["items"])
        self.assertIn("fondement", entretien.schema()["properties"]["taches"]["items"]["properties"])

    def test_un_nom_ecrit_est_retire_de_la_transcription_et_refuse_ailleurs(self):
        cr = copy.deepcopy(EXEMPLE)
        cr["noms_a_retirer"] = ["Kaitlyn"]
        texte = entretien.rendre_transcription(cr, [{"role": "user", "texte": "Kaitlyn répond aux emails."}])
        self.assertNotIn("Kaitlyn", texte)
        self.assertIn("[retiré] répond", texte)
        self.assertEqual(entretien.controler(cr), [])
        cr["reponses"][0]["synthese"] += " Kaitlyn s'en occupe."
        self.assertTrue(any("noms_a_retirer" in e for e in entretien.controler(cr)))

    def test_la_consigne_se_lit_avec_le_consultant_par_defaut(self):
        texte = entretien.consigne("besoin", "dirigeante", "Exemple")
        self.assertNotIn("de le consultant", texte)
        self.assertIn("pour le consultant", texte)


class UneSeuleMaison(unittest.TestCase):
    """La base de questions est la seule maison des questions : chaque contrôle se prouve par un sabotage, sur une
    copie de la base et des compétences qui la lisent."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        racine = pathlib.Path(self._tmp.name)
        self.base = racine / "base"
        shutil.copytree(entretien.BASE, self.base)
        self.skills = racine / "skills"
        for nom in entretien._index()[1]:
            (self.skills / nom).mkdir(parents=True)
            shutil.copy(entretien.SKILLS / nom / "SKILL.md", self.skills / nom / "SKILL.md")

    def tearDown(self):
        self._tmp.cleanup()

    def ecarts(self):
        return entretien.verifier_base(self.base, self.skills)

    def remplacer(self, fichier, avant, apres):
        f = self.base / fichier
        texte = f.read_text(encoding="utf-8")
        self.assertIn(avant, texte)
        f.write_text(texte.replace(avant, apres, 1), encoding="utf-8")

    def test_la_base_du_pack_est_saine(self):
        self.assertEqual(entretien.verifier_base(), [])
        self.assertEqual(self.ecarts(), [])

    def test_les_guides_fixes_se_lisent_dans_la_base(self):
        court = entretien.questionnaire("court")
        self.assertEqual([q["base"] for q in court["questions"]], ["EQ01", "EQ10", "EQ05"])
        self.assertEqual([q["base"] for q in entretien.questionnaire("besoin")["questions"]],
                         [f"CA0{i}" for i in range(1, 9)])
        self.assertEqual(entretien.questionnaire("direction")["questions"][0]["theme"], "Objectifs")
        self.assertEqual(entretien.questionnaire("processus")["questions"][0]["theme"], "")

    def test_une_question_corrigee_dans_la_base_l_est_dans_le_guide(self):
        self.remplacer("decouverte-direction.md", "Quels sont les deux ou trois résultats",
                       "Quels sont les trois résultats")
        vrai = entretien.BASE
        entretien.BASE = self.base
        try:
            q = entretien.questionnaire("direction")["questions"][0]["question"]
        finally:
            entretien.BASE = vrai
        self.assertTrue(q.startswith("Quels sont les trois résultats"))

    def test_sabotage_un_doublon_dans_un_autre_sujet(self):
        ca01 = entretien.base("cadrage")[0]["question"]
        self.remplacer("prospection.md", "| la personne |\n", "| la personne |\n| PR99 | "
                       + ca01.upper().replace("É", "E") + " | Rien | la personne |\n")
        self.assertTrue(any("même question que CA01" in e for e in self.ecarts()), self.ecarts())

    def test_sabotage_un_sujet_absent_de_l_index(self):
        f = self.base / "README.md"
        f.write_text(f.read_text(encoding="utf-8").replace("| [Le contenu](contenu.md) | CO |", "| Le contenu | CO |"),
                     encoding="utf-8")
        self.assertIn("contenu.md : absent du tableau des sujets du README", self.ecarts())

    def test_sabotage_une_ligne_sans_decision_ou_au_d_abord_inconnu(self):
        self.remplacer("crm.md", "| Les étapes à corriger en premier | la personne |", "|  | le CRM |")
        ecarts = self.ecarts()
        self.assertTrue(any(e.startswith("CR01 : « Ce qu'elle décide » est vide") for e in ecarts), ecarts)
        self.assertTrue(any(e.startswith("CR01 : « D'abord »") for e in ecarts), ecarts)

    def test_sabotage_un_prefixe_pris_par_deux_sujets(self):
        self.remplacer("contenu.md", "| CO01 |", "| TR90 |")
        ecarts = self.ecarts()
        self.assertTrue(any("préfixe TR pris par deux sujets" in e for e in ecarts), ecarts)

    def test_sabotage_un_nom_d_index_qui_n_est_plus_le_titre(self):
        self.remplacer("crm.md", "# Base de questions : le CRM et le suivi commercial", "# Base de questions : le CRM")
        self.assertIn("README : le sujet crm s'appelle « Le CRM et le suivi commercial », son fichier « Le CRM »",
                      self.ecarts())

    def test_sabotage_un_tiret_cadratin(self):
        self.remplacer("reporting.md", "Quand l'objectif est de mesurer et de décider :",
                       "Quand l'objectif est de mesurer \u2014 et de décider :")
        self.assertTrue(any(e.startswith("reporting.md : tiret cadratin") for e in self.ecarts()))

    def test_sabotage_une_competence_lectrice_sans_son_rappel(self):
        f = self.skills / "cadrer-besoin" / "SKILL.md"
        f.write_text(f.read_text(encoding="utf-8").replace("base-questions", "banque"), encoding="utf-8")
        self.assertIn("cadrer-besoin : son SKILL.md ne renvoie pas à la base de questions en tête (40 premières "
                      "lignes)", self.ecarts())

    def test_ajouter_range_a_la_fin_de_la_partie_avec_le_numero_suivant(self):
        n = entretien.ajouter("crm", "2", "Quelles propriétés personnalisées ne sont plus remplies depuis six mois ?",
                              "Les propriétés à archiver", "l'outil", dossier=self.base)
        self.assertEqual(n, "CR14")
        q = entretien.base("crm", self.base)
        self.assertEqual([x["id"] for x in q if x["partie"] == "Les données et leurs sources"][-1], "CR14")
        self.assertEqual(self.ecarts(), [])

    def test_ajouter_refuse_un_doublon_de_toute_la_base(self):
        with self.assertRaises(entretien.Erreur) as e:
            entretien.ajouter("crm", "1", "quel résultat concret doit etre obtenu pour que la mission soit "
                              "consideree comme reussie", "Rien", dossier=self.base)
        self.assertIn("une question finit par", str(e.exception))
        with self.assertRaises(entretien.Erreur) as e:
            entretien.ajouter("crm", "1", "quel résultat concret doit etre obtenu pour que la mission soit "
                              "consideree comme reussie ?", "Rien", dossier=self.base)
        self.assertIn("CA01 (cadrage)", str(e.exception))
        with self.assertRaises(entretien.Erreur):
            entretien.ajouter("crm", "1", "Une question neuve ?", "", dossier=self.base)

    def test_ajouter_ouvre_une_partie_seulement_si_on_le_demande(self):
        with self.assertRaises(entretien.Erreur):
            entretien.ajouter("contenu", "La relecture", "Qui relit un post avant qu'il parte ?", "Le relecteur",
                              dossier=self.base)
        n = entretien.ajouter("contenu", "La relecture", "Qui relit un post avant qu'il parte ?", "Le relecteur",
                              creer_partie=True, dossier=self.base)
        self.assertEqual(n, "CO03")
        self.assertEqual(entretien.base("contenu", self.base)[-1]["partie"], "La relecture")
        self.assertIn("Retour d'expérience", (self.base / "contenu.md").read_text(encoding="utf-8"))
        self.assertEqual(self.ecarts(), [])

    def test_creer_sujet_l_inscrit_dans_l_index(self):
        entretien.creer_sujet("facturation", "FA", "la facturation", "Les factures, les relances, les paiements",
                              "Ce qui se fait aujourd'hui", "Combien de factures partent chaque mois, et par quel "
                              "outil ?", "Le volume et l'outil de départ", "l'outil", dossier=self.base)
        self.assertIn("facturation", entretien.sujets(self.base))
        self.assertEqual(entretien.base("facturation", self.base)[0]["id"], "FA01")
        self.assertEqual(self.ecarts(), [])
        with self.assertRaises(entretien.Erreur):
            entretien.creer_sujet("factures", "FA", "les factures", "…", "…", "Une autre question ?", "Rien",
                                  dossier=self.base)

    # ---- l'index des sujets : deux familles, chacune en groupes nommés (28/10/2026)
    RANGEMENT = [
        ("Les étapes d'une mission", [
            ("Premier contact", ["premier-echange"]),
            ("Découvrir", ["decouverte-direction", "decouverte-equipes"]),
            ("Cadrer", ["cadrage", "outils-et-acces"]),
            ("Analyser et chiffrer", ["processus", "rentabilite"]),
            ("Mettre en service et suivre", ["essai-et-mise-en-service", "transmission", "suivi-de-mission"]),
        ]),
        ("Ce que veut le client", [
            ("Trouver des clients", ["ciblage", "prospection"]),
            ("Suivre ses contacts et ses ventes", ["crm", "emailing"]),
            ("Servir ses clients", ["support-client", "accueil-des-clients"]),
            ("Ses données et ses chiffres", ["donnees", "reporting"]),
            ("Produire du contenu", ["contenu"]),
        ]),
    ]

    def creer(self, sujet="facturation", prefixe="FA", **options):
        return entretien.creer_sujet(sujet, prefixe, "la " + sujet, "Quand le sujet se pose", "Ce qui se fait",
                                     f"Combien de {sujet} partent chaque mois, et par quel outil ?",
                                     "Le volume et l'outil de départ", "l'outil", dossier=self.base, **options)

    def groupes(self, famille):
        return dict(dict(entretien.rangement(self.base))[famille])

    def test_l_index_range_les_dix_neuf_sujets_en_deux_familles_et_dix_groupes(self):
        self.assertEqual(entretien.rangement(), self.RANGEMENT)
        self.assertEqual(entretien.rangement(self.base), self.RANGEMENT)
        inscrits = sorted(s for _, groupes in entretien.rangement() for _, sujets in groupes for s in sujets)
        self.assertEqual(inscrits, entretien.sujets())
        self.assertEqual((len(self.RANGEMENT), sum(len(g) for _, g in self.RANGEMENT), len(inscrits)), (2, 10, 19))

    def test_sabotage_un_sujet_hors_de_tout_groupe(self):
        self.remplacer("README.md", "#### Premier contact\n\n", "")
        self.assertIn("README : le sujet premier-echange n'est pas rangé dans un groupe (#### …) d'une famille (### …)",
                      self.ecarts())

    def test_sabotage_une_ligne_de_sujet_posee_hors_de_l_index(self):
        self.remplacer("README.md", "## Se servir de la base\n",
                       "## Se servir de la base\n\n| [Le contenu](contenu.md) | CO | Un second rangement |\n")
        ecarts = self.ecarts()
        self.assertIn("README : le sujet contenu est listé deux fois", ecarts)
        self.assertIn("README : le sujet contenu n'est pas rangé dans un groupe (#### …) d'une famille (### …)", ecarts)

    def test_sabotage_un_groupe_sans_sujet(self):
        self.remplacer("README.md", "| [Le contenu](contenu.md) | CO | Produire du contenu avec l'IA |\n", "")
        ecarts = self.ecarts()
        self.assertIn("README : le groupe « Produire du contenu » n'a aucun sujet", ecarts)
        self.assertIn("contenu.md : absent du tableau des sujets du README", ecarts)

    def test_sabotage_une_famille_sans_groupe(self):
        self.remplacer("README.md", "## Se servir de la base\n", "### Une famille vide\n\n## Se servir de la base\n")
        self.assertIn("README : la famille « Une famille vide » n'a aucun groupe", self.ecarts())

    def test_sabotage_un_sujet_deux_fois_dans_l_index(self):
        ligne = "| [Le contenu](contenu.md) | CO | Produire du contenu avec l'IA |\n"
        self.remplacer("README.md", ligne, ligne + ligne)
        self.assertIn("README : le sujet contenu est listé deux fois", self.ecarts())

    def test_sabotage_deux_groupes_de_meme_nom(self):
        self.remplacer("README.md", "#### Cadrer\n", "#### DÉCOUVRIR\n")
        self.assertIn("README : deux groupes s'appellent « DÉCOUVRIR »", self.ecarts())

    def test_creer_sujet_sans_groupe_va_au_dernier_groupe_de_ce_que_veut_le_client(self):
        self.creer()
        self.assertEqual(entretien.rangement(self.base)[1][1][-1], ("Produire du contenu", ["contenu", "facturation"]))
        self.assertEqual(entretien.rangement(self.base)[0], self.RANGEMENT[0])
        self.assertEqual(self.ecarts(), [])

    def test_creer_sujet_dans_le_groupe_nomme_sans_se_soucier_de_la_casse_ni_des_accents(self):
        self.creer(groupe="SERVIR SES CLIENTS")
        self.assertEqual(self.groupes("Ce que veut le client")["Servir ses clients"],
                         ["support-client", "accueil-des-clients", "facturation"])
        self.assertEqual(self.groupes("Ce que veut le client")["Produire du contenu"], ["contenu"])
        self.creer("avenants", "AV", groupe="Cadrer")  # un groupe de l'autre famille
        self.assertEqual(self.groupes("Les étapes d'une mission")["Cadrer"],
                         ["cadrage", "outils-et-acces", "avenants"])
        self.assertEqual(self.ecarts(), [])

    def test_un_groupe_inconnu_est_refuse_sans_rien_ecrire_sauf_avec_creer_groupe(self):
        avant = (self.base / "README.md").read_text(encoding="utf-8")
        with self.assertRaises(entretien.Erreur) as e:
            self.creer(groupe="Facturer et encaisser")
        self.assertIn("--creer-groupe", str(e.exception))
        self.assertIn("Servir ses clients", str(e.exception))  # les groupes connus aident à choisir
        self.assertEqual((self.base / "README.md").read_text(encoding="utf-8"), avant)
        self.assertFalse((self.base / "facturation.md").exists())
        self.creer(groupe="Facturer et encaisser", creer_groupe=True)
        self.assertEqual(entretien.rangement(self.base)[1][1][-1], ("Facturer et encaisser", ["facturation"]))
        self.assertEqual(len(entretien.rangement(self.base)[1][1]), 6)
        self.assertEqual(entretien.rangement(self.base)[0], self.RANGEMENT[0])
        self.assertEqual(self.ecarts(), [])

    def test_un_nom_de_groupe_vide_ou_malforme_est_refuse(self):
        for nom in ("", "   ", "Facturer \u2014 encaisser", "Factures | relances"):
            with self.assertRaises(entretien.Erreur, msg=repr(nom)):
                self.creer(groupe=nom, creer_groupe=True)
        self.assertFalse((self.base / "facturation.md").exists())

    def test_un_index_sans_groupes_recoit_le_sujet_a_la_suite_du_dernier(self):
        f = self.base / "README.md"
        f.write_text(re.sub(r"^#{3,4} .*\n", "", f.read_text(encoding="utf-8"), flags=re.M), encoding="utf-8")
        self.creer()
        rangees = [l for l in f.read_text(encoding="utf-8").splitlines() if l.startswith("| [")]
        self.assertTrue(rangees[-1].startswith("| [La facturation](facturation.md) | FA |"), rangees[-1])
        with self.assertRaises(entretien.Erreur):
            self.creer("avenants", "AV", groupe="Cadrer")

    def test_la_ligne_de_commande_nomme_le_groupe(self):
        vrai = entretien.BASE
        entretien.BASE = self.base
        sortie, erreur = io.StringIO(), io.StringIO()
        base = ["creer-sujet", "--sujet", "facturation", "--prefixe", "FA", "--titre", "la facturation", "--quand",
                "Les factures", "--partie", "Aujourd'hui", "--question", "Combien de factures partent chaque mois ?",
                "--decide", "Le volume"]
        try:
            with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreur):
                inconnu = entretien.main(base + ["--groupe", "Facturer"])
                code = entretien.main(base + ["--groupe", "Facturer", "--creer-groupe"])
        finally:
            entretien.BASE = vrai
        self.assertEqual((inconnu, code), (1, 0), erreur.getvalue())
        self.assertIn("--creer-groupe", erreur.getvalue())
        self.assertEqual(entretien.rangement(self.base)[1][1][-1], ("Facturer", ["facturation"]))


CR_EN_LIGNE = json.loads((ICI / "compte-rendu-en-ligne-fictif.json").read_text(encoding="utf-8"))
SECTIONS_EN_LIGNE = SECTIONS + ["## Pistes", "## Pour la base de questions"]
LIGNE_DE_L_HOTE = {"base": "premier-echange", "mode": "en-ligne", "sujets": ["support-client"]}  # son `questionnaire`


def sujets_dans_l_ordre_de_l_index():
    """Les sujets dans l'ordre du README, lus par `rangement`, sans passer par les fonctions de l'agent en ligne."""
    return [s for _, groupes in entretien.rangement() for _, sujets in groupes for s in sujets]


def rangees_de_l_index():
    """{sujet: (préfixe, nom, quand l'ouvrir)}, lu ligne à ligne dans le tableau du README."""
    sortie = {}
    for ligne in (entretien.BASE / "README.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| \[([^\]]+)\]\(([a-z0-9-]+)\.md\) \| ([A-Z]{2,4}) \| (.+) \|$", ligne)
        if m:
            sortie[m.group(2)] = (m.group(3), m.group(1), m.group(4))
    return sortie


def lancer(*arguments):
    """La ligne de commande : (code, sortie standard, sortie d'erreur)."""
    sortie, erreur = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreur):
        code = entretien.main(list(arguments))
    return code, sortie.getvalue(), erreur.getvalue()


def taille_affichee(texte):
    m = re.search(r"consigne en ligne : ([\d ]+) caractères", texte)
    return int(m.group(1).replace(" ", "")) if m else None


class AgentEnLigne(unittest.TestCase):
    """L'agent d'entretien en ligne : un visiteur, sans consultant avant l'entretien. Il choisit ses questions dans la
    base, jamais en dehors. La ligne que l'hôte garde porte sa consigne, le schéma de son compte rendu et ses sujets."""

    def test_la_commande_ecrit_la_ligne_que_l_hote_garde(self):
        with tempfile.TemporaryDirectory() as d:
            fichier = pathlib.Path(d) / "dossier" / "ligne.json"
            code, sortie, erreur = lancer("consigne-en-ligne", "--sortie", str(fichier))
            ligne = json.loads(fichier.read_text(encoding="utf-8"))
            self.assertEqual([f.name for f in fichier.parent.iterdir()], ["ligne.json"])  # aucun fichier provisoire
        self.assertEqual((code, erreur), (0, ""))
        self.assertEqual(list(ligne), ["titre", "guide", "consigne", "schema_compte_rendu", "questionnaire"])
        self.assertEqual(ligne["guide"], "en-ligne")
        self.assertEqual(ligne["questionnaire"], {"base": "premier-echange", "mode": "en-ligne",
                                                  "sujets": sujets_dans_l_ordre_de_l_index()})
        self.assertEqual(sorted(ligne["questionnaire"]["sujets"]), entretien.sujets())
        self.assertEqual(ligne["consigne"], entretien.consigne_en_ligne())
        self.assertEqual(ligne["schema_compte_rendu"], entretien.schema_en_ligne())
        self.assertIn(str(fichier), sortie)
        self.assertEqual(taille_affichee(sortie), len(ligne["consigne"]))

    def test_la_ligne_s_ecrit_avec_des_fins_de_ligne_unix_et_une_ecriture_manquee_se_dit(self):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            fichier, dossier = d / "ligne.json", d / "cible"
            self.assertEqual(lancer("consigne-en-ligne", "--sortie", str(fichier))[0], 0)
            self.assertNotIn(b"\r\n", fichier.read_bytes())
            dossier.mkdir()
            code, _, erreur = lancer("consigne-en-ligne", "--sortie", str(dossier))  # un dossier : on ne l'écrase pas
            restes = sorted(p.name for p in d.iterdir())
        self.assertEqual(code, 1)
        self.assertIn("écriture impossible", erreur)
        self.assertEqual(restes, ["cible", "ligne.json"])  # aucun fichier provisoire resté

    def test_sans_sortie_le_json_seul_va_sur_la_sortie_standard_et_la_taille_sur_l_autre(self):
        code, sortie, erreur = lancer("consigne-en-ligne")
        ligne = json.loads(sortie)
        self.assertEqual(code, 0)
        self.assertEqual(ligne["guide"], "en-ligne")
        self.assertEqual(taille_affichee(erreur), len(ligne["consigne"]))
        self.assertIn("visé : moins de 60 000", erreur)

    def test_la_consigne_porte_la_methode_les_outils_l_index_et_toutes_les_questions(self):
        consigne = entretien.consigne_en_ligne()
        self.assertNotIn("{{", consigne)
        for outil in ("`afficher`", "`terminer_entretien`"):
            self.assertIn(outil, consigne)
        rangees = rangees_de_l_index()
        self.assertEqual(sorted(rangees), entretien.sujets())
        for sujet, (prefixe, nom, quand) in rangees.items():
            self.assertIn(f"- {sujet} ({prefixe}) | {nom} | {quand}\n", consigne)
        for sujet in entretien.sujets():
            for q in entretien.base(sujet):
                self.assertIn(f"{q['id']} {q['question']} → {q['decide']}", consigne, q["id"])

    def test_une_question_qui_se_cherche_ailleurs_que_chez_la_personne_est_marquee(self):
        lignes = entretien.consigne_en_ligne().splitlines()
        vus = set()
        for sujet in entretien.sujets():
            for q in entretien.base(sujet):
                ligne = next(l for l in lignes if l.startswith(q["id"] + " "))
                vus.add(q["dabord"])
                marque = {"l'outil": " [outil]", "un document": " [document]"}.get(q["dabord"])
                if marque:
                    self.assertTrue(ligne.endswith(marque), ligne)
                else:
                    self.assertFalse(ligne.endswith(("]", "[outil]", "[document]")), ligne)
        self.assertEqual(vus, {"la personne", "l'outil", "un document"})  # la base les contient tous : l'essai mord

    def test_la_consigne_dit_la_methode_et_les_interdits(self):
        consigne = " ".join(entretien.consigne_en_ligne().split())  # une phrase coupée par un retour à la ligne se lit entière
        for attendu in (
                "Tu ne poses que des questions de la base",  # jamais une question absente
                "12 au plus",  # douze questions
                "ce que la page a déjà demandé",  # jamais ce que la page a posé
                "2 à 6 textes de 60 caractères au plus",  # les réponses suggérées
                "Je ne sais pas",
                "de 3 à 7 étapes",  # le plan de l'audit
                "ni prix, ni volume, ni gain, ni délai",  # rien promettre
                "Conseiller avant la fin",
                "un mot de passe, une clé",
                "[retiré]",
                "Est-ce juste ? Voulez-vous ajouter ou corriger quelque chose ?",  # le récapitulatif validé
                "Aucun mot de passe ni clé"):
            self.assertIn(attendu, consigne)

    def test_la_consigne_tient_sous_la_limite_et_ne_nomme_personne(self):
        consigne = entretien.consigne_en_ligne()
        self.assertLess(len(consigne), 60000)
        self.assertEqual(entretien.LIMITE_CONSIGNE_EN_LIGNE, 60000)
        for fichier in ("agent-en-ligne.md", "consigne-en-ligne.md", "compte-rendu-en-ligne.schema.json"):
            texte = (entretien.COMPETENCE / "references" / fichier).read_text(encoding="utf-8")
            for interdit in ("—", "–", "@", "http", "Florent", "ZEROGRAVITY", "Gremelinn0", "Pilotage"):
                self.assertNotIn(interdit, texte, fichier)
                self.assertNotIn(interdit, consigne)

    def test_le_schema_du_compte_rendu_en_ligne(self):
        s = entretien.schema_en_ligne()
        self.assertEqual(s["required"], ["demande", "contexte", "sujet", "reponses", "pistes", "questions_ouvertes",
                                         "prochaine_etape"])
        p = s["properties"]
        self.assertEqual(set(p), set(s["required"]) | {"pour_la_base", "noms_a_retirer"})
        self.assertEqual(p["contexte"]["required"], ["taille", "metier", "outils"])
        self.assertEqual(p["contexte"]["properties"]["outils"]["type"], "array")
        self.assertEqual(p["reponses"]["items"]["required"], ["id", "question", "reponse"])
        self.assertEqual((p["reponses"]["minItems"], p["reponses"]["maxItems"]), (1, 12))
        self.assertEqual(p["pistes"]["items"]["required"], ["constat", "piste"])
        self.assertEqual(p["sujet"]["enum"], sujets_dans_l_ordre_de_l_index())
        code, sortie, _ = lancer("schema", "--guide", "en-ligne")
        self.assertEqual((code, json.loads(sortie)), (0, s))
        self.assertEqual(json.loads(lancer("schema")[1])["required"][0], "role")  # sans guide : l'autre schéma

    def test_la_methode_et_la_consigne_disent_les_memes_limites_que_le_code(self):
        self.assertEqual((entretien.CHOIX_EN_LIGNE, entretien.CHOIX_LONGUEUR, entretien.PLAN_EN_LIGNE,
                          entretien.MAX_EN_LIGNE), ((2, 6), 60, (3, 7), 12))
        doc = (entretien.COMPETENCE / "references" / "agent-en-ligne.md").read_text(encoding="utf-8")
        bloc = next(b for b in re.findall(r"```json\n(.*?)\n```", doc, re.S) if '"suggestions"' in b)
        afficher = json.loads(bloc)["properties"]
        choix = afficher["suggestions"]["properties"]["choix"]
        self.assertEqual((choix["minItems"], choix["maxItems"], choix["items"]["maxLength"]), (2, 6, 60))
        self.assertEqual((afficher["plan"]["minItems"], afficher["plan"]["maxItems"]), (3, 7))
        self.assertEqual(afficher["plan"]["items"]["properties"]["etat"]["enum"], ["fait", "en_cours", "a_venir"])
        consigne = entretien.consigne_en_ligne()
        for fragment in ("2 à 6 textes de 60 caractères", "de 3 à 7 étapes", "12 au plus",
                         "`etat` vaut `fait`, `en_cours` ou `a_venir`"):
            self.assertIn(fragment, consigne)

    def test_la_competence_porte_la_nouvelle_regle_et_cite_la_methode(self):
        skill = (entretien.COMPETENCE / "SKILL.md").read_text(encoding="utf-8")
        for fichier in ("agent-en-ligne.md", "consigne-en-ligne.md", "compte-rendu-en-ligne.schema.json"):
            self.assertIn(fichier, skill)
            self.assertTrue((entretien.COMPETENCE / "references" / fichier).exists(), fichier)
        self.assertIn("l'agent choisit ses questions dans la base, jamais en dehors", skill)
        self.assertNotIn("| laisser l'IA choisir ses questions en direct | jamais |", skill)  # l'ancien rejet sans réserve

    def test_verifier_affiche_la_taille_de_la_consigne(self):
        code, sortie, _ = lancer("verifier")
        self.assertEqual(code, 0, sortie)
        self.assertRegex(sortie, r"aucun écart \(consigne en ligne : [\d ]+ caractères sur 60 000\)")


class AgentEnLigneSurUneCopie(unittest.TestCase):
    """Les contrôles de la consigne, prouvés par un sabotage sur une copie de la base."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.base = pathlib.Path(self._tmp.name) / "base"
        shutil.copytree(entretien.BASE, self.base)

    def tearDown(self):
        self._tmp.cleanup()

    def barrer(self, fichier, numero, jusque_dans_le_numero=False):
        """Retire une question de la base à la manière du pack : elle garde son numéro, et se lit barrée."""
        f = self.base / fichier
        lignes = f.read_text(encoding="utf-8").splitlines()
        for i, ligne in enumerate(lignes):
            if ligne.startswith(f"| {numero} |"):
                c = [x.strip() for x in ligne.strip().strip("|").split("|")]
                c[1], c[2] = f"~~{c[1]}~~", f"~~{c[2]}~~"
                if jusque_dans_le_numero:
                    c[0] = f"~~{c[0]}~~"
                lignes[i] = "| " + " | ".join(c) + " |"
                break
        else:
            self.fail(f"{numero} absent de {fichier}")
        f.write_text("\n".join(lignes) + "\n", encoding="utf-8")

    def test_une_question_barree_n_est_pas_dans_la_consigne(self):
        q1, q2, q3 = entretien.base("crm", self.base)[:3]
        self.assertIn(q1["question"], entretien.consigne_en_ligne(self.base))
        self.barrer("crm.md", q1["id"])
        self.barrer("crm.md", q2["id"], jusque_dans_le_numero=True)
        consigne = entretien.consigne_en_ligne(self.base)
        for q in (q1, q2):
            self.assertNotIn(q["question"], consigne, q["id"])
            self.assertNotIn(q["id"] + " ", consigne, q["id"])
            self.assertNotIn(q["id"], entretien.questions_en_ligne(self.base))
        self.assertIn(f"{q3['id']} {q3['question']} → {q3['decide']}", consigne)

    def test_une_question_retiree_ne_se_repond_pas(self):
        pris = {r["id"] for r in CR_EN_LIGNE["reponses"]}
        q = next(q for q in entretien.base("support-client", self.base) if q["id"] not in pris)
        cr = copy.deepcopy(CR_EN_LIGNE)
        cr["reponses"][2]["id"] = q["id"]
        self.assertEqual(entretien.controler_en_ligne(cr, dossier=self.base), [])
        self.barrer("support-client.md", q["id"])
        ecarts = entretien.controler_en_ligne(cr, dossier=self.base)
        self.assertTrue(any("n'est pas une question de la base" in e for e in ecarts), ecarts)

    def test_un_index_qui_ne_concorde_pas_avec_les_fichiers_est_refuse(self):
        f = self.base / "README.md"
        f.write_text(f.read_text(encoding="utf-8").replace(
            "| [Le contenu](contenu.md) | CO | Produire du contenu avec l'IA |\n", ""), encoding="utf-8")
        with self.assertRaises(entretien.Erreur) as e:
            entretien.consigne_en_ligne(self.base)
        self.assertIn("ne concordent pas", str(e.exception))

    def test_verifier_refuse_une_consigne_trop_longue(self):
        self.assertEqual(entretien.verifier_base(self.base), [])
        limite = entretien.LIMITE_CONSIGNE_EN_LIGNE
        entretien.LIMITE_CONSIGNE_EN_LIGNE = 1000
        try:
            ecarts = entretien.verifier_base(self.base)
        finally:
            entretien.LIMITE_CONSIGNE_EN_LIGNE = limite
        self.assertTrue(any(e.startswith("consigne en ligne : ") and "plus que les 1 000" in e for e in ecarts), ecarts)


class NoteDeLAgentEnLigne(unittest.TestCase):
    """Le compte rendu de l'agent en ligne donne une note de même structure que les autres, avec ses pistes ; le contrôle
    refuse ce qui enfreint la méthode : une question hors base, trop de réponses, une adresse, un prix."""

    def cr(self):
        return copy.deepcopy(CR_EN_LIGNE)

    def ecrire(self, cr, messages=None, ligne=None):
        with tempfile.TemporaryDirectory() as d:
            fichiers = entretien.ecrire_note(cr, d, messages, ligne)
            return [f.name for f in fichiers], [f.read_text(encoding="utf-8") for f in fichiers]

    def test_un_compte_rendu_en_ligne_donne_une_note_de_meme_structure(self):
        self.assertEqual(entretien.controler(self.cr()), [])
        messages = [{"role": "assistant", "texte": "Hello"}, {"role": "user", "texte": "Hi"}]
        noms, textes = self.ecrire(self.cr(), messages, LIGNE_DE_L_HOTE)  # comme l'hôte : la ligne en 4e argument
        self.assertRegex(noms[0], r"^entretien-visiteur-[0-9a-f]{6}-2026-10-28\.md$")
        self.assertEqual(noms[1], noms[0].replace(".md", ".transcription.md"))
        note = textes[0]
        self.assertRegex(note.splitlines()[0], r"^# Entretien — visiteur [0-9a-f]{6}, boutique en ligne · 2026-10-28 · 13 min$")
        positions = [note.index(s) for s in SECTIONS_EN_LIGNE]
        self.assertEqual(positions, sorted(positions))
        partie = next(q["partie"] for q in entretien.base("support-client") if q["id"] == "SC05")
        self.assertIn(f"### SC05 · {partie}", note)
        self.assertIn("*Roughly how many customer messages do you get per week, and through which channels?*", note)
        self.assertIn("> « About 80 a week, mostly email, a few on Instagram. »", note)
        self.assertIn("> « I want an agent that answers my customers, I spend my evenings on emails. »", note)
        self.assertIn("Contexte : métier : boutique en ligne ; taille : 8 personnes ; outils : boîte de réception, "
                      "tableur, outil de boutique en ligne.", note)
        self.assertIn("→ piste : Un agent pourrait préparer les réponses de suivi de commande", note)
        self.assertIn("Prochaine étape : À définir avec le consultant.", note)
        self.assertIn("- Combien coûterait un agent", note)
        self.assertIn("- Les clients professionnels ont-ils un interlocuteur à part ?", note)
        self.assertIn("À relire par le consultant avant de l'ajouter à `references/base-questions/support-client.md`.", note)
        self.assertIn(f"Transcription intégrale : `{noms[1]}`", note)
        self.assertIn("5 questions choisies dans la base (sujet : support-client)", note)
        self.assertNotIn("`[F]`", note)  # rien n'est un fait : tout est dit de mémoire

    def test_sans_pour_la_base_la_section_reste(self):
        cr = self.cr()
        cr.pop("pour_la_base")
        cr["pistes"] = []
        note = self.ecrire(cr)[1][0]
        self.assertIn("## Pour la base de questions\n\nRien à ajouter.", note)
        self.assertIn("## Pistes\n\nAucune piste relevée.", note)

    def test_la_commande_note_accepte_un_compte_rendu_en_ligne(self):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / "cr.json").write_text(json.dumps(self.cr()), encoding="utf-8")
            (d / "messages.json").write_text(json.dumps([{"role": "user", "texte": "write to jane@example.com"}]),
                                             encoding="utf-8")
            code, sortie, erreur = lancer("note", "--compte-rendu", str(d / "cr.json"), "--transcription",
                                          str(d / "messages.json"), "--sortie", str(d / "mission"))
            self.assertEqual(code, 0, erreur)
            self.assertEqual(len(sortie.split()), 2)
            self.assertEqual(len(list((d / "mission").iterdir())), 2)
            transcription = next((d / "mission").glob("*.transcription.md")).read_text(encoding="utf-8")
        self.assertNotIn("jane@example.com", transcription)
        self.assertIn("[retiré]", transcription)

    def test_la_duree_la_langue_et_le_role_de_l_hote_sont_facultatifs(self):
        cr = self.cr()
        cr.pop("duree_minutes")
        cr.pop("langue")
        note = self.ecrire(cr)[1][0]
        self.assertRegex(note.splitlines()[0], r"boutique en ligne · 2026-10-28$")
        self.assertIn("Langue : non précisée", note)
        cr["role"] = "gérante"
        self.assertEqual(self.ecrire(cr)[0][0], "entretien-gerante-2026-10-28.md")

    def test_deux_visiteurs_le_meme_jour_ne_s_ecrasent_pas(self):
        autre = self.cr()
        autre["reponses"][1]["reponse"] = "About 200 a week."
        premier = self.ecrire(self.cr())[0][0]
        self.assertNotEqual(premier, self.ecrire(autre)[0][0])
        self.assertEqual(premier, self.ecrire(self.cr())[0][0])  # la même note garde son nom

    def test_un_nom_ecrit_est_retire_de_la_transcription_et_refuse_ailleurs(self):
        cr = self.cr()
        cr["noms_a_retirer"] = ["Sophie"]
        texte = entretien.rendre_transcription(cr, [{"role": "user", "texte": "Sophie answers the emails."}])
        self.assertNotIn("Sophie", texte)
        self.assertIn("[retiré] answers", texte)
        self.assertEqual(entretien.controler(cr), [])
        cr["reponses"][0]["reponse"] += " Sophie helps."
        self.assertTrue(any("noms_a_retirer" in e for e in entretien.controler(cr)))

    def test_le_questionnaire_de_la_ligne_doit_etre_celui_de_l_agent_en_ligne(self):
        self.assertEqual(entretien.controler(self.cr(), q=LIGNE_DE_L_HOTE), [])
        self.assertTrue(any("le compte rendu suit le guide en-ligne" in e
                            for e in entretien.controler(self.cr(), q={"guide": "prepare"})))

    # Sabotages : chaque règle de la méthode, cassée une fois, doit faire refuser la note, et rien n'est écrit.
    def refuse(self, modifier, attendu):
        cr = self.cr()
        modifier(cr)
        ecarts = entretien.controler(cr)
        self.assertTrue(any(attendu in e for e in ecarts), ecarts)
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(entretien.Erreur):
                entretien.ecrire_note(cr, d)
            self.assertEqual(list(pathlib.Path(d).iterdir()), [])

    def test_une_question_absente_de_la_base_est_refusee(self):
        self.refuse(lambda cr: cr["reponses"][1].update(id="ZZ99"), "reponses[2] : 'ZZ99' n'est pas une question de la base")

    def test_douze_reponses_au_plus(self):
        ids = [q["id"] for q in entretien.base("support-client")][:13]

        def reponses(n):
            return [{"id": i, "question": "Une question ?", "reponse": "Une réponse."} for i in ids[:n]]
        cr = self.cr()
        cr["reponses"] = reponses(12)
        self.assertEqual(entretien.controler(cr), [])
        self.refuse(lambda cr: cr.update(reponses=reponses(13)), "13 réponses, 12 au plus")

    def test_la_meme_question_deux_fois_est_refusee(self):
        self.refuse(lambda cr: cr["reponses"][2].update(id="SC01"), "la question SC01 est déjà dans les réponses")

    def test_le_sujet_est_un_sujet_de_la_base(self):
        self.refuse(lambda cr: cr.update(sujet="sujet-qui-n-existe-pas"), "n'est pas un sujet de la base")

    def test_aucune_adresse_ni_numero_dans_le_compte_rendu(self):
        self.refuse(lambda cr: cr["reponses"][0].update(reponse="Write me at jane@example.com"),
                    "reponses[1].reponse : une adresse ou un numéro")
        self.refuse(lambda cr: cr["reponses"][0].update(reponse="Call +1 212 555 0100"),
                    "reponses[1].reponse : une adresse ou un numéro")
        self.refuse(lambda cr: cr.update(demande="Mail me: jane@example.com"), "demande : une adresse ou un numéro")
        self.refuse(lambda cr: cr["questions_ouvertes"].append("Rappeler le 06 12 34 56 78"),
                    "questions_ouvertes : une adresse ou un numéro")

    def test_un_prix_n_est_pas_une_piste(self):
        self.refuse(lambda cr: cr["pistes"][0].update(piste="Un agent à 990 € par mois."), "pistes[1].piste : un prix")
        self.refuse(lambda cr: cr["pistes"][1].update(piste="Cela coûterait 5 000 euros."), "pistes[2].piste : un prix")
        self.refuse(lambda cr: cr.update(prochaine_etape="Un audit à 500 euros HT."), "prochaine_etape : un prix")
        cr = self.cr()  # un montant dit par la personne, dans un constat, n'est pas un prix donné par l'agent
        cr["pistes"][0]["constat"] = "Elle dit payer 300 € par mois un prestataire."
        self.assertEqual(entretien.controler(cr), [])

    def test_un_champ_manquant_ou_un_texte_vide_est_refuse(self):
        self.refuse(lambda cr: cr.pop("pistes"), "champ manquant : pistes")
        self.refuse(lambda cr: cr["reponses"][0].update(reponse="  "), "reponses[1].reponse : un texte est attendu")
        self.refuse(lambda cr: cr.update(reponses=[]), "reponses : au moins une réponse")
        self.refuse(lambda cr: cr.update(reponses={"id": "SC01"}), "reponses : au moins une réponse")  # pas de plantage
        self.refuse(lambda cr: cr["contexte"].pop("taille"), "contexte.taille")
        self.refuse(lambda cr: cr.update(prochaine_etape=""), "prochaine_etape : un texte est attendu")

    def test_la_date_est_posee_par_l_hote(self):
        self.refuse(lambda cr: cr.pop("date"), "champ manquant : date (l'hôte la pose)")
        self.refuse(lambda cr: cr.update(date="28/10/2026"), "date : AAAA-MM-JJ attendu")
        self.refuse(lambda cr: cr.update(duree_minutes="treize"), "duree_minutes")


if __name__ == "__main__":
    unittest.main()
