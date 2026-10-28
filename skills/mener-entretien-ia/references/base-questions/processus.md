# Base de questions : l'automatisation d'un processus

Avant d'automatiser un processus ou d'y confier une étape à l'IA. La partie 1 porte les huit questions
d'`auditer-processus` (étape 9), posées en une seule fois, après avoir cherché la réponse dans le besoin, les
sources et l'observation ; leurs réponses remplissent la rubrique 8 du diagnostic (`20-diagnostic.md`) et sont
l'entrée de `rediger-cahier-des-charges`. Le guide `processus` de `mener-entretien-ia` les pose telles quelles.
Les parties suivantes décrivent le travail réel, le simplifient avant de rien construire (`concevoir-solution`,
option 0) et bornent ce qu'on confie à un agent. La description du travail et ses mesures se prennent d'abord dans
l'outil (`auditer-processus`, étape 2), puis avec les équipes (`decouverte-equipes`) ; la grille de stabilité, le
consultant la remplit lui-même (`auditer-processus/references/modeles.md`, rubrique 5).

## 1. Les huit questions d'automatisation

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| AP01 | Quel événement déclenche le processus, et quel résultat doit-il produire ? | Le déclencheur et le résultat attendu | la personne |
| AP02 | Quelles étapes sont stables et répétitives, lesquelles exigent une décision humaine ? | Ce qui s'automatise, ce qui reste humain | la personne |
| AP03 | Quels systèmes, comptes et droits faut-il lire ou modifier ? | Les accès et les branchements | la personne |
| AP04 | Quel volume, quelle fréquence, quel niveau de criticité ? | Le dimensionnement et le niveau de contrôle | l'outil |
| AP05 | Quelles erreurs sont acceptables, lesquelles doivent bloquer, et qui alerter ? | Les erreurs tolérées, les blocages, les alertes | la personne |
| AP06 | Quelles données sensibles, règles de conformité ou validations humaines doivent encadrer l'IA ? | Les garde-fous de l'IA | la personne |
| AP07 | Quel cas limite doit absolument fonctionner avant de généraliser ? | Le cas d'essai décisif | la personne |
| AP08 | Qui maintiendra automatisations, prompts, modèles et accès après livraison ? | La maintenance | la personne |

## 2. Décrire le travail réel

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| AP09 | Quel est le processus réel : les volumes, les cas fréquents, qui fait quoi aujourd'hui, avec quels outils ? | La solution à construire d'après le processus actuel | l'outil |
| AP10 | Quelles réunions donnent lieu à un compte rendu, sont-elles enregistrées, et pour qui écrit-on les comptes rendus, à partir de quoi ? | Le périmètre d'une automatisation des comptes rendus | la personne |

## 3. Simplifier d'abord

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| AP11 | Que perdrait-on si cette étape disparaissait, et qui en dépend ? | Supprimer l'étape plutôt que l'automatiser | la personne |

## 4. Confier une étape à un agent

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| AP12 | Que doit faire l'agent, et pour qui ? | Le résultat attendu : une automatisation ou un agent | la personne |
| AP13 | Quelles actions l'agent a-t-il le droit de faire, avec quels plafonds, et quand passe-t-il la main ? | Les limites de l'agent | la personne |
| AP14 | Qui traitera les cas que l'agent passe, à l'aise avec quels outils, et quels jours ? | L'interface adaptée à la personne qui reprend | la personne |

## Pièces à demander

- Un accès en lecture à l'outil du processus, sur une période nommée (trois mois par défaut).
- La transcription d'une personne qui fait réellement la tâche, avec son accord.
- La procédure écrite, s'il y en a une.
- Un export des occurrences, quand rien n'est mesuré.
- L'accès à l'outil d'automatisation déjà en place (Make, n8n, Zapier), s'il y en a un.
