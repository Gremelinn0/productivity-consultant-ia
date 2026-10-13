"""Sabotages de la recette (85-recette.md, rubrique 6) : un test qui n'a jamais échoué ne prouve rien.

Pour chaque garde-fou protégé par un test, une régression plausible (celle qu'une modification future introduirait
par mégarde) est introduite dans une COPIE de la version gelée ; le test visé doit échouer sur la copie. La copie est
jetée, l'empreinte de la version gelée est comparée à celle du début (rien n'a bougé), puis le test visé est relancé
sur la version gelée : il doit réussir. La version gelée n'est jamais modifiée : ce script ne fait que la lire.

Commande (depuis ce dossier) : `python -X utf8 sabotage.py` ; code de sortie 0 si tous les sabotages ont fait échouer
leur test et si tous les rétablissements sont vérifiés. Chaque régression est écrite en une ligne. Bibliothèque
standard seulement.
"""
from __future__ import annotations

import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
LIVRAISON = (ICI.parent / "80-construction" / "livraison").resolve()
sys.path.insert(0, str(LIVRAISON))

import flux_relances as fr  # noqa: E402

# Valeur fictive qui ressemble à une clé (S-13). Elle se compose à l'exécution : le texte d'une forme de clé réelle
# n'est écrit dans aucun fichier du dépôt, et aucune sortie ne le montre en entier.
TEMOIN_CLE = "sk_" + "live_" + "9f8e7d6c5b4a3928" + "1706f5e4d3c2b1a0"

# (type, fichier, ancien, nouveau) · ("ajouter", fichier, texte) · ("supprimer", chemin relatif)
SABOTAGES = [
    dict(id="S-1", test="T13", protege="cas limite critique : fraîcheur du rapprochement (CA-10)",
         regression="retirer le contrôle de fraîcheur du rapprochement à l'étape 1",
         patches=[("remplacer", "flux_relances.py", "jours_ouvres_entre(dernier, jour, self.regles.feries) > self.regles.fraicheur", "False")]),
    dict(id="S-2", test="T12", protege="dédoublonnage : un brouillon par clé",
         regression="sauter la recherche de la clé dans « propositions » et dans la boîte avant de créer un brouillon",
         patches=[("remplacer", "flux_relances.py", 'if etat in ("brouillon créé", "envoyée"):', "if False:"),
                  ("remplacer", "flux_relances.py", "existant = self._brouillons.get(cle)", "existant = None")]),
    dict(id="S-3", test="T10", protege="permissions : le compte de service n'envoie pas (EF-10)",
         regression="donner le droit d'envoi au compte de service de la messagerie",
         patches=[("remplacer", "essai_s2_s3.py", 'SERVICE_MESSAGERIE: {"creer_brouillon", "lire", "lister", "supprimer_brouillon"},',
                   'SERVICE_MESSAGERIE: {"creer_brouillon", "lire", "lister", "supprimer_brouillon", "envoyer"},')]),
    dict(id="S-4", test="T18", protege="interrupteur « Suspendre » lu à chaque passage de la veille",
         regression="ne plus lire la case « Suspendre » pendant la veille",
         patches=[("remplacer", "flux_relances.py", 'suspendu = commande.get("suspendre") == "oui"', "suspendu = False")]),
    dict(id="S-5", test="T17", protege="plafond de 100 propositions par exécution",
         regression="relever le plafond à un milliard",
         patches=[("remplacer", "flux_relances.py", "len(evaluation) > self.regles.plafond", "len(evaluation) > 10 ** 9")]),
    dict(id="S-6", test="T22", protege="changement non approuvé : empreinte des règles et des modèles",
         regression="supprimer le refus quand l'empreinte diffère de la version approuvée",
         patches=[("remplacer", "flux_relances.py", 'raise ChangementNonApprouve("règles ou modèles modifiés hors de la version approuvée")', "return")]),
    dict(id="S-7", test="T29", protege="reprise après plantage : brouillon créé avant l'enregistrement de la clé",
         regression="ne plus adopter le brouillon déjà présent dans la boîte (pas de réconciliation)",
         patches=[("remplacer", "flux_relances.py", "existant = self._brouillons.get(cle)", "existant = None")]),
    dict(id="S-8", test="T07", protege="validation humaine des comptes clés (alerte « envoi hors validation »)",
         regression="retirer l'alerte quand un compte clé part d'un autre compte que celui du responsable financier",
         patches=[("remplacer", "flux_relances.py", "prop[\"dossier\"] == DOSSIER_COMPTES_CLES and expediteur != RESPONSABLE_FINANCIER", "False")]),
    dict(id="S-9", test="T03", protege="exclusion des factures payées (relance à tort)",
         regression="retirer le motif d'exclusion « payée »",
         patches=[("remplacer", "flux_relances.py", 'ligne["etat_paiement"].strip() == "rapprochée"', "False")]),
    dict(id="S-10", test="T22", protege="processus instable : l'exécution garde les règles de son début",
         regression="relire les règles à chaque brouillon",
         patches=[("remplacer", "flux_relances.py", "    def _composer(self, prop: Proposition):\n        ligne = prop.ligne\n",
                   "    def _composer(self, prop: Proposition):\n        self.regles = charger_regles(self.classeur)\n        ligne = prop.ligne\n")]),
    dict(id="S-11", test="T02", protege="une facture ne saute jamais de niveau",
         regression="proposer le niveau atteint par l'âge au lieu du niveau qui suit la dernière relance",
         patches=[("remplacer", "flux_relances.py", "            niveau = dernier + 1\n", "            niveau = atteint\n")]),
    dict(id="S-12", test="T18", protege="alerte sur silence (flux non lancé à 10 h)",
         regression="désactiver l'alerte « aucune exécution »",
         patches=[("remplacer", "flux_relances.py",
                   '            self._alerter([RESPONSABLE_FINANCIER], "aucune exécution", "10", "silence",\n'
                   '                          f"aucune exécution le {jour} à {self.regles.silence_heure}")\n', "            pass\n")]),
    dict(id="S-13", test="T33", protege="secrets : aucune valeur de secret dans la livraison",
         regression="glisser dans le code une valeur fictive qui ressemble à une clé",
         patches=[("ajouter", "flux_relances.py", '\nAPI_KEY = "' + TEMOIN_CLE + '"\n')]),
    dict(id="S-14", test="T34", protege="retour arrière : l'export de la version précédente existe",
         regression="supprimer l'export de la version précédente (archives/flux-relances-v1.0.zip)",
         patches=[("supprimer", "archives/flux-relances-v1.0.zip")]),
    dict(id="S-15", test="T06", protege="EF-04 : un litige signalé retire le brouillon",
         regression="ne plus relire la liste des litiges à la veille",
         patches=[("remplacer", "flux_relances.py",
                   'litiges = {l["numero_facture"].strip() for l in self._lire_veille("pilotage", "litiges")}', "litiges = set()")]),
    dict(id="S-16", test="T27", protege="lecture après écriture : le brouillon relu est celui qui était voulu",
         regression="neutraliser la comparaison du corps et de la clé relus",
         patches=[("remplacer", "flux_relances.py", 'or relu.corps != corps or relu.entetes.get("X-Relance-Id") != cle):', "or False):")]),
    dict(id="S-17", test="T32", protege="aucun nom ni adresse de contact dans les traces",
         regression="écrire le nom du contact dans le journal d'une proposition retenue",
         patches=[("remplacer", "flux_relances.py", '                          "compte clé" if prop.compte_cle else "")',
                   '                          "compte clé" if prop.compte_cle else ligne["nom_contact"])')]),
]


def sha(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def empreintes() -> dict:
    return {nom: sha(LIVRAISON / nom) for nom in ("flux_relances.py", "essai_s2_s3.py", "MANIFESTE.sha256")}


def lancer(tests: list, livraison: Path | None):
    env = {k: v for k, v in os.environ.items() if k != "FLUX_LIVRAISON"}
    if livraison is not None:
        env["FLUX_LIVRAISON"] = str(livraison)
    r = subprocess.run([sys.executable, "-X", "utf8", str(ICI / "test_recette.py"), *tests], capture_output=True,
                       text=True, encoding="utf-8", env=env, cwd=ICI)
    return r.returncode, r.stdout + r.stderr


def bilan(sortie: str):
    m = re.search(r"BILAN : (\d+) tests joués · (\d+) réussis · (\d+) échoués · (\d+) en erreur", sortie)
    return tuple(int(x) for x in m.groups()) if m else None


def tests_en_echec(sortie: str) -> list:
    ids = []
    for ligne in sortie.splitlines():
        m = re.match(r"\s*(T-\d+b?) ·.*\.\.\. (FAIL|ERROR)$", ligne)
        if m and m.group(1) not in ids:
            ids.append(m.group(1))
    return ids


def premiere_exception(sortie: str) -> str:
    lignes = sortie.splitlines()
    for i, ligne in enumerate(lignes):
        if ligne.startswith("Traceback (most recent call last):"):
            for suivante in lignes[i + 1:]:
                if suivante and not suivante.startswith(" "):
                    return suivante.strip()[:160]
    return ""


def appliquer(copie: Path, patches: list) -> None:
    for patch in patches:
        if patch[0] == "remplacer":
            _, fichier, ancien, nouveau = patch
            chemin = copie / fichier
            texte = chemin.read_text(encoding="utf-8")
            if texte.count(ancien) != 1:
                raise SystemExit(f"sabotage impossible : {texte.count(ancien)} occurrence(s) de {ancien[:60]!r} dans {fichier}")
            chemin.write_text(texte.replace(ancien, nouveau, 1), encoding="utf-8", newline="\n")
        elif patch[0] == "ajouter":
            _, fichier, texte = patch
            with open(copie / fichier, "a", encoding="utf-8", newline="\n") as f:
                f.write(texte)
        elif patch[0] == "supprimer":
            (copie / patch[1]).unlink()


def main() -> int:
    for flux in (sys.stdout, sys.stderr):
        if hasattr(flux, "reconfigure"):
            flux.reconfigure(encoding="utf-8")
    debut = empreintes()
    print(f"Sabotages de la recette · version gelée {fr.VERSION}")
    for nom, valeur in debut.items():
        print(f"  {nom:18s} SHA-256 {valeur}")
    print("  contrôle de la livraison contre son manifeste : " + ("conforme" if not fr.verifier_livraison(LIVRAISON) else "ÉCART"))
    print()
    resultats = []
    for s in SABOTAGES:
        print(f"{s['id']} · test visé {s['test']} · protège : {s['protege']}")
        print(f"  régression introduite dans une copie : {s['regression']}")
        copie = Path(tempfile.mkdtemp(prefix="sabotage-")) / "livraison"
        try:
            shutil.copytree(LIVRAISON, copie, ignore=shutil.ignore_patterns("__pycache__"))
            appliquer(copie, s["patches"])
            code, sortie = lancer([s["test"]], copie)
            echec_vise = code != 0 and (bilan(sortie) or (0, 0, 0, 0))[2:] != (0, 0)
            print(f"  test visé sur la copie : {'ÉCHEC, comme attendu' if echec_vise else 'RESTE VERT : test invalide'}"
                  + (f" · {premiere_exception(sortie)}" if echec_vise else ""))
            code_tous, sortie_tous = lancer([], copie)
            echoues = tests_en_echec(sortie_tous)
            b = bilan(sortie_tous)
            print(f"  suite entière sur la copie : {len(echoues)} test(s) en échec sur {b[0] if b else '?'} : {', '.join(echoues) or 'aucun'}")
        finally:
            shutil.rmtree(copie.parent, ignore_errors=True)
        fin = empreintes()
        intacte = fin == debut and not fr.verifier_livraison(LIVRAISON)
        code2, sortie2 = lancer([s["test"]], None)
        b2 = bilan(sortie2)
        vert = code2 == 0 and b2 is not None and b2[2:] == (0, 0)
        print(f"  copie jetée ; version gelée inchangée (empreintes et manifeste) : {'oui' if intacte else 'NON'}")
        print(f"  test visé relancé sur la version gelée : {'réussi' if vert else 'ÉCHOUÉ'}")
        resultats.append((s["id"], s["test"], bool(echec_vise), intacte, vert))
        print()
    n = len(resultats)
    echecs = sum(1 for r in resultats if r[2])
    retablis = sum(1 for r in resultats if r[3])
    verts = sum(1 for r in resultats if r[4])
    print(f"BILAN : {n} sabotages · {echecs} échecs constatés · {retablis} rétablissements vérifiés · {verts} re-tests réussis")
    return 0 if echecs == n and retablis == n and verts == n else 1


if __name__ == "__main__":
    sys.exit(main())
