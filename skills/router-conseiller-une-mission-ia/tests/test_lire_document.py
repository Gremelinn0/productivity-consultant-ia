"""Le convertisseur des pièces jointes : un vrai Word et un vrai Excel minimaux, un fichier cassé, un format refusé."""
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "lire_document.py"
W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
S = 'xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"'


def lancer(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], capture_output=True, text=True)


class Conversion(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())

    def test_word_paragraphes_et_tableau(self):
        f = self.d / "a.docx"
        with zipfile.ZipFile(f, "w") as z:
            z.writestr("word/document.xml", f'<w:document {W}><w:body><w:p><w:r><w:t>Relances clients</w:t></w:r></w:p>'
                       '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>Outil</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>HubSpot</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'
                       '</w:body></w:document>')
        self.assertEqual(lancer(f, self.d / "s.md").returncode, 0)
        t = (self.d / "s.md").read_text(encoding="utf-8")
        self.assertIn("Relances clients", t)
        self.assertIn("| Outil | HubSpot |", t)

    def test_excel_chaines_partagees_et_nombres(self):
        f = self.d / "a.xlsx"
        with zipfile.ZipFile(f, "w") as z:
            z.writestr("xl/workbook.xml", f'<workbook {S} xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Ventes" sheetId="1" r:id="rId1"/></sheets></workbook>')
            z.writestr("xl/_rels/workbook.xml.rels", '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="x" Target="worksheets/sheet1.xml"/></Relationships>')
            z.writestr("xl/sharedStrings.xml", f'<sst {S}><si><t>Mois</t></si></sst>')
            z.writestr("xl/worksheets/sheet1.xml", f'<worksheet {S}><sheetData><row r="1"><c r="A1" t="s"><v>0</v></c><c r="C1"><v>42</v></c></row></sheetData></worksheet>')
        self.assertEqual(lancer(f, self.d / "s.md").returncode, 0)
        t = (self.d / "s.md").read_text(encoding="utf-8")
        self.assertIn("## Ventes", t)
        self.assertIn("| Mois |  | 42 |", t)

    def test_fichier_casse_ne_produit_rien(self):
        f = self.d / "a.docx"
        f.write_bytes(b"pas une archive")
        self.assertEqual(lancer(f, self.d / "s.md").returncode, 2)
        self.assertFalse((self.d / "s.md").exists())

    def test_format_refuse(self):
        f = self.d / "a.txt"
        f.write_text("x")
        self.assertEqual(lancer(f, self.d / "s.md").returncode, 2)


if __name__ == "__main__":
    unittest.main()
