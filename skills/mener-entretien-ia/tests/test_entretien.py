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
        for guide, n in attendus.items():
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


if __name__ == "__main__":
    unittest.main()
