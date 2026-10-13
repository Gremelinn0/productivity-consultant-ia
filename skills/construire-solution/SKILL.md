---
name: construire-solution
description: >-
  Quand la spécification et le plan sont validés, la porte constatée (ou sans objet) et qu'il faut
  construire la solution retenue (« construis le flux », « implémente la spécification », « build the
  workflow ») → construire par tranches contrôlables, dans un environnement d'essai nommé, sur des
  données fictives ou anonymisées, avec les garde-fous de la spécification dès la première tranche qui
  agit (simulation des envois, clé de dédoublonnage, journal, reprise sur erreur, secrets jamais en
  clair) ; chercher d'abord un modèle existant ; tracer les écarts avec la spécification ; écrire la
  fiche d'exploitation ; rendre une version gelée prête pour la recette. Étape 80 de la porte « besoin
  connu » du pack consultant-ia, après le plan. Triggers : « construire la solution », « implémenter »,
  « build », « workflow », « environnement d'essai », « sandbox », « mode simulation », « dry run »,
  « fiche d'exploitation », « version gelée », « n8n », « Make », « Zapier ».
metadata:
  scope: "la construction de l'option retenue et spécifiée, dans un environnement d'essai et sur des données fictives ou anonymisées, jusqu'à une version gelée prête pour la recette"
  owns: "le découpage en tranches, l'environnement d'essai, les garde-fous construits, la recherche d'un modèle existant avant de construire, le registre des écarts avec la spécification, le journal des versions, la fiche d'exploitation, la liste de ce qui reste au client"
  consumes: "60-specification (version lue), 40-solutions (option, plateforme, porte), 70-plan (lots, porte, limites du lot), 30-exigences et 50-rentabilite du cas ; mission/sources/ ; mission/journal.md ; COMPAGNONS.md du pack"
---

# Construire la solution

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/80-construction.md` et le dossier
> `mission/cas-<slug>/80-construction/`. Preuve : le valideur déclare une version précise « prête pour la
> recette », et la décision s'inscrit dans `mission/journal.md`. Contrôle de forme : le document porte les
> onze rubriques du modèle ; l'environnement d'essai est nommé et son isolement essayé ; la porte est
> constatée au journal, sans objet ou sautée à la demande d'un rôle nommé ; chaque exigence Indispensable
> ou Importante de la phase a sa tranche et aucune tranche n'est sans exigence ; chaque garde-fou de
> `60-specification` §7 à §11 est construit ou écarté par un écart tracé ; chaque contrôle de tranche est
> exécuté (commande ou procédure, sortie, date) ou prévu, jamais « réussi » sans preuve ; aucun secret ni
> donnée personnelle dans le dossier, avec la méthode du contrôle ; la fiche d'exploitation répond aux quatre
> questions (comment vérifier que ça marche, que faire en cas d'incident, qui joindre, comment revenir en
> arrière) ; la version est numérotée, exportée et gelée avec son empreinte ; chaque nombre a son statut
> `[F]`, `[H]` ou `[E]` (définis dans `ARCHITECTURE.md`). Exemple de référence : `examples/` du pack
> (cas fictif : maquette exécutable en six tranches, deux versions gelées). **Boucle** : aucune.

## Ce que cette compétence résout

Entre une spécification validée et un dispositif qui marche, les projets se perdent de la même façon :
on construit d'un bloc, on teste à la fin, et l'on découvre qu'un envoi réel était possible depuis le
premier jour, qu'un même événement crée deux écritures, qu'un secret traîne dans un export, et que
personne ne sait quoi faire quand le flux s'arrête. Cette compétence construit l'option retenue par
petites tranches qu'on peut contrôler, dans un environnement d'essai où rien de réel ne peut partir, avec
les garde-fous de la spécification posés dès que quelque chose agit.

Résultat attendu : une version numérotée et gelée, prête pour la recette (`tester-solution`) ; ce qui est
construit, où, et ce qui diffère de `60-specification` ; la fiche d'exploitation d'une page, qui dit comment
vérifier que ça marche, que faire en cas d'incident, qui joindre et comment revenir en arrière ; la liste de
ce qui reste au client dans ses propres outils.

## Stratégie

1. **La spécification fait foi ; la construction ne l'améliore pas.** Une fonction ajoutée « parce que
   c'est facile » est une dérive, une fonction oubliée un manque : chaque exigence Indispensable ou
   Importante de la phase a sa tranche, chaque tranche sert au moins une exigence. Ce que la construction
   découvre (un trou, une règle ambiguë, un connecteur qui ne sait pas) est un écart : il se trace et se
   traite à son niveau (étape 7), jamais en silence.
2. **Des tranches qu'on contrôle, pas un bloc.** Une tranche est un comportement de bout en bout (une
   entrée, une sortie qu'on peut lire) qui couvre des étapes de `60-specification` §4 ; quand un défaut
   apparaît, on sait dans quelle tranche. Une tranche n'est pas un lot de `70-plan` : le lot est une
   période du projet, la tranche un morceau de la construction. Le constructeur contrôle chaque tranche
   mais ne déclare aucun critère d'acceptation « réussi » : la recette le dit, sur une version gelée.
3. **Rien de réel ne peut partir de l'essai** (règle 7, `ARCHITECTURE.md`). L'essai a un nom, des comptes
   de test sans droit d'envoi ni d'écriture chez un tiers, des données fictives. Une consigne (« ne pas
   envoyer ») se retourne par erreur, l'absence de droit non. Le mode simulation est le mode par défaut ;
   passer au réel n'est pas un réglage du constructeur : c'est une action sur un outil réel, proposée en
   `90-mise-en-service` et faite par le client après validation de cette action.
4. **Les garde-fous se construisent avec la première tranche qui agit.** Un dispositif livré chemin
   heureux d'abord marche jusqu'au premier incident, et « la fin » n'arrive jamais. Journal d'exécution,
   simulation, interrupteur, clé de dédoublonnage, reprise : au socle (tranche 0) ou à la première
   tranche qui écrit quelque chose. Détail et contrôle de chacun : `references/garde-fous.md`.
5. **Toute plateforme se construit sous le même contrat.** Versions fixées ; identifiants réels relus dans
   l'outil, jamais supposés ; secrets dans le coffre de la plateforme ; simulation ou environnement isolé ;
   relecture des changements avant de les appliquer ; autorisation avant tout effet externe ; état
   réellement enregistré relu après chaque écriture ; sauvegarde et retour arrière définis avant la mise en
   service (`references/garde-fous.md`, partie 1). Le compagnon d'une plateforme (`COMPAGNONS.md`) apporte
   la syntaxe et les pièges de son outil, pas un autre contrat, et ne choisit jamais une autre plateforme
   que celle décidée en `40-solutions`.
6. **Ce qui existe d'abord** (règle 6, `ARCHITECTURE.md`). Avant d'écrire, chercher un modèle publié (bibliothèques de
   modèles des éditeurs de flux, flux publics, brique interne) et le contrôler : auteur, autorisations
   demandées, coût à l'exécution, ce qu'il fait en plus de ce qu'on veut. Il se lit en entier avant
   l'import, et s'importe désactivé, dans l'essai seulement. Non cherché ou introuvable faute d'accès :
   « non vérifié `[H]` », jamais « n'existe pas ».
7. **Les secrets restent chez le client.** Le pack n'en lit ni n'en écrit aucun. Les connexions de test
   sont créées par le client dans le coffre de l'outil ; la construction n'en connaît que le nom, et la
   fiche d'exploitation dit où chacun est rangé et qui en répond, jamais sa valeur. Tout ce qui se range
   dans `80-construction/` (export, script, journal, capture) est balayé avant d'être rangé. Un secret
   aperçu par accident n'est pas recopié : on le signale, le client le révoque.
8. **Des données fictives, ou anonymisées et dites telles.** Le jeu d'essai reproduit la structure et les
   proportions d'une situation réelle (par exemple le rejeu d'une séance observée) sans donnée
   personnelle. Fictif de préférence ; anonymisé quand le sens l'exige, par le client ou avec lui, avec
   la méthode écrite et un contrôle de ce qui reste. « Anonymisé » est une affirmation qui se vérifie.
9. **Une étape d'IA se construit bornée et se règle sur un jeu à part.** Rôle borné, consignes
   versionnées, sortie vérifiée avant usage, abstention possible ; liste fermée d'actions et plafonds
   pour un agent. Les consignes se règlent sur un jeu de mise au point : le jeu d'évaluation de
   `tester-solution` ne sert pas à les régler.
10. **Une version, une empreinte, un retour arrière essayé.** Chaque état livré a un numéro, une date, un
    export rangé et une empreinte. La recette porte sur une version gelée ; toute modification ensuite
    est une nouvelle version dont les tests se rejouent. C'est aussi le sort d'un défaut `D-xx` rendu par
    la recette, le pilote ou l'exploitation : correction en nouvelle version, tests rejoués en 85 avant
    toute nouvelle action en 90, hors mesures d'attente. Un retour arrière jamais essayé n'en est pas un :
    la version précédente est restaurée une fois dans l'essai, durée relevée.
11. **La construction relève ce qu'elle apprend sur les chiffres.** Effort réel, consommation sur le rejeu
    (unité facturée × volume), limites rencontrées, maintenance pressentie : comparés aux seuils de
    `50-rentabilite`. Un dépassement remonte au décideur et à `chiffrer-rentabilite`, il ne se corrige
    pas en silence. Ces relevés `[F]` serviront à `mesurer-gains`.

## Étapes

1. **Vérifier le point de départ.** `40-solutions` retient-il quelque chose à construire ? Option 0 seule :
   cette étape n'a pas d'objet ; le dire, ne produire aucun livrable 80 ni 85, et passer à
   `piloter-mise-en-service`, dont le registre porte les simplifications qui touchent un outil. Sinon, lire
   `mission/journal.md` et le dossier du cas : `60-specification` validée (noter la version lue), `70-plan`
   validé, et la porte de `40-solutions` §10 (reprise en `60-specification` §1) constatée par une ligne du
   journal avec sa pièce, ou « sans objet ». Porte non constatée : dire ce qui manque et proposer l'étape
   de `70-plan` qui la constate ; si le décideur maintient sa demande, construire avec « porte sautée à la
   demande de <rôle> » en tête du livrable et faire inscrire l'étape sautée au journal. Lire « ce qu'on ne
   fait pas dans ce lot » de `70-plan` : ce sont des limites de la construction. Dire qui construit
   (`40-solutions` §5) : le pack, seul ou avec un compagnon, ou un tiers (le pack prépare alors les tranches
   et les garde-fous, reçoit la livraison et en contrôle chaque point). Dire la plateforme : celle de
   `40-solutions` ; si `40` ne nomme que la famille, celle que le plan a arrêtée (devis, page de l'éditeur
   lue) et que le décideur a confirmée au journal ; sinon question bloquante `Q-xx`, et la construction
   attend.
2. **Chercher ce qui existe : première action de construction.** Reprendre la famille 2 de `40-solutions`
   §5, souvent « non vérifié `[H]` », pour la plateforme décidée en 40 : bibliothèques de modèles des
   éditeurs de flux, flux publics, briques internes (`references/garde-fous.md`, partie 6). Par candidat :
   auteur, dernière mise à jour, licence, exigences couvertes, autorisations demandées, coût à
   l'exécution, ce qu'il fait en plus (appels externes, envois). Décision : base · inspiration · rien, avec
   la raison. La recherche est bornée par une durée annoncée avant ; sans accès aux pages : « non vérifié
   `[H]` » et le rôle qui peut la faire. Rien ne s'importe avant que l'essai existe (étape 3).
3. **Poser l'environnement d'essai.** Un nom, donné une fois (`essai-<slug>`) et repris tel quel en 85 et
   90 ; où il vit, qui le détient, les comptes de test (de service, droits minimaux, jamais personnels),
   ce qui n'y existe pas (envoi réel, écriture chez un tiers, secret de production). Lister ce que le
   client doit mettre à disposition, avec le rôle et la date. Prouver l'isolement : un accès de test à la
   production échoue, et le mode simulation écrit dans une sortie simulée au lieu d'agir. Données : jeu
   d'essai fictif ou anonymisé, produit par qui, contrôlé comment (`references/garde-fous.md`, partie 3).
4. **Choisir le compagnon de la plateforme.** Ouvrir `COMPAGNONS.md` du pack à la ligne de la plateforme
   décidée en `40-solutions` (flux sans code, scénario, script, agent, serveur d'outils). Compagnon listé
   et disponible dans la session : l'appeler pour ce qui est propre à l'outil (syntaxe, composants,
   débogage), et ne dire qu'on s'en est servi que s'il a réellement été appelé. Aucun compagnon : méthode
   de repli maison, dite telle (`references/garde-fous.md`, partie 5). Dans les deux cas le tronc reste
   celui-ci : tranches, garde-fous, écarts, fiche, version gelée.
5. **Découper en tranches.** Tranche 0, le socle (essai nommé, mode simulation, journal d'exécution,
   interrupteur, réglages), puis une tranche par comportement de bout en bout : d'abord ce qui porte le
   cas limite critique de `60-specification` §12 et les validations humaines, le reste par valeur. Pour
   chaque tranche : étapes de §4, exigences servies, tests de §12 qu'elle rend exécutables, garde-fous
   posés, contrôle prévu. Les réglages du pilote (§4, §13) sont des paramètres construits, pas des
   retouches à la main le jour J. La table exigence → tranche ne laisse aucune exigence orpheline.
6. **Construire, une tranche après l'autre.** Pour chacune : construire (versions fixées, identifiants
   relus dans l'outil, règles dans des données lisibles par leur propriétaire plutôt que dans la
   logique), relire le changement avant de l'appliquer, relire l'état enregistré après chaque écriture,
   exécuter le contrôle de tranche et noter le résultat (exécuté avec sa preuve, ou prévu). Passer à la
   suivante seulement si le contrôle passe. Étape d'IA : `references/garde-fous.md`, partie 4.
7. **Tracer les écarts avec la spécification.** Chaque fois que la construction diffère de `60` ou la
   complète, une ligne : rubrique concernée, constat, traitement. Une précision qui change un comportement,
   un seuil ou un nombre → version datée de `60-specification`, ligne « correction » au journal, valideur
   informé (`ARCHITECTURE.md`). Un trou à trancher → question `Q-xx`, à la suite de la série de `60` §16.
   Un écart soupçonné, non confirmable à la construction, s'écrit aussi : « soupçon », avec le test de 85.
   Ce que la plateforme de `40-solutions` ne sait pas faire → la tranche s'arrête et le décideur tranche
   avec `concevoir-solution` ; aucune autre plateforme n'est prise en douce. Un choix de réalisation sans
   effet visible (un nom, un ordre interne) n'est pas un écart.
8. **Relever ce que la construction apprend sur les chiffres.** Effort réel (heures par rôle, source),
   consommation sur le rejeu comparée à `40-solutions` §8, limites de la plateforme rencontrées,
   maintenance pressentie. Comparer aux seuils de `50-rentabilite` ; un dépassement est dit au décideur,
   avec renvoi à `chiffrer-rentabilite`. Sans relevé : `[H]`, et le rôle qui peut le fournir.
9. **Geler une version.** Passer la liste « prêt pour la recette » (`references/modeles.md`, partie D) :
   tranches contrôlées, garde-fous construits ou écartés par un écart tracé, simulation et retour arrière
   essayés, livraison balayée (secrets, données personnelles), écarts traités, version numérotée avec son
   empreinte et plus rien de modifié depuis. Une case « non » : la version n'est pas gelée. Une maquette
   se gèle « pour la recette de la maquette » (partie D) : la recette sur la plateforme reste à faire.
10. **Écrire la fiche d'exploitation et ce qui reste au client.** La fiche d'une page
    (`references/modeles.md`, partie B) : ce que fait le dispositif, puis toujours quatre réponses, sous
    ces quatre titres : comment vérifier que ça marche (quoi regarder, où, quand, résultat normal) ; que
    faire en cas d'incident (par symptôme : première action, qui prévenir, quand suspendre) ; qui joindre
    (rôles, suppléants, escalade) ; comment revenir en arrière (interrupteur, ancienne méthode, version
    précédente). Aucune n'est omise ni renvoyée à l'oral : `90-mise-en-service` les vérifie, les fait
    dérouler par un tiers, et toute lacune revient ici par version datée. Puis la liste, sans rien faire :
    secrets à poser dans le coffre, comptes à créer, accès à ouvrir, import dans les outils réels, passage
    de la simulation au réel. Chaque ligne deviendra une action `A-xx` (action sur un outil réel) proposée
    en `90-mise-en-service` avec son retour arrière.
11. **Finir par la décision attendue** : prêt pour la recette (version X), ou écarts à trancher. Proposer
    `tester-solution`. Quand le valideur tranche, ajouter une ligne à `mission/journal.md`.

## Le livrable

Le modèle complet, ses consignes de remplissage, la fiche d'exploitation, le journal des versions et la
liste « prêt pour la recette » sont dans `references/modeles.md` : l'ouvrir pour rédiger. Les titres
ci-dessous sont ceux du modèle.

Squelette de `mission/cas-<slug>/80-construction.md` :

```markdown
# Construction — <titre court>
Date · Option construite (40-solutions) · Construit par (rôle) · Valideur (rôle) · Décideur (rôle) · Rédigé par · Version · Spécification lue (version)
Mode : <le pack construit | avec un compagnon | un tiers construit, le pack contrôle> · Porte : <constatée le …, pièce | sans objet | sautée à la demande de …>
## 1. Point de départ — livrables lus (versions), phase construite, limites du lot
## 2. Ce qui existait déjà — recherche d'un modèle, décision
## 3. Environnement d'essai — nom, comptes de test, données, isolement essayé
## 4. Plateforme et compagnon — plateforme de 40, compagnon ou repli, versions fixées
## 5. Tranches — du socle à la dernière : contrôle de chacune, table exigence → tranche
## 6. Garde-fous — chaque garde-fou de 60 §7 à §11 : où il est construit, comment il a été contrôlé
## 7. Livré — où, en quelle version, empreinte, balayage des secrets
## 8. Écarts avec la spécification — rubrique, constat, traitement
## 9. Chiffres relevés — effort, consommation, limites, maintenance, comparés à 50
## 10. Fiche d'exploitation (ses quatre réponses : vérifier, incident, joindre, revenir en arrière) et ce qui reste au client
## 11. Questions ouvertes
## Décision attendue
```

Le dossier `80-construction/` range ce que le pack écrit : `journal-versions.md`, `fiche-exploitation.md`,
`donnees-essai/`, `sorties-simulees/`, `livraison/` (code, export du flux sans secret, règles, modèles de
messages). Ligne de journal, quand le valideur tranche (exemple fictif) :

```markdown
- 2026-11-10 · cas-relances-factures · 80-construction validé par le responsable financier · « version 1.0 gelée pour la recette ; deux écarts traités, une question ouverte »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Des tranches contrôlables | un défaut se localise ; un bloc testé à la fin ne dit pas lequel de ses morceaux est faux | construire d'un bloc, tester à la fin | la solution tient en une seule étape : une tranche suffit |
| Garde-fous avec la première tranche qui agit | un dispositif sans journal, sans arrêt ni dédoublonnage marche jusqu'au premier incident | chemin heureux d'abord, garde-fous ensuite | jamais |
| Absence de droit plutôt que consigne ; simulation par défaut | une consigne se retourne par erreur, un droit absent non | écrire « ne pas envoyer » dans la fiche | un test exige un vrai envoi, même vers une boîte de test : le client crée une boîte de capture propre à l'essai et valide cette action précise |
| Un tronc maison, un compagnon par plateforme | la méthode (tranches, garde-fous, écarts) ne change pas d'une plateforme à l'autre ; la syntaxe, si | écrire dans le pack la méthode de chaque plateforme | une plateforme revient dans presque toutes les missions et son compagnon n'est plus tenu |
| Le constructeur ne déclare aucun critère « réussi » | celui qui construit voit ce qu'il a voulu faire ; la recette doit pouvoir échouer | confondre contrôles de tranche et recette | jamais |
| L'écart se trace dans la spécification | deux documents qui divergent font passer la recette sur un comportement que personne n'a validé | corriger la construction seulement | choix de réalisation sans effet visible : pas un écart |
| Données fictives ou anonymisées, jamais « juste pour voir » | une donnée réelle dans un dossier de mission ou un outil d'essai est une fuite que personne ne verra | rejouer sur un export réel | le client rejoue chez lui et ne rend que des résultats sans donnée personnelle |

## Frontières

- Les exigences, la spécification et ses garde-fous (étapes, erreurs, dédoublonnage, secrets,
  observabilité, tests) → `rediger-cahier-des-charges` ; une précision trouvée en construisant y retourne
  par version datée.
- Le choix de l'option, de la plateforme, de qui construit et de la porte → `concevoir-solution` ; le
  constat de la porte et le calendrier → `planifier-deploiement`.
- Coûts, point mort, hypothèses `[H]` → `chiffrer-rentabilite` (elle recalcule, ici on relève).
- Exécuter la recette, saboter les tests, évaluer l'IA, tenir le registre des défauts `D-xx`, rendre le
  verdict → `tester-solution`.
- Toute action sur un outil réel (importer en production, activer, envoyer, écrire chez un tiers, créer
  des comptes ou poser des secrets de production) → proposée en `piloter-mise-en-service` avec son retour
  arrière, faite par le client après validation de l'action. Les comptes et secrets de l'essai sont créés
  par le client avant la construction.
- Mesurer le gain réel → `mesurer-gains`. L'état de la mission et le journal → `router-mission-ia`.
- Plateformes et compagnons → `COMPAGNONS.md` du pack.
- Un écart qui remet l'option en cause renvoie à `concevoir-solution`, par le routeur (`router-mission-ia`).

## Preuves restantes

- Rédigée le 12/10/2026. Essayée sur la mission fictive de `examples/` : maquette exécutable en six tranches, 28 contrôles
  de tranche verts en 1.0 et en 1.1, balayage sans reste, retour arrière essayé en 0,5 s, deux versions gelées « pour la recette
  de la maquette ». La recette a trouvé quatre défauts de logique (D-03 à D-06), dont deux soupçonnés à l'écriture et non tracés
  en rubrique 8 (d'où la ligne « soupçon ») : le constructeur était aussi le testeur. Aucune plateforme touchée.
- NON MESURÉ : si onze rubriques et un socle (tranche 0) suffisent à une vraie construction ; si la liste
  « prêt pour la recette » attrape les défauts que la recette trouverait sinon ; ce que coûte le balayage
  des secrets ; si un tiers peut suivre la méthode de repli sans compagnon.
- Sources et crédits : méthodes générales (tranches de bout en bout, mode simulation, relecture après écriture,
  empreinte d'une version). Compagnons crédités dans `COMPAGNONS.md`, jamais copiés ici. Réécrit avec nos mots.
