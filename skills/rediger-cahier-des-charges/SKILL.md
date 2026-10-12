---
name: rediger-cahier-des-charges
description: >-
  Quand le besoin est cadré et diagnostiqué et qu'il faut l'écrire pour consulter des prestataires ou
  comparer des solutions (« rédige le cahier des charges », « écris les exigences »), ou quand l'option
  est choisie et chiffrée et qu'il faut la spécifier pour l'équipe qui construit (« écris le PRD »,
  « la spécification de l'agent ») → rédiger, selon l'état du dossier, soit les exigences sans nommer
  de solution, soit la spécification complète de l'option retenue : étapes, données, erreurs, tests,
  porte et pilote, indicateurs. Troisième et sixième étapes de la porte « besoin connu » du pack
  consultant-ia. Triggers : « cahier des charges », « exigences », « expression des exigences »,
  « spécification fonctionnelle », « PRD », « requirements », « critères d'acceptation », « user
  stories », « appel d'offres », « RFP ».
metadata:
  scope: "les exigences d'un besoin cadré, avant le choix d'une solution, ou la spécification de l'option retenue et chiffrée"
  owns: "le cahier d'exigences (mode exigences) et la spécification de type PRD (mode spécification), leurs deux modèles, la priorisation des exigences, les critères d'acceptation, les indicateurs (identifiants IND), leur protocole de lecture et leurs seuils de production"
  consumes: "10-besoin et 20-diagnostic du cas ; mission/sources/ ; mission/journal.md pour choisir le mode ; en mode spécification, 30-exigences, 40-solutions (dont la porte) et 50-rentabilite"
---

# Rédiger le cahier des charges

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/30-exigences.md` (mode exigences) ou
> `mission/cas-<slug>/60-specification.md` (mode spécification). Preuve : le demandeur valide le
> document, et la décision s'inscrit dans `mission/journal.md`. Contrôle de forme : le document porte
> les douze rubriques (exigences) ou les dix-sept (spécification) de son modèle, et la ligne qui annonce
> son mode ; chaque exigence a un identifiant et une priorité ; chaque indicateur un identifiant `IND-xx` ;
> chaque critère d'acceptation est testable ; chaque nombre a son statut `[F]`, `[H]` ou `[E]` (définis
> dans `ARCHITECTURE.md`) ; le mode exigences ne nomme aucune solution hors des rubriques Intégrations et
> Contraintes. Exemple de référence : `examples/` du pack. **Boucle** : aucune.

## Ce que cette compétence résout

« Cahier des charges » désigne deux documents qui ne servent pas à la même chose. Avant le choix
d'une solution, il fixe ce que le dispositif doit faire, pour consulter des prestataires ou comparer
des options sur un même énoncé : s'il nomme déjà une solution, la comparaison est faussée d'avance.
Après le choix, il décrit l'option retenue de façon que l'équipe qui construit n'ait aucune question
à poser : étapes, données, droits, erreurs, tests, pilote.

Résultat attendu : des exigences numérotées, classées et testables ; puis une spécification de type
PRD qu'un constructeur qui n'a pas vécu la mission peut suivre.

## Stratégie

1. **Le mode se lit dans le dossier, pas dans la demande.** On demande « le cahier des charges » à
   deux moments qui n'appellent pas le même document. Une spécification écrite sur une option non
   validée se jette dès que l'option change ; des exigences écrites après le choix ne servent plus
   qu'à le justifier.
2. **Décrire ce qu'il faut obtenir, pas la solution** (mode exigences). Une exigence qui nomme un
   outil ferme la comparaison avant qu'elle ait lieu. Test : en remplaçant l'outil par un autre, la
   phrase reste-t-elle vraie ? Non → elle décrit une solution, on la réécrit. Les systèmes en place à
   lire ou modifier sont des faits d'environnement : on les nomme une fois, en rubrique 6, avec une
   étiquette (S1, S2…) que les autres rubriques reprennent.
3. **Une exigence qu'on ne peut pas tester n'en est pas une.** « Rapide », « simple », « fiable » se
   disputent à la livraison, au moment le plus cher pour le découvrir. Chaque exigence reçoit un
   seuil, un cas et un moyen de vérification, écrits en critère d'acceptation. Les nombres d'un jeu
   d'essai sont des paramètres choisis : `[H]` s'ils sont inventés, `[F]` s'ils reprennent un relevé.
   Chaque nombre porte son statut (`[F]`, `[H]`, `[E]`, définis dans `ARCHITECTURE.md`).
4. **Classer sans complaisance.** Indispensable : sans elle, le dispositif ne règle plus le problème de
   `10-besoin`. Important : le cœur marche sans elle, l'usage en souffre. Souhaitable : confort. Si
   presque tout est indispensable, rien ne l'est, et `concevoir-solution` écarte des options à tort.
5. **Un identifiant par exigence, et tout s'y rattache.** Critères, tests et indicateurs renvoient à
   `EF-01`, `EF-02`… : on voit ce qui n'est testé nulle part et ce qui est construit sans avoir été
   demandé.
6. **Les garanties d'exécution se spécifient avant la construction.** Erreurs, doublons, secrets,
   journal, interrupteur d'arrêt : un dispositif livré sans eux marche jusqu'au premier incident, puis
   personne ne sait quoi faire. Ce sont des exigences, pas des détails de réalisation.
7. **Un indicateur sert une décision, et ses seuils vivent à un seul endroit.** Sans décision au bout,
   c'est de la décoration ; sans mesure de départ, on ne saura jamais s'il a bougé ; sans prudence sur
   l'attribution, on s'attribuera un gain dû à la saison. Les exigences nomment l'indicateur (`IND-xx`), sa
   raison et sa cible ; la spécification fixe son protocole et ses seuils de production ; le pilote a ses
   propres seuils, dits comme tels.
8. **Écrire pour quelqu'un qui n'a pas vécu la mission.** Le lecteur est un prestataire ou une équipe
   de construction : pas de renvoi à « la réunion de mardi », sigles définis, inconnues écrites comme
   telles.

## Étapes

1. **Choisir le mode d'après le dossier.** Lire `mission/journal.md` et `mission/cas-<slug>/`. Si le
   journal porte, pour ce cas, la validation de `40-solutions` et celle de `50-rentabilite` avec la
   décision d'y aller → mode spécification. « Mesurer d'abord » y mène aussi quand la mesure est au
   calendrier : la spécification se prépare, la construction attend la porte de `40-solutions` ; « ne pas y
   aller » n'ouvre pas la spécification. Sinon → mode exigences. Annoncer le mode et sa raison en une ligne,
   écrite en tête du livrable ; le routeur peut annoncer un mode : on le recalcule, le dossier fait foi.
   - Spécification demandée alors que 40 ou 50 n'est pas validé : dire ce qui manque et proposer
     `concevoir-solution` ou `chiffrer-rentabilite`. Si la personne maintient sa demande, écrire la
     spécification avec « option imposée par <rôle> » en tête et les coûts non chiffrés en `[H]`, et
     faire inscrire l'étape sautée au journal.
   - `10-besoin` ou `20-diagnostic` manque en mode exigences : le dire et proposer `cadrer-besoin` ou
     `auditer-processus`. N'écrire malgré tout que sur demande, avec `[H]` sur ce que le diagnostic
     aurait mesuré.
2. **Lire ce qui existe**, sans reposer ce qui est répondu : `10-besoin`, `20-diagnostic`,
   `mission/sources/` ; en mode spécification aussi `30-exigences`, l'option retenue, son repli et sa porte dans
   `40-solutions`, `50-rentabilite`. Si `30-exigences` existe déjà et doit changer : version suivante datée
   (1.1), mêmes identifiants, ligne « correction » au journal (`ARCHITECTURE.md`), et dire si `40-solutions` ou
   `50-rentabilite` sont à revoir.
3. **Mode exigences : dérouler le modèle** (`references/modeles.md`, partie A) dans l'ordre. Reprendre
   du dossier tout ce qui y figure ; écrire d'abord le processus cible en mots, les exigences en
   découlent ; poser en une seule fois les questions qui manquent, les plus décisives d'abord. Ce qui reste sans
   réponse va en rubrique 12, avec le rôle qui répond ; une réponse reçue s'y date.
4. **Classer et rendre testable.** Donner à chaque exigence un identifiant et une priorité (Stratégie
   4). Écrire au moins un critère d'acceptation par exigence Indispensable, « Donné / Quand / Alors »
   ou seuil mesurable avec son moyen de vérification ; couvrir cas nominal, erreur, limite, cas interdit.
5. **Définir les indicateurs.** Mode exigences : pour chacun, un identifiant `IND-xx`, son type (activité,
   qualité, conversion, résultat), la décision qu'il permet, sa mesure de départ avec son statut et la période où
   elle est fiable, la cible issue de `10-besoin` ; pas de seuils ici. Mode spécification : la fréquence de lecture,
   le responsable de la qualité de la donnée, les seuils de production (correction, alerte, arrêt ; « arrêt : sans
   objet » pour un indicateur de contexte) et la façon d'attribuer sans fausse causalité. À tout indicateur de volume
   ou de rapidité, associer un indicateur de qualité.
6. **Mode spécification : partir de l'option retenue** (`references/modeles.md`, partie B). Reprendre
   chaque exigence Indispensable et Important dans le comportement étape par étape, avec la table
   exigence → étape → test ; marquer les validations humaines décidées dans `40-solutions` ; faire de
   chaque « ce qui doit être vrai » un test ou une vérification du pilote ; reprendre la porte de
   `40-solutions`, avec sa mesure, son agrégation et sa date ; rédiger ensuite les garanties d'exécution (erreurs,
   dédoublonnage, secrets, observabilité, environnements).
7. **Aligner sur les chiffres.** Volumes et temps de maintenance de la spécification doivent concorder
   avec `50-rentabilite` ; en cas d'écart, le dire et renvoyer à `chiffrer-rentabilite` plutôt que
   corriger en silence. Le propriétaire de la maintenance (qui décide, détient les comptes) peut différer de celui qui
   fait les heures : le dire, le coût de `50-rentabilite` suit le taux de celui qui les fait.
8. **Relire avec le bon test.** Exigences : chercher les noms d'outils hors Intégrations et Contraintes,
   puis se demander si un prestataire pourrait chiffrer sans question bloquante. Spécification :
   lister les questions qu'un constructeur extérieur poserait ; chacune désigne une rubrique à compléter. Si
   une question révèle un trou dans `30-exigences`, corriger `30-exigences` par une version datée, pas
   seulement la spécification.
9. **Finir par la décision attendue**, proposer la suite (`concevoir-solution` après les exigences,
   `planifier-deploiement` après la spécification). Quand le demandeur valide, ajouter une ligne à
   `mission/journal.md`.

## Le livrable

Deux modèles. Les consignes de remplissage rubrique par rubrique, les tableaux types, un exemple de
ligne d'indicateur et le test du constructeur sont dans `references/modeles.md` : l'ouvrir pour
rédiger. Les titres ci-dessous sont ceux du modèle.

Squelette de `mission/cas-<slug>/30-exigences.md` (mode exigences) :

```markdown
# Exigences — <titre court>
Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle) · Rédigé par · Version
Mode exigences : <raison tirée du journal, en une ligne>
## 1. Contexte et objectifs — renvois vers 10-besoin et 20-diagnostic, vocabulaire défini
## 2. Utilisateurs et rôles — qui utilise, qui valide, qui est touché
## 3. Processus cible — décrit en mots, sans outil ; ce qu'il suppose déjà en place
## 4. Exigences fonctionnelles — EF-01… classées Indispensable / Important / Souhaitable
## 5. Données — sources, champs indispensables, seuils de qualité, exclusions, brutes / enrichies / validées, source qui tranche, données personnelles, volumes
## 6. Intégrations — systèmes à lire ou modifier (S1, S2…), accès disponibles
## 7. Exigences non fonctionnelles — sécurité, conformité (dont RGPD), disponibilité, délai, traçabilité, validation humaine, politique d'erreur
## 8. Contraintes — budget, calendrier, outils imposés
## 9. Critères d'acceptation — testables, un par exigence Indispensable au moins
## 10. Indicateurs — IND-xx, décision permise, départ, cible ; pas de seuils
## 11. Hors périmètre — avec la raison
## 12. Questions ouvertes — Q-xx, avec le rôle qui répond, bloquantes ou non
## Décision attendue
```

Squelette de `mission/cas-<slug>/60-specification.md` (mode spécification) :

```markdown
# Spécification — <titre court>
Date · Option retenue (40-solutions) · Demandeur (rôle) · Valideur (rôle) · Rédigé par · Version
Mode spécification : <raison tirée du journal, en une ligne>
## 1. Problème et objectif — renvois vers 10-besoin, 30-exigences, 50-rentabilite ; la porte reprise de 40-solutions
## 2. Non-objectifs — avec la raison
## 3. Utilisateurs et scénarios — « En tant que …, je veux …, afin de … »
## 4. Comportement étape par étape — avec les points de validation humaine (et le rôle borné du modèle d'IA, s'il y en a un)
## 5. Flux de données — d'où vers où, sous quelle forme, conservé combien de temps
## 6. Intégrations et droits — moindre privilège, comptes de service
## 7. Gestion des erreurs — reprises, file des échecs, alerte, interrupteur d'arrêt
## 8. Dédoublonnage — clé stable vérifiée avant toute écriture non répétable
## 9. Secrets — dans le coffre de l'outil, jamais en clair
## 10. Observabilité — journal, compte des réussites et échecs, alerte sur silence
## 11. Environnements et versions — test avant production, sauvegarde, retour arrière
## 12. Plan de test et recette — dont le cas limite critique
## 13. Pilote — périmètre, mode, seuils de poursuite et d'arrêt du pilote
## 14. Indicateurs — protocole de mesure et seuils de production
## 15. Risques — probabilité, impact, parade, signal d'alerte
## 16. Questions ouvertes
## 17. Propriétaire de la maintenance — par son rôle, avec un suppléant
## Décision attendue
```

Lignes de journal, au moment où le demandeur tranche (exemples fictifs) :

```markdown
- 2026-10-21 · cas-relances-factures · 30-exigences validé par la direction financière · « validation humaine avant tout envoi à un client »
- 2026-11-12 · cas-relances-factures · 60-specification validé par la direction financière et la direction informatique · « pilote sur une seule entité »
- 2026-11-14 · cas-relances-factures · 30-exigences corrigées (version 1.1 : EF-01 précisée) · confirmées par la direction financière · « une facture écartée une semaine revient la suivante »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Une compétence, deux modes | la spécification reprend les exigences et leurs identifiants : un seul vocabulaire | deux compétences séparées | la spécification devient assez lourde pour exiger sa propre méthode |
| Le mode se déduit du journal | un mode choisi à l'oreille produit une spécification sur une option non validée | demander le mode à chaque fois | jamais : le dossier se relit, il ne se devine pas |
| Exigences sans solution nommée | comparer des prestataires sur le même énoncé | écrire les exigences autour de l'outil que le client imagine | le client impose un outil : il passe en contrainte, nommé comme tel |
| Garanties d'exécution exigées dès la spécification | un dispositif sans chemin d'erreur ni arrêt marche jusqu'au premier incident | les laisser à l'équipe de construction | l'équipe applique un standard écrit qui les couvre : la spécification y renvoie |
| Trois niveaux de priorité | assez fin pour trier, assez simple pour être tenu | une note sur dix, ou quatre niveaux | des dizaines d'exigences à arbitrer : on ajoute un rang à l'intérieur d'un niveau |
| Seuils de production au seul protocole de la spécification | deux endroits pour des seuils proches finissent par diverger | des seuils dans les exigences et dans la spécification | jamais : les exigences nomment la cible, la spécification fixe les seuils |
| Pilote : seuils ici, calendrier ailleurs | la spécification dit quoi vérifier et à quel seuil poursuivre ou arrêter ; `planifier-deploiement` dit quand et avec qui | tout écrire dans la spécification | jamais : deux calendriers divergent |

## Frontières

- Le besoin, le périmètre, les critères de succès → `cadrer-besoin`.
- Le processus actuel, ses mesures et ses causes → `auditer-processus`.
- Le choix de l'option, sa porte et la matrice de comparaison → `concevoir-solution`.
- Gains, coûts, maintenance chiffrée, scénarios → `chiffrer-rentabilite`.
- Calendrier, simplifications, constat de la porte, déploiement, formation, communication, pré-mortem, rythme des
  revues d'indicateurs après déploiement → `planifier-deploiement` ; ici on fixe chaque indicateur, sa décision, son
  départ, sa fréquence de lecture souhaitée et ses seuils.
- L'état de la mission et le journal des décisions → `router-mission-ia`.
- Construire, tester en réel, mesurer le gain après déploiement : hors du pack.
- Facultatif : si le plugin `product-management` d'Anthropic est installé, sa compétence `write-spec`
  peut approfondir un PRD de produit logiciel. Ne dire qu'on l'a utilisée que si elle a réellement été
  appelée.

## Preuves restantes

- Éprouvée sur la mission fictive du 12/10/2026 (`examples/`), qui a relevé 94 frictions : les deux modèles se
  remplissent sans rubrique vide ni solution nommée dans les exigences, les corrections sont dans cette version.
- NON MESURÉ sur une mission réelle : le premier cas réel dira si douze et dix-sept rubriques sont
  trop ou trop peu, et si un prestataire peut chiffrer à partir des seules exigences.
- Sources et crédits : structure PRD, priorisation et critères d'acceptation inspirés de la compétence
  `write-spec` du plugin `product-management` d'Anthropic (Apache-2.0,
  https://github.com/anthropics/knowledge-work-plugins) ; garanties d'exécution (dédoublonnage, erreurs
  et file des échecs, secrets, observabilité, environnements) adaptées de la compétence
  `automation-strategy` d'Eric Risco (MIT, https://github.com/ericrisco/rsc-harness). Réécrit avec
  nos mots.
