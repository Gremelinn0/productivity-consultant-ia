---
name: concevoir-solution
description: >-
  Quand les exigences sont écrites et qu'il faut choisir comment y répondre (« quelle solution
  choisir ? », « on automatise avec quoi ? », « n8n ou du code ? », « faut-il vraiment automatiser ? »)
  → poser la stratégie d'automatisation (faut-il automatiser, quel type de solution, sur quelle
  plateforme), puis comparer de vraies options, dont ne rien construire et les outils déjà en place, sur
  une matrice (couverture des exigences, coûts, fiabilité, données, dépendance, délai), et recommander
  d'abord, avec le contre-argument, la condition d'arrêt et l'option de repli ; quand il faut
  standardiser avant de construire, retenir l'option sous une porte mesurable.
  Quatrième étape de la porte « besoin connu » du pack consultant-ia. Triggers : « choisir une
  solution », « comparer les options », « faut-il automatiser », « build or buy », « quelle
  plateforme », « agent ou workflow », « solution design », « automation strategy ».
metadata:
  scope: "le choix de la réponse à un besoin déjà traduit en exigences : faut-il automatiser, quelle option, construite par qui, et sous quelle porte"
  owns: "la stratégie d'automatisation (faire ou non, quel type de solution, quelle plateforme et qui la nomme), la porte d'entrée « faut-il automatiser », le catalogue d'options, la matrice d'évaluation, le partage entre automatisme et humain, la recommandation avec son contre-argument et son repli, la porte de démarrage quand on standardise d'abord"
  consumes: "30-exigences, 20-diagnostic et 10-besoin du cas ; mission/sources/ ; mission/journal.md ; les pages des éditeurs pour les capacités et les prix, lues au moment du choix"
---

# Concevoir la solution

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/40-solutions.md`. Preuve : le décideur
> choisit l'option, et la décision s'inscrit dans `mission/journal.md`. Contrôle de forme : la fiche
> porte les onze rubriques du modèle, porte comprise ; l'option 0 figure dans la matrice ; l'option de
> repli est examinée avec la même grille que l'option retenue ; chaque nombre a son statut `[F]`, `[H]`
> ou `[E]` (définis dans `ARCHITECTURE.md`) ; toute capacité ou tout prix de plateforme est daté ou marqué
> `[H]`. Exemple de référence : `examples/` du pack. **Boucle** : aucune.

## Ce que cette compétence résout

Face à un besoin, le réflexe est de choisir un outil : celui qu'on connaît, celui qu'un fournisseur a
présenté, celui dont on a lu un article. Le choix se fait alors avant les deux questions qui comptent :
faut-il construire quelque chose, et quel est le chemin le plus simple pour que la tâche soit faite ?
Cette compétence les pose dans l'ordre, compare des options réellement différentes aux exigences
écrites, et recommande en disant ce qui renverserait sa recommandation.

Résultat attendu : une fiche qui commence par la recommandation, montre la matrice dont elle sort, et
laisse au décideur le choix de l'option et de qui la construit.

## Stratégie

1. **Savoir s'il faut construire avant de savoir quoi.** Automatiser a un coût permanent : maintenance,
   pannes, accès à renouveler. Quatre facteurs ensemble disent si ce coût se justifie : fréquence,
   temps gagné par occurrence, taux d'erreur à la main, stabilité du processus. Fréquent et stable avec
   un vrai gain → oui. Fréquent mais instable → standardiser d'abord. Forte valeur mais jugement à
   chaque fois → assister, ne pas automatiser. Standardiser d'abord n'arrête pas la mission : une option
   à construire peut être retenue sous une porte, pendant que l'option 0 s'applique.
2. **Partir du chemin le plus simple, pas d'un outil.** La question est « quel est le chemin le plus
   simple pour exécuter cette tâche ? ». Sans elle, l'outil connu devient la réponse avant que les
   options à coût nul aient été regardées.
3. **Ce qui existe passe avant ce qu'on construit.** Configurer un outil déjà en place, réutiliser un
   modèle ou une application du marché : vérifier avant de construire. Faire construire ce qui existe
   déjà coûte sans que personne le voie, puisque personne n'a comparé.
4. **Garder l'humain dans la boucle par conception.** Jugement, actions irréversibles ou à fort impact
   (argent, suppression, envoi en masse, publication), cas rares à fort enjeu : l'automatisme prépare,
   un humain valide l'action finale. Le jour où l'automatisme se trompe avec assurance, un clic coûte
   moins que l'erreur répétée à l'échelle.
5. **De vraies options, examinées avec la même rigueur.** Si l'option préférée gagne parce que les
   autres n'ont pas été creusées, la matrice est une mise en scène. L'option 0 y figure toujours ; le
   repli reçoit la même grille que l'option retenue.
6. **Juger sur les exigences, pas sur les goûts.** Une exigence Indispensable non couverte élimine
   l'option ; la matrice compare ce qui reste. Sans cela, la comparaison dérive vers la préférence
   technique de celui qui construit.
7. **Compter le coût de fonctionnement dans l'unité que le fournisseur facture** : exécution, action ou
   crédit, tâche, utilisateur. La même automatisation coûte très différemment selon l'unité ; c'est
   l'axe qui fait exploser une facture à l'échelle, et on ne le découvre qu'après le choix si on ne
   le calcule pas avant.
8. **Vérifier ce qui bouge vite au moment du choix.** Capacités et prix des plateformes changent en
   quelques mois : lire la page de l'éditeur, noter la date, sinon marquer `[H]`. Chaque nombre porte son
   statut : `[F]` fait (page ou devis datés, relevé), `[H]` hypothèse, `[E]` estimation ; définitions dans
   `ARCHITECTURE.md`.
9. **Recommander d'abord, puis exposer ce qui renverserait la recommandation.** Le décideur lit la
   réponse avant les preuves. Sans contre-argument ni condition d'arrêt, ce n'est pas une
   recommandation, c'est un pari.

## Étapes

La stratégie d'automatisation que cette étape pose tient en trois décisions, dans cet ordre : **faire ou
non** (étape 2), **quel type de solution** (flux, agent, appel direct à un modèle, logiciel du marché ou
code : les options 0 à 7, étapes 3 à 6), **quelle plateforme, et qui la nomme** (étapes 7 à 9, rubrique 8).
Pour la plateforme, cinq critères de la matrice pèsent le plus : le coût
complet (maintenance et unité facturée comprises), la fiabilité, le lieu des données, la compétence interne
pour maintenir, la réversibilité (sortie possible). Si la fiche ne donne que la famille de plateforme (flux
sans code, scénario, script, agent), elle dit qui tranche la plateforme avant la construction : la
plateforme arrêtée par `70-plan` et confirmée par le décideur au journal fait foi (`ARCHITECTURE.md`).

1. **Lire ce qui existe.** `30-exigences` d'abord : s'il manque, appeler `rediger-cahier-des-charges`
   en mode exigences, sinon on compare des options à des préférences. Puis `20-diagnostic` (mesures,
   causes, simplifications déjà repérées), `10-besoin` (décision attendue), `mission/sources/`.
2. **Passer la porte d'entrée.** Remplir les quatre facteurs avec les valeurs du diagnostic et leur
   statut. Verdict : automatiser · standardiser d'abord · assister seulement · ne rien construire.
   « Standardiser d'abord » a deux sorties : l'option 0 seule est retenue, ou une option à construire est
   retenue sous une porte (rubrique 10) — l'option 0 s'applique alors dès maintenant et la construction attend
   la porte. Dans les deux cas, le plan de simplification appartient à `planifier-deploiement`. Lecture des
   quatre facteurs, piège du processus cassé et garde-fou financier qui suit : `references/criteres-et-options.md`,
   partie 1.
3. **Poser la question du chemin le plus simple.** Quelles étapes se suppriment, se fusionnent, se
   réordonnent, passent à quelqu'un d'autre ? Écrire l'option 0 précisément : ce qui change, ce qu'elle
   règle des exigences, ce qu'elle ne règle pas.
4. **Partager le processus cible entre machine et humain.** Pour chaque étape de `30-exigences` §3 :
   automatisée, préparée puis validée par un humain, ou humaine ; un niveau par étape, le plus prudent. Justifier
   en une phrase toute étape qui n'est pas « humaine » alors qu'elle touche un jugement, une action irréversible
   ou un fort impact.
5. **Parcourir les huit familles d'options** (catalogue : `references/criteres-et-options.md`, partie
   2) : une ligne par famille, « retenue » ou « écartée parce que… ». Chercher réellement ce qui existe
   déjà — outils connectés à la session en lecture seule, documentation des éditeurs, modèles publics
   — et écrire « non vérifié `[H]` » quand la recherche n'a pas été faite ou n'a pas pu l'être (pas d'accès à
   ces pages) ; elle passe alors en rubrique 9, avec son responsable et sa date.
6. **Retenir trois ou quatre options pour la matrice** : l'option 0, au moins une option « existant »
   (1 ou 2) quand l'une est pertinente, au moins une option à construire. Pour chacune, dire qui
   construit : équipe interne, éditeur de l'outil, recrutement, indépendant, prestataire (partie 3).
7. **Remplir la matrice** (critères et plateformes : parties 4 et 5). D'abord les éliminatoires, puis
   les neuf critères ; chaque cellule porte une appréciation, une raison courte et le statut du
   chiffre. Un tarif ou une capacité de plateforme est daté (« lu le … sur la page de l'éditeur ») ou `[H]`.
   L'option 0 ne s'élimine pas par la couverture ; une option éliminée garde sa colonne, marquée telle. Pour une
   option fournisseur, lire aussi sa continuité (disponibilité promise, support, préavis d'arrêt), le devenir des
   données à la résiliation et la sortie (critère « dépendance et portabilité »).
8. **Lire la matrice, ne pas la sommer.** Dégager l'option retenue et le repli. Si les décideurs ne
   s'accordent pas sur ce qui compte, leur faire classer les trois critères les plus importants et
   relire la matrice avec ce classement.
9. **Éprouver la recommandation.** Contre-argument le plus fort ; ce qui doit être vrai, chaque
   condition avec la personne qui la confirme ; ce qui ferait changer d'avis ; condition d'arrêt
   observable. Un seuil qui ne se calcule qu'au business case s'écrit « fixé par le point mort de
   `50-rentabilite` » et la porte le reprend. Examiner le repli avec la même grille. Si le contre-argument
   est plus fort que les raisons, changer de recommandation. Pour arbitrer, appeler
   `router-consulting-strategy` (lentille options stratégiques) ; le livrable reste celui de cette étape.
10. **Écrire la fiche en commençant par la recommandation**, finir par la décision attendue, proposer
    `chiffrer-rentabilite` (business case de l'option retenue et du repli, apport de chaque phase). Quand le
    décideur tranche, ajouter une ligne à `mission/journal.md`. Une solution imposée par le client suit le même
    chemin : la matrice vérifie qu'elle couvre les exigences et documente un repli ; le journal note
    « option imposée par <rôle> ». Si l'option retenue est la 0 seule, la suite se décide avec le client : un plan
    de simplification (`planifier-deploiement`), ou la fin de la mission du cas.

## Le livrable

Le modèle complet, ses consignes de remplissage et la règle de la porte sont dans `references/modeles.md` :
l'ouvrir pour rédiger. Les titres ci-dessous sont ceux du modèle.

Squelette de `mission/cas-<slug>/40-solutions.md` :

```markdown
# Solutions — <titre court>
Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle, ou la règle qui le désigne selon le montant) · Rédigé par · Exigences lues
## 1. Recommandation — option, porte, trois raisons, ce qui doit être vrai, contre-argument, ce qui ferait changer d'avis, condition d'arrêt, repli
## 2. Faut-il automatiser ? — quatre facteurs, un verdict
## 3. Le chemin le plus simple — l'option 0, précisément
## 4. Où l'humain reste dans la boucle — un niveau par étape
## 5. Les options examinées — huit familles, de 0 à 7
## 6. Matrice — éliminatoires, puis neuf critères
## 7. L'option de repli — même grille que l'option retenue
## 8. Plateforme ou code — unité facturée, volume, coût mensuel, sortie
## 9. À vérifier avant de signer — hypothèses, qui les confirme, avant quand
## 10. Porte — condition de démarrage, mesure, agrégation, seuil, date ; « sans objet » sinon
## 11. Questions ouvertes
## Décision attendue
```

Ligne de journal, au moment où le décideur tranche (exemple fictif) :

```markdown
- 2026-10-28 · cas-relances-factures · 40-solutions validé par la direction financière · « option 4 retenue, construite par un indépendant, sous la porte de la rubrique 10 ; repli : option 0 »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| La porte d'entrée avant les options | un processus instable ou rare fait échouer une automatisation plus sûrement qu'un mauvais outil | comparer les outils directement | le client a déjà acté qu'il automatise et le diagnostic montre un processus stable : la porte se remplit en deux lignes |
| Une option retenue sous une porte quand il faut standardiser d'abord | la mission ne s'arrête pas à la simplification, et la construction ne part pas avant la preuve | retenir l'option 0 seule et clore ; ou construire tout de suite | la simplification suffit : la porte n'est jamais franchie, l'option 0 reste |
| Matrice lue, pas additionnée | une somme pondérée cache l'arbitrage et donne une fausse précision | un score total sur cent | les décideurs demandent un classement chiffré : on le fournit en plus, pondérations visibles |
| L'option 0 toujours dans la matrice | c'est la moins chère, et elle n'a aucun défenseur naturel : personne ne la propose | ne comparer que des constructions | jamais |
| Capacités et prix datés ou `[H]` | ils changent en quelques mois ; une valeur recopiée ressemble à une valeur mesurée | un tableau de prix figé dans la compétence | jamais |
| Repli examiné avec la même grille | un repli qui n'est qu'un nom rend la condition d'arrêt théorique | « on verra plus tard » | le décideur écarte explicitement le repli |
| Validation humaine par défaut sur l'irréversible | une erreur confiante à l'échelle coûte plus qu'un clic | autonomie totale d'emblée | un pilote montre un taux d'erreur très bas et l'action est réversible : on desserre, par décision écrite |

## Frontières

- Les exigences, entrée obligatoire de cette étape → `rediger-cahier-des-charges` (mode exigences).
- La spécification détaillée de l'option retenue, qui reprend la porte → `rediger-cahier-des-charges`
  (mode spécification).
- Gains, coûts complets, scénarios, retour sur investissement → `chiffrer-rentabilite` ; ici,
  seulement un ordre de grandeur du coût de fonctionnement, pour comparer.
- Le processus actuel, ses mesures et ses causes → `auditer-processus`.
- Calendrier, plan de simplification, constat de la porte, pilote planifié, formation, pré-mortem →
  `planifier-deploiement`.
- L'état de la mission et le journal des décisions → `router-mission-ia`.
- Construire l'option retenue, en essai → `construire-solution`, qui reprend l'option et la plateforme de
  cette fiche ; la recette → `tester-solution` ; toute action sur un outil de l'entreprise →
  `piloter-mise-en-service`.
- Pour une plateforme ou un fournisseur précis : `COMPAGNONS.md` du pack, lignes « Stratégie
  d'automatisation » et « Concevoir ». On ne dit s'en être servi que si on l'a réellement appelé ; sans
  compagnon, la méthode ci-dessus est le repli maison.

## Preuves restantes

- Éprouvée sur la mission fictive du 12/10/2026 (`examples/`), qui a relevé 94 frictions : la fiche se remplit
  avec l'option 0 dans la matrice, un repli examiné et une porte ; les corrections sont dans cette version.
- NON MESURÉ sur une mission réelle : le premier cas réel dira si neuf critères sont trop ou trop
  peu, si la porte d'entrée qualitative suffit sans seuils chiffrés et si une porte à une condition suffit.
- Sources et crédits : les compagnons de cette étape et leurs licences sont dans `COMPAGNONS.md` ; les
  méthodes dont elle s'inspire (porte d'entrée, unités de facturation, plateforme ou code, matrice
  comparative, options réelles et recommandation d'abord) sont créditées dans la section « Sources et
  crédits » du `README.md`. Réécrit avec nos mots, aucun texte repris.
