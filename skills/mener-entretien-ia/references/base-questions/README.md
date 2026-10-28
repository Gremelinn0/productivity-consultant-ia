# La base de questions

Toutes les questions qu'on pose à une entreprise, rangées par sujet, chacune avec la décision qu'elle sert et
l'endroit où chercher sa réponse avant de la demander. On ne réinvente pas les questions à chaque mission : on les
prend ici, on n'adapte que les mots, et on range ici ce qui manquait. Les guides fixes de `mener-entretien-ia`
(`direction`, `equipes`, `court`, `besoin`, `processus`) sont des blocs de cette base : le script les lit ici, et
une question corrigée ici l'est partout.

## Les sujets

Le nom d'un sujet est le titre de son fichier ; le préfixe ouvre le numéro de chacune de ses questions. Deux
familles, chacune en petits groupes : les étapes d'une mission valent pour toute demande, dans l'ordre où on les
traverse ; ce que veut le client se choisit selon l'objectif de la demande.

### Les étapes d'une mission

#### Premier contact

| Sujet | Préfixe | Quand l'ouvrir |
|---|---|---|
| [Le premier échange avec un prospect](premier-echange.md) | PE | Avant toute mission : une entreprise qui n'a encore rien demandé, ou qui vient de se manifester |

#### Découvrir

| Sujet | Préfixe | Quand l'ouvrir |
|---|---|---|
| [La découverte avec la direction](decouverte-direction.md) | DI | Aucun besoin nommé : où l'IA peut aider, vu par la direction |
| [La découverte avec les équipes](decouverte-equipes.md) | EQ | Aucun besoin nommé : le travail réel des équipes, tâche par tâche |

#### Cadrer

| Sujet | Préfixe | Quand l'ouvrir |
|---|---|---|
| [Le cadrage d'un besoin](cadrage.md) | CA | Toute demande : le résultat attendu, le périmètre, qui décide, le budget, la date, les contraintes |
| [Les outils, les comptes et les accès](outils-et-acces.md) | OA | Toute mission : ce qui est en place, qui paie, quels accès, la confidentialité |

#### Analyser et chiffrer

| Sujet | Préfixe | Quand l'ouvrir |
|---|---|---|
| [L'automatisation d'un processus](processus.md) | AP | Avant d'automatiser un processus ou d'y confier une étape à l'IA |
| [La valeur et la rentabilité](rentabilite.md) | RT | Chiffrer ce que le projet rapporte, et ce qu'il demande aux équipes |

#### Mettre en service et suivre

| Sujet | Préfixe | Quand l'ouvrir |
|---|---|---|
| [L'essai et la mise en service](essai-et-mise-en-service.md) | ES | Avant un essai ou une mise en service : le pré-mortem, le pilote, toucher à ce qui tourne |
| [La transmission et l'adoption](transmission.md) | TR | Faire vivre le dispositif sans le consultant |
| [L'accueil, le suivi et le bilan d'une mission](suivi-de-mission.md) | SM | Une fois la mission signée : la facturation, le suivi, la décision de fin |

### Ce que veut le client

#### Trouver des clients

| Sujet | Préfixe | Quand l'ouvrir |
|---|---|---|
| [Le ciblage, qui viser et comment le repérer](ciblage.md) | CI | Avant toute prospection : les meilleurs clients, la cible, les décideurs, les signaux, les exclusions |
| [La prospection et l'acquisition](prospection.md) | PR | Trouver de nouveaux clients : les canaux, les comptes, les messages, l'essai |

#### Suivre ses contacts et ses ventes

| Sujet | Préfixe | Quand l'ouvrir |
|---|---|---|
| [Le CRM et le suivi commercial](crm.md) | CR | Le CRM et le suivi commercial |
| [L'emailing et les relances automatiques](emailing.md) | EM | Les emails aux contacts et aux clients, les relances après un achat raté |

#### Servir ses clients

| Sujet | Préfixe | Quand l'ouvrir |
|---|---|---|
| [Support client et agent du service client](support-client.md) | SC | Le service client, ou un agent qui répond aux clients |
| [L'accueil des nouveaux clients](accueil-des-clients.md) | AC | Accueillir les nouveaux clients de l'entreprise |

#### Ses données et ses chiffres

| Sujet | Préfixe | Quand l'ouvrir |
|---|---|---|
| [Les données, l'enrichissement et la segmentation](donnees.md) | DO | La qualité des données, l'enrichissement, la segmentation |
| [Le reporting et les indicateurs](reporting.md) | RE | Les indicateurs, les tableaux de bord, un écart à expliquer |

#### Produire du contenu

| Sujet | Préfixe | Quand l'ouvrir |
|---|---|---|
| [Le contenu](contenu.md) | CO | Produire du contenu avec l'IA |

## Se servir de la base

1. **Choisir le sujet de l'objectif** : une demande, un sujet ; deux objectifs, deux entretiens. Sans besoin
   nommé, c'est une découverte : `decouverte-direction`, puis `decouverte-equipes`. Avant toute mission, le premier
   échange (`premier-echange`).
2. **Lire le bloc** : `python skills/mener-entretien-ia/scripts/entretien.py base --sujet <sujet>`. Le cadrage
   s'y ajoute quand le sujet ne pose pas déjà ces questions dans ses mots ; les outils et les accès
   (`outils-et-acces`), quand il faudra brancher quelque chose.
3. **Chercher chaque réponse avant de la demander**, là où « D'abord » le dit : **l'outil** se lit soi-même, en
   lecture seule (`auditer-processus`, étape 2) ; **un document** se demande ; **la personne** se pose. Une
   réponse sûre ne se redemande pas, une réponse incertaine se fait confirmer, une réponse absente se demande.
4. **Préparer le questionnaire** : `entretien.py preparer --base <sujet> --garder XX01,XX02,…` en tire le
   brouillon, douze questions au plus, à valider avant l'entretien (`references/questionnaire-prepare.md`).
5. **Au premier contact, deux questions au plus** : celles qui changent le périmètre, le coût ou les conditions
   de réussite (`cadrer-besoin`, étape 3). Le reste attend l'entretien.
6. **Demander l'occurrence réelle et l'ordre de grandeur** (« la dernière fois… », « combien par semaine ? ») :
   règles communes de `decouvrir-cas-usage/references/guides-entretien.md`.

Un « Retour d'expérience » sous une partie renvoie au cas publié d'un praticien : le lien est la source de la
question, pas une preuve de résultat. Les « Pièces à demander » d'un sujet sont les documents et les accès qui
évitent de poser la question.

## Enrichir la base

Après chaque entretien, audit ou rendez-vous, ce qui a manqué se range ici, dans la même passe. La note d'un
entretien guidé le propose déjà (« Pour la base de questions »).

- **Une question qui a servi** : elle a changé le cadrage, le coût ou la réussite d'une mission.
- **Pas de doublon** : chercher dans toute la base, pas seulement dans le sujet. Une question déjà là se
  reformule à sa place ; elle ne s'ajoute pas une seconde fois.
- **Sans le client** : ni son nom, ni ses outils, ni ses chiffres. La question doit servir ailleurs.
- **Au seul sujet qui convient**, à la bonne partie, avec la décision qu'elle sert et son « D'abord ».
- **Un numéro donné ne change plus** : une question retirée garde le sien, barré.

`entretien.py ajouter --sujet <sujet> --partie <numéro ou titre> --question "…" --decide "…" --dabord "la personne"`
range la question : il refuse celle qui est déjà dans la base (accents, casse et ponctuation mis à part), donne le
numéro suivant et place la ligne à la fin de la partie. Un sujet qui manque s'ouvre avec la question qui le fait
naître : `entretien.py creer-sujet --sujet <nom> --prefixe XX --titre "…" --quand "…" --partie "…" --question "…"
--decide "…" [--groupe "…"]`, qui l'inscrit dans l'index des sujets ci-dessus, à la fin du groupe que nomme
`--groupe` (par défaut le dernier groupe de « Ce que veut le client »). Un groupe qui n'existe pas est refusé, sauf
avec `--creer-groupe`, qui l'ouvre à la fin de cette famille. Finance, ressources humaines, juridique : pas de sujet
tant qu'aucune question n'y a servi ; le cadrage et l'automatisation d'un processus suffisent.

## Ce qui n'est pas dans la base

- **Les grilles que le consultant remplit lui-même**, sans les poser : la stabilité d'un processus
  (`auditer-processus/references/modeles.md`, rubrique 5), la porte d'automatisation et les familles d'options
  (`concevoir-solution/references/criteres-et-options.md`), le plan de transmission (`planifier-deploiement`,
  `70-plan.md`, rubrique 4) et la fiche d'exploitation (`construire-solution`). Les questions à poser pour la
  reprise du dispositif sont dans `transmission`.
- **Les réglages d'un outil**, posés à la personne qui l'installe et non à l'entreprise (`propale-setup`).
- **Les questions d'organisation** (un jour de rendez-vous, un accord de principe) et **les validations propres à
  un client** (« on les retire ? ») : elles vivent dans son dossier.
- **Le questionnaire d'une mission** : il vit dans `mission/sources/`.

## Qui part de la base

Les compétences du pack qui posent ou préparent des questions lisent d'abord le bloc de leur sujet, puis rangent
ici ce qu'elles ajoutent ; chacune le rappelle en tête de son `SKILL.md`.

- `mener-entretien-ia` : le questionnaire préparé, les guides fixes, la note qui propose ce qui manquait, et l'agent en
  ligne, qui y choisit ses questions (douze au plus, jamais en dehors) devant un visiteur sans consultant avant l'entretien.
- `cadrer-besoin` : le cadrage (`cadrage`) et le bloc du sujet de l'objectif.
- `decouvrir-cas-usage` : les entretiens de découverte (`decouverte-direction`, `decouverte-equipes`).
- `auditer-processus` : les questions d'automatisation (`processus`) et celles de l'objectif.
- `concevoir-solution` : simplifier avant de construire, les limites d'un agent (`processus`).
- `chiffrer-rentabilite` : la valeur, le temps libéré, le temps donné (`rentabilite`).
- `planifier-deploiement` : le pré-mortem et le pilote (`essai-et-mise-en-service`), la reprise (`transmission`).
- `rediger-cahier-des-charges` : ce que le cahier des charges ne sait pas encore (`cadrage`, `processus`).

`python skills/mener-entretien-ia/scripts/entretien.py verifier` contrôle la base : un préfixe par sujet, aucune
question en double dans toute la base, une décision et un « D'abord » à chaque ligne, l'index des sujets à jour
(chaque sujet une seule fois, rangé dans un groupe d'une famille), et le rappel en tête de chaque compétence citée
ci-dessus. `scripts/verifier_pack.py` le lance aussi.
