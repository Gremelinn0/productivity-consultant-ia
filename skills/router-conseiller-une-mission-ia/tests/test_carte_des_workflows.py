"""La carte des workflows : un titre par métier, un workflow par ligne, jamais une compétence, et un refus plutôt qu'un trou."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "carte_des_workflows.py"
CARTE = Path(__file__).parents[1] / "references" / "carte-des-workflows.md"
PARCOURS = Path(__file__).parents[1] / "references" / "parcours-en-ligne.md"


def wf(slug, metier, titre="Un titre", resume="Un résumé."):
    return {"slug": slug, "metiers": [metier], "titre": titre, "resume": resume,
            "etapes": [{"competences": [{"nom": "competence-secrete"}]}]}


def lancer(d, workflows):
    source, sortie = d / "w.json", d / "carte.md"
    source.write_text(json.dumps({"workflows": workflows}), encoding="utf-8")
    r = subprocess.run([sys.executable, str(SCRIPT), str(source), "--date", "2026-11-05", "--sortie", str(sortie)],
                       capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONUTF8": "1"})
    return r, sortie


class Carte(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())

    def test_un_titre_par_metier_dans_l_ordre_et_jamais_une_competence(self):
        r, sortie = lancer(self.d, [wf("b", "vente", "Vendre", "Vendre mieux."), wf("a", "conseil", "Conseiller", "Conseiller mieux.")])
        self.assertEqual(r.returncode, 0, r.stderr)
        t = sortie.read_text(encoding="utf-8")
        self.assertIn("Instantané du 2026-11-05", t)
        self.assertLess(t.index("## Conseil"), t.index("## Vente"))
        self.assertIn("- **Vendre** : Vendre mieux.", t)
        self.assertNotIn("competence-secrete", t)

    def test_un_metier_sans_libelle_est_refuse(self):
        r, sortie = lancer(self.d, [wf("a", "metier-neuf")])
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse(sortie.exists())

    def test_un_workflow_sans_resume_est_refuse(self):
        r, sortie = lancer(self.d, [wf("a", "vente", resume="")])
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse(sortie.exists())

    def test_une_source_vide_n_ecrit_rien(self):
        r, sortie = lancer(self.d, [])
        self.assertEqual(r.returncode, 1)
        self.assertFalse(sortie.exists())

    def test_la_carte_du_pack_existe_et_la_regle_6_la_cite(self):
        self.assertIn("## Conseil", CARTE.read_text(encoding="utf-8"))
        self.assertIn("references/carte-des-workflows.md", PARCOURS.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
