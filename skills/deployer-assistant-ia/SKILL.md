---
name: deployer-assistant-ia
description: >-
  Quand une entreprise veut donner un assistant IA à une équipe sans nommer un processus à automatiser (« on veut
  Claude pour toute l'équipe », « quel plan prendre », « ChatGPT ou Copilot pour nos équipes ? », « il nous faut une
  charte IA », « des salariés utilisent déjà ChatGPT avec leur compte », « et pour le RGPD ? ») → partir de l'usage
  réel, choisir l'assistant et le plan sur des contraintes écrites et des faits lus le jour même, écrire la charte
  d'usage, préparer le dossier de conformité, lister les réglages, prévoir le pilote, la formation par rôle et le
  rendez-vous de pilotage. Module du pack consultant-ia : il ne possède aucune étape, il prépare le dossier
  (assistant, charte, conformité, indicateurs) que la mise en service du pack Créer un agent IA reprend ; il n'agit pas. Triggers : « déployer Claude », « déployer Copilot »,
  « ChatGPT Business », « Claude Team », « licences IA », « charte IA », « IA fantôme », « adoption de l'IA », « shadow
  AI », « AI rollout ».
metadata:
  scope: "une équipe à équiper d'un assistant IA général (Claude, ChatGPT, Copilot ou un autre), sans processus nommé à automatiser, de l'usage déjà là jusqu'au pilotage"
  owns: "le relevé de l'usage réel, le choix de l'assistant et du plan, la charte d'usage, le dossier de conformité préparé, la liste des réglages à proposer, la formation par rôle, le rendez-vous de pilotage et les indicateurs du parcours court"
  consumes: "mission/cas-<slug>/10-besoin.md ; mission/sources/ ; le sujet assistant-ia de la base de questions de mener-entretien-ia ; les pages officielles des éditeurs et les textes de droit, lus le jour de la mission"
---

# Déployer un assistant IA dans une équipe

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/90-mise-en-service/assistant-ia.md` et
> `mission/cas-<slug>/90-mise-en-service/charte-usage.md`. Preuve : le décideur valide le choix, la charte et les
> indicateurs, et la décision s'inscrit dans `mission/journal.md`. Contrôle de forme : les rubriques du modèle sont
> présentes ; chaque fait sur un éditeur porte sa page officielle et sa date de lecture, ou « non vérifié » ; chaque
> nombre son statut `[F]`, `[H]` ou `[E]` (définis dans `ARCHITECTURE.md`) ; aucun gain annoncé ; aucune conclusion
> juridique. Aucune action dans un outil réel : la mise en service du pack Créer un agent IA la reprend. **Boucle** : aucune.

> ❓ **Une question pour l'entreprise sort de la base de questions** (`mener-entretien-ia/references/base-questions/`,
> un fichier par sujet ; ici le sujet assistant-ia, avec cadrage et transmission au besoin) : lire d'abord le bloc du
> sujet, ne poser que ce qui manque, puis y ranger ce qui manquait (`entretien.py ajouter`).

## Ce que cette compétence résout

« On veut un assistant IA pour l'équipe » est la mission la plus fréquente et la plus simple : aucun processus à
construire, un abonnement, des réglages. Le reste du pack n'y répond pas bien : onze étapes pour acheter des licences,
c'est trop. Sans méthode, la mission se perd autrement : des salariés sur des comptes personnels que personne n'a
vus, un plan choisi sur une page de prix périmée, une charte de dix pages que personne ne lit, des statistiques par
personne laissées actives sans que personne l'ait décidé, des sièges payés qui dorment.

Cette compétence prépare le déploiement en une fois : ce qui se fait déjà, l'assistant et le plan qui tiennent les
contraintes, la charte, le dossier de conformité, les réglages, le pilote, la formation et le rendez-vous de pilotage.

Résultat attendu : un document que le décideur lit en dix minutes et valide, une charte d'une page, et une liste
d'actions prêtes pour la mise en service du pack Créer un agent IA.

## Stratégie

1. **Partir de l'usage qui existe.** Une équipe sans assistant officiel en utilise souvent déjà un, sur des comptes
   personnels. C'est le premier risque à fermer et le meilleur renseignement sur les besoins. On relève qui, avec quel
   compte, pour quoi, en comptant par équipe et sans chercher de coupable (règle 4).
2. **Le plan suit les contraintes écrites, le plus petit qui les tient.** Données, lieu de traitement, connexion
   unique, traces, nombre de sièges : écrites d'abord, avec leur source. Un plan supérieur doit citer la contrainte qui
   l'impose. L'option de ne rien ajouter se compare toujours : une licence déjà payée suffit parfois (règle 6).
3. **Un fait sur un éditeur se lit le jour même.** Plans, prix, options et conditions changent en quelques mois.
   `references/fiches-assistants.md` dit où lire et quoi relever ; ses valeurs datées sont un repère, jamais une source
   du livrable. Chaque fait du livrable porte sa page officielle et sa date de lecture ; une page inaccessible s'écrit
   « non vérifié ».
4. **La charte tient en une page et vaut dès le premier compte.** Les règles que chacun garde en tête :
   les trois questions avant de coller, ce que l'assistant peut faire dans les outils, quoi faire en cas de doute
   (`references/charte-usage.md`). Le détail va dans la formation.
5. **Le droit se prépare, il ne se conclut pas.** Le pack réunit les pièces et pose les bonnes questions au rôle
   compétent (`references/dossier-conformite.md`). Il ne donne pas d'avis juridique et ne propose aucune base légale
   toute faite : elle dépend de la finalité, et c'est le responsable du traitement qui la décide.
6. **On suit l'usage, pas les personnes** (règle 4). Une statistique par personne est une donnée sur un salarié, et
   certains éditeurs la montrent à l'administrateur sans réglage pour la couper : relever ce qui existe, puis décider
   par écrit qui la regarde et pour quoi, l'annoncer à l'équipe, ne jamais en faire un indicateur de performance. La
   recommandation par défaut est de lire par équipe, l'exploitant agrégeant l'export si l'outil n'a pas de vue d'équipe.
   Une équipe de moins de cinq personnes `[H]` se lit avec une autre : un total sur trois personnes les identifie.
7. **Former sur les tâches de l'équipe, par rôle.** Une heure sur les tâches relevées à l'étape 2 vaut mieux qu'une
   présentation de l'outil. Chacun repart avec la règle qui dit où poser quelle demande et ses instructions écrites, et
   réussit un essai sans le consultant.
8. **Le pilotage est un rendez-vous, pas un tableau de bord.** Un exploitant nommé, un point par mois (sièges dormants,
   consommation, alertes), une revue par trimestre (connecteurs, tâches planifiées, charte, faits de la fiche). Un siège
   qui dort se traite comme un signal : on demande ce qui manque avant de le retirer.
9. **Aucun gain promis.** Le chiffre de l'éditeur reste chez l'éditeur. On pose une mesure de départ datée et des
   indicateurs ; le gain se lit en 95, sur relevé.

## Étapes

1. **Vérifier que c'est bien ce cas.** Lire `10-besoin.md` et `mission/sources/`. Le parcours court vaut quand la
   demande est d'équiper une équipe d'un assistant général. La fiche porte alors la ligne `Parcours : déploiement d'un
   assistant`. Elle nomme un processus à automatiser : c'est le parcours normal, et l'assistant devient une option de
   `concevoir-solution`. Personne ne sait dire à quoi il servirait : `decouvrir-cas-usage`, en version courte.
2. **Relever l'usage réel.** Questions AS01 à AS03. Lire ce qui se lit sans déranger : licences payées, total des notes de
   frais, journaux d'accès que l'entreprise accepte de fournir, en comptes et par équipe, jamais par nom. Une enquête courte et anonyme suffit
   à une petite équipe. Noter trois à cinq tâches récurrentes par rôle, avec leur durée : elles serviront à la formation
   et à la mesure de départ.
3. **Écrire les contraintes.** Questions AS04 à AS07, et AS08 pour les personnes à consulter. Un tableau : contrainte, source, statut, ce qu'elle impose au
   plan. Une contrainte dite de mémoire reste `[H]` jusqu'à sa pièce (contrat, clause, attestation demandée).
4. **Comparer.** Trois colonnes au plus : ne rien ajouter, et deux candidats, dont celui qui s'impose par l'existant
   (la suite bureautique déjà payée). Lire `references/fiches-assistants.md`, puis relever chaque ligne de sa grille sur
   les pages officielles, le jour même. Pour une décision difficile, appeler `router-consulting-strategy` (lentille
   options stratégiques). Écrire la recommandation, ce qui la ferait changer, et le plan minimal. Un outil déjà inclus
   dans une licence payée est la colonne « ne rien ajouter » ; le second candidat reste libre. Une recommandation ne
   repose sur un fait non vérifié que s'il est écrit comme condition.
5. **Chiffrer simplement.** Sièges × prix × 12 mois, plus l'usage estimé pour un plan facturé à l'usage et le temps
   interne de mise en place et de pilotage, calcul montré, statut `[E]`, devise et hors taxes écrits. Le prix lu le jour
   même est un `[F]` daté ; un repère de la fiche reste `[H]` ; le nombre de sièges reste `[H]` jusqu'à sa validation. Aucune ligne de
   gain. Un déploiement assez gros pour demander un business case passe par `chiffrer-rentabilite` : son montant
   déclencheur se fixe avec le décideur, `[H]`.
6. **Écrire la charte.** Questions AS09 à AS12 : la charte nomme son responsable et dit ce qui est suivi. Remplir le modèle de `references/charte-usage.md` avec les tâches et les
   outils de l'équipe, dans `90-mise-en-service/charte-usage.md`.
7. **Préparer le dossier de conformité.** À partir des réponses AS05, AS06, AS08 et AS11, suivre
   `references/dossier-conformite.md` : les pièces à réunir, les questions
   à poser, à qui, et ce qui doit précéder le pilote. Le calendrier du pilote part de ces réponses, jamais l'inverse. Un
   sujet sans réponse s'écrit `Q-xx`.
8. **Fermer l'usage non officiel, lister les réglages.** Les comptes personnels relevés à l'étape 2 : une action `A-xx`
   pour passer au compte de l'entreprise, sans coupable, et ce qui a déjà été collé (données clients ou sous clause)
   devient une `Q-xx` au rôle compétent. Puis, à partir d'AS07 et d'AS10, une ligne par réglage à proposer en `A-xx` : compte de l'organisation, connexion unique,
   rôles, durée de conservation, entraînement sur les données, connecteurs, extension du navigateur, plafonds, alertes,
   statistiques par personne (AS11 : masquer les noms là où l'outil le permet, sinon la décision de la stratégie 6), modèle par défaut. Chacune avec son retour arrière, ou « aucun » écrit en clair. Rien ne se fait ici :
   la liste entre au registre de `90-mise-en-service.md`.
9. **Prévoir le pilote et la formation.** Un petit groupe volontaire de plusieurs rôles, une durée et des critères
   écrits avant, valeurs `[H]` jusqu'à leur validation : usage réel sur les tâches notées, incidents, questions restées
   sans réponse. La formation par rôle reprend ces tâches, la règle « où poser quoi » et les niveaux d'instructions de
   `references/fiches-assistants.md`, partie 2. Elle se vérifie par un essai sans le consultant, et sa trace se garde :
   qui, quand, sur quoi.
10. **Préparer le pilotage et la mesure.** L'exploitant et son suppléant viennent d'AS12. Écrire les deux
    rendez-vous. Poser les indicateurs `IND-xx` avec leur source, leur méthode et leurs seuils : part des sièges actifs
    par équipe, tâches passées par l'assistant, durée de ces tâches, incidents, coût réel. Dater la mesure de départ
    avant le pilote, sur les tâches et leur durée : sans elle, aucun gain ne pourra se déclarer observé. Un indicateur
    qui n'existe pas avant le premier siège part de zéro ; les familles non suivies se déclarent « non relevées : raison ».
11. **Relire et faire décider.** Relecture de la règle commune 8 (`ARCHITECTURE.md`). Le décideur valide le choix, la
    charte, les réglages à proposer et les indicateurs ; une ligne au journal. Étape suivante : la mise en service, au pack Créer un agent IA.
12. **Enrichir la base.** Ce qui a manqué se range dans le sujet assistant-ia, sans le nom du client ni ses chiffres
    (`entretien.py ajouter`, puis `entretien.py verifier`). Un fait d'éditeur périmé se corrige dans
    `references/fiches-assistants.md`, avec sa nouvelle date.

## Le livrable

`mission/cas-<slug>/90-mise-en-service/assistant-ia.md`, avec la charte à côté. La mise en service du pack Créer un agent IA y renvoie en tête
de `90-mise-en-service.md` quand elle le crée :

```markdown
# Déploiement d'un assistant IA : <équipe> · <date>
Demandeur · Décideur · Exploitant pressenti · Version · Pages officielles lues le <date>
## À lire d'abord
La recommandation en trois lignes, le coût annuel `[E]`, la décision attendue.
## 1. L'usage réel : comptes, équipes, tâches récurrentes et leur durée
## 2. Les contraintes : contrainte, source, statut, ce qu'elle impose
## 3. Les options comparées : ne rien ajouter et deux candidats, un fait par ligne, page officielle, date de lecture ; la recommandation et ce qui la ferait changer
## 4. Le coût : calcul montré, sans ligne de gain
## 5. Le dossier de conformité : pièces, questions, réponses, Q-xx ouvertes, ce qui précède le pilote
## 6. Les réglages à proposer : A-xx, réglage, valeur, retour arrière
## 7. Le pilote et la formation : groupe, durée, critères écrits avant, formation par rôle, trace de la formation
## 8. Le pilotage et la mesure : exploitant, suppléant, les deux rendez-vous, IND-xx, mesure de départ datée
## Décision attendue
```

Dans ce parcours, ce document tient lieu de 60 et de 70 pour la mise en service du pack Créer un agent IA et pour `mesurer-gains` : sa rubrique 7
donne les critères du pilote, sa rubrique 8 les indicateurs, leurs seuils et la mesure de départ. Le mode opératoire de
l'exploitant s'écrit dans `90-mise-en-service.md`, à sa propre rubrique 8.

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Un module sans étape, comme `auditer-crm` | le pipeline et ses douze compétences ne changent pas ; ce qui touche un outil reste en 90, le gain reste en 95 | une treizième compétence d'étape ; un second pipeline | un livrable de ce parcours ne trouve sa place ni en 90 ni en 95 |
| Un parcours court : 10, ce module, 90, 95 | sans processus à construire, 20 à 85 n'ont pas d'objet ; onze étapes font fuir la mission la plus simple | faire remplir chaque étape « sans objet » à la main | une mission montre qu'il fallait un diagnostic : elle repart par le parcours normal |
| Une méthode valable pour tout assistant, Claude en première fiche | le client doit pouvoir comparer ; une méthode écrite pour un éditeur vend cet éditeur | un guide propre à Claude | jamais |
| Les faits d'éditeur datés en référence, relus à chaque mission | un plan ou une option change en quelques mois | écrire les plans dans la méthode ; se fier à une ressource de seconde main | jamais |
| Aucune base légale toute faite, aucune conclusion juridique | elle dépend de la finalité ; le pack ne donne pas d'avis juridique | une mention type à recopier dans le registre | jamais |
| Lire par équipe, statistiques par personne à décider par écrit | règle 4 : on observe le travail, pas les personnes, et un indicateur individuel tue l'usage qu'il veut mesurer ; un réglage pour couper la vue de l'administrateur n'existe pas partout | laisser le réglage de l'éditeur ; promettre qu'on peut toujours la couper | l'entreprise a une finalité écrite, annoncée et validée par le rôle compétent |
| Aucun gain annoncé avant 95 | règle 2 ; les chiffres d'éditeur ne se transposent pas | reprendre un gain publié dans le coût | jamais |
| Les questions dans un sujet réservé au consultant | elles supposent une mission engagée ; la consigne de l'agent en ligne n'en grossit pas | les ouvrir à l'agent en ligne | des visiteurs arrivent avec cette demande : ouvrir le sujet |

## Frontières

- Automatiser un processus nommé, construire un agent ou un flux → le parcours normal, de `cadrer-besoin` à
  `mesurer-gains`. Un assistant peut y être une option de `concevoir-solution`.
- Toute action dans un outil réel (créer l'organisation, couper un réglage, ouvrir un connecteur) → la mise en service du pack Créer un agent IA,
  action par action. Les décisions de feu vert, de fin de pilote et de bascule y vivent.
- La lecture des relevés et la décision continuer, corriger, étendre ou arrêter → `mesurer-gains`. Le business case d'un
  gros déploiement → `chiffrer-rentabilite`.
- Une question de conformité, de droit du travail ou de représentation du personnel se pose au rôle compétent : ce module
  prépare, il ne conclut pas.
- Les questions vivent dans la base de `mener-entretien-ia` (sujet assistant-ia) ; ce module n'en recopie aucune.
- Hors du pack : administrer l'assistant après la transmission, un programme complet de conduite du changement, une
  formation longue, la vente ou la revente de licences.

## Preuves restantes

- Essai à blanc le 06/11/2026 sur une PME fictive de 38 salariés, Microsoft 365 en place, CSE, sans délégué à la
  protection des données : quinze frictions relevées (ordre des questions, usage gratuit à fermer, rôle par défaut,
  statut des repères, lecture par petite équipe), corrigées.
- NON MESURÉ : le module n'a pas encore servi sur une vraie mission.
- Sources : le manque a été repéré dans un wiki sur le déploiement de Claude en entreprise. La méthode est rédigée ici,
  aucun texte n'en est repris ; ses faits ont été relus aux sources officielles (`references/fiches-assistants.md`).
