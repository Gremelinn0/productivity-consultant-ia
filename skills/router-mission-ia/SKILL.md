---
name: router-mission-ia
description: >-
  Quand une mission de conseil IA ou d'automatisation commence ou reprend — un besoin à automatiser,
  une entreprise qui demande « où l'IA peut-elle nous aider ? », un audit IA, une stratégie
  d'automatisation à bâtir, ou « où en est la mission ? » — → afficher l'état du dossier de mission,
  choisir la porte (besoin connu ou découverte), lancer l'étape suivante du pack consultant-ia et
  tenir le journal des décisions. Porte d'entrée du pack. Triggers : « mission IA », « audit IA »,
  « on veut automatiser », « par où commencer avec l'IA », « trouver nos cas d'usage », « stratégie
  d'automatisation », « où en est la mission », « AI consulting », « automation strategy », « use
  case discovery », « /mission-besoin », « /mission-decouverte ».
metadata:
  scope: "une mission de conseil IA et automatisation dans une entreprise, de la première question au plan d'automatisation"
  owns: "l'état de la mission dérivé du dossier mission/, le choix de la porte, l'ordre des étapes, le journal des décisions, de leurs corrections et de la clôture"
  consumes: "le dossier mission/ du répertoire de travail ; les sept compétences d'étape du pack ; ARCHITECTURE.md"
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
bonne compétence. Les sept compétences d'étape font le travail ; elle ne refait celui d'aucune.

## Stratégie

1. **L'état d'abord, toujours calculé.** Avant toute réponse, même pour « rien à faire », afficher
   l'état dérivé du dossier `mission/`. Un fichier qui déclarerait « étape faite » mentirait le jour
   où quelqu'un modifie le dossier à la main ; les fichiers présents, eux, ne mentent pas.
2. **Une porte se choisit sur un test simple.** La personne peut-elle nommer le processus concerné en
   une phrase ? Oui → porte 1, « besoin connu ». Non → porte 2, « découverte ». En cas de doute, la
   porte 2 commence court et rend la main dès qu'un cas clair apparaît.
3. **L'ordre protège la décision.** On ne compare pas des solutions avant d'avoir des exigences, on ne
   chiffre pas une option qu'on n'a pas décrite, on ne planifie pas ce qu'on n'a pas décidé de faire.
   Sauter une étape reste possible quand l'utilisateur le demande ; on écrit alors dans le journal ce
   qui a été sauté et pourquoi.
4. **Chaque étape finit par une décision humaine.** La compétence d'étape propose ; la personne
   tranche ; la porte inscrit la décision au journal. Le pack ne valide jamais à la place du client.
5. **Un cas porte un seul nom, fixé une fois.** `cadrer-besoin` choisit le slug du dossier ; la porte, le
   journal et les renvois le reprennent tel quel. Deux noms pour un cas font deux dossiers et un état faux.
6. **Rien ne sort du dossier de mission.** Ni envoi, ni publication, ni modification d'un outil de
   l'entreprise.

## Étapes

### 1. Afficher l'état

Lire `mission/` (le créer avec `journal.md` et `sources/` s'il n'existe pas), puis afficher :

```text
Mission           <nom du dossier de travail>          porte(s) : découverte · besoin connu
Découverte        00 ✓  01 ✓  02 ✓  03 ✓  04 ✓         décision en attente : aucune
cas-relances-factures  10 ✓  20 ✓  30 —  40 —  50 —  60 —  70 —
À lancer          Tri des tickets entrants · Statut de commande
Dernière décision 2026-10-14 · cas-relances-factures · 20-diagnostic validé
Hypothèses ouvertes  6 [H] sur les livrables du cas, sans doublon
Étape suivante    rediger-cahier-des-charges (exigences) pour cas-relances-factures
```

Chaque ligne se calcule à la lecture :
- `✓` = le fichier existe ; `—` = il manque ;
- « étape suivante » = le premier fichier manquant dans l'ordre de la porte, pour le cas le plus
  récemment modifié ; si les sept fichiers existent et que le journal valide `70-plan.md` :
  « clore le cas <slug> » ; quand tous les cas retenus sont clos ou écartés : « clore la mission » ;
- « décision en attente » = un livrable existe mais aucune ligne de `journal.md` ne valide sa dernière
  version ;
- « à lancer » = les cas que la validation de `02-portefeuille.md` retient (« on creuse : … ») et qui n'ont
  pas encore de dossier `cas-<slug>/` ; un cas mis en attente ou écarté n'y figure pas ;
- « hypothèses ouvertes » = le nombre de `[H]` distincts sur tous les livrables du cas (ou de la
  découverte, s'il n'y a pas de cas) : un énoncé repris dans plusieurs livrables compte une fois ; ni
  légende ni rappel de définition ;
- un dossier `mission/` vide affiche « aucune mission en cours » et pose la question de la porte.

### 2. Choisir la porte

- `/mission-besoin <besoin>` ou une demande qui nomme un processus → porte 1, à partir de
  `cadrer-besoin`, qui fixe le slug et ouvre `mission/cas-<slug>/`.
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
| 1 — besoin connu | `cadrer-besoin` | 10-besoin |
| | `auditer-processus` | 20-diagnostic |
| | `rediger-cahier-des-charges` (exigences) | 30-exigences |
| | `concevoir-solution` | 40-solutions |
| | `chiffrer-rentabilite` (business case) | 50-rentabilite |
| | `rediger-cahier-des-charges` (spécification) | 60-specification |
| | `planifier-deploiement` (plan + pré-mortem) | 70-plan |

Appeler la compétence de l'étape par son nom, avec le chemin du dossier du cas. Quand la porte 2
lance un cas, `cadrer-besoin` reçoit la fiche du cas dans `02-portefeuille.md` pour ne pas reposer
les questions déjà répondues.

### 4. Tenir le journal

Une ligne par décision, datée. Le cas s'écrit `découverte` pour les livrables 00 à 04 et
`cas-<slug>` pour 10 à 70. Trois formes :

```markdown
- 2026-10-14 · cas-relances-factures · 20-diagnostic validé par la direction financière · « on standardise le modèle de relance avant d'automatiser »
- 2026-10-21 · cas-relances-factures · 30-exigences corrigées (version 1.1 : EF-01 précisée) · confirmées par la direction financière · « une facture écartée une semaine revient la suivante »
- 2026-11-03 · cas-relances-factures · porte constatée par la direction financière · « trois lundis conformes ; fiche de porte jointe »
```

- **Un livrable validé** : date, cas, livrable, décision, rôle de qui a tranché, et sa phrase si elle éclaire
  la suite.
- **Une correction** : quand une étape trouve un trou dans un livrable déjà validé, elle le corrige par une
  version datée (voir `ARCHITECTURE.md`) ; la ligne dit la version et le motif, et qui la confirme.
- **Une décision sans livrable** : porte constatée, fin de pilote, bascule. La ligne cite la pièce qui la
  prouve (fiche de porte, relevé du pilote, sauvegarde).
- **Une étape sautée** : « 30-exigences sauté à la demande de … : besoin déjà spécifié par l'éditeur ».

### 5. Clore

Quand `70-plan.md` est validé : écrire dans `journal.md`, section « Clôture », un bloc pour le cas —
les décisions du journal en cinq lignes au plus, les hypothèses `[H]` encore ouvertes (leur nombre et les
plus lourdes) et les mesures de départ à relever avant de construire. Pour une découverte sans cas lancé,
c'est `04-feuille-de-route.md` validée qui clôt. Quand tous les cas retenus sont clos ou écartés, un dernier
bloc clôt la mission. La construction n'appartient pas au pack : la spécification et le plan sont les
entrées de l'équipe qui construit.

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
Décisions : … (cinq lignes au plus). Hypothèses ouvertes : … Mesures de départ à relever avant de construire : …
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| État calculé depuis les fichiers | un état déclaré se périme sans bruit | un fichier `etat.md` mis à jour à chaque étape | jamais : un résumé peut s'ajouter, il ne remplace pas le calcul |
| Deux portes, un seul pipeline | la découverte débouche sur des besoins, qui suivent la même chaîne | deux méthodes séparées | une mission révèle un besoin que la chaîne ne sait pas traiter |
| Un dossier par cas, nommé une fois | chaque besoin a sa décision, son chiffrage et son plan ; un seul nom évite deux dossiers pour un cas | un document unique pour toute la mission ; un nom choisi par chaque étape | jamais : un rapport de synthèse peut s'ajouter à la fin |
| Le journal ne porte que des décisions, leurs corrections et la clôture | il doit rester lisible en deux minutes | y consigner aussi le travail fait | jamais |
| Une correction se trace, elle ne se réécrit pas | on doit pouvoir dire quelle version a servi à quelle décision | corriger le livrable sans le dire | une faute de frappe sans effet sur un nombre ni sur une décision : correction directe |

## Frontières

- Le contenu de chaque étape appartient à sa compétence : `decouvrir-cas-usage`, `cadrer-besoin`,
  `auditer-processus`, `rediger-cahier-des-charges`, `concevoir-solution`, `chiffrer-rentabilite`,
  `planifier-deploiement`.
- La carte complète, les contrats et les règles communes vivent dans `ARCHITECTURE.md` du pack.
- Construire l'automatisation ou l'agent, mesurer le gain réel après déploiement : hors du pack.

## Preuves restantes

- Éprouvée sur la mission fictive du 12/10/2026 (`examples/`), reprise depuis son seul dossier ; les
  frictions relevées sur l'état, le nom du cas, le journal et la clôture sont corrigées ici.
- NON MESURÉ sur une mission réelle : le premier cas réel dira si le compte des hypothèses ouvertes
  aide à décider et si une seule ligne de journal suffit pour une décision à plusieurs rôles.
