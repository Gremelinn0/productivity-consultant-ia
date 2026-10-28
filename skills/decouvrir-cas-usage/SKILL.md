---
name: decouvrir-cas-usage
description: >-
  Quand une entreprise veut savoir où l'IA peut l'aider sans pouvoir nommer un processus (« où
  peut-on utiliser l'IA chez nous ? », « on perd du temps mais on ne sait pas où », « trouvez-nous
  des cas d'usage ») → brancher le contexte, cartographier les tâches réelles des équipes, les trier
  en cinq issues (éliminer, simplifier d'abord, automatiser, déléguer à l'IA, garder) et rendre un
  portefeuille de cas d'usage classés, avec la décision : quels cas creuser. Porte « on ne part
  d'aucun besoin » du pack consultant-ia ; chaque cas retenu entre ensuite par la porte « besoin
  connu », à partir de cadrer-besoin. Triggers : « où l'IA peut nous aider », « découverte de cas
  d'usage », « use case discovery », « cartographier les tâches », « portefeuille de cas d'usage »,
  « par où commencer avec l'IA », « opportunités d'automatisation », « AI opportunity assessment ».
metadata:
  scope: "une entreprise ou une équipe qui ne nomme aucun besoin précis, du contexte au portefeuille de cas d'usage classés, avant tout cadrage, diagnostic détaillé ou choix de solution"
  owns: "le contexte branché, la cartographie des tâches, le tri en cinq issues, les fiches de cas d'usage et leur classement, les guides d'entretien"
  consumes: "mission/sources/ ; les outils connectés à la session, en lecture seule et avec autorisation ; les réponses aux entretiens ; mission/journal.md"
---

# Découvrir les cas d'usage

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/00-contexte.md`, `mission/01-cartographie-taches.md` et
> `mission/02-portefeuille.md`. Preuve : le décideur choisit les cas à creuser, et la décision s'inscrit
> dans `mission/journal.md`. Contrôle de forme : la cartographie porte ses douze colonnes et l'issue de
> chaque tâche parmi cinq, chaque fiche de cas ses onze rubriques, chaque nombre son statut `[F]`, `[H]`
> ou `[E]` (définis dans `ARCHITECTURE.md`). Exemple de référence : `examples/` du pack. **Boucle** : aucune.

> ❓ **Une question pour l'entreprise sort de la base de questions** (`mener-entretien-ia/references/base-questions/`, un fichier par sujet) :
> lire d'abord le bloc du sujet, ne poser que ce qui manque, puis y ranger ce qui manquait (`entretien.py ajouter`).

## Ce que cette compétence résout

« Où l'IA peut-elle nous aider ? » n'est pas un besoin, c'est une question sur un travail que l'entreprise ne voit
plus : la direction parle d'objectifs, les équipes de leurs journées, et personne ne met les deux côte à côte. Cette
compétence part du travail réel : elle branche ce que l'entreprise fournit, recense les tâches, décide pour chacune
si elle doit disparaître, être simplifiée d'abord, automatisée, confiée à l'IA ou rester humaine, puis rend une liste
courte de cas d'usage classés.

Résultat attendu : trois documents (contexte, cartographie, portefeuille) et une décision — quels cas creuser. Pas
de solution choisie, pas de chiffrage fin.

## Stratégie

1. **Partir du travail, pas de l'outil.** Un cas d'usage décrit un résultat métier reproductible (« les relances de
   factures échues partent à temps »), jamais un produit ni un workflow ; sinon le portefeuille se remplit de
   technologies qui cherchent un problème.
2. **Interroger le travail, pas les personnes.** On demande ce qui se passe, on écrit des rôles plutôt que des noms,
   on ne juge personne : quelqu'un qui se sent évalué cache ses contournements, et ce sont eux qui révèlent les
   meilleures pistes.
3. **Observé avant déclaré, déclaré avant supposé.** Un enregistrement du travail vaut mieux qu'un entretien, qui
   vaut mieux qu'un document, qui vaut mieux qu'une intuition. Chaque ligne dit d'où elle vient ; une tâche sans
   source n'entre pas dans la cartographie. Chaque nombre porte son statut : `[F]` fait (relevé, pièce, ou règle
   énoncée par son détenteur), `[H]` hypothèse (dit de mémoire, avec qui peut le confirmer), `[E]` estimation (calcul
   montré) ; définitions dans `ARCHITECTURE.md`.
4. **Trier avant de construire.** Éliminer, simplifier d'abord, automatiser, déléguer à l'IA, garder — on pose les
   questions dans cet ordre, car automatiser une mauvaise habitude la rend seulement plus rapide. Ce qui existe déjà
   (outil en place, modèle, brique du marché) passe avant ce qu'on construit.
5. **Un ordre de grandeur suffit, et une liste courte se décide.** On compare des cas, on ne promet pas de gains :
   estimé n'est pas mesuré. Trois à cinq cas à faible effort et forte valeur, idéalement un par équipe, valent mieux
   que quarante idées : chaque équipe voit un gain proche et adopte la suite.

## Étapes

1. **Vérifier la porte, puis ouvrir le dossier.** La personne peut-elle nommer le processus en une phrase ? Oui →
   `cadrer-besoin` : la découverte ne retarde pas ce qui est déjà clair. Non, ou doute → découverte courte, qui rend
   la main dès qu'un cas clair apparaît. Créer `mission/`, `mission/sources/` et `mission/journal.md` s'ils
   manquent.
2. **Brancher le contexte, dans cet ordre**, en nommant chaque source dans `00-contexte.md` :
   - les fichiers déposés dans `mission/sources/` (procédures, exports, organigramme, comptes rendus,
     transcriptions) ;
   - les outils déjà connectés à la session, inventoriés d'après les outils réellement disponibles et sans rien lire
     d'abord. Autorisation explicite de l'entreprise, source par source (qui, quand, quel périmètre), puis lecture
     seule. Minimiser les données personnelles : lire catégories, objets, volumes et dates des tickets plutôt que
     les messages des personnes, ne rien copier de nominatif ;
   - l'entretien de cadrage avec la direction (guide direction), mené avant de rédiger `00` : il apporte les
     objectifs, les contraintes, le budget et les essais passés que la fiche entreprise exige.

   Ce qui manque s'écrit comme manquant ; les entretiens et séances prévus s'écrivent « à venir », avec leur date.
   Sans aucune source, s'arrêter à `00-contexte.md` et au guide d'entretien : on ne devine pas les tâches. Faire
   valider `00` (sources, équipes à écouter).
3. **Mener les entretiens des équipes** : semaine type, tâches répétitives, volumes, outils, copier-coller,
   validations, erreurs, exceptions, ce qu'elles voudraient ne plus faire. Questions, version courte, modèle de
   note : `references/guides-entretien.md`, à adapter aux équipes et aux outils déjà repérés. Si la session ne mène
   pas l'entretien, remettre le guide au consultant et lire sa note, déposée dans `mission/sources/`. Après chaque
   entretien ou séance, la ligne « à venir » de `00` prend sa date réelle ; si la liste des sources manquantes ou des
   équipes à écouter change, `00` prend une version datée et le journal une ligne « correction ».
4. **Proposer la séance d'enregistrement, la source la plus riche** : des personnes font réellement leurs tâches
   pendant qu'on enregistre (vidéo ou partage d'écran) en commentant à voix haute, avec leur accord et celui de la
   direction ; la transcription est déposée dans `mission/sources/`. Le pack n'enregistre rien lui-même (protocole :
   `references/guides-entretien.md`).
5. **Chercher les signaux** dans les sources : demandes récurrentes, rapports faits à la main, copier-coller entre
   outils, tableurs utilisés comme base de données, validations par courriel, double saisie. Un signal n'est pas une
   tâche : il dit où poser la question.
6. **Cartographier (`01`).** Une ligne par tâche, douze colonnes — équipe, tâche, déclencheur, fréquence, durée par
   occurrence, volume, outils, données, passages entre équipes, erreurs / reprises, stabilité des règles, source —,
   chaque ligne avec sa source. Les unités se disent sous le tableau : durée par unité traitée, volume par mois,
   temps mensuel = durée × volume. Fusionner une tâche décrite par deux sources, garder les écarts entre leurs
   versions, puis faire relire le tableau par les équipes : s'y reconnaissent-elles ?
7. **Trier chaque tâche en cinq issues**, en pesant quatre critères — la **fréquence**, le **coût** (temps et
   argent par occurrence), la **valeur** (ce que la tâche apporte), le **risque si ça se trompe** — et écrire
   pourquoi. Poser les questions dans l'ordre du tableau : la tâche, ou sa cause, peut-elle disparaître ? les règles
   sont-elles assez claires ? Une tâche qui naît d'un défaut d'information (le client demande un statut parce qu'aucun
   avis ne part) se teste d'abord en « Éliminer la cause » ; ce test devient une action de la vague 0 de la feuille de
   route.

   | Issue | Quand | Ce qu'on en fait |
   |---|---|---|
   | **Éliminer** | prend du temps, apporte peu, personne ne remarquerait sa disparition ; ou née d'un défaut dont on peut supprimer la cause | souvent le gain le plus rapide : on supprime, on ne construit rien |
   | **Simplifier d'abord** | règles floues ou non écrites, tâche faite de plusieurs façons, étape mécanique d'un processus instable | standardiser ou simplifier, re-mesurer, puis reclasser la tâche dans une autre issue |
   | **Automatiser** | même schéma à chaque fois, relie plusieurs outils, règles stables | on construit une fois, puis on surveille |
   | **Déléguer à l'IA** | processus clair, résultat contrôlable | l'IA prépare ou exécute, un humain valide si nécessaire |
   | **Garder** | jugement, relation, négociation, décision importante | l'IA peut préparer, comparer, challenger, sans porter la responsabilité |

   « Simplifier d'abord » n'est pas une destination. Des règles floues ne donnent jamais « Automatiser ». Faire
   valider `01`.
8. **Formuler les cas d'usage (`02`).** Chaque tâche « Automatiser », « Déléguer à l'IA » ou « Simplifier d'abord »
   devient une fiche ; une tâche « Garder » seulement si l'IA y prépare, compare ou challenge sans décider (la fiche
   nomme qui décide). Dédoublonner : même déclencheur + même transformation + même résultat + même responsable = un
   seul cas ; secteur, canal ou outil différents = variantes ; données, validation, contraintes réglementaires ou
   résultat économique différents = cas séparés. `references/catalogue-cas-usage.md` rappelle les pistes de chaque
   fonction : aide-mémoire, pas preuve — une piste qu'aucune tâche de `01` ne fonde reste une hypothèse `[H]`.
9. **Classer.** *Valeur* : ordre de grandeur du gain mensuel `[E]` = durée par unité × volume mensuel (exemple de
   calcul, fictif : 10 minutes par relance × 120 relances par mois = 1 200 minutes, soit 20 heures par mois, un plafond
   que le chiffrage réduira). *Facilité* (données disponibles, règles stables, accès aux outils, peu d'exceptions) et
   *risque si ça se trompe* se notent haut, moyen ou bas, avec une raison d'une ligne que `planifier-deploiement`
   reprendra ; quand une donnée manque, noter « à classer » et écrire la donnée et qui la fournit. Un cas n'est pas plus
   facile que sa donnée la moins accessible ; un risque haut n'écarte pas le cas, il impose une validation humaine. Un
   cas « Simplifier d'abord » se classe sur ce qu'il vaudra après simplification. Quatre classes :
   - **Gains rapides** : valeur notable, facilité haute, risque bas ou couvert par une validation ;
   - **Projets** : valeur haute mais facilité moyenne ou basse, ou risque qui impose des garde-fous ;
   - **À creuser** : une donnée manquante empêche de classer — écrire laquelle et qui la fournit ;
   - **À écarter** : valeur faible, risque disproportionné ou besoin déjà couvert — écrire la raison.
10. **Recommander, puis s'arrêter sur la décision.** Recommander trois à cinq cas à faible effort et forte valeur,
    idéalement un par équipe concernée, et dire ce qui ferait changer cette recommandation. Pour arbitrer,
    appeler `router-consulting-strategy` (lentille priorisation) ; le livrable reste celui de cette étape. À chaque
    validation (`00`, `01`, `02`), ajouter une ligne à `mission/journal.md` ; celle de `02` nomme les cas à creuser. Proposer
    ensuite `chiffrer-rentabilite` (ordre de grandeur des seuls cas à creuser → `03-chiffrage.md`),
    `planifier-deploiement` (feuille de route → `04-feuille-de-route.md`), puis `cadrer-besoin` pour chaque cas
    retenu, depuis sa fiche.

## Le livrable

Trois documents dans `mission/`. Les modèles complets, les consignes de remplissage et les lignes de journal sont
dans `references/modeles.md` : l'ouvrir pour rédiger. Les titres ci-dessous sont ceux du modèle.

Squelette de `mission/00-contexte.md` :

```markdown
# Contexte — <entreprise ou périmètre>
Date · Demandeur (rôle) · Valideur (rôle) · Rédigé par
## 1. Fiche entreprise — activité, équipes, outils, données, objectifs, contraintes, essais passés
## 2. Sources branchées et autorisations obtenues — une ligne par source ; « à venir » prend sa date réelle
## 3. Sources manquantes — ce qu'elles empêchent de conclure, qui peut les fournir
## Décision attendue
```

Squelette de `mission/01-cartographie-taches.md` :

```markdown
# Cartographie des tâches — <périmètre>
Date · Demandeur (rôle) · Valideur (rôle) · Rédigé par
## 1. Les tâches — douze colonnes, unités dites sous le tableau
## 2. Écarts gardés et tâches non observées
## 3. Le tri — l'issue de chaque tâche parmi cinq, et pourquoi
## Décision attendue
```

Squelette de `mission/02-portefeuille.md` :

```markdown
# Portefeuille de cas d'usage — <périmètre>
Date · Demandeur (rôle) · Valideur (rôle) · Rédigé par
## 1. Vue d'ensemble — un cas par ligne : valeur, facilité, risque, classe
## 2. Fiches — onze rubriques par cas, de « Résultat » à « Déjà disponible »
## 3. Recommandation — à éliminer d'abord, trois à cinq cas, ce qui ferait changer d'avis
## Décision attendue
```

Ligne de journal, au moment où le décideur tranche (une par document validé ; l'étiquette de cas est « découverte ») :

```markdown
- 2026-10-07 · découverte · 02-portefeuille validé par la direction générale · « on creuse : relances de factures, tri des tickets, comptes rendus de rendez-vous »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Cinq issues, « Éliminer » en tête, « Simplifier d'abord » avant « Automatiser » | beaucoup de gains rapides n'exigent aucune technologie, et automatiser une mauvaise habitude la fige | ne chercher que ce qui est automatisable | l'entreprise vient de simplifier ses processus : « Éliminer » et « Simplifier d'abord » peuvent rester vides, on l'écrit |
| Cartographier des tâches, pas des postes ni des personnes | une carte de personnes se lit comme une évaluation et fait cacher les contournements | un organigramme noté « potentiel IA » par poste | jamais |
| Observation et entretiens plutôt qu'un questionnaire général | chacun décrit la procédure, pas ses contournements | un formulaire envoyé à tous les salariés | l'enregistrement est refusé ou impossible : entretiens seuls, durées et volumes en `[H]` |
| Entretien de cadrage de la direction avant `00` | la fiche entreprise exige objectifs, contraintes et budget, que seule la direction donne | valider `00` avant tout entretien | la direction n'est pas disponible : `00` s'écrit avec ces rubriques en `[H]` et se met à jour après |
| Ordre de grandeur, pas de business case | classer demande de comparer, pas de promettre ; le détail appartient à `chiffrer-rentabilite` | un business case complet par cas dès la découverte | un seul cas intéresse la direction : la porte « besoin connu » le chiffre |
| Trois à cinq cas recommandés | une liste courte se décide, et chaque équipe voit un gain proche | classer et défendre tous les cas trouvés | la direction veut une couverture exhaustive : le portefeuille reste long, la recommandation reste courte |

## Frontières

- Un processus nommé en une phrase, un besoin exprimé → `cadrer-besoin` (porte « besoin connu »), puis le détail du
  processus : étapes, mesures, causes → `auditer-processus`.
- L'ordre de grandeur des gains et des coûts → `chiffrer-rentabilite` ; l'ordre de mise en œuvre, vague 0 des
  suppressions et simplifications comprise → `planifier-deploiement` ; les exigences et la comparaison de solutions
  d'un cas → `rediger-cahier-des-charges`, `concevoir-solution`. L'état de la mission et le journal des décisions →
  `router-mission-ia`.
- Facultatif : les outils connectés à la session (documents, messagerie, tickets, CRM) ne servent qu'en lecture ; ne
  dire qu'on a lu une source que si l'outil a réellement été appelé.

## Preuves restantes

- Éprouvée sur la mission fictive du 12/10/2026 (`examples/`), qui a relevé 94 frictions ; celles qui touchent la
  découverte sont corrigées ici.
- NON MESURÉ sur une mission réelle : le premier cas réel dira si les douze colonnes suffisent, si le tri en cinq
  issues est assez fin et si trois à cinq cas est le bon nombre.
- Sources et crédits : la méthode dont s'inspire la forme de l'entretien est créditée dans la section « Sources et
  crédits » du `README.md` ; `COMPAGNONS.md` liste les compagnons du pack. Méthode réécrite, aucun passage repris.
