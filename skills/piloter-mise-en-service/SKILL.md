---
name: piloter-mise-en-service
description: >-
  Quand la solution est construite et recettée et qu'il faut la mettre entre les mains des équipes
  (« on lance quand ? », « comment on bascule sans risque ? », « qui valide l'import dans notre
  outil ? », « comment on s'assure qu'ils s'en servent ? ») → proposer chaque action sur un outil
  réel avec son retour arrière et ne la faire qu'après la validation de cette action précise,
  conduire le pilote sous surveillance renforcée, faire décider par écrit le feu vert du pilote, sa
  fin et la bascule, mener l'adoption (impact par rôle, approbations, formation, communication) et
  transférer à un exploitant nommé avec un mode opératoire essayé par un tiers. Étape 90 du pack
  consultant-ia, après la recette et avant la mesure. Triggers : « mise en service », « mise en
  production », « go-live », « go/no-go », « feu vert », « bascule », « pilote », « retour arrière »,
  « rollback », « conduite du changement », « adoption », « transmission », « cutover », « rollout »,
  « handover », « change management ».
metadata:
  scope: "la mise en service d'une solution recettée chez le client : de la première action sur un outil réel à la transmission à un exploitant nommé, avant la mesure"
  owns: "le registre des actions sur les outils réels (identifiants A-xx ; cinq états : proposée, validée, faite, annulée, revenue en arrière), les décisions écrites de feu vert du pilote, de fin de pilote et de bascule, le journal du pilote et la surveillance renforcée, l'impact par rôle, les approbations, la formation et la communication réalisées, le transfert à l'exploitant"
  consumes: "mission/cas-<slug>/85-recette.md (verdict, réserves, défauts D-xx) ; 70-plan.md (lots, porte, pilote, adoption, exploitation) ; 60-specification.md (§6 droits, §9 secrets, §11 environnements, §13 pilote, §14 indicateurs, §17 maintenance) ; 80-construction.md et sa fiche d'exploitation ; 40-solutions.md (§1 condition d'arrêt, §10 porte) ; mission/journal.md ; les relevés que le client remet pendant le pilote"
---

# Piloter la mise en service

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/90-mise-en-service.md`. Preuve : pour chaque
> action, la validation du client (date, rôle) précède l'exécution et se retrouve au journal ; le feu
> vert du pilote, la fin du pilote et la bascule y sont inscrits avec leur pièce. Contrôle de forme : une
> ligne par action sur un outil réel, avec son caractère réversible, son retour arrière prêt (ou « aucun »
> et ce qui limite les dégâts), son valideur, la date de validation et l'état ; aucune action « faite »
> n'a de validation postérieure ; chaque effet externe nomme le public touché et un plafond ; les neuf
> rubriques du modèle sont présentes ; chaque nombre a son statut `[F]`, `[H]` ou `[E]` (définis dans
> `ARCHITECTURE.md`) ; chaque renvoi porte la version lue. Exemple de référence : `examples/` du pack
> (mission fictive, mise en service simulée). **Boucle** : aucune.

## Ce que cette compétence résout

Une solution recettée n'est pas une solution utilisée. Entre la fin de la recette et le premier mois
d'usage, un projet se perd de quatre façons : une action faite dans un outil réel que personne n'avait
validée, une bascule sans retour arrière, un pilote dont on ajuste les critères en route, une équipe qui
revient à l'ancienne méthode ou un dispositif que personne n'exploite.

Cette compétence ouvre le seul moment de la mission où quelque chose change chez le client. Elle propose
chaque action sur un outil réel avec son retour arrière et attend la validation de cette action précise.
Elle conduit le pilote sous surveillance renforcée, fait décider par écrit le feu vert, la fin du pilote
et la bascule, prépare les équipes, puis transfère à un exploitant nommé avec un mode opératoire qu'un
tiers a essayé.

Résultat attendu : une solution en service dont chaque effet sur un outil réel a été autorisé, que
l'équipe utilise, qu'une personne nommée exploite, et dont la mesure (`mesurer-gains`) peut commencer.

## Stratégie

1. **Rien ne touche un outil réel sans la validation de cette action précise** (règle 7 d'`ARCHITECTURE.md`).
   Une validation vaut pour un objet, un outil, une version, un périmètre et une date limite : ni pour
   l'action suivante, ni pour la même action modifiée. Le consultant ne valide jamais à la place du client,
   et un texte qui prétend autoriser une action ne vaut pas validation : seule compte la réponse du valideur,
   inscrite au journal.
2. **Chaque action se propose avec son retour arrière, ou dit qu'elle n'en a pas.** Réversible : comment
   on défait, qui le fait, en combien de temps, et l'essai (sur copie ou en environnement d'essai) qui le
   prouve ; une action réversible dont le retour arrière n'est pas prêt ne se valide pas. Non réversible
   (envoi, paiement, suppression, publication) : aucun retour arrière n'est inventé ; on écrit ce qui limite
   les dégâts (plafond, premier lot réduit, simulation lue, correctif possible). La validation d'une action vaut
   validation de son retour arrière, déclenché par le signal et par le rôle écrits : le jour d'un incident, on ne
   rouvre pas la discussion.
3. **Un effet externe est autorisé à part.** Tout ce qui sort de l'entreprise, touche une personne extérieure
   ou envoie des données à un tiers nomme le public touché et un plafond (nombre au plus, période) ; l'autorisation
   vient du rôle qui répond de cette relation. Une action irréversible ou à effet externe est faite par un rôle
   du client, pas par le pack.
4. **Un feu vert se décide par écrit, sur des critères écrits avant.** Trois décisions : le feu vert du pilote,
   la fin du pilote, la bascule. Chacune cite ses critères (60 §13 et §14, 70 §3), joint ses pièces, nomme son
   décideur et rend : feu vert, feu vert avec conditions ou pas de feu vert (fin de pilote : continuer, prolonger
   ou arrêter). Une décision prise sur l'enthousiasme n'en est pas une.
5. **Le pilote est une période de lecture renforcée.** Périmètre réduit, relevés fréquents, retour à l'ancienne
   méthode possible chaque jour, et une surveillance renforcée : qui lit quoi, à quel rythme, jusqu'à quel critère
   de sortie. Ses relevés sont des faits d'occurrence qui nourrissent la décision de fin de pilote ; ils ne
   déclarent aucun gain (c'est le rôle de `mesurer-gains`).
6. **L'adoption se prépare par rôle.** Pour chaque rôle touché : ce qui change, ce qui disparaît, ce qui reste, la
   formation, qui approuve cette façon de travailler. Une équipe qui n'y gagne rien reprend l'ancienne voie. L'adoption
   se compte en occurrences passées par le dispositif, jamais en personnes évaluées (règle 4).
7. **Le transfert se fait à des personnes nommées qui l'acceptent.** L'exploitant (maintenance courante, 60 §17) et le
   propriétaire (décide des règles, détient les comptes) ont chacun un suppléant, un mode opératoire essayé par quelqu'un
   qui ne l'a pas écrit, et leur acceptation écrite. Envoyer un document n'est pas transférer.
8. **La mise en service ne clôt pas le cas.** À la bascule commencent l'exploitation, la formation des nouveaux arrivants,
   la supervision, le traitement des incidents, la continuité (suppléants) et la mesure : l'exploitant et le propriétaire
   les tiennent. Le cas se clôt après la mesure, pas avant.
9. **Tout changement après le feu vert est une action nouvelle.** Version, règle, consigne d'un modèle, droit, périmètre :
   nouvelle `A-xx`, validée avant, et tests concernés rejoués (`tester-solution`). Aucune action n'est « faite » sans
   validation antérieure, et rien ne se régularise après coup. Un changement fait hors registre (urgence, initiative du
   client) s'écrit au journal comme un incident daté ; le registre propose la suite en `A-xx` nouvelles, validées avant
   d'être faites, et la mesure est prévenue : la période n'est plus comparable.
10. **Un défaut bloquant ouvert en exploitation se contient par des actions comme les autres.** Suspendre, retirer,
    prévenir : des `A-xx` marquées « mesure d'attente » (elles ne changent ni la solution ni ses règles), proposées et
    validées une à une. Le verdict de 85 rendu sur la version en service est relu au journal (« verdict relu : pas prêt
    pour la version en service ») jusqu'à la correction recettée. Détail : `references/modeles.md`, rubrique 2.

## Étapes

1. **Lire ce qui existe et vérifier le point de départ.** Lire `85-recette.md` (verdict, réserves, défauts `D-xx`
   ouverts), `70-plan.md`, `60-specification.md` (§6, §9, §11, §13, §14, §17), `80-construction.md` (version
   construite, fiche d'exploitation), `40-solutions.md` (§1, §10) et le journal.
   - `85-recette.md` absent : dire ce qui manque et proposer `tester-solution`. Si le client maintient sa demande,
     écrire « recette sautée à la demande de <rôle> » en tête, la faire inscrire au journal, ne proposer que des
     actions réversibles et un pilote en parallèle, sans effet sortant.
   - Verdict « pas prêt » : s'arrêter, lister les défauts bloquants, renvoyer à `construire-solution` ou `tester-solution`.
     « Prêt avec réserves » : chaque réserve est fermée avant le feu vert, ou acceptée par le décideur comme condition du
     pilote (rôle, échéance).
   - La porte de `40-solutions.md` §10 est-elle constatée au journal ? Sinon, le dire et la faire constater avant toute action.
   - Option 0 retenue seule, ou lot fait seulement de simplifications : ni 80 ni 85, on arrive ici depuis `70-plan.md` (le routeur le permet).
     Une simplification qui ne modifie aucun outil (supprimer une étape, clarifier une règle) est une décision inscrite au journal. Celle qui
     modifie un outil a sa ligne `A-xx` : le registre est ouvert pour elle seule, validée à part avec son retour arrière, sans attendre un verdict
     de recette. Sous une porte, les simplifications du premier lot de 70 se mènent de même avant la construction. L'adoption se mène dans tous les cas.
   - Une échéance du plan déjà passée se redate ici, avec l'ancienne date. Une valeur ou une décision que le terrain
     contredit se corrige dans `70-plan.md` par version datée (`ARCHITECTURE.md`).
2. **Dresser le registre des actions.** Parcourir droits, secrets, environnements et lots, puis lister chaque action qui
   touche un outil réel : comptes de service et droits ; secrets (leur nom, leur endroit, leur propriétaire : le pack ne voit
   ni ne pose jamais la valeur) ; sauvegarde datée avant modification ; installation de la version construite ; chargement
   de règles ou de données ; alertes et destinataires ; interrupteur ; premier effet externe ; désactivation de l'ancienne voie ;
   communications. Une ligne par action (modèle et fiche d'action : `references/modeles.md` ; actions types et leur retour
   arrière : `references/actions-types.md`). Deux actions ne partagent une ligne que si outil, valideur, moment et retour arrière
   sont les mêmes.
3. **Faire valider action par action.** Présenter à chaque valideur, en clair : ce qui change, où, ce qu'on a observé en
   recette (`T-xx`, pièce), ce qui peut mal tourner, comment on défait, le plafond. Il répond par action ; on inscrit sa réponse
   (date, rôle) au journal, une ligne par validation avec les identifiants, et sa pièce quand elle existe (message déposé dans
   `mission/sources/`). Une validation dont la date limite est passée revient à « proposée ». Une action validée ne se modifie pas :
   si elle change, on l'annule et on en propose une nouvelle. Une action est « faite » quand son effet est constaté dans l'outil,
   pas quand quelqu'un dit l'avoir faite.
4. **Décider le feu vert du pilote.** Fiche de décision (`references/modeles.md`, rubrique 3) : verdict de la recette et réserves,
   porte, critères du pilote signés sans changement (60 §13), actions de préparation faites, interrupteur et alertes essayés de
   bout en bout, mode opératoire essayé par un tiers, surveillance renforcée organisée, utilisateurs prévenus. Décideur : celui de
   60 §13. Ligne de journal avec la pièce.
5. **Conduire le pilote.** Tenir le journal du pilote : date, mode (parallèle, préparation avec validation, réel), relevés `IND-xx`
   avec leur source, écarts expliqués un à un, incidents. Un défaut trouvé en pilote prend le numéro `D-xx` suivant ; sa correction
   repasse par `construire-solution` puis `tester-solution` avant toute nouvelle action, hors mesures d'attente (stratégie 10). Ne pas
   changer les critères en route ; un jour
   où une règle change ne compte pas. Si la solution contient de l'IA : échantillon relu par un humain (taux et rôle de 60 §4),
   comparé au seuil de la recette, et coût d'usage relevé. Le client remet des compteurs et des durées, jamais des données personnelles.
6. **Décider la fin du pilote.** Rejouer d'abord le pré-mortem au jalon prévu par 70 §8 (`planifier-deploiement`), avec les raisons d'échec
   écrites seules par les rôles concernés. Puis appliquer les critères signés, sans les changer : continuer, prolonger ou arrêter, avec la mesure
   de chaque critère. Noter les hypothèses `[H]` de `50-rentabilite.md` que le pilote a levées ou non : elles passent à `mesurer-gains`.
   « Arrêter » ramène à l'option de repli par des actions de retrait (`A-xx`).
7. **Préparer et décider la bascule.** Fiche de bascule : jour et ordre (70 §3), sauvegarde datée de la veille, actions `A-xx` du jour,
   retour arrière (signal, qui le déclenche, comment on vérifie que l'ancienne méthode a repris), lectures du premier jour, seuils d'arrêt
   de 60 §14 en vigueur, critère de sortie de la surveillance renforcée. L'ancienne méthode reste disponible jusqu'à cette sortie.
   Décideur, puis ligne de journal.
8. **Mener l'adoption.** Impact par rôle ; approbations (qui approuve la nouvelle façon de travailler ; une question de conformité, de droit
   du travail ou de représentation du personnel se pose au rôle compétent, le pack ne conclut pas) ; formation faite et vérifiée par un essai
   sans le consultant ; communication (le pack rédige, l'envoi est une `A-xx`) ; support après la transmission et ce qui relève d'une nouvelle
   mission. Chacune des six questions de 70 §4 passe de « réponse du plan » à « fait le …, pièce … ».
9. **Transférer à l'exploitant.** Vérifier que le mode opératoire dit quatre choses : comment vérifier que ça marche, que faire en cas
   d'incident (par symptôme), qui joindre (rôles, suppléants, escalade), comment revenir en arrière. Le faire dérouler par quelqu'un qui ne l'a
   pas écrit. Une lacune se corrige dans `80-construction/fiche-exploitation.md` par révision datée (ligne « correction » au journal), et la rubrique 10
   de `80-construction.md` cite la nouvelle révision : la fiche n'existe qu'à un endroit. Relire la liste des accès
   (comptes de l'entreprise, aucun compte personnel), noter où sont les secrets (jamais leur valeur) et la version en service, puis obtenir
   l'acceptation écrite de l'exploitant et du propriétaire, avec la durée du support.
10. **Passer la main à la mesure.** Écrire ce que reçoit `mesurer-gains` : début de la période (la bascule), versions en service, registre des
    changements, hypothèses `[H]` restées ouvertes, relevés à fournir (qui, quand, quel rythme, 70 §6). Une ligne de journal pour la transmission.
    Ne pas clore le cas. Si la décision de fin de pilote est « arrêter », la suite est le retrait (actions `A-xx`), puis la clôture.

## Le livrable

Le modèle complet, la fiche d'une action, les fiches de décision, les tableaux d'adoption et de transfert et les pièges sont dans
`references/modeles.md` : l'ouvrir pour rédiger. Les titres ci-dessous sont ceux du modèle.

Squelette de `mission/cas-<slug>/90-mise-en-service.md` :

```markdown
# Mise en service — <titre court du cas>
Date de mise à jour · Demandeur (rôle) · Responsable du cas (rôle) · Décideur de la mise en service (rôle) · Rédigé par · Version · Sources : 60, 70, 80, 85 (versions lues)
## 1. Point de départ — verdict de 85 et réserves, défauts ouverts, porte, écarts avec le plan
## 2. Registre des actions — A-xx : quoi, où, effet externe, retour arrière, valideur, validation, état, preuve
## 3. Feu vert du pilote — critères, pièces, décision
## 4. Pilote — journal, surveillance renforcée
## 5. Fin du pilote — critères signés, mesures, décision
## 6. Bascule — fiche, retour arrière, premier jour, décision
## 7. Adoption — impact par rôle, approbations, formation, communication, six questions
## 8. Exploitation et transfert — mode opératoire essayé, accès, acceptation, support
## 9. Ce que reçoit la mesure — début de période, versions, hypothèses ouvertes, relevés à fournir
## Décision attendue
```

Lignes de journal, au moment où le client tranche (exemples fictifs) :

```markdown
- 2026-11-12 · cas-saisie-commandes · A-01 à A-04 validées par la direction des opérations · « compte de service, droits en lecture, sauvegarde, import de la version 1.0 inactive ; retour arrière prêt et essayé pour chacune »
- 2026-11-16 · cas-saisie-commandes · feu vert du pilote donné par la direction commerciale · « une réserve acceptée (D-04) ; une équipe, mode parallèle le premier jour »
- 2026-12-09 · cas-saisie-commandes · fin du pilote : continuer, décidé par la direction commerciale · « critères de la fiche signée atteints, relevé joint »
- 2026-12-14 · cas-saisie-commandes · bascule faite · « sauvegarde du vendredi jointe ; surveillance renforcée jusqu'au 2027-01-15 »
- 2026-12-15 · cas-saisie-commandes · transmission acceptée par le propriétaire et l'exploitante · « mode opératoire déroulé par la suppléante ; support de l'indépendant jusqu'au 2027-01-13 »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Une validation par action, avec son retour arrière | « on lance » ne dit ni ce qui change ni comment défaire | une validation globale de la bascule | plusieurs actions ont même outil, valideur, moment et retour arrière : une ligne, identifiants listés |
| Le pack n'exécute pas lui-même une action irréversible ou à effet externe | l'autorisation, les accès et la responsabilité restent chez le client | agir par un connecteur après un « oui » général | le client demande par écrit qu'un outil connecté exécute une action précise, limitée par un plafond |
| Un effet externe porte un public et un plafond | sans plafond, une erreur se répète à l'échelle avant qu'on la voie | valider « envoyer les confirmations » sans limite | jamais |
| Trois décisions écrites, critères signés avant | décider après coup, c'est décider sur l'enthousiasme | une décision orale, ou des critères ajustés pendant le pilote | jamais |
| Le pilote ne déclare aucun gain | premier mois biaisé par la nouveauté et la montée en charge | annoncer le gain à la fin du pilote | jamais : le gain se déclare dans `mesurer-gains` |
| L'ancienne méthode reste disponible jusqu'à la sortie de la surveillance renforcée | le retour arrière n'existe que si l'ancienne voie marche encore | la retirer à la bascule | le propriétaire accepte par écrit de la retirer plus tôt |
| Le cas reste ouvert après la bascule | exploitation, adoption et mesure commencent à ce moment | clore à la mise en service | jamais |

## Frontières

- Le calendrier, les lots, le pré-mortem et le rythme des revues → `planifier-deploiement` ; ici on exécute et on trace. Critères du
  pilote, seuils, droits, secrets et plan de test → `rediger-cahier-des-charges` (60) : on les cite, on ne les change pas en route.
- Construire, corriger, écrire la fiche d'exploitation → `construire-solution`. Tester, rejouer la recette ou l'évaluation de l'IA
  après un défaut ou un changement → `tester-solution`.
- Mesurer le gain, comparer au départ, décider continuer · corriger · étendre · arrêter → `mesurer-gains`. Les actions de correction,
  d'extension ou de retrait qu'il décide reviennent ici sous forme d'`A-xx`.
- L'état de la mission et le journal → `router-mission-ia`.
- Une plateforme ou un outil précis → `COMPAGNONS.md` du pack, ligne de l'étape 90 ; sans compagnon, la méthode ci-dessus est le repli maison.
- Hors du pack : agir dans les outils du client sans validation, lire ou poser un secret, écrire aux clients du client, conclure sur la
  conformité ou le droit du travail.

## Preuves restantes

- Écrite le 2026-10-12 pour le pack V2. Essayée une fois, de bout en bout, sur la mission fictive de `examples/`, mais entièrement simulée :
  aucun outil réel, des rôles et des décisions inventés. Le registre a porté 25 actions, dont une refusée (A-16), une faite hors registre
  (A-17), arrêtée par le garde-fou puis annulée et écrite comme incident, avec sa suite A-18 validée avant d'être faite, et deux mesures
  d'attente (A-24, A-25) pour un défaut bloquant trouvé en exploitation ; feu vert avec conditions, pilote de quatre lundis, fin de pilote,
  bascule, adoption par rôle, transmission à trois rôles. La fiche d'exploitation déroulée par un tiers a montré trois lacunes ; deux
  révisions de plus sont venues du pré-mortem rejoué et d'une panne de l'éditeur.
- NON MESURÉ avec de vraies personnes : si le registre d'actions reste tenable sur un petit dispositif (neuf colonnes), si trois décisions
  écrites suffisent, si la surveillance renforcée a la bonne durée (celle de l'exemple n'est pas terminée au 2027-01-12), si une mesure
  d'attente tient jusqu'à la correction, et si les valideurs acceptent une validation par action.
- Sources et crédits : les compagnons de cette étape et leurs licences sont dans `COMPAGNONS.md`. La méthode est écrite avec nos mots :
  retour arrière, mode parallèle, feu vert écrit et surveillance renforcée sont des pratiques courantes de mise en production, aucun texte repris.
