# Compagnons — les compétences d'autres auteurs qui vont avec le pack

Le pack ne contient que ses propres compétences. Pour certaines étapes, une compétence publiée par un
éditeur ou un praticien reconnu va plus loin sur une plateforme précise : elle est citée ici, avec le
commit lu, sa licence et la condition où l'appeler. Elle n'est jamais copiée dans le pack, et une étape
ne dit l'avoir utilisée que si elle l'a réellement appelée. Sans compagnon installé, chaque étape suit
sa méthode maison.

Lecture du 12 octobre 2026 : fichiers lus au commit indiqué, notés sur 100 avec une grille de lecture
(adéquation, procédure, vérification, maintenance, portabilité, sécurité, contexte, provenance). Ce
sont des notes de lecture, pas des essais. Avant d'installer un compagnon, relire sa version du jour.

| Étape | Compagnon | Éditeur · licence | Ce qu'il apporte | Quand l'appeler |
|---|---|---|---|---|
| Diagnostiquer | [`process-doc`](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/operations/skills/process-doc/SKILL.md) | Anthropic · Apache-2.0 | rédiger le mode opératoire d'un processus : rôles, exceptions, indicateurs | pour documenter le processus cible après l'audit |
| Stratégie d'automatisation | [`automation-strategy`](https://github.com/ericrisco/rsc-harness/blob/5343ea565c39c00d329793606e8d609da2faa004/skills/automation-strategy/SKILL.md) | Eric Risco · MIT | arbitrer automatiser ou non, acheter ou construire, la plateforme, le coût de maintien | pour approfondir le choix de plateforme ; prix et capacités à revérifier le jour même |
| Concevoir | [`vendor-review`](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/operations/skills/vendor-review/SKILL.md) | Anthropic · Apache-2.0 | comparer des fournisseurs : coût complet, risques, continuité, sortie | quand une option repose sur un logiciel du marché |
| Spécifier | [`write-spec`](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/product-management/skills/write-spec/SKILL.md) | Anthropic · Apache-2.0 | structurer une spécification produit et ses critères d'acceptation | pour une solution qui devient un produit interne suivi |
| Construire (n8n) | [`n8n-workflow-lifecycle-official`](https://github.com/n8n-io/skills/blob/180b8415e3b73f78828cfa01e908e67f89f2a139/skills/n8n-workflow-lifecycle-official/SKILL.md), [`n8n-node-configuration-official`](https://github.com/n8n-io/skills/blob/180b8415e3b73f78828cfa01e908e67f89f2a139/skills/n8n-node-configuration-official/SKILL.md), [`n8n-credentials-and-security-official`](https://github.com/n8n-io/skills/blob/180b8415e3b73f78828cfa01e908e67f89f2a139/skills/n8n-credentials-and-security-official/SKILL.md), [`n8n-agents-official`](https://github.com/n8n-io/skills/blob/180b8415e3b73f78828cfa01e908e67f89f2a139/skills/n8n-agents-official/SKILL.md) | n8n · Apache-2.0 | planifier, câbler, valider et livrer un flux ; lire le vrai schéma des nœuds ; ranger les secrets ; agents dans n8n | quand la plateforme retenue est n8n (instance récente et accès requis) |
| Construire (Make) | [`make-endpoints`](https://github.com/integromat/make-skills/blob/c4f35df44df20ab538dbdf9df524671c336522ab/skills/make-endpoints/SKILL.md) · [`make`](https://github.com/ericrisco/rsc-harness/blob/5343ea565c39c00d329793606e8d609da2faa004/skills/make/SKILL.md) | Make · MIT ; Eric Risco · MIT | découvrir les actions, vérifier les droits, relire après écriture ; conduire des scénarios et réutiliser des modèles | quand la plateforme retenue est Make |
| Construire (agent codé) | [`building-pydantic-ai-agents`](https://github.com/pydantic/skills/blob/585b93fc80c755b88cc23746bb6797c53adc0674/skills/building-pydantic-ai-agents/SKILL.md) | Pydantic · MIT | agents Python avec outils, retours typés et doubles de test | quand la solution est un agent écrit en Python |
| Tester (IA) | [`logfire-evals`](https://github.com/pydantic/skills/blob/585b93fc80c755b88cc23746bb6797c53adc0674/skills/logfire-evals/SKILL.md) · [`creating-online-evaluations`](https://github.com/PostHog/skills/blob/546b1c90f2cee491798f967b2a6fff3f2f75e816/skills/omnibus/creating-online-evaluations/SKILL.md) · [`exploring-llm-evaluations`](https://github.com/PostHog/skills/blob/546b1c90f2cee491798f967b2a6fff3f2f75e816/skills/omnibus/exploring-llm-evaluations/SKILL.md) | Pydantic · MIT ; PostHog · MIT | jeux d'évaluation versionnés, juges calibrés, contrôles continus tirés des échecs réels | quand l'entreprise utilise déjà ces outils d'observation |
| Tester (n8n) | [`n8n-debugging-official`](https://github.com/n8n-io/skills/blob/180b8415e3b73f78828cfa01e908e67f89f2a139/skills/n8n-debugging-official/SKILL.md) · [`n8n-error-handling-official`](https://github.com/n8n-io/skills/blob/180b8415e3b73f78828cfa01e908e67f89f2a139/skills/n8n-error-handling-official/SKILL.md) | n8n · Apache-2.0 | chercher la cause dans les exécutions ; prévoir erreurs, replis et alertes | quand la plateforme retenue est n8n |
| Mettre en service | [`runbook`](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/operations/skills/runbook/SKILL.md) · [`change-request`](https://github.com/anthropics/knowledge-work-plugins/blob/02ffa99ff00ce4d3046ccebabb8357cb39f3ab06/operations/skills/change-request/SKILL.md) | Anthropic · Apache-2.0 | mode opératoire d'exploitation ; demande de changement avec impacts, approbations, formation | pour une entreprise qui a déjà un processus de gestion des changements |
| Mettre en service (Azure) | [`azure-prepare`](https://github.com/microsoft/azure-skills/blob/0727d81638d64b6888f796287ee00baecfb08ced/skills/azure-prepare/SKILL.md) · [`azure-deploy`](https://github.com/microsoft/azure-skills/blob/0727d81638d64b6888f796287ee00baecfb08ced/skills/azure-deploy/SKILL.md) | Microsoft · MIT | préparer puis déployer avec l'outil en ligne de commande d'Azure | seulement si l'entreprise déploie sur Azure avec cet outil |
| Mesurer | [`exploring-ai-failures`](https://github.com/PostHog/skills/blob/546b1c90f2cee491798f967b2a6fff3f2f75e816/skills/omnibus/exploring-ai-failures/SKILL.md) · [`querying-posthog-data`](https://github.com/PostHog/skills/blob/546b1c90f2cee491798f967b2a6fff3f2f75e816/skills/omnibus/querying-posthog-data/SKILL.md) · [`llm-analytics-setup`](https://github.com/PostHog/skills/blob/546b1c90f2cee491798f967b2a6fff3f2f75e816/skills/posthog/all/skills/llm-analytics-setup/SKILL.md) | PostHog · MIT | repérer les échecs silencieux dans les traces ; calculer usages et métriques ; coûts et latences des appels d'IA | quand l'entreprise utilise PostHog |
| Mesurer | [`logfire-instrumentation`](https://github.com/pydantic/skills/blob/585b93fc80c755b88cc23746bb6797c53adc0674/skills/logfire-instrumentation/SKILL.md) · [`logfire-query`](https://github.com/pydantic/skills/blob/585b93fc80c755b88cc23746bb6797c53adc0674/skills/logfire-query/SKILL.md) | Pydantic · MIT | instrumenter un agent ; lire erreurs, coûts, durées et tendances | quand l'entreprise utilise Logfire |

**Ce qu'aucun compagnon ne fait à la place du pack** : diagnostiquer le travail réel, arbitrer
l'économie, choisir entre les plateformes, décider de la mise en service et prouver le gain métier. Les
traces techniques d'un outil d'observation sont une source de mesure, jamais à elles seules la preuve
d'un gain.

**Modèles prêts à l'emploi** : avant de construire, chercher dans les bibliothèques de modèles des
éditeurs (https://n8n.io/workflows/, https://www.make.com/en/templates). Un modèle peut venir d'un
membre de la communauté : vérifier son auteur, ses autorisations et ses coûts avant de l'importer.

## Quand deux compétences se disputent une demande

Plusieurs compétences installées peuvent répondre à la même demande : un runbook, une spécification, un
mode opératoire génériques existent aussi chez d'autres éditeurs. Dans une mission, l'étape du pack
possède le livrable. Un compagnon n'est appelé que par l'étape, dans la condition écrite ci-dessus ; si
une autre compétence a répondu à sa place, son texte devient une source de l'étape, rangée dans
`mission/sources/`, et l'étape le reprend dans son modèle (`router-mission-ia`, étape 3). Hors d'une
mission, le pack n'a pas à prendre la demande.

Essai du 13 octobre 2026, dans une session chargée de 151 compétences (le pack, les plugins `operations`
et `product-management` d'Anthropic et une centaine d'autres), deux tirages par demande. Pour quatre
demandes de mission, le pack a répondu 4 fois sur 8, un plugin tiers 1 fois (« documenter le processus
actuel »), aucune compétence 3 fois. Pour deux demandes hors mission, le pack n'a jamais répondu. Avec
autant de compétences, Claude ne voit plus leurs descriptions et choisit sur leurs noms. Pour qu'une
mission passe à coup sûr par le pack, la commencer par `/mission-besoin` ou `/mission-decouverte`, puis
la reprendre par « où en est la mission ? ». Deux tirages et un seul modèle : un ordre de grandeur, pas
une statistique.

## Idées reprises d'outils non lus

- **Clara**, plugin pour consultants de Fabio Annovazzi (Mparanza), au catalogue des plugins Codex
  (version 0.1.235 au 13 octobre 2026) et sur GitHub sous licence AGPL-3.0
  (https://github.com/fabioannovazzi/app_files/tree/main/plugins/clara). Ni lu ni installé à ce jour :
  seule sa description publique a servi. L'idée de valider un livrable contre la demande et les preuves
  avant de le remettre est réécrite dans la règle commune 8 d'`ARCHITECTURE.md`.
