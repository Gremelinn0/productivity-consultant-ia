# Modèles — feuille de route et plan de déploiement

À ouvrir pour rédiger : la partie A pour `mission/04-feuille-de-route.md` (portefeuille, porte « aucun besoin »),
la partie B pour `mission/cas-<slug>/70-plan.md` (un cas, porte « besoin connu »), la partie C pour le
pré-mortem qui se range dans l'un ou l'autre (déroulé complet : `pre-mortem.md`), la partie D pour les lignes de
journal. Les titres et numéros de rubrique sont ceux des squelettes de `SKILL.md`. Les phrases en italique sous un
titre sont des consignes de remplissage : elles disparaissent du document rendu.

Règles de remplissage :

- Chaque nombre porte son statut, ceux d'`ARCHITECTURE.md` : `[F]` fait, `[H]` hypothèse (avec le rôle qui
  confirme), `[E]` estimation (calcul montré). Les dates et les durées d'un plan sont des propositions `[H]` que
  le décideur confirme en validant : une phrase en tête de document le dit.
- Des rôles, jamais des noms de personnes.
- En-tête : demandeur, valideur du livrable et décideur quand ils diffèrent. Pour un plan, le responsable du cas
  (le rôle qui le porte) et le décideur du plan (le rôle qui le valide) s'écrivent séparément quand ils diffèrent.
- Tableaux : toujours la ligne de séparation `|---|` sous l'en-tête.
- Un renvoi cite le livrable, le § et, si le livrable a été corrigé, la version lue (« 60-specification §13, v1.1 »).
  Un identifiant (EF, CA, T, R, IND, Q) se cite tel quel, sans le redéfinir.
- Citer, jamais recopier : le plan renvoie aux critères du pilote (§13 de la spécification) et aux indicateurs
  `IND-xx` (§14) ; il ne réécrit pas leurs valeurs, sauf dans un pré-mortem où une condition d'arrêt doit rester
  lisible.
- Un livrable amont validé qui se révèle faux ou incomplet se corrige par une version datée et une ligne
  « correction » au journal (`ARCHITECTURE.md`). Redater une échéance déjà passée à la date du plan n'est pas une
  correction : le plan le dit, avec l'ancienne date.

## A. Feuille de route — modèle de `mission/04-feuille-de-route.md`

```markdown
# Feuille de route — <entreprise ou périmètre>

Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle) · Rédigé par · Sources : 02-portefeuille, 03-chiffrage (et 00-contexte pour les contraintes)
*Une ligne d'annonce : ce que le document ordonne, et l'horizon.*

## 1. Les cas, notés
*Reprendre la facilité et le risque de 02-portefeuille ; un « à classer » y devient une note ici, avec la donnée
qui l'a levé. La valeur est le gain net central de 03-chiffrage, avec sa fourchette.*

| Cas | Équipe | Valeur (gain net central, fourchette) `[E]` | Facilité | Risque | Rang |
|---|---|---|---|---|---|
| | | | | | |

*Principe d'ordre en une phrase : ce qui fait passer un cas avant un autre, combien démarrent ensemble, et pourquoi
il n'y a pas de première vague de trois cas quand il n'y a pas trois gains rapides.*

## 2. La séquence
*La colonne « Prérequis » est un renvoi court à la rubrique 3 (« voir 3 : règles, lettrage… ») ; le détail daté vit
là-bas, une seule fois. La vague 0 réunit les actions sans construction (éliminer, simplifier, standardiser,
vérifier) : elle a son responsable, son jalon et sa pièce, et s'écrit « aucun indicateur suivi » avec la mesure de
départ de ce qu'on supprime.*

| Vague | Cas | Prérequis | Dépend de | Responsable (rôle) | Jalon `[H]` | Indicateur déjà suivi · mesure de départ |
|---|---|---|---|---|---|---|
| 0 | | | | | | aucun indicateur suivi · <mesure de départ> |
| 1 | | voir 3 | | | | |

## 3. Socle commun et prérequis à lever d'abord
*D'abord le socle commun : ce qui sert à plusieurs cas et se lève une seule fois (plateformes retenues ou
envisagées `[H]`, qui les exploite, règles de sécurité communes : comptes de l'entreprise, droits, secrets, lieu
des données). Puis ce qui manque (donnée, accès, processus à standardiser), pour quels cas, qui le lève, pour
quelle date. Une échéance déjà passée à la date du document est redatée ici.*

| Socle commun | Retenu ou envisagé `[H]` | Qui l'exploite (rôle) | Règles de sécurité communes | Pour quels cas |
|---|---|---|---|---|
| | | | | |

| Ce qui manque | Pour quels cas | Qui le lève | Pour quelle date `[H]` |
|---|---|---|---|
| | | | |

## 4. Ce qu'on ne fait pas maintenant
| Cas ou chantier | Pourquoi pas maintenant | Se rouvre si |
|---|---|---|
| | | |

## 5. Pré-mortem
*Gabarit de la partie C, rubrique numérotée 5.*

## Décision attendue
Valider l'ordre, les cas de la première vague et leurs responsables, le socle commun (plateformes, qui les
exploite, règles de sécurité), puis lancer le premier cas : il entre par `cadrer-besoin`.
```

## B. Plan de déploiement — modèle de `mission/cas-<slug>/70-plan.md`

```markdown
# Plan de déploiement — <titre court du cas>

Date · Demandeur (rôle) · Responsable du cas (rôle) · Décideur du plan (rôle) · Rédigé par · Sources : 30-exigences, 40-solutions, 50-rentabilite, 60-specification (version lue)
*Une ligne d'annonce : pour qui est écrit le plan, le mode (plan de déploiement : 60-specification est présente),
les étiquettes S1… reprises de 30-exigences §6, la numérotation continue des étapes pour tout le plan, et « toutes
les échéances sont des propositions `[H]` que le décideur du plan confirme en validant ».*

## 1. Objectif et critères de réussite
*Repris du besoin et des exigences.*

| Critère | Cible | Mesure de départ | Source |
|---|---|---|---|
| | | | |

*Puis la réussite du plan lui-même : la date d'horizon et, s'il y en a une, l'échéance ferme de l'entreprise.*

## 2. Lots
*Sous ce titre : la charge des personnes pendant les lots (heures par rôle, reprises de 50-rentabilite), en disant
si les séances habituelles ou celles du pilote y sont comprises ; et les lots qui se chevauchent, avec ce qui
dépend des deux.*

### Lot 1 — <nom> (durée `[H]`, du <date> au <date>)
*Le lot 0, ou le premier lot, porte les simplifications du diagnostic (20-diagnostic §7), la mesure de départ et la
re-mesure qui nourrit la porte. Trois à six étapes ; au-delà, scinder.*

| # | Étape | Responsable (rôle) | Preuve que c'est fait | Dépend de |
|---|---|---|---|---|
| 1 | | | | — |

Ce qu'on ne fait pas dans ce lot : …

## 3. Porte, pilote, recette et mise en production
*Porte : seulement si 40-solutions §10 en pose une ; sinon « sans objet ». Elle reprend la condition, sa mesure
avec son agrégation (moyenne, minimum ou chaque occurrence), la date au plus tôt, le rôle qui la constate et
l'étape qui la constate ; elle dit ce qui se passe si une condition est « non » (la construction ne démarre pas,
l'option 0 reste en place, repli). Le détail des conditions vit dans l'étape qui les constate, une seule fois.*

*Pilote : périmètre · dates · critères de poursuite, de prolongation et d'arrêt (renvoi à 60-specification §13,
signés avant de commencer : on cite la fiche signée sans recopier les valeurs) · hypothèses `[H]` de
50-rentabilite à confirmer · décideur de la suite — continuer, prolonger ou arrêter.*

*Recette : qui accepte (pas celui qui construit), sur quelles données, quand.*

*Mise en production : jour et ordre de bascule · retour arrière (qui, sur quel signal, comment on vérifie que
l'ancienne méthode a repris) · interrupteur. Le plan prévoit ; les actions, le feu vert et la bascule se
tiennent dans 90-mise-en-service.*

## 4. Adoption
*Une réponse, un rôle et une échéance par question, ou `?`.*

1. Qui reprendra le dispositif, avec quel niveau d'autonomie ?
2. Quels gestes l'équipe doit-elle savoir faire sans le consultant ?
3. Quels rôles ont besoin d'une formation, d'un guide, d'une vidéo ou d'une documentation technique ?
4. Quels accès, propriétaires de comptes et procédures de secours faut-il transmettre ?
5. Comment vérifier que l'équipe a compris et sait corriger une erreur courante ?
6. Quel support après la transmission, et qu'est-ce qui relève d'une nouvelle mission ?

## 5. Exploitation
*Propriétaire et suppléant (rôles, de 60-specification §17) · maintenance : qui, rythme, heures `[H]` (cohérentes
avec 50-rentabilite, au taux de celui qui la fait) · fiche d'une page (la même que 60-specification §17), qui
répond à quatre questions : comment vérifier que ça marche, que faire en cas d'incident, qui joindre, comment revenir
en arrière ; essayée par quelqu'un qui ne l'a pas écrite · comptes et accès à transmettre · alertes. Une limite de coût ou d'usage qui
n'est pas un indicateur se calcule ici, calcul montré, et se relève chaque mois.*

## 6. Protocole de mesure
*Les `IND-xx` et leurs seuils de production sont définis dans la spécification, rubrique 14 ; les seuils du pilote, rubrique 13.
Reprendre chaque indicateur par son identifiant, sans réécrire ses valeurs. Pendant le pilote, l'arrêt est celui de
la rubrique 13 ; après la bascule, celui de la rubrique 14. Un indicateur de contexte sans seuil d'arrêt s'écrit
« sans objet ».*

| Indicateur (`IND-xx`, intitulé de 60-specification §14) | Relu par (rôle) | Rythme de la revue | Action au seuil de correction | Action au seuil d'alerte | Action au seuil d'arrêt |
|---|---|---|---|---|---|
| | | | | | |

## 7. Communication
| Public | Message (le pourquoi d'abord) | Canal | Moment |
|---|---|---|---|
| | | | |

*Pour chaque public : ce qui change, ce qui disparaît, ce qui reste.*

## 8. Pré-mortem
*Gabarit de la partie C, rubrique numérotée 8.*

## Décision attendue
Valider le plan et lancer le premier lot — ou le corriger. Les réponses attendues avec la validation se listent
ici (suppléant à désigner, échéance à tenir sans glissement, dates d'absence à fournir).
```

## C. Pré-mortem — gabarit à ranger dans la feuille de route (rubrique 5) ou dans le plan (rubrique 8)

```markdown
## <n>. Pré-mortem

Thèse attaquée : … (une ou deux phrases falsifiables)
Contributions : rôles consultés, ou « rédigé par le consultant seul » (et l'étape du plan où chacun écrit seul ses raisons d'échec).
Point de départ des conditions d'arrêt (plan d'un cas seulement) : celle de 40-solutions §1, et les histoires qui la reprennent.

| # | Histoire d'échec (au passé) | Vraisemblance | Gravité | Signal d'alerte précoce | Parade | Condition d'arrêt | Propriétaire (rôle) | Classement |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | (pré-mortem n° 1) si elle a durci le plan | | | |

Écartées : objection — raison.
Verdict : engager | durcir | pivoter — en une phrase, avec le compte : « n parades manquantes sur m histoires retenues ».
Version durcie (si durcir) : ce qui s'ajoute au plan, étape par étape, chaque ajout renvoyant à son numéro d'histoire.
À rejouer : aux jalons suivants.
```

## D. Lignes de journal

Une par décision, avec l'étiquette « découverte » pour `04-feuille-de-route.md` et `cas-<slug>` pour le plan. Les
décisions qui n'ont pas de livrable (porte constatée, fin de pilote, bascule) citent la pièce qui les prouve :

```markdown
- 2026-11-04 · découverte · 04-feuille-de-route validée par le comité de direction · « première vague : un cas par équipe ; le cas des achats attend la donnée fournisseurs »
- 2026-11-18 · cas-saisie-commandes · 70-plan validé par la direction commerciale · « pilote sur une équipe, arrêt si l'adoption reste sous le seuil convenu »
- 2026-11-24 · cas-saisie-commandes · porte constatée par le responsable des opérations · « sept conditions remplies, fiche de porte jointe »
- 2026-11-30 · découverte · 04-feuille-de-route corrigée (version 1.1 : seuil de retard de la colonne « litige » ramené à trois jours ouvrés, comme dans la spécification) · confirmée par la direction générale
- 2026-12-09 · cas-saisie-commandes · fin du pilote : continuer, décidé par le responsable des opérations · « critères de la fiche signée atteints, relevé joint »
- 2026-12-14 · cas-saisie-commandes · bascule faite · « séance avec le flux seul ; sauvegarde du vendredi jointe »
```
