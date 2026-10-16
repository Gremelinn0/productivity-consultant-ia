# Architecture — consultant-ia

Ce fichier est la carte canonique du pack. Si une compétence et cette carte se contredisent, on
corrige l'écart au lieu de documenter deux méthodes.

Le pack porte **la méthode d'une mission de conseil IA et automatisation, de l'idée à la solution
mesurée** : comprendre le travail réel, trouver ce qui mérite d'être automatisé, comparer les
solutions, chiffrer, spécifier et planifier, puis construire et tester dans un environnement d'essai,
mettre en service action par action et mesurer ce que la solution rapporte vraiment. Il ne décide pas
à la place du client, il ne touche aucun outil réel sans la validation de l'action précise (règle 7) et
il ne détient aucune donnée propre à une entreprise : celles-ci vivent dans le dossier de la mission.

## Les trois statuts d'un nombre

Ils sont définis ici, une seule fois. Chaque compétence qui écrit un nombre le rappelle en une ligne
et renvoie à cette définition ; les guides d'entretien aussi.

| Statut | Sens | À écrire à côté |
|---|---|---|
| `[F]` fait | observé, appuyé par une pièce, ou décision ou contrainte énoncée par son détenteur (la source est l'entretien ou la pièce). Une valeur proposée puis acceptée à la validation devient `[F]` | la source : la pièce, l'entretien, ou la ligne du journal qui consigne l'accord |
| `[H]` hypothèse | déclaré de mémoire, supposé, ou paramètre choisi (seuil, jeu d'essai) | le rôle qui peut la confirmer |
| `[E]` estimation | calculée à partir de `[F]` et de `[H]` | le calcul, montré |

Une durée chronométrée sur une seule occurrence est `[F]` pour cette occurrence et `[H]` comme durée
typique. Un nombre sans statut est une erreur, pas un style.

**Un gain n'est un fait qu'en 95.** Un gain observé en `95-mesure`, dont tous les termes sont `[F]` sur
la même période (relevé daté, source, méthode, responsable), est `[F]`. C'est le seul endroit du pack où
un gain devient un fait : l'estimation de `50-rentabilite` reste intacte, le réel s'écrit à côté.

## Deux portes, un seul pipeline

| Porte | Commande | Quand | Ce qu'on obtient |
|---|---|---|---|
| **1 — On part d'un besoin** | `/mission-besoin` | quelqu'un nomme un processus ou une douleur en une phrase (« automatiser la relance des factures », « un agent pour le support ») | besoin cadré → diagnostic → exigences → solutions comparées → rentabilité → spécification → plan → solution construite en essai → recette → mise en service → gain mesuré |
| **2 — On ne part d'aucun besoin** | `/mission-decouverte` | la question est « où l'IA peut-elle nous aider ? » | contexte branché → cartographie des tâches → tri → portefeuille de cas d'usage → ordre de grandeur → feuille de route ; chaque cas retenu entre ensuite par la porte 1 |

**Frontière, décidable** : la personne peut-elle nommer le processus concerné en une phrase ?
Oui → porte 1. Non → porte 2. En cas de doute, la porte 2 commence par une découverte courte et
rend la main dès qu'un cas clair apparaît.

```text
PORTE 2 — aucun besoin
  decouvrir-cas-usage ................................. 00-contexte · 01-cartographie-taches · 02-portefeuille
  chiffrer-rentabilite (ordre de grandeur) ............ 03-chiffrage
  planifier-deploiement (feuille de route) ............ 04-feuille-de-route
        │ chaque cas retenu entre par cadrer-besoin
        ▼
PORTE 1 — besoin connu
  DÉCIDER
  cadrer-besoin ....................................... 10-besoin
  auditer-processus ................................... 20-diagnostic
  rediger-cahier-des-charges (exigences) .............. 30-exigences
  concevoir-solution (stratégie d'automatisation) ..... 40-solutions
  chiffrer-rentabilite (business case) ................ 50-rentabilite
  rediger-cahier-des-charges (spécification) .......... 60-specification
  planifier-deploiement (plan + pré-mortem) ........... 70-plan
  CONSTRUIRE ET ÉPROUVER — environnement d'essai, données fictives ou anonymisées
  construire-solution ................................. 80-construction
  tester-solution ..................................... 85-recette
  METTRE EN SERVICE ET MESURER — outils réels, action par action
  piloter-mise-en-service ............................. 90-mise-en-service
  mesurer-gains ....................................... 95-mesure

Cerveau des décisions, appelé là où une étape décide : router-consulting-strategy
```

Un lot fait seulement de simplifications (`40-solutions` ne retient que l'option 0, rien à construire)
passe de `70-plan` à `90-mise-en-service` sans 80 ni 85 : le registre de 90 ne porte alors que les
actions sur les outils que ces simplifications modifient. L'ordre exact et les conditions d'ouverture
de chaque étape sont dans `router-mission-ia`.

## Les douze compétences

| Rôle | Compétence | Responsabilité unique |
|---|---|---|
| Porte | `router-mission-ia` | affiche l'état de la mission, choisit la porte, lance l'étape suivante, tient le journal des décisions |
| Découvrir | `decouvrir-cas-usage` | brancher le contexte, cartographier les tâches, les trier en cinq issues, rendre un portefeuille de cas classés |
| Cadrer | `cadrer-besoin` | reformuler le besoin, vérifier que c'est le bon problème, fixer périmètre, contraintes et critères de succès, nommer le dossier du cas |
| Auditer | `auditer-processus` | décrire le processus actuel, le mesurer, trouver les goulets et leurs causes, simplifier avant d'automatiser |
| Spécifier | `rediger-cahier-des-charges` | mode **exigences** (avant le choix, sans solution) et mode **spécification** (PRD de la solution retenue, indicateurs et seuils compris) |
| Concevoir | `concevoir-solution` | la stratégie d'automatisation (faire ou non, quel type de solution, quelle plateforme), de vraies options dont ne rien construire, une recommandation, une porte quand il faut standardiser avant de construire |
| Chiffrer | `chiffrer-rentabilite` | ordre de grandeur d'un portefeuille ou business case d'une option, hypothèses visibles, scénarios |
| Planifier | `planifier-deploiement` | feuille de route d'un portefeuille (avec son socle commun) ou plan de déploiement d'un cas : simplifications, porte, pilote, adoption, rythme des revues d'indicateurs, pré-mortem |
| Construire | `construire-solution` | construire par tranches contrôlables dans un environnement d'essai, sur des données fictives ou anonymisées, avec les garde-fous de la spécification ; rendre une version gelée et sa fiche d'exploitation |
| Tester | `tester-solution` | la recette de chaque critère d'acceptation (preuves, sabotage), l'évaluation de l'IA à part, un verdict : « prêt », « prêt avec réserves » ou « pas prêt » |
| Mettre en service | `piloter-mise-en-service` | le registre des actions sur les outils réels (chacune validée par le client, avec son retour arrière), le pilote, la bascule, l'adoption, le transfert à un exploitant nommé |
| Mesurer | `mesurer-gains` | lire les relevés réels, les comparer au départ et au business case, déclarer un gain observé, décider : continuer, corriger, étendre ou arrêter |

Aucune compétence ne refait le travail d'une autre ligne. Si une responsabilité a un propriétaire
ci-dessus, on l'appelle. Le dossier `skills/` contient en plus `router-consulting-strategy`, qui arbitre
sans posséder d'étape : voir la section suivante.

## Le cerveau des décisions

`router-consulting-strategy` apporte la discipline de décision : cadrage, options réelles, contre-cas,
conditions d'arrêt, recommandation d'abord. Il ne possède aucune étape ni aucun dossier : chaque étape
garde son livrable et son modèle, l'appelle au moment de décider et n'en recopie pas la méthode. C'est
une copie embarquée, jamais éditée ici : `python scripts/verifier_pack.py` vérifie qu'elle reste
identique à sa source.

| Étape qui décide | Ce qu'elle lui demande | Lentille (nom dans sa table) |
|---|---|---|
| `decouvrir-cas-usage` | classer le portefeuille de cas d'usage | priorisation (prioritization) |
| `concevoir-solution` | la stratégie d'automatisation et le choix de l'option, avec son contre-cas | options stratégiques (strategic options) |
| `chiffrer-rentabilite` | la recommandation et ses conditions d'arrêt | business case |
| `planifier-deploiement` | l'ordre des priorités et le verdict du pré-mortem | priorisation, risques et parades (prioritization, risk & mitigation) |
| `mesurer-gains` | continuer, corriger, étendre ou arrêter | options stratégiques, hypothèses restantes (strategic options, assumption audit) |

Même notation des nombres : son registre `F` / `H` / `E` est celui des statuts `[F]`, `[H]` et `[E]`
définis plus haut. `cadrer-besoin` ne l'appelle que si la demande est elle-même une décision d'affaires
ambiguë (marché, offre, investissement). Une étape ne dit l'avoir appelé que si elle l'a réellement fait.

## Le dossier de mission — l'état vit une seule fois

Tout livrable s'écrit dans `mission/` à la racine du dossier de travail. Le routeur dérive l'état
de ce dossier à chaque appel ; aucun fichier d'état ne déclare « fait ».

```text
mission/
  journal.md                 décisions humaines, datées (qui a tranché quoi), corrections, clôture
  sources/                   ce que l'entreprise fournit : documents, exports, transcriptions, relevés de mesure
  00-contexte.md             porte 2 : fiche entreprise, sources branchées et manquantes
  01-cartographie-taches.md  porte 2 : une ligne par tâche observée, puis le tri
  02-portefeuille.md         porte 2 : cas d'usage classés, décision attendue
  03-chiffrage.md            porte 2 : ordre de grandeur des gains et des coûts par cas
  04-feuille-de-route.md     porte 2 : ordre de mise en œuvre du portefeuille, socle commun compris
  cas-<slug>/                un dossier par besoin traité par la porte 1
    10-besoin.md
    20-diagnostic.md
    30-exigences.md
    40-solutions.md          dont la porte, quand on standardise avant de construire
    50-rentabilite.md
    60-specification.md
    70-plan.md
    80-construction.md       ce qui est construit en essai, écarts avec la spécification, version gelée
    80-construction/         versions, fiche d'exploitation, données d'essai, sorties simulées, livraison
    85-recette.md            preuves, défauts, évaluation de l'IA, verdict pour le pilote
    85-recette/              facultatif : preuves longues et jeu d'évaluation (EV-xx)
    90-mise-en-service.md    registre des actions sur les outils réels, pilote, bascule, adoption, transfert
    95-mesure.md             relevés, gain observé, décision ; une version par revue
```

Un besoin traité seul par la porte 1 n'a que `journal.md` et son dossier `cas-<slug>/`.

## Les règles communes — chaque compétence les applique

1. **Chaque nombre porte son statut** (`[F]`, `[H]` ou `[E]`, définis plus haut).
2. **Estimé n'est pas mesuré.** Un gain reste « estimé » jusqu'à ce qu'on l'observe après la mise en
   service, et seule `95-mesure` le déclare observé. Aucune statistique de marché sans lien vers sa
   source ; sinon c'est une `[H]`.
3. **L'humain tranche à chaque étape.** Chaque livrable finit par « Décision attendue » ; la
   décision prise s'inscrit dans `journal.md`, avec la date et la personne. Le pack propose, il ne
   valide jamais à la place du client ou du consultant.
4. **On observe le travail, jamais les personnes.** La cartographie décrit des tâches, des temps
   et des outils ; elle n'évalue aucun salarié et ne nomme personne sans nécessité.
5. **Supprimer et simplifier avant d'automatiser.** Automatiser une mauvaise habitude la rend
   seulement plus rapide. Une simplification qui change l'organisation (supprimer une étape, clarifier
   une règle) est une décision inscrite au journal ; celle qui modifie un outil est une action `A-xx`
   de `90-mise-en-service`.
6. **Ce qui existe déjà passe avant ce qu'on construit.** Un outil en place, un modèle, une brique
   du marché : on le compare toujours aux options à construire.
7. **Rien ne touche un outil réel sans la validation de l'action précise.** Le pack lit ce qu'on lui
   donne, écrit dans `mission/`, construit et teste dans un environnement d'essai, avec des données
   fictives ou anonymisées. Toute action sur un outil de l'entreprise (importer un flux, écrire dans un
   logiciel, envoyer, publier) est proposée dans 90-mise-en-service avec son retour arrière, et ne se
   fait qu'après la validation de cette action par le client.
8. **Relire chaque livrable avant de le remettre.** Avant la « Décision attendue », la compétence relit
   son livrable contre trois choses. Le besoin (`10-besoin`, ou `00-contexte` pour une découverte) : il
   répond à ce qui est demandé, dans le périmètre. Les preuves : chaque nombre et chaque affirmation qui
   pèse sur la décision renvoie à sa source (`mission/sources/`, un livrable validé) ou à son calcul ;
   sinon il devient une `[H]` ou une question `Q-xx`. Chaque calcul affiché se refait, arrondis compris :
   une égalité qui ne tombe pas juste se corrige. La source se note au moment où le chiffre s'écrit ;
   une source retrouvée après coup se dit « retrouvée après coup », jamais présentée comme l'origine. Les
   livrables déjà validés : une contradiction se corrige par une version datée, jamais en silence. Ce qui
   ne passe pas se corrige avant la remise.

## Les conventions communes

- **Le nom d'un cas.** `cadrer-besoin` fixe le slug une seule fois : deux à quatre mots, sans accent
  (`relances-factures`). Le dossier s'appelle `cas-<slug>` ; le routeur, le journal et tous les
  renvois le reprennent tel quel.
- **Les rôles d'un livrable.** L'en-tête distingue le demandeur, le valideur du livrable et le
  décideur quand ils diffèrent. Quand un seul rôle tient les trois, une seule mention suffit.
- **Les identifiants.** `EF` exigence fonctionnelle, `ENF` non fonctionnelle, `CA` critère
  d'acceptation, `T` test, `R` risque, `IND` indicateur, `Q` question ouverte, `D` défaut trouvé en
  recette, en pilote ou en exploitation (une seule série par cas), `A` action sur un outil réel (registre
  de 90), `EV` cas d'évaluation d'un composant d'IA (jeu de 85). Chaque série est numérotée une fois
  pour tout le cas : `Q-07` désigne la même question de 30 à 95, `D-04` le même défaut, et un numéro
  n'est jamais réutilisé.
- **Actions, incidents et écarts.** Une action `A-xx` passe par cinq états : proposée · validée · faite ·
  annulée (abandonnée avant d'être faite) · revenue en arrière (faite, puis défaite : la ligne garde les
  deux dates). Un incident de production s'écrit en ligne datée ; il prend un `D-xx` si c'est un défaut du
  dispositif, ou renvoie à son `R-xx` si c'est un risque qui s'est réalisé. Un écart de construction n'a
  pas d'identifiant propre : on le désigne par la rubrique de 60 qu'il touche, et s'il demande une
  décision, il ouvre une `Q-xx` à la suite de la série du cas.
- **Corriger un livrable déjà validé.** On ne réécrit pas en silence. Le livrable prend une version
  datée, avec son motif, dans son en-tête (« Version 1.1, précisée le 2026-10-12 : seuil ramené à
  trois jours ouvrés ») et `journal.md` reçoit une ligne « correction ». L'étape qui trouve un trou en
  amont le corrige ainsi, puis en informe le valideur du livrable corrigé.
- **Les renvois.** Un renvoi cite le livrable et le § ; si le livrable a été corrigé, il cite aussi la
  version lue (« 60-specification §13, v1.1 »). Sans version, il vise la version 1.
- **Les seuils.** Un indicateur a un identifiant `IND-xx` ; ses seuils de production vivent à un
  seul endroit, le protocole de la spécification. Les seuils du pilote sont distincts, et dits tels.
- **La plateforme.** `40-solutions` nomme la plateforme ; si elle ne donne que la famille (flux sans
  code, scénario, script, agent), elle dit qui tranche la plateforme avant la construction. Dans ce cas,
  la plateforme arrêtée par `70-plan` et confirmée par le décideur au journal fait foi ; sans elle,
  `construire-solution` attend (question bloquante).
- **L'environnement d'essai.** `construire-solution` le nomme une fois (`essai-<slug>`) ; `tester-solution`
  et `piloter-mise-en-service` reprennent ce nom tel quel. Rien de réel ne peut en partir : la simulation
  y est le mode par défaut.

## Brancher le contexte

Sources lues, dans cet ordre, et toujours nommées dans le livrable :

1. les fichiers déposés dans `mission/sources/` (procédures, exports, organigramme, comptes rendus,
   transcription d'une vidéo où quelqu'un fait la tâche, et, après la mise en service, les relevés de
   mesure que le client dépose) ;
2. les outils déjà connectés à la session (documents, messagerie, CRM…), en lecture seule ;
3. les entretiens : la compétence prépare le guide, la personne répond, la synthèse cite la source ;
4. ce qui manque est écrit comme manquant, jamais supposé.

## Ce que le pack ne fait pas

- Toucher un outil réel sans la validation de l'action précise. Il construit et teste dans un
  environnement d'essai ; l'import en production, l'écriture dans un logiciel de l'entreprise, l'envoi
  et la publication sont des actions du client, proposées une à une avec leur retour arrière.
- Remplacer les entretiens : il les prépare et les synthétise.
- Décider à la place du client : il recommande, avec ce qui ferait changer la recommandation.
- Relever à la place du client : la mesure se lit sur les relevés que l'entreprise fournit. Le pack ne
  pose aucun compteur et ne lit ni ne pose aucun secret.

## Intégrations facultatives

`COMPAGNONS.md` liste les compétences d'autres auteurs qui vont plus loin sur une plateforme ou un outil
précis (flux, scénario, agent codé, évaluation de l'IA, mise en service, mesure), avec leur licence et la
condition où les appeler. Elles ne sont jamais copiées dans le pack. Une étape ne dit s'en être servie
que si elle les a réellement appelées ; sans compagnon, elle suit sa méthode maison.

`COMPLEMENTAIRES.md` liste de la même façon les compétences d'autres auteurs qui aident à concevoir
l'architecture d'un système IA (agents, mémoire, intégrations, site) puis à fabriquer ses compétences, ses
agents et sa mémoire, avec leur auteur, leur licence et leur commande d'installation. Elles sont
facultatives aussi : le livrable reste celui de l'étape (`concevoir-solution` ou `construire-solution`) et
le parcours ne change pas.

## Ce qui reste imparfait

- Pas encore éprouvé sur une mission réelle. La mission fictive (`examples/`) a éprouvé les étapes de
  décision et relevé 94 frictions, corrigées. Elle a ensuite été prolongée jusqu'à la mesure : la
  construction et la recette y sont réelles (une maquette exécutable en bibliothèque standard, 43 tests,
  17 sabotages), la mise en service et la mesure sont simulées (rôles, décisions et relevés inventés,
  calculs réels). Aucune plateforme n'a été touchée, et le constructeur y est aussi le testeur ; chaque
  compétence dit, dans « Preuves restantes », ce qui n'est pas mesuré.
- Un seul essai comparé, qui ne démontre pas d'avantage. Le 13/10/2026, la même mission fictive a été
  menée par une session avec le pack et par une session sans ; un autre modèle les a notées à l'aveugle sur
  une grille de 15 points écrite avant l'essai : 14 contre 12. L'écart est sous le seuil de 3 points fixé
  d'avance. Il tient à des gains mieux qualifiés et à la maintenance comptée dans le coût complet. L'aveugle
  était imparfait : les livrables du pack se nommaient eux-mêmes.
- Dans une session chargée de nombreuses compétences, une demande de mission peut partir vers une autre
  compétence (essai du 13/10, dans `COMPAGNONS.md`) : une mission se commence par `/mission-besoin` ou
  `/mission-decouverte`.
- Les compagnons de `COMPAGNONS.md` et les compétences de `COMPLEMENTAIRES.md` sont lus, pas essayés : leurs
  notes sont des notes de lecture.
- Le chiffrage ne vaut que par ses mesures d'entrée : sans temps mesurés, il reste une fourchette.
  De même, la mesure ne vaut que par les relevés que le client fournit : sans relevé, `95-mesure` reste
  une demande de relevés et aucun gain n'est un fait.
- La découverte dépend de ce que l'entreprise branche et des entretiens ; le pack n'observe pas le
  travail tout seul.
- Ce que l'hôte ne permet pas d'exécuter (instance d'essai inaccessible, code non exécutable) reste
  « prévu » : la version ne peut alors pas être déclarée prête pour la recette.
- L'adoption par les équipes se prépare par rôle dans 90 (formation, approbations, communication) ; ce
  n'est pas un programme complet de conduite du changement.
- La recherche de l'existant (pages des éditeurs, modèles publics) suppose un accès au moment du
  choix ; sans accès, elle s'écrit « non vérifiée » et le pack le dit.
- En français seulement.

## Documentation canonique

1. **Ce fichier** — architecture, contrats, règles et conventions communes.
2. **`router-mission-ia`** — comportement de la porte et état en direct.
3. Chaque compétence — la méthode de sa responsabilité.
4. **README** — présentation et installation.
5. **`COMPAGNONS.md`** — les compétences d'autres auteurs qui vont avec le pack, et leurs licences.
6. **`COMPLEMENTAIRES.md`** — les compétences d'autres auteurs qui aident à concevoir l'architecture d'un
   système IA puis à fabriquer ses compétences, ses agents et sa mémoire, avec leur commande d'installation.
7. `examples/` — une mission fictive déroulée par les deux portes, jamais une source de méthode.
