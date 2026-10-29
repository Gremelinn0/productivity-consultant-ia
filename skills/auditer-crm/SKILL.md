---
name: auditer-crm
description: >-
  Quand le besoin d'une mission touche au CRM (« audite notre CRM », « on veut mettre en place un CRM »,
  « le CRM est en bazar », « fais le cahier des charges CRM », « quel CRM choisir », « optimise notre
  pipeline ») → auditer le CRM en place sur ses quatre volets (automatisations et intégrations,
  données, ventes, tableaux de bord), mesurer usage et qualité des données, rendre un bilan priorisé
  (gains rapides, plan d'action), puis écrire le cahier des charges CRM et ses annexes dans le modèle
  d'exigences du pack. Module CRM du pack consultant-ia, appelé par auditer-processus et
  rediger-cahier-des-charges ; son agent, l'auditeur CRM, mène tout l'audit en lecture seule. Triggers :
  « audit CRM », « cahier des charges CRM », « mise en place d'un CRM », « optimiser le CRM », « refonte
  du CRM », « qualité des données du CRM », « pipeline », « Pipedrive », « HubSpot », « CRM audit ».
metadata:
  scope: "un CRM à auditer, à choisir, à mettre en place ou à optimiser, dans un cas de la porte « besoin connu »"
  owns: "la grille d'audit CRM (quatre volets, contrôles, statuts de constat), le bilan priorisé d'un audit CRM, la trame qui dit ce que chaque rubrique d'un cahier des charges CRM doit trancher, ses annexes (pipelines, droits, catalogue), le cas anonymisé d'un projet CRM planifié puis arrêté"
  consumes: "mission/cas-<slug>/10-besoin.md ; mission/sources/ (exports, captures, notes d'entretien) ; le CRM et ses outils voisins, en lecture seule ; les sujets crm et crm-parametrage de la base de questions de mener-entretien-ia ; le modèle d'exigences de rediger-cahier-des-charges"
---

# Audit, conseil et cahier des charges CRM

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/20-diagnostic/audit-crm.md` (l'audit et son bilan) et,
> pour une mise en place ou une refonte, `mission/cas-<slug>/30-exigences/annexes-crm.md` (les tableaux du cahier des
> charges). Preuve : le demandeur valide le bilan puis les exigences, et chaque décision s'inscrit dans
> `mission/journal.md`. Contrôle de forme : l'audit porte ses quatre volets et sa vue d'usage ; chaque constat a l'un
> des quatre statuts (`confirmé`, `à vérifier`, `incohérent`, `à mettre en place`) et l'écran, l'export ou l'entretien
> qui le fonde ; chaque recommandation a son plan d'action, son impact et sa faisabilité ; chaque nombre son statut
> `[F]`, `[H]` ou `[E]` (définis dans `ARCHITECTURE.md`). Aucune action dans le CRM réel : elle passe par
> `piloter-mise-en-service`. **Boucle** : aucune.

> ❓ **Une question pour l'entreprise sort de la base de questions** (`mener-entretien-ia/references/base-questions/`,
> un fichier par sujet ; ici `crm` pour le diagnostic, `crm-parametrage` pour le cahier des charges, `donnees` et
> `reporting` au besoin) : lire d'abord le bloc du sujet, ne poser que ce qui manque, puis y ranger ce qui manquait
> (`entretien.py ajouter`).

## Ce que cette compétence résout

Un CRM se dégrade sans bruit : des champs que personne ne remplit, des pipelines aux étapes identiques, des
automatisations créées par un ancien prestataire et que personne n'ose couper, des rapports payés que personne
n'ouvre. Pour le refondre, on crée souvent des champs et des automatisations avant d'avoir décidé qui doit voir quoi,
quelle donnée fait foi et ce que veut dire chaque étape. Cette compétence suit trois temps : mesurer l'existant sans
y toucher, rendre un bilan court qui priorise, puis écrire un cahier des charges qui tranche chaque réglage avant le
paramétrage.

Résultat attendu : un audit dont chaque constat se vérifie, un bilan où chaque recommandation a son plan d'action, et
des exigences CRM qu'un intégrateur peut chiffrer sans rouvrir l'entretien.

## Stratégie

1. **Mesurer avant de demander.** Le CRM se lit lui-même : quotas d'usage, champs, pipelines, automatisations,
   historique des propriétés. L'entretien confirme ce que l'outil montre et cherche le reste (`auditer-processus`,
   étape 2). Une question dont « D'abord » vaut `l'outil` ne se pose pas avant d'avoir regardé.
2. **La configuration n'est pas l'usage.** Un pipeline paramétré n'est pas un pipeline suivi, un workflow actif n'est
   pas un workflow qui enrôle. Aucun constat ne se tire d'un seul écran : chaque constat dit l'écran, l'export ou
   l'entretien qui le fonde, et reste `à vérifier` tant qu'un second témoin manque.
3. **Lecture seule, toujours.** L'audit ne crée, ne modifie ni ne supprime rien dans le CRM du client ; une
   correction est une action `A-xx` de `90-mise-en-service`, validée une à une (règle 7). Ce qu'on trouve inutile
   s'archive, jamais ne se supprime : un segment sans référence peut être lu par un autre segment.
4. **Un bilan se lit en cinq minutes.** Un audit exhaustif mais illisible ne sert pas : le premier retour reçu sur un
   audit de ce type disait la difficulté à lire et le manque de priorisation. Le bilan ne refait pas l'analyse : il
   ne garde que les recommandations, les gains rapides en tête, chacune avec son plan d'action, et il montre celles
   qui n'en ont pas encore.
5. **Décider avant de paramétrer.** Le cahier des charges tranche d'abord les acteurs, les droits, la donnée qui fait
   foi, l'identifiant d'un contact et le sens de chaque étape ; les champs et les automatisations viennent après. Il
   reste dans le modèle d'exigences du pack (douze rubriques) : le CRM ne crée pas un second format.
6. **Sans nom d'éditeur dans les exigences.** Le mode exigences ne nomme pas de solution hors des rubriques
   Intégrations et Contraintes ; les spécificités d'un éditeur (plans, groupes de visibilité, ensembles de droits)
   n'entrent qu'en spécification, une fois l'outil choisi par `concevoir-solution`.

## Étapes

1. **Brancher l'existant.** Lire `10-besoin.md` et `mission/sources/`. Demander un accès en lecture au CRM et aux
   outils qui l'alimentent (formulaires, automatisation, messagerie, outil de rendez-vous) avec une seule adresse pour
   toutes les invitations ; les accès manquants s'écrivent comme manquants (règle « Brancher le contexte »). Ne
   jamais lire ni recevoir un mot de passe : un accès se donne par invitation ou par un coffre partagé.
2. **Relever la vue d'usage.** Remplir la rubrique 1 de la grille (`references/grille-audit.md`) : volumes, quotas
   et limites de l'abonnement, part utilisée. Un quota proche de sa limite ou un module jamais utilisé est un constat.
3. **Préparer l'entretien.** Prendre le bloc `crm` de la base (`entretien.py base --sujet crm`), écarter ce que
   l'étape 2 a établi, faire confirmer ce qui est incertain : douze questions au plus, par rôle (direction, ventes,
   marketing, service client), validées avant l'entretien. Le consultant le mène, ou une IA par écrit
   (`mener-entretien-ia`) ; sa note entre dans `mission/sources/`.
4. **Auditer les quatre volets** dans l'ordre de la grille : automatisations, intégrations et outils ; données
   (sources, champs critiques, complétude, valeurs, doublons, enrichissement, segmentation) ; ventes (pipelines,
   étapes, délais, raisons de perte, activités, vues et filtres, attribution, prévision) ; tableaux de bord. Chaque
   constat prend son statut et son témoin. Une fonctionnalité répartie sur plusieurs écrans se lit par navigation
   guidée : une hypothèse écrite avant chaque écran, un constat après, jusqu'à couverture complète.
5. **Écrire le bilan.** Recommandations seulement, regroupées par volet, gains rapides d'abord ; pour chacune :
   description, plan d'action, impact `[E]` ou `[H]`, faisabilité, et le projet ou la tâche qui la porte quand il
   existe. Une recommandation sans plan d'action se marque comme telle, jamais ne disparaît. Le bilan se termine par
   les actions prioritaires et la décision attendue. Prévoir une restitution courte (synthèse d'une page, et une
   vidéo de présentation si le client la demande).
6. **Relire et faire décider.** Relecture de la règle commune 8 (`ARCHITECTURE.md`) : chaque nombre repris d'un
   export se recalcule. Le demandeur valide les causes et les priorités ; la décision s'inscrit au journal. Le
   bilan alimente `20-diagnostic.md` (goulets, causes, simplifications à faire d'abord), que `auditer-processus` écrit.
7. **Écrire le cahier des charges CRM** (mise en place, changement d'outil ou refonte). Constituer les besoins
   cas d'usage par cas d'usage (la méthode est dans `references/trame-cahier-des-charges.md`), poser les questions du
   sujet `crm-parametrage` qui restent ouvertes, puis remplir les douze rubriques du modèle d'exigences de
   `rediger-cahier-des-charges` avec ce que la trame demande pour un CRM. Les tableaux longs (pipelines et étapes,
   droits par rôle, catalogue, raisons de perte, automatisations souhaitées) vont dans les annexes.
8. **Conseiller le choix de l'outil.** Garder le CRM en place, changer d'édition ou changer d'outil se compare dans
   `concevoir-solution`, avec les critères de la grille (rubrique 6) ; l'option « garder et simplifier » se chiffre
   toujours.
9. **Enrichir la base.** Ce qui a manqué pendant l'audit se range dans `crm` ou `crm-parametrage`, sans le nom du
   client ni ses chiffres (`entretien.py ajouter`, puis `entretien.py verifier`).

## Le livrable

`mission/cas-<slug>/20-diagnostic/audit-crm.md`, annexe de `20-diagnostic.md` :

```markdown
# Audit CRM : <entreprise ou équipe> · <date>
Demandeur · Valideur · Accès lus (CRM, outils, en lecture seule) · Entretiens (rôles, dates) · Accès manquants
## Bilan, à lire d'abord
Les gains rapides (trois à cinq), les actions prioritaires, la décision attendue.
## 1. Vue d'usage
## 2. Automatisations, intégrations et outils
## 3. Données
## 4. Ventes
## 5. Tableaux de bord
Pour chaque volet : constats (statut, témoin), puis recommandations (description, plan d'action, impact, faisabilité,
projet qui la porte ou « sans plan d'action »).
## Ce qui reste à vérifier
## Décision attendue
```

Pour une mise en place ou une refonte : les exigences dans `30-exigences.md`, au modèle de
`rediger-cahier-des-charges`, et leurs tableaux dans `mission/cas-<slug>/30-exigences/annexes-crm.md`, au gabarit de
`references/trame-cahier-des-charges.md`. Un exemple de projet entier, anonymisé, planifié puis arrêté, est
`references/cas-reseau-immobilier.md`.

## L'agent

L'auditeur CRM (`agents/auditeur-crm.md` du pack) déroule les étapes 1 à 6, et la 7 quand on la lui demande, dans
une session qui a accès au CRM en lecture : il lit, mesure, prépare le questionnaire, remplit la grille, écrit
l'audit et le bilan, et s'arrête avant toute action sur le CRM réel. Devant un visiteur en ligne, sans consultant
avant l'entretien, c'est l'agent en ligne de `mener-entretien-ia` qui interroge, avec les questions du sujet `crm` ;
le sujet `crm-parametrage` lui est fermé, il suppose une mission engagée.

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Un module CRM qui alimente 20 et 30, pas une étape de plus | le pipeline du pack reste le même ; un audit CRM est un diagnostic, un cahier des charges CRM est un cahier d'exigences | une étape propre au CRM entre 20 et 30 ; un second format de cahier des charges | un livrable CRM ne trouve sa place dans aucune rubrique |
| Quatre volets : automatisations et intégrations, données, ventes, tableaux de bord | ce sont les quatre familles de constats des audits repris ; chacune a son propriétaire chez le client | un audit par fonctionnalité de l'éditeur | un cinquième volet revient dans trois audits |
| Quatre statuts de constat | « config ≠ usage » ne se tient qu'avec un statut qui dit ce qui manque pour conclure | constat vrai ou faux | jamais |
| Un bilan fait des seules recommandations, gains rapides d'abord | un audit lu comme illisible et peu priorisé est le premier retour reçu sur ce travail | rendre l'audit complet comme livrable final | le client demande l'analyse détaillée : elle reste dans les volets |
| Les questions de paramétrage dans un sujet réservé au consultant | elles supposent une mission engagée ; posées à un visiteur, elles l'égarent, et elles pèseraient sur la consigne de l'agent en ligne | les mettre dans `crm`, ouvert à l'agent en ligne | un visiteur arrive avec un cahier des charges à écrire : il faut d'abord une mission |
| Archiver, jamais supprimer, ce qu'on trouve inutile | un segment sans référence peut être lu par un autre ; un workflow éteint peut être saisonnier | supprimer ce qui semble mort | jamais |
| Les éléments propres à un éditeur seulement en spécification | les exigences doivent pouvoir comparer plusieurs CRM | une trame écrite pour un seul éditeur (la trame d'origine l'était) | jamais en mode exigences |
| L'ancienne méthode reprise sans les noms de ses clients | le pack est public ; un cas sert par sa forme, pas par son nom | citer les clients des audits d'origine | le client publie lui-même le cas et l'autorise |

## Frontières

- Le diagnostic du processus, ses goulets et ses causes → `auditer-processus`, qui reçoit le bilan et écrit
  `20-diagnostic.md`. Le cahier d'exigences et son modèle → `rediger-cahier-des-charges` ; cette compétence dit ce
  qu'un CRM y ajoute. Le choix entre garder, changer d'édition et changer d'outil → `concevoir-solution`.
- Les questions vivent dans la base de `mener-entretien-ia` (`crm`, `crm-parametrage`) ; cette compétence n'en
  recopie aucune.
- Toute action dans le CRM réel (archiver un segment, corriger un champ, couper un workflow) → `piloter-mise-en-service`,
  action par action, avec son retour arrière. Le paramétrage lui-même → `construire-solution`, en environnement d'essai.
- Les procédures propres à un éditeur (appels d'API, écrans, assistant intégré) relèvent d'une compétence de cet
  éditeur, installée à part ; l'audit en reprend les constats, pas les gestes.

## Preuves restantes

- Méthode reprise d'audits et de cahiers des charges CRM réels (deux éditeurs, sept missions ou ébauches), de trois
  assistants conversationnels de l'auteur et d'une boîte à outils d'audit d'un éditeur ; les noms, chiffres et pièces
  des clients n'y sont pas. Provenance : `references/grille-audit.md`, dernière section.
- NON MESURÉ : le module n'a pas encore servi de bout en bout sur une mission ; le premier audit dira si quatre volets
  suffisent et si le bilan se lit vraiment en cinq minutes.
- NON MESURÉ : l'agent `auditeur-crm` n'a été lancé sur aucun CRM ; ses limites (lecture seule, arrêt avant toute
  action) sont écrites, pas éprouvées.
- Les seuils (taux de complétude acceptable, délai d'alerte d'une affaire) ne sont pas fixés : aucune source ne les
  chiffrait de façon générale ; ils se décident avec le client et s'écrivent `[H]`.
