# Compétences complémentaires — concevoir l'architecture d'un système IA

Le pack ne contient que ses propres compétences. Quand l'option retenue en `40-solutions` est un système (des
agents, une mémoire, des intégrations) ou comprend un site, des compétences d'autres auteurs aident à en
dessiner l'architecture (étape `concevoir-solution`). La fabrication des pièces (une compétence, un agent, une
mémoire) est au pack Créer un agent IA (`construire-solution`), qui porte ses propres compétences complémentaires
(`skill-creator`, `agent-development`, `memory-management`). Elles sont citées ici avec leur auteur,
leur licence, la version lue et leur commande d'installation. Elles sont **facultatives** et ne sont jamais
copiées dans le pack : sans elles, chaque étape suit sa méthode maison et le parcours ne change pas.

Les compagnons de `COMPAGNONS.md` vont plus loin sur une plateforme ou un outil précis (n8n, Make, un agent
écrit en Python). Celles-ci servent quelle que soit la plateforme : elles dessinent le système.

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

## Comment les employer

- **Le livrable reste celui de l'étape.** Si l'une d'elles répond à la place de l'étape, son texte entre dans
  `mission/sources/` comme une source datée, l'étape le reprend dans son modèle et le journal le note
  (`router-mission-ia`, étape 3, « Une autre compétence installée a répondu à la place de l'étape »). Une étape
  ne dit s'en être servie que si elle l'a réellement appelée.
- **N'installer que ce que la mission utilise.** Un plugin apporte d'autres compétences que celle citée, et
  `engineering` déclare des connecteurs (messagerie, agenda, tâches, code) : n'en
  autoriser un que si la mission le demande, en lecture seule et source par source. Avec beaucoup de
  compétences installées, Claude choisit sur les noms (essai du 13 octobre dans `COMPAGNONS.md`) : commencer
  une mission par `/mission-besoin` ou `/mission-decouverte`.

**Ce qu'aucune d'elles ne fait à la place du pack** : choisir l'option, chiffrer, spécifier, construire, recetter,
mettre en service, prouver un gain. Dessiner une architecture n'est pas choisir une option : `40-solutions` compare,
recommande, et le décideur tranche.

## Lectures et réserves

- **Versions lues.** `knowledge-work-plugins` au commit `33eeda1`, `marketingskills` au commit `365b412` ;
  BMad à sa version stable `v6.12.4` (commit `bab9082`).
- **BMad.** Sa branche principale est une préversion de la version 7, annoncée pour le 16 octobre 2026, dont les
  compétences et l'installation changent : le tableau suit la version stable et la commande de son README
  (Node.js 20.12 ou plus, Python 3.10 ou plus, uv). Relire ce README avant d'installer. BMad™ est une marque de
  BMad Code, LLC, que la licence MIT ne couvre pas ; elle est citée pour décrire une compatibilité, sans lien
  officiel.
- **Licences.** Lues dans le dépôt de chaque compétence : Apache-2.0 pour les deux d'Anthropic, MIT pour les trois
  autres. GitHub affiche « Other » pour BMad parce qu'un avis de marque suit le texte MIT ; son `package.json` et
  son README disent MIT.
- **Lues, pas essayées.** Le tableau décrit ce que disent leurs fichiers, pas ce qu'elles donnent sur une mission.
