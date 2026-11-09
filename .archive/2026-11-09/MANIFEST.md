# Archive du 2026-11-09 : construire-solution et tester-solution

Décision de Florent, 09/11/2026 : le pack Conseil IA ne fait que le conseil.

## Provenance
- `construire-solution/` : ancien `skills/construire-solution/` (SKILL.md, references/garde-fous.md, references/modeles.md).
- `tester-solution/` : ancien `skills/tester-solution/` (SKILL.md, references/evaluation-ia.md, methodes-de-test.md, modeles.md).
- `complementaires-construire-solution.md` : les 3 lignes « construire-solution » du tableau de `COMPLEMENTAIRES.md`
  (`skill-creator`, `agent-development`, `memory-management`), retirées du pack ; elles suivent `construire-solution`.

## Nouvelle maison
Pack « Créer un agent IA » : compétences globales `construire-solution` et `tester-solution` (sans préfixe
`consultant-ia:`), copiées aussi dans le plugin `creer-un-agent-ia` ; workflow du site `creer-un-agent-ia`, étapes
Construire et Tester. Contrat inchangé : elles lisent `60-specification.md` et `70-plan.md` du dossier de mission et
écrivent `80-construction.md` et `85-recette.md` ; le pack conseil reprend à `95-mesure.md` (`mesurer-gains`).

## Restaurer
`git mv .archive/2026-11-09/construire-solution skills/construire-solution` (idem `tester-solution`), remettre les
3 lignes de `complementaires-construire-solution.md` dans `COMPLEMENTAIRES.md`, et rétablir `construire-solution`
dans `ETAPES_COMPLEMENTAIRES` et la liste de contrôle des noms dépréciés de `scripts/verifier_pack.py`.
