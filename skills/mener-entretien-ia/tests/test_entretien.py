"""Essais de scripts/entretien.py : python -m unittest discover -s skills/mener-entretien-ia/tests"""
import copy
import json
import pathlib
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
        self.assertEqual(len(q), 39)
        self.assertEqual(len({x["id"] for x in q}), 39)
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


if __name__ == "__main__":
    unittest.main()
