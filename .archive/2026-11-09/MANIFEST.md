# Archive du 2026-11-09 : construire-solution et tester-solution

Décision du mainteneur, 09/11/2026 : le pack Conseil IA ne fait que le conseil.

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

## Ajout du 2026-11-09 (soir) : piloter-mise-en-service

Décision du mainteneur, 09/11/2026, définitive : la mise en service quitte le pack Conseil IA comme `construire-solution`
et `tester-solution` (le conseil ne construit rien et n'agit pas dans les outils réels ; il planifie, évalue et mesure).

### Provenance
- `piloter-mise-en-service/` : ancien `skills/piloter-mise-en-service/` (SKILL.md, references/actions-types.md,
  references/modeles.md), déplacé par `git mv`, contenu inchangé (la ligne « rejoint le pack » en tête du SKILL.md y reste).

### Nouvelle maison
Pack « Créer un agent IA » : compétence globale `piloter-mise-en-service` (plugin `creer-un-agent-ia`, workflow du site
`creer-un-agent-ia`, étape Mettre en service). Contrat inchangé : elle lit `60-specification.md`, `70-plan.md`,
`80-construction.md` et `85-recette.md`, écrit `90-mise-en-service.md` ; `mesurer-gains` (95) se rouvre ici quand 90 est
validé au journal. `deployer-assistant-ia` reste ici : il prépare le dossier que la mise en service reprend.

### Restaurer
`git mv .archive/2026-11-09/piloter-mise-en-service skills/piloter-mise-en-service`, remettre la ligne « Mettre en
service » dans la table de `ARCHITECTURE.md`, les renvois d'origine dans les `SKILL.md` du pack, et retirer
`piloter-mise-en-service` de `AU_PACK_CREER_UN_AGENT` dans `scripts/verifier_pack.py`.
