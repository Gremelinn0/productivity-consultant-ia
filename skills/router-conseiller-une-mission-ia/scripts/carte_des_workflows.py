"""Écrit references/carte-des-workflows.md, la liste des workflows publiés que lit l'agent du parcours en ligne.

L'agent hébergé n'a pas internet : il ne peut pas ouvrir la carte du site pour dire de quel côté vient un cas
(`references/parcours-en-ligne.md`, règle 6). Ce script en fait un instantané, à relancer quand un workflow est publié,
retiré ou renommé, avant de remonter le pack sur l'agent.

Usage :
  python skills/router-conseiller-une-mission-ia/scripts/carte_des_workflows.py <workflows.generated.json> [--date AAAA-MM-JJ]

La source est le fichier public du site : il ne contient que les workflows publiés et leurs compétences publiques.
Seuls le titre et le résumé de chaque workflow entrent ici, jamais ses compétences.
"""
import argparse
import datetime
import json
import pathlib
import sys

SORTIE = pathlib.Path(__file__).resolve().parents[1] / "references" / "carte-des-workflows.md"
METIERS = {
    "conseil": "Conseil",
    "vente": "Vente",
    "marketing": "Marketing",
    "relation-client": "Relation client",
    "rh": "Ressources humaines",
    "dev": "Développement",
    "design": "Design",
}
ENTETE = """# La carte des workflows : ce qui existe déjà

Instantané du {date} de la carte publique, à l'usage de l'agent du parcours en ligne, qui n'a pas internet. Un cas
d'usage est **couvert par la carte** quand un workflow ci-dessous sait le mener : `02-portefeuille.md` le dit en citant
son titre. Sinon, il est **propre à l'entreprise** : `02-portefeuille.md` le dit aussi. Le rattachement est un jugement
sur le résultat attendu, pas sur les mots employés.
"""


def rendre(workflows, date):
    """Le texte de la carte : un titre par métier, dans l'ordre de METIERS, un workflow par ligne, triés par titre."""
    groupes = {}
    for wf in workflows:
        metiers = wf.get("metiers") or []
        if not metiers or not wf.get("titre") or not wf.get("resume"):
            raise ValueError(f"workflow incomplet : {wf.get('slug')}")
        groupes.setdefault(metiers[0], []).append(wf)
    inconnus = sorted(set(groupes) - set(METIERS))
    if inconnus:
        raise ValueError(f"métier sans libellé : {', '.join(inconnus)}")
    lignes = [ENTETE.format(date=date)]
    for slug, libelle in METIERS.items():
        if slug not in groupes:
            continue
        lignes.append(f"## {libelle}\n")
        for wf in sorted(groupes[slug], key=lambda w: w["titre"]):
            lignes.append(f"- **{wf['titre']}** : {wf['resume'].strip()}")
        lignes.append("")
    return "\n".join(lignes).rstrip() + "\n"


def main(argv=None):
    parseur = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parseur.add_argument("source", type=pathlib.Path, help="le fichier workflows.generated.json du site")
    parseur.add_argument("--date", default=datetime.date.today().isoformat())
    parseur.add_argument("--sortie", type=pathlib.Path, default=SORTIE)
    args = parseur.parse_args(argv)
    workflows = json.loads(args.source.read_text(encoding="utf-8"))["workflows"]
    if not workflows:
        print("Aucun workflow dans la source : rien n'est écrit.", file=sys.stderr)
        return 1
    args.sortie.write_text(rendre(workflows, args.date), encoding="utf-8", newline="\n")
    print(f"Écrit : {args.sortie.name} ({len(workflows)} workflows).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
