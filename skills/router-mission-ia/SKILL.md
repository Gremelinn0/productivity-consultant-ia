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
  owns: "l'état de la mission dérivé du dossier mission/, le choix de la porte, l'ordre des étapes, le journal des décisions"
  consumes: "le dossier mission/ du répertoire de travail ; les sept compétences d'étape du pack ; ARCHITECTURE.md"
---

# Mission IA — la porte du pack

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Ne produit aucun livrable métier : elle affiche l'état, choisit
> l'étape et écrit `mission/journal.md`. Preuve : l'état affiché correspond aux fichiers présents
> dans `mission/` (aucune ligne n'est recopiée d'un fichier d'état). Contrôle : la mission fictive
> de `examples/` se reprend depuis son seul dossier. **Boucle** : aucune.

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
5. **Rien ne sort du dossier de mission.** Ni envoi, ni publication, ni modification d'un outil de
   l'entreprise.

## Étapes

### 1. Afficher l'état

Lire `mission/` (le créer avec `journal.md` et `sources/` s'il n'existe pas), puis afficher :

```text
Mission           <nom du dossier de travail>          porte(s) : découverte · besoin connu
Découverte        00 ✓  01 ✓  02 ✓  03 —  04 —        décision en attente : quels cas creuser
cas-relances      10 ✓  20 ✓  30 —  40 —  50 —  60 —  70 —
Dernière décision 2026-10-14 · cas-relances · 20-diagnostic validé
Hypothèses ouvertes  6 [H] dans le dernier livrable
Étape suivante    rediger-cahier-des-charges (exigences) pour cas-relances
```

Chaque ligne se calcule à la lecture :
- `✓` = le fichier existe ; `—` = il manque ; l'étape suivante est le premier fichier manquant dans
  l'ordre de la porte, pour le cas le plus récemment modifié ;
- « décision en attente » = un livrable existe mais aucune ligne de `journal.md` ne le valide ;
- « hypothèses ouvertes » = nombre de `[H]` dans le dernier livrable modifié ;
- un dossier `mission/` vide affiche « aucune mission en cours » et pose la question de la porte.

### 2. Choisir la porte

- `/mission-besoin <besoin>` ou une demande qui nomme un processus → porte 1, à partir de
  `cadrer-besoin`, dans un nouveau dossier `mission/cas-<slug>/`.
- `/mission-decouverte` ou « où l'IA peut-elle nous aider ? » → porte 2, à partir de
  `decouvrir-cas-usage`.
- Une mission qui reprend → l'étape suivante affichée, sans reposer la question.

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

Quand la personne tranche, ajouter une ligne à `mission/journal.md` :

```markdown
- 2026-10-14 · cas-relances · 20-diagnostic validé par la direction financière · « on standardise le modèle de relance avant d'automatiser »
```

Date, cas (ou « découverte »), livrable, décision, rôle de qui a tranché, et sa phrase si elle
éclaire la suite. Une étape sautée s'écrit aussi : « 30-exigences sauté à la demande de … : besoin
déjà spécifié par l'éditeur ».

### 5. Clore

Quand `70-plan.md` (ou `04-feuille-de-route.md` pour une découverte sans cas lancé) est validé :
résumer en cinq lignes les décisions du journal, lister les hypothèses `[H]` encore ouvertes et les
mesures de départ à relever avant de construire. La construction n'appartient pas au pack : la
spécification et le plan sont les entrées de l'équipe qui construit.

## Le livrable

`mission/journal.md`, seul fichier qu'écrit cette porte ; les livrables d'étape appartiennent à
leur compétence. Modèle de départ :

```markdown
# Journal de mission — <entreprise ou équipe>

Ouverte le 2026-10-14 · Porte : découverte | besoin connu

## Décisions
- 2026-10-14 · découverte · 00-contexte validé par la direction · « sources : CRM en lecture et deux entretiens »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| État calculé depuis les fichiers | un état déclaré se périme sans bruit | un fichier `etat.md` mis à jour à chaque étape | jamais : un résumé peut s'ajouter, il ne remplace pas le calcul |
| Deux portes, un seul pipeline | la découverte débouche sur des besoins, qui suivent la même chaîne | deux méthodes séparées | une mission révèle un besoin que la chaîne ne sait pas traiter |
| Un dossier par cas | chaque besoin a sa décision, son chiffrage et son plan | un document unique pour toute la mission | jamais : un rapport de synthèse peut s'ajouter à la fin |
| Le journal ne porte que des décisions | il doit rester lisible en deux minutes | y consigner aussi le travail fait | jamais |

## Frontières

- Le contenu de chaque étape appartient à sa compétence : `decouvrir-cas-usage`, `cadrer-besoin`,
  `auditer-processus`, `rediger-cahier-des-charges`, `concevoir-solution`, `chiffrer-rentabilite`,
  `planifier-deploiement`.
- La carte complète, les contrats et les règles communes vivent dans `ARCHITECTURE.md` du pack.
- Construire l'automatisation ou l'agent, mesurer le gain réel après déploiement : hors du pack.

## Preuves restantes

- Éprouvée sur la mission fictive de `examples/`, reprise depuis son seul dossier.
- NON MESURÉ sur une mission réelle complète.
