# Compétences complémentaires — concevoir l'architecture d'un système IA, puis fabriquer ses compétences, ses agents et sa mémoire

Le pack ne contient que ses propres compétences. Quand l'option retenue en `40-solutions` est un système (des
agents, une mémoire, des intégrations) ou comprend un site, des compétences d'autres auteurs aident à en
dessiner l'architecture (étape `concevoir-solution`), puis à en fabriquer les pièces en environnement d'essai :
une compétence, un agent, une mémoire (étape `construire-solution`). Elles sont citées ici avec leur auteur,
leur licence, la version lue et leur commande d'installation. Elles sont **facultatives** et ne sont jamais
copiées dans le pack : sans elles, chaque étape suit sa méthode maison et le parcours ne change pas.

Les compagnons de `COMPAGNONS.md` vont plus loin sur une plateforme ou un outil précis (n8n, Make, un agent
écrit en Python). Celles-ci servent quelle que soit la plateforme : elles dessinent le système, puis aident à
fabriquer ses pièces.

Lecture du 16 octobre 2026, à la source : dépôt d'origine, licence, noms de la place de marché et du plugin lus
dans son `marketplace.json` (pour BMad, la commande de son README), description du `SKILL.md` au commit indiqué
dans le lien. Aucune n'a été essayée sur une mission : ce sont des notes de lecture, comme celles de
`COMPAGNONS.md`. Avant d'installer, relire la version du jour.

| Étape | Compétence | À quoi elle sert dans une mission | Installation | Auteur · licence |
|---|---|---|---|---|
| `concevoir-solution` | [`system-design`](https://github.com/anthropics/knowledge-work-plugins/blob/33eeda1e8fd856455b05479d13a0f85b5f803744/engineering/skills/system-design/SKILL.md) (plugin `engineering`) | Dessiner l'architecture de l'option retenue quand c'est un système : composants, flux de données, contrats entre les pièces, limites de charge, compromis. Cadre de conception général, pas propre à l'IA : les points de validation humaine, les droits de l'agent et sa mémoire restent à poser dans `40-solutions` | `/plugin marketplace add anthropics/knowledge-work-plugins`<br>`/plugin install engineering@knowledge-work-plugins` | Anthropic · Apache-2.0 |
| `concevoir-solution` | [`architecture`](https://github.com/anthropics/knowledge-work-plugins/blob/33eeda1e8fd856455b05479d13a0f85b5f803744/engineering/skills/architecture/SKILL.md) (plugin `engineering`) | Consigner un choix structurant de l'option retenue en une fiche de décision (contexte, options, conséquences), ou relire une proposition d'architecture. Une fiche par choix, par exemple où vit la mémoire d'un agent ; la comparaison des options reste dans `40-solutions` | `/plugin marketplace add anthropics/knowledge-work-plugins`<br>`/plugin install engineering@knowledge-work-plugins` | Anthropic · Apache-2.0 |
| `concevoir-solution` | [`bmad-architecture`](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/src/bmm-skills/plan/bmad-architecture/SKILL.md) (méthode BMad) | Rédiger avec le décideur le court document qui fixe ce qui doit rester cohérent quand plusieurs pièces sont construites séparément (paradigme, frontières, propriétaire des données) ; elle questionne avant de rédiger. À prendre quand plusieurs agents ou plusieurs équipes construiront la solution | `npx bmad-method install` | BMad Code, LLC · MIT |
| `concevoir-solution` | [`bmad-agent-architect`](https://github.com/bmad-code-org/BMAD-METHOD/blob/bab9082c3e884e0d72c759bcd1a6d90bcc01be84/src/bmm-skills/agents/bmad-agent-architect/SKILL.md) (méthode BMad) | Un interlocuteur « architecte » (Winston) pour discuter l'architecture et ses compromis avant d'écrire ; il lance `bmad-architecture` au besoin. Persona pensée pour le logiciel, pas pour l'IA en particulier | `npx bmad-method install` | BMad Code, LLC · MIT |
| `concevoir-solution` | [`site-architecture`](https://github.com/coreyhaines31/marketingskills/blob/365b412152b9542499ca1439426f7fc3cc92bb65/skills/site-architecture/SKILL.md) (plugin `marketing-skills`) | Planifier l'arborescence d'un site : pages, navigation, adresses, maillage interne. Seulement quand la solution comprend un site | `/plugin marketplace add coreyhaines31/marketingskills`<br>`/plugin install marketing-skills@marketingskills` | Corey Haines · MIT |
| `construire-solution` | [`skill-creator`](https://github.com/anthropics/claude-plugins-official/blob/ea10b213686c90bb1984b2016937310e05336cf3/plugins/skill-creator/skills/skill-creator/SKILL.md) (plugin `skill-creator`) | Écrire une compétence, la tester sur des cas d'essai, mesurer sa performance et régler sa description de déclenchement. Quand la solution est une compétence ou en contient une ; le résultat se range dans `80-construction/livraison/`, éprouvé sur des données fictives | `/plugin install skill-creator@claude-plugins-official` | Anthropic · Apache-2.0 |
| `construire-solution` | [`agent-development`](https://github.com/anthropics/claude-plugins-official/blob/ea10b213686c90bb1984b2016937310e05336cf3/plugins/plugin-dev/skills/agent-development/SKILL.md) (plugin `plugin-dev`) | Écrire un sous-agent de Claude Code : description, outils, consignes, conditions de déclenchement ; le plugin fournit aussi un agent qui en génère un premier jet. Quand la solution est un agent qui vit dans Claude Code ; pour un agent écrit en Python ou dans n8n, voir `COMPAGNONS.md` | `/plugin install plugin-dev@claude-plugins-official` | Anthropic · Apache-2.0 |
| `construire-solution` | [`memory-management`](https://github.com/anthropics/knowledge-work-plugins/blob/33eeda1e8fd856455b05479d13a0f85b5f803744/productivity/skills/memory-management/SKILL.md) (plugin `productivity`) | Organiser la mémoire d'un assistant en deux niveaux : un fichier court toujours chargé (personnes, sigles, projets actifs) et un dossier détaillé consulté au besoin. Patron pour un assistant qui doit parler le vocabulaire de l'entreprise ; elle ne couvre ni l'historique d'une conversation ni l'état d'un flux. Dans l'essai, avec des noms fictifs | `/plugin marketplace add anthropics/knowledge-work-plugins`<br>`/plugin install productivity@knowledge-work-plugins` | Anthropic · Apache-2.0 |

## Comment les employer

- **Le livrable reste celui de l'étape.** Si l'une d'elles répond à la place de l'étape, son texte entre dans
  `mission/sources/` comme une source datée, l'étape le reprend dans son modèle et le journal le note
  (`router-mission-ia`, étape 3, « Une autre compétence installée a répondu à la place de l'étape »). Une étape
  ne dit s'en être servie que si elle l'a réellement appelée.
- **On fabrique en essai.** Compétence, agent et mémoire se construisent dans l'environnement d'essai, sur des
  données fictives ou anonymisées. Les poser chez le client est une action `A-xx` de `90-mise-en-service`, avec
  son retour arrière, validée par le client (règle 7 d'`ARCHITECTURE.md`).
- **N'installer que ce que la mission utilise.** Un plugin apporte d'autres compétences que celle citée, et
  `engineering` comme `productivity` déclarent des connecteurs (messagerie, agenda, tâches, code) : n'en
  autoriser un que si la mission le demande, en lecture seule et source par source. Avec beaucoup de
  compétences installées, Claude choisit sur les noms (essai du 13 octobre dans `COMPAGNONS.md`) : commencer
  une mission par `/mission-besoin` ou `/mission-decouverte`.

**Ce qu'aucune d'elles ne fait à la place du pack** : choisir l'option, chiffrer, spécifier, recetter, mettre en
service, prouver un gain. Dessiner une architecture n'est pas choisir une option : `40-solutions` compare,
recommande, et le décideur tranche.

## Lectures et réserves

- **Versions lues.** `knowledge-work-plugins` au commit `33eeda1`, `marketingskills` au commit `365b412`,
  `claude-plugins-official` au commit `ea10b21` ; BMad à sa version stable `v6.12.4` (commit `bab9082`).
- **BMad.** Sa branche principale est une préversion de la version 7, annoncée pour le 16 octobre 2026, dont les
  compétences et l'installation changent : le tableau suit la version stable et la commande de son README
  (Node.js 20.12 ou plus, Python 3.10 ou plus, uv). Relire ce README avant d'installer. BMad™ est une marque de
  BMad Code, LLC, que la licence MIT ne couvre pas ; elle est citée pour décrire une compatibilité, sans lien
  officiel.
- **Licences.** Lues dans le dépôt de chaque compétence : Apache-2.0 pour les cinq d'Anthropic, MIT pour les trois
  autres. GitHub affiche « Other » pour BMad parce qu'un avis de marque suit le texte MIT ; son `package.json` et
  son README disent MIT.
- **Lues, pas essayées.** Le tableau décrit ce que disent leurs fichiers, pas ce qu'elles donnent sur une mission.
