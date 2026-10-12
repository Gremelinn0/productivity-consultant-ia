---
name: concevoir-solution
description: >-
  Quand les exigences sont écrites et qu'il faut choisir comment y répondre (« quelle solution
  choisir ? », « on automatise avec quoi ? », « n8n ou du code ? », « faut-il vraiment automatiser ? »)
  → décider d'abord s'il faut automatiser, puis comparer de vraies options, dont ne rien construire et
  les outils déjà en place, sur une matrice (couverture des exigences, coûts, fiabilité, données,
  dépendance, délai), et recommander d'abord, avec le contre-argument, la condition d'arrêt et l'option
  de repli. Quatrième étape de la porte « besoin connu » du pack consultant-ia. Triggers : « choisir
  une solution », « comparer les options », « faut-il automatiser », « build or buy », « quelle
  plateforme », « agent ou workflow », « solution design », « automation strategy ».
metadata:
  scope: "le choix de la réponse à un besoin déjà traduit en exigences : faut-il automatiser, quelle option, construite par qui"
  owns: "la porte d'entrée « faut-il automatiser », le catalogue d'options, la matrice d'évaluation, le partage entre automatisme et humain, la recommandation avec son contre-argument et son repli"
  consumes: "30-exigences, 20-diagnostic et 10-besoin du cas ; mission/sources/ ; mission/journal.md ; les pages des éditeurs pour les capacités et les prix, lues au moment du choix"
---

# Concevoir la solution

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/40-solutions.md`. Preuve : le décideur
> choisit l'option, et la décision s'inscrit dans `mission/journal.md`. Contrôle de forme : la fiche
> porte les dix rubriques du modèle ; l'option 0 figure dans la matrice ; l'option de repli est
> examinée avec la même grille que l'option retenue ; chaque nombre a son statut `[F]`, `[H]` ou `[E]` ;
> toute capacité ou tout prix de plateforme est daté ou marqué `[H]`. Exemple de référence :
> `examples/` du pack. **Boucle** : aucune.

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
   chaque fois → assister, ne pas automatiser.
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
   quelques mois : lire la page de l'éditeur, noter la date, sinon marquer `[H]`.
9. **Recommander d'abord, puis exposer ce qui renverserait la recommandation.** Le décideur lit la
   réponse avant les preuves. Sans contre-argument ni condition d'arrêt, ce n'est pas une
   recommandation, c'est un pari.

## Étapes

1. **Lire ce qui existe.** `30-exigences` d'abord : s'il manque, appeler `rediger-cahier-des-charges`
   en mode exigences, sinon on compare des options à des préférences. Puis `20-diagnostic` (mesures,
   causes, simplifications déjà repérées), `10-besoin` (décision attendue), `mission/sources/`.
2. **Passer la porte d'entrée.** Remplir les quatre facteurs avec les valeurs du diagnostic et leur
   statut. Verdict : automatiser · standardiser d'abord · assister seulement · ne rien construire.
   « Standardiser d'abord » fait de l'option 0 la recommandation et renvoie à `auditer-processus`.
   Lecture des quatre facteurs, piège du processus cassé et garde-fou financier qui suit :
   `references/criteres-et-options.md`, partie 1.
3. **Poser la question du chemin le plus simple.** Quelles étapes se suppriment, se fusionnent, se
   réordonnent, passent à quelqu'un d'autre ? Écrire l'option 0 précisément : ce qui change, ce qu'elle
   règle des exigences, ce qu'elle ne règle pas.
4. **Partager le processus cible entre machine et humain.** Pour chaque étape de `30-exigences` §3 :
   automatisée, préparée puis validée par un humain, ou humaine. Justifier en une phrase toute étape
   qui n'est pas « humaine » alors qu'elle touche un jugement, une action irréversible ou un fort impact.
5. **Parcourir les huit familles d'options** (catalogue : `references/criteres-et-options.md`, partie
   2) : une ligne par famille, « retenue » ou « écartée parce que… ». Chercher réellement ce qui existe
   déjà — outils connectés à la session en lecture seule, documentation des éditeurs, modèles publics
   — et écrire « non vérifié `[H]` » quand la recherche n'a pas été faite.
6. **Retenir trois ou quatre options pour la matrice** : l'option 0, au moins une option « existant »
   (1 ou 2) quand l'une est pertinente, au moins une option à construire. Pour chacune, dire qui
   construit : équipe interne, éditeur de l'outil, recrutement, indépendant, prestataire (partie 3).
7. **Remplir la matrice** (critères et plateformes : parties 4 et 5). D'abord les éliminatoires, puis
   les neuf critères ; chaque cellule porte une appréciation, une raison courte et le statut du
   chiffre. Un tarif ou une capacité de plateforme est daté (« lu le … sur la page de l'éditeur ») ou `[H]`.
8. **Lire la matrice, ne pas la sommer.** Dégager l'option retenue et le repli. Si les décideurs ne
   s'accordent pas sur ce qui compte, leur faire classer les trois critères les plus importants et
   relire la matrice avec ce classement.
9. **Éprouver la recommandation.** Contre-argument le plus fort ; ce qui doit être vrai, chaque
   condition avec la personne qui la confirme ; ce qui ferait changer d'avis ; condition d'arrêt
   observable. Examiner le repli avec la même grille. Si le contre-argument est plus fort que les
   raisons, changer de recommandation.
10. **Écrire la fiche en commençant par la recommandation**, finir par la décision attendue, proposer
    `chiffrer-rentabilite` (business case de l'option retenue et du repli). Quand le décideur
    tranche, ajouter une ligne à `mission/journal.md`. Une solution imposée par le client suit le même
    chemin : la matrice vérifie qu'elle couvre les exigences et documente un repli ; le journal note
    « option imposée par <rôle> ». Si l'option retenue est la 0, la suite se décide avec le client :
    un plan de simplification, ou la fin de la mission du cas.

## Le livrable

Modèle de `mission/cas-<slug>/40-solutions.md` :

```markdown
# Solutions — <titre court>

Date · Décideur (rôle) · Rédigé par · Exigences lues : 30-exigences du <date>

## 1. Recommandation
**Option retenue** : <numéro et nom>, construite par <interne · éditeur · recrutement · indépendant · prestataire>.
**Trois raisons porteuses** : 1. … 2. … 3. …
**Ce qui doit être vrai** : chaque condition avec la personne qui peut la confirmer `[H]`.
**Contre-argument le plus fort** : …
**Ce qui ferait changer d'avis** : …
**Condition d'arrêt** : le signal observable, avec son seuil, qui fait arrêter ou revenir au repli.
**Option de repli** : <option>, et pourquoi elle vient en second.

## 2. Faut-il automatiser ?
| Facteur | Valeur | Statut et source |
Quatre lignes : fréquence · temps gagné par occurrence · taux d'erreur à la main · stabilité du processus.
Verdict : automatiser · standardiser d'abord · assister seulement · ne rien construire — et pourquoi.

## 3. Le chemin le plus simple
La question, la réponse, ce qu'on supprime ou simplifie avant tout.

## 4. Où l'humain reste dans la boucle
| Étape du processus cible | Niveau (automatisée · préparée puis validée · humaine) | Pourquoi | Rôle qui valide |

## 5. Les options examinées
| N° | Famille | Retenue pour la matrice ? | Pourquoi |
Huit lignes, de 0 (ne rien construire) à 7 (hybride). Pour chaque option retenue : en quoi elle
consiste, qui la construit, ce qui existe déjà et se réutilise, ce qui a été vérifié (où, quand) ou `[H]`.

## 6. Matrice
Éliminatoires : exigence Indispensable non couverte · contrainte ferme violée (outil imposé, budget
plafond, lieu des données).
| Critère | Option A | Option B | Option C |
Une colonne par option, et deux pour une même option si deux profils de constructeur sont plausibles
(coût, délai et maintenance changent). Neuf lignes : couverture des exigences · coût de construction ·
coût de fonctionnement (unité facturée × volume) · maintenance · fiabilité et risque · sécurité et
lieu des données · dépendance et portabilité · compétences internes pour maintenir · délai.
Cellule : favorable · acceptable · défavorable, une raison courte, le statut du chiffre.

## 7. L'option de repli
Même grille de lecture que l'option retenue : raisons, conditions, contre-argument.

## 8. Plateforme ou code
Seulement si une option passe par une plateforme sans code : unité de facturation, volume, ordre de
grandeur du coût mensuel `[E]`, page de l'éditeur lue (date) ou `[H]`, façon d'en sortir.

## 9. À vérifier avant de signer
Hypothèses `[H]` restantes, qui les confirme, avant quelle date.

## 10. Questions ouvertes
`?` …

## Décision attendue
Choisir l'option retenue, le repli ou l'option 0 (ne rien construire), et dire qui construit.
```

Ligne de journal, au moment où le décideur tranche (exemple fictif) :

```markdown
- 2026-10-28 · cas-relances-factures · 40-solutions validé par la direction financière · « option 4 retenue, construite par un indépendant ; repli : option 1 »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| La porte d'entrée avant les options | un processus instable ou rare fait échouer une automatisation plus sûrement qu'un mauvais outil | comparer les outils directement | le client a déjà acté qu'il automatise et le diagnostic montre un processus stable : la porte se remplit en deux lignes |
| Matrice lue, pas additionnée | une somme pondérée cache l'arbitrage et donne une fausse précision | un score total sur cent | les décideurs demandent un classement chiffré : on le fournit en plus, pondérations visibles |
| L'option 0 toujours dans la matrice | c'est la moins chère, et elle n'a aucun défenseur naturel : personne ne la propose | ne comparer que des constructions | jamais |
| Capacités et prix datés ou `[H]` | ils changent en quelques mois ; une valeur recopiée ressemble à une valeur mesurée | un tableau de prix figé dans la compétence | jamais |
| Repli examiné avec la même grille | un repli qui n'est qu'un nom rend la condition d'arrêt théorique | « on verra plus tard » | le décideur écarte explicitement le repli |
| Validation humaine par défaut sur l'irréversible | une erreur confiante à l'échelle coûte plus qu'un clic | autonomie totale d'emblée | un pilote montre un taux d'erreur très bas et l'action est réversible : on desserre, par décision écrite |

## Frontières

- Les exigences, entrée obligatoire de cette étape → `rediger-cahier-des-charges` (mode exigences).
- La spécification détaillée de l'option retenue → `rediger-cahier-des-charges` (mode spécification).
- Gains, coûts complets, scénarios, retour sur investissement → `chiffrer-rentabilite` ; ici,
  seulement un ordre de grandeur du coût de fonctionnement, pour comparer.
- Le processus actuel, ses mesures et ses causes → `auditer-processus`.
- Calendrier, pilote planifié, formation, pré-mortem → `planifier-deploiement`.
- L'état de la mission et le journal des décisions → `router-mission-ia`.
- Construire l'automatisation ou l'agent : hors du pack.
- Facultatif : si `automation-strategy` est installé, il peut approfondir le choix de plateforme ; si
  `router-consulting-strategy` l'est, l'arbitrage d'affaires entre options. Ne dire qu'on s'en est
  servi que s'ils ont réellement été appelés.

## Preuves restantes

- À éprouver sur la mission fictive de `examples/` (dossier vide à la rédaction) : la fiche doit se
  remplir avec l'option 0 dans la matrice et un repli examiné.
- NON MESURÉ sur une mission réelle : le premier cas réel dira si neuf critères sont trop ou trop
  peu, et si la porte d'entrée qualitative suffit sans seuils chiffrés.
- Sources et crédits : porte d'entrée « faut-il automatiser », piège du processus cassé, unités de
  facturation, comparaison plateforme ou code et anti-motifs adaptés de la compétence
  `automation-strategy` d'Eric Risco (MIT, https://github.com/ericrisco/rsc-harness) ; options
  réelles, contre-cas et recommandation d'abord inspirés de `router-consulting-strategy`
  (https://github.com/Gremelinn0/claude-skill-hub) ; matrice comparative inspirée de la compétence
  `vendor-review` du plugin `operations` d'Anthropic (Apache-2.0,
  https://github.com/anthropics/knowledge-work-plugins). Réécrit avec nos mots.
