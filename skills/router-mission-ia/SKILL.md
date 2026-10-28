---
name: router-mission-ia
description: >-
  Quand une mission de conseil IA ou d'automatisation commence ou reprend — un besoin à automatiser,
  une entreprise qui demande « où l'IA peut-elle nous aider ? », un audit IA, une stratégie
  d'automatisation à bâtir, ou « où en est la mission ? » — → afficher l'état du dossier de mission,
  choisir la porte (besoin connu ou découverte), lancer l'étape suivante du pack consultant-ia, de la
  découverte jusqu'à la mesure du gain, et tenir le journal des décisions. Porte d'entrée du pack.
  Triggers : « mission IA », « audit IA », « on veut automatiser », « par où commencer avec l'IA »,
  « trouver nos cas d'usage », « stratégie d'automatisation », « où en est la mission », « AI
  consulting », « automation strategy », « use case discovery », « /mission-besoin »,
  « /mission-decouverte ».
metadata:
  scope: "une mission de conseil IA et automatisation dans une entreprise, de la première question à la solution mesurée"
  owns: "l'état de la mission dérivé du dossier mission/, le choix de la porte, l'ordre des étapes et leurs conditions d'ouverture, le journal des décisions, de leurs corrections et de la clôture"
  consumes: "le dossier mission/ du répertoire de travail ; les onze compétences d'étape du pack ; ARCHITECTURE.md"
---

# Mission IA — la porte du pack

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Ne produit aucun livrable métier : elle affiche l'état, choisit
> l'étape et écrit `mission/journal.md`. Preuve : l'état affiché correspond aux fichiers présents
> dans `mission/` (aucune ligne n'est recopiée d'un fichier d'état). Contrôle : la mission fictive
> de `examples/` se reprend depuis son seul dossier, et le bloc d'état de son README se recalcule à
> l'identique. **Boucle** : aucune.

## Ce que cette compétence résout

Une mission de conseil IA se perd de deux façons : on part sur une solution avant d'avoir compris le
travail réel, ou on accumule des documents sans savoir lequel décide quoi. Cette porte tient l'ordre
des étapes, montre à chaque reprise où en est la mission et ce qui attend une décision, et lance la
bonne compétence. Les onze compétences d'étape font le travail ; elle ne refait celui d'aucune.

## Stratégie

1. **L'état d'abord, toujours calculé.** Avant toute réponse, même pour « rien à faire », afficher
   l'état dérivé du dossier `mission/`. Un fichier qui déclarerait « étape faite » mentirait le jour
   où quelqu'un modifie le dossier à la main ; les fichiers présents, eux, ne mentent pas.
2. **Une porte se choisit sur un test simple.** La personne peut-elle nommer le processus concerné en
   une phrase ? Oui → porte 1, « besoin connu ». Non → porte 2, « découverte ». En cas de doute, la
   porte 2 commence court et rend la main dès qu'un cas clair apparaît.
3. **L'ordre protège la décision.** On ne compare pas des solutions avant d'avoir des exigences, on ne
   chiffre pas une option qu'on n'a pas décrite, on ne planifie pas ce qu'on n'a pas décidé de faire, on
   ne met pas en service ce qui n'a pas été recetté et on ne déclare pas un gain avant de l'avoir mesuré.
   Sauter une étape reste possible quand l'utilisateur le demande ; on écrit alors dans le journal ce
   qui a été sauté et pourquoi.
4. **Chaque étape finit par une décision humaine.** La compétence d'étape propose ; la personne
   tranche ; la porte inscrit la décision au journal. Le pack ne valide jamais à la place du client.
5. **Un cas porte un seul nom, fixé une fois.** `cadrer-besoin` choisit le slug du dossier ; la porte, le
   journal et les renvois le reprennent tel quel. Deux noms pour un cas font deux dossiers et un état faux.
6. **Rien ne touche un outil réel sans la validation de l'action précise** (règle 7,
   `ARCHITECTURE.md`). Cette porte n'écrit que `mission/journal.md` : construire et tester se fait en
   essai, et chaque action sur un outil de l'entreprise passe par `piloter-mise-en-service`.

## Étapes

### 1. Afficher l'état

Lire `mission/` (le créer avec `journal.md` et `sources/` s'il n'existe pas), puis afficher :

```text
Mission           <nom du dossier de travail>          porte(s) : découverte · besoin connu
Découverte        00 ✓  01 ✓  02 ✓  03 ✓  04 ✓         décision en attente : aucune
cas-relances-factures  10 ✓  20 ✓  30 —  40 —  50 —  60 —  70 —  80 —  85 —  90 —  95 —
À lancer          Tri des tickets entrants · Statut de commande
Dernière décision 2026-10-14 · cas-relances-factures · 20-diagnostic validé
Questions ouvertes  2 Q-xx sans réponse inscrite au journal
Entretiens        questionnaire-relances-factures-2026-10-12 · note reçue
Étape suivante    rediger-cahier-des-charges (exigences) pour cas-relances-factures
```

Chaque ligne se calcule à la lecture :
- `✓` = le fichier existe ; `—` = il manque ; `80` et `85` affichent « sans objet » quand
  `40-solutions.md` ne retient que l'option 0 (rien à construire) ;
- « étape suivante » = le premier fichier manquant dans l'ordre de la porte (10 à 70, puis 80, 85, 90, 95),
  pour le cas le plus récemment modifié, sous les conditions d'ouverture ci-dessous ; « 95-mesure, revue du
  <date> » quand la décision de `95-mesure.md` est « corriger » (le cas reste ouvert), la date étant celle de la
  revue suivante inscrite au journal ; « clore le cas <slug> » dès que le journal consigne la décision de
  `95-mesure.md` en régime établi, une décision d'arrêt ou le renoncement du client aux relevés ; quand tous
  les cas retenus sont clos ou écartés : « clore la mission » ;
- « décision en attente » = un livrable, ou une pièce annexe (fiche d'exploitation, fiche de montage), existe
  mais aucune ligne de `journal.md` ne valide sa dernière version ou révision ; pour `90` et `95`, qui se
  tiennent à jour, c'est la décision que leur dernière version attend (validation d'actions, feu vert, fin
  du pilote, bascule, transmission, revue de mesure) ;
- « à lancer » = les cas que la validation de `02-portefeuille.md` retient (« on creuse : … ») et qui n'ont
  pas encore de dossier `cas-<slug>/` ; un cas mis en attente ou écarté n'y figure pas ;
- « entretiens » = chaque questionnaire préparé de `mission/sources/` (`questionnaire-<objet>-<date>.md`), suivi
  de « note reçue » quand une note `entretien-…` le cite, sinon « en attente ». Un questionnaire en attente
  pour un cas sans `10-besoin.md` fait de l'étape suivante « recevoir l'entretien, puis cadrer-besoin » ;
- « questions ouvertes » = le nombre de `Q-xx` du cas (les identifiants cités dans ses livrables, de 10 à 95 ;
  ceux de la découverte, s'il n'y a pas de cas) sans réponse inscrite au journal : une `Q-xx` est répondue
  quand une ligne du journal la cite avec « répondue ». Le compte ne demande aucun jugement ; ni légende ni
  rappel de définition ;
- un dossier `mission/` vide affiche « aucune mission en cours » et pose la question de la porte.

**Conditions d'ouverture de 80 à 95**, lues au journal et aux livrables, jamais déclarées dans un fichier
d'état :

- `80` : `70-plan.md` validé et la porte de `40-solutions.md` §10 constatée au journal ou « sans objet » ;
  sinon l'étape suivante est « constater la porte » (étape de `70-plan.md`, rubrique 3) ;
- `85` : `80-construction.md` déclaré « prêt pour la recette » au journal ;
- `90` : un verdict de `85-recette.md` « prêt » ou « prêt avec réserves », prononcé et validé au journal. Un
  « pas prêt » renvoie à `construire-solution` ; s'il remet l'option en cause, une ligne du journal renvoie à
  `concevoir-solution` et le routeur rouvre 40. Un verdict relu « pas prêt pour la version en service »
  (défaut bloquant trouvé après le feu vert) ne ferme pas 90 : seules les mesures d'attente y restent ouvertes ;
- `95` : la bascule inscrite au journal. La première version est la demande de relevés ; ensuite, une
  version par revue de la période de mesure ;
- option 0 seule, ou simplification qui modifie un outil : un lot fait seulement de simplifications passe de
  `70-plan.md` à `90-mise-en-service.md`, sans 80 ni 85 ; le registre de 90 ne porte alors que les actions
  sur les outils réels que ces simplifications demandent.

### 2. Choisir la porte

- `/mission-besoin <besoin>` ou une demande qui nomme un processus → porte 1, à partir de
  `cadrer-besoin`, qui fixe le slug et ouvre `mission/cas-<slug>/`. L'objectif nommé, l'entretien qui le
  précise se prépare avant la fiche : les questions qui manquent pour cet objectif, après lecture de tout ce qui
  est accessible (`cadrer-besoin`, étape 3). Le consultant le mène en direct, ou une IA par écrit, en ligne ou
  dans la session de l'entreprise (`mener-entretien-ia`) ; sa note entre dans `mission/sources/`.
- `/mission-decouverte` ou « où l'IA peut-elle nous aider ? » → porte 2, à partir de
  `decouvrir-cas-usage`.
- Une mission qui reprend → l'étape suivante affichée, sans reposer la question. Un cas « à lancer »
  repart par `cadrer-besoin`, avec sa fiche de `02-portefeuille.md`.

### 3. Lancer l'étape suivante

| Porte | Ordre des étapes | Livrable |
|---|---|---|
| 2 — découverte | `decouvrir-cas-usage` | 00-contexte, 01-cartographie-taches, 02-portefeuille |
| | `chiffrer-rentabilite` (ordre de grandeur) | 03-chiffrage |
| | `planifier-deploiement` (feuille de route) | 04-feuille-de-route |
| | chaque cas retenu → porte 1 | `cas-<slug>/` |
| 1 — besoin connu | l'entretien de l'objectif (`cadrer-besoin` étape 3 ; `mener-entretien-ia` s'il est écrit) | sources : questionnaire, note d'entretien |
| | `cadrer-besoin` | 10-besoin |
| | `auditer-processus` | 20-diagnostic |
| | `rediger-cahier-des-charges` (exigences) | 30-exigences |
| | `concevoir-solution` | 40-solutions |
| | `chiffrer-rentabilite` (business case) | 50-rentabilite |
| | `rediger-cahier-des-charges` (spécification) | 60-specification |
| | `planifier-deploiement` (plan + pré-mortem) | 70-plan |
| | `construire-solution` (en essai) | 80-construction |
| | `tester-solution` (recette) | 85-recette |
| | `piloter-mise-en-service` | 90-mise-en-service |
| | `mesurer-gains` | 95-mesure |

Appeler la compétence de l'étape par son nom, avec le chemin du dossier du cas. Quand la porte 2
lance un cas, `cadrer-besoin` reçoit la fiche du cas dans `02-portefeuille.md` pour ne pas reposer
les questions déjà répondues. Un défaut ou une décision de `90` ou `95` (corriger, étendre, arrêter)
renvoie à l'étape qui le traite : `construire-solution` puis `tester-solution` pour une correction,
`piloter-mise-en-service` pour toute action sur un outil, `chiffrer-rentabilite` pour une extension.

**Une autre compétence installée a répondu à la place de l'étape** (un runbook, une spécification, un mode
opératoire génériques venus d'un autre plugin) : dans une mission, le livrable reste celui de l'étape. Le
texte produit entre dans `mission/sources/` comme une source datée, l'étape le reprend dans son modèle et le
journal le note. Un compagnon (`COMPAGNONS.md`) n'est appelé que par l'étape, dans la condition écrite pour lui.

### 4. Tenir le journal

Une ligne par décision, datée. Le cas s'écrit `découverte` pour les livrables 00 à 04 et
`cas-<slug>` pour 10 à 95. Trois formes :

```markdown
- 2026-10-14 · cas-relances-factures · 20-diagnostic validé par la direction financière · « on standardise le modèle de relance avant d'automatiser »
- 2026-10-21 · cas-relances-factures · 30-exigences corrigées (version 1.1 : EF-01 précisée) · confirmées par la direction financière · « une facture écartée une semaine revient la suivante »
- 2026-11-03 · cas-relances-factures · porte constatée par la direction financière · « trois lundis conformes ; fiche de porte jointe »
```

- **Un livrable validé** : date, cas, livrable, décision, rôle de qui a tranché, et sa phrase si elle éclaire
  la suite. Avant de l'inscrire, la relecture de la règle commune 8 (`ARCHITECTURE.md`) a eu lieu : un
  livrable dont un nombre ou une affirmation décisive n'a ni source ni calcul retourne à son étape.
- **Une correction** : quand une étape trouve un trou dans un livrable déjà validé, elle le corrige par une
  version datée (voir `ARCHITECTURE.md`) ; la ligne dit la version et le motif, et qui la confirme. Une pièce
  annexe d'un livrable (fiche d'exploitation, fiche de montage) suit la même forme, avec « révision n » à la
  place de « version » ; sa validation attend comme celle d'un livrable.
- **Une décision sans livrable** : porte constatée, construction prête pour la recette, verdict de la recette
  prononcé ou relu, réponse à une question (« Q-xx répondue », une ligne par réponse ou par lot du même
  répondant), validation d'actions `A-xx` (une ligne par validation, avec les identifiants), feu vert du pilote,
  fin de pilote, bascule, retour arrière d'une action, transmission acceptée, décision de la mesure. La ligne
  cite la pièce qui la prouve (fiche de porte, relevé du pilote, sauvegarde, message du valideur).
- **Une étape sautée** : « 30-exigences sauté à la demande de … : besoin déjà spécifié par l'éditeur ».

### 5. Clore

Un cas se clôt après la mesure, pas à la validation du plan : quand le journal consigne la décision de
`95-mesure.md` en régime établi (continuer, étendre, arrêter ; « corriger » laisse le cas ouvert jusqu'à la
revue suivante), ou plus tôt sur une décision d'arrêt écrite du client, ou quand il renonce aux relevés (le
gain reste alors estimé, rien n'est `[F]`). Dans `journal.md`, section « Clôture », écrire un bloc pour le
cas : les décisions du journal en cinq lignes au plus, les hypothèses `[H]` les plus lourdes (celles dont
dépend le gain, sans les compter), le gain observé `[F]` et le gain encore estimé `[E]`, chacun avec sa
période, et les relevés à poursuivre (qui, quand). Pour une découverte sans cas lancé, c'est `04-feuille-de-route.md`
validée qui clôt. Quand tous les cas retenus sont clos ou écartés, un dernier bloc clôt la mission.

## Le livrable

`mission/journal.md`, seul fichier qu'écrit cette porte ; les livrables d'étape appartiennent à
leur compétence. Modèle de départ :

```markdown
# Journal de mission — <entreprise ou équipe>

Ouverte le 2026-10-14 · Porte : découverte | besoin connu

## Décisions
- 2026-10-14 · découverte · 00-contexte validé par la direction · « sources : CRM en lecture et deux entretiens »
- 2026-10-16 · découverte · 02-portefeuille validé par la direction · « on creuse : tri des tickets, relances de factures »

## Clôture
### cas-relances-factures — 2026-11-18
Décisions : … (cinq lignes au plus). Hypothèses lourdes : … Gain observé `[F]` : … · gain encore estimé `[E]` : … Relevés à poursuivre : …
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| État calculé depuis les fichiers | un état déclaré se périme sans bruit | un fichier `etat.md` mis à jour à chaque étape | jamais : un résumé peut s'ajouter, il ne remplace pas le calcul |
| Deux portes, un seul pipeline | la découverte débouche sur des besoins, qui suivent la même chaîne | deux méthodes séparées | une mission révèle un besoin que la chaîne ne sait pas traiter |
| Un dossier par cas, nommé une fois | chaque besoin a sa décision, son chiffrage et son plan ; un seul nom évite deux dossiers pour un cas | un document unique pour toute la mission ; un nom choisi par chaque étape | jamais : un rapport de synthèse peut s'ajouter à la fin |
| Le journal ne porte que des décisions, leurs corrections et la clôture | il doit rester lisible en deux minutes | y consigner aussi le travail fait | jamais |
| Une correction se trace, elle ne se réécrit pas | on doit pouvoir dire quelle version a servi à quelle décision | corriger le livrable sans le dire | une faute de frappe sans effet sur un nombre ni sur une décision : correction directe |
| Chaque étape de 80 à 95 s'ouvre sur la décision écrite de la précédente | la recette testerait ce qui n'est pas prêt, la mise en service agirait sur ce qui n'est pas recetté, la mesure lirait ce qui n'est pas en service | tout lancer d'un bloc pour gagner du temps | un lot fait seulement de simplifications : il passe de 70 à 90 |
| Le cas se clôt après la mesure ou sur un arrêt écrit | un plan validé n'est pas un résultat : le gain se lit sur relevé | clore à la validation du plan | le client renonce à construire avec le pack : une décision d'arrêt écrite clôt le cas |

## Frontières

- Le contenu de chaque étape appartient à sa compétence : `decouvrir-cas-usage`, `cadrer-besoin`,
  `auditer-processus`, `rediger-cahier-des-charges`, `concevoir-solution`, `chiffrer-rentabilite`,
  `planifier-deploiement`, `construire-solution`, `tester-solution`, `piloter-mise-en-service`,
  `mesurer-gains`.
- La carte complète, les contrats et les règles communes vivent dans `ARCHITECTURE.md` du pack.
- Cette porte n'agit dans aucun outil de l'entreprise : toute action passe par `piloter-mise-en-service`,
  action par action. L'arbitrage d'une décision d'affaires → `router-consulting-strategy`, appelé par les
  étapes qui décident ; il ne possède aucun livrable.
- Hors du pack : exploiter la solution après la transmission, collecter les relevés à la place du client.

## Preuves restantes

- Éprouvée sur la mission fictive du 12/10/2026 (`examples/`), reprise depuis son seul dossier : les étapes 10 à 70,
  puis 80 à 95 avec leurs conditions d'ouverture et un « corriger » qui laisse le cas ouvert. Les frictions relevées
  sur l'état, le nom du cas, le journal et la clôture sont corrigées ici.
- Écrits d'après les contrats des quatre compétences, jamais parcourus, même en fiction : le passage direct de 70 à
  90, la clôture après la mesure, « étendre » et « arrêter ».
- NON MESURÉ sur une mission réelle : le premier cas réel dira si le compte des questions ouvertes
  aide à décider et si une seule ligne de journal suffit pour une décision à plusieurs rôles.
