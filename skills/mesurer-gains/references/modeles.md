# Modèles — mesure après mise en service

À ouvrir pour rédiger `mission/cas-<slug>/95-mesure.md` : la partie A donne le modèle du livrable (dont la demande de données), la partie B les lignes de journal, la partie C les pièges.
Les titres et numéros de rubrique sont ceux du squelette de `SKILL.md`. La méthode (statuts, comparabilité, recalcul avec un exemple, échecs, cas difficiles, règles de décision,
portefeuille) est dans `mesure.md`. Les phrases en italique sous un titre sont des consignes de remplissage : elles disparaissent du document rendu. Les exemples sont fictifs.

Règles de remplissage :

- Chaque nombre porte son statut, ceux d'`ARCHITECTURE.md`. Ici, et ici seulement, un gain peut être `[F]` : relevé daté, avec source, méthode et propriétaire, ou calcul montré dont tous les
  termes sont `[F]` pour la même période. Un terme supposé fait du résultat une `[E]` et se nomme. Une projection est `[E]`. Un relevé sans période, sans source ou sans méthode est `[H]`.
- Des rôles, jamais des noms de personnes. Aucune donnée personnelle dans le dossier : des compteurs, des durées, des agrégats par rôle.
- Tout renvoi cite le livrable, le § et la version lue (« 60-specification §14, v1.1 »). `IND-xx`, `EV-xx`, `D-xx`, `A-xx`, `R-xx` se citent tels quels.
- `50-rentabilite.md` n'est jamais réécrit : le réel s'écrit ici, l'écart se lit terme par terme.
- Chaque revue produit une nouvelle version du document (1.0, 1.1…) : l'en-tête donne le motif (« Version 1.1, revue du 2027-02-09 : relevé de janvier »), l'historique (rubrique 10) garde
  la période et la décision de chaque version. Une correction de fond d'une version déjà validée suit la règle de `ARCHITECTURE.md` (version datée, ligne « correction » au journal).
- Tableaux : toujours la ligne de séparation `|---|` sous l'en-tête.

## A. Modèle de `mission/cas-<slug>/95-mesure.md`

```markdown
# Mesure — <titre court du cas>

Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle) · Rédigé par · Version · Période mesurée (du … au …, périmètre) · Sources : 20-diagnostic, 50-rentabilite, 60-specification §14, 70-plan §6, 90-mise-en-service (version lue de chacun)
Lecture : première lecture | revue n° k — données reçues le … | aucune donnée reçue : ce document est la demande de relevés
*Une ligne d'annonce : ce que le document compare, sur quelle période, et « le réel s'écrit ici ; 50-rentabilite garde l'estimation sur laquelle la décision d'y aller a été prise ». Sans aucune donnée :
la rubrique 1 (demande de relevés) et la décision attendue suffisent ; rien n'est `[F]`, le document le dit.*

## 1. Données reçues et leurs limites
*Une ligne par relevé. « Comparable au départ » : même définition, même méthode, même source, même périmètre, période de longueur et de saison comparables. Un relevé sans période, source ou méthode est `[H]`.*

| Relevé | Rôle qui l'a relevé | Période | Méthode | Dépôt (`mission/sources/…`) | Comparable au départ ? | Statut |
|---|---|---|---|---|---|---|
| | | | | | | |

Version en service pendant la période : … · dernière version validée au registre de 90-mise-en-service : … → identique · différente (période « version non validée »).
Règles d'exclusion écrites avant la lecture : … (cas atypiques écartés, avec leur raison). Le résultat se montre avec et sans.

**Demande de données** — *obligatoire dès qu'un relevé manque ; c'est tout le livrable quand aucune donnée n'est reçue. Une ligne par `IND-xx` et par terme de 50-rentabilite §2 non couvert.*

| Ce qu'on relève | Pour quel `IND-xx` ou terme de 50 | Méthode (la même qu'au départ) | Période | Rôle qui relève | Dépôt et format | Pour le | Exclusions écrites d'avance |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 2. Indicateurs
*Une ligne par `IND-xx` de 60-specification §14, rangée par famille : volume · temps humain complet (retouches et supervision comprises) · erreurs · qualité · satisfaction · adoption active · coûts d'usage ·
incidents · maintenance. Une famille couverte par un terme de 50 §2 ou un relevé de 70 §5 plutôt que par un `IND-xx` renvoie à la rubrique 3 ou 4 et signale le trou de 60 ; une famille sans aucun relevé s'écrit « non
relevée : raison ». Propriétaire, période et méthode viennent de 60 §14 ; absents, c'est un trou de 60 à corriger par version datée. Les seuils sont ceux de 60 §14, cités, jamais refaits. Position : dans les seuils ·
correction · alerte · arrêt.*

| Famille | `IND-xx` | Propriétaire · méthode | Départ (valeur · période · statut) | Observé (valeur · période · statut) | Écart au départ | Seuils (cités) | Position |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 3. Business case terme par terme
*Les termes de 50-rentabilite §2, un par ligne. Position dans l'éventail : sous le bas · entre le bas et le central · entre le central et le haut · au-dessus du haut. Puis les conditions du point mort de 50 §4, recalculées
avec les termes observés quand ce point mort supposait les autres termes au central.*

| Terme (50 §2) | Estimé : bas · central · haut | Observé (période · statut) | Position | Écart au central |
|---|---|---|---|---|
| | | | | |

| Condition du point mort (50 §4) | Seuil | Observé | Passe ? |
|---|---|---|---|
| | | | |

## 4. Gain et coûts réels
*Mêmes formules que 50 (`chiffrer-rentabilite`, `formules.md` §2 à §4), valeurs observées. Un terme observé en exploitation contient déjà l'adoption : ne pas la réappliquer. Le calcul est montré sous le tableau.
Statut : `[F]` si tous les termes sont `[F]`, sinon `[E]` avec le terme supposé nommé ; le retour projeté est `[E]`, par la seule formule de 50 §4 ; un gain net nul ou négatif s'écrit « pas de retour ».*

| Ligne | Estimé (50, central) | Observé | Écart | Statut |
|---|---|---|---|---|
| Gain brut par mois | | | | |
| dont temps libéré réemployé | | | | |
| dont erreurs évitées | | | | |
| Construction payée (facture) | | | | |
| Construction mobilisée (heures notées de pilote, recette, formation) | | | | |
| Fonctionnement par mois : abonnements | | | | |
| Coûts d'usage par mois (exécutions, appels, jetons, crédits) | | | | |
| Maintenance par mois (heures notées × taux de celui qui la fait) | | | | |
| Incidents (heures de reprise × taux, coûts directs) | | | | |
| Gain net par mois | | | | |
| Retour : constaté (cumul réel), projeté `[E]` (formule de 50 §4) ou « pas de retour » (gain net nul ou négatif) | | | | |

## 5. Adoption et usage
*Adoption active = occurrences passées par le dispositif ÷ occurrences totales, par rôle ; pas les comptes ouverts, pas les formations suivies. Contournements : tableur parallèle, ancienne voie reprise, demandes de
dérogation. Jamais une ligne par personne.*

| Rôle | Occurrences totales | Passées par le dispositif | Adoption active | Contournements constatés | Cause probable |
|---|---|---|---|---|---|
| | | | | | |

## 6. Cas lus, échecs et incidents
*Échantillon : taille `[H]` fixée avant la lecture ; tirage (au hasard, plus les réclamations, plus les cas à risque de 60 §12) ; lu par <rôle du client> ; période. Catégories : celles de 85-recette (pour l'IA, les familles
d'erreurs des `EV-xx`). Chaque échec compte une fois, par le premier mode qui l'a trouvé.*

| Catégorie d'échec | Trouvés | par alerte | par lecture | par réclamation | Action |
|---|---|---|---|---|---|
| | | | | | |

Taux d'échec dans l'échantillon aléatoire : … sur n = … (fourchette large si n est petit). Part des échecs vus par une alerte : … Échecs silencieux : … → alerte ou contrôle à ajouter et à tester : …

*Incidents de la période : une ligne datée par incident, sans identifiant propre. Un incident qui révèle un défaut de la solution prend un `D-xx` (série continue) ; un incident qui réalise un risque prévu renvoie à son `R-xx`.*

| Date | Ce qui s'est passé | Détecté par | Durée | Effet | Cause | `D-xx` · `R-xx` |
|---|---|---|---|---|---|---|
| | | | | | | |

Histoires du pré-mortem (70 §8) produites : … · signal qui a parlé : … · histoire non prévue : … (à ajouter au pré-mortem à la prochaine revue).

## 7. Cas difficiles
*Pour chacun : « non constaté », ou le constat et la conduite (méthode : `mesure.md` §5).*

| Cas | Constaté ? | Constat | Conduite |
|---|---|---|---|
| Adoption nulle ou presque | | | |
| Gain net devenu négatif | | | |
| Changement non approuvé | | | |

## 8. Décision
*Réponse d'abord. Règles par défaut `[H]` : `mesure.md` §6, à confirmer par le décideur.*

Décision proposée : continuer · corriger · étendre · arrêter.
Trois raisons au plus : …
Ce qui la renverserait : …
Contre-cas le plus fort : … (`router-consulting-strategy`, si appelé : le dire ; sinon l'écrire soi-même)

| Action | Rôle | Date | Passe par 90 (`A-xx`) ? |
|---|---|---|---|
| | | | |

Prochaine lecture : <date> · relevés attendus : …

## 9. Ce que la mesure change pour le portefeuille
*Sans porte découverte : ce qui servira aux cas suivants du même client, ou « sans objet ». Une correction de `02`, `03` ou `04` se fait par version datée et ligne « correction » au journal, par la compétence qui le possède.*

| Paramètre ou décision | Supposé (document · version) | Observé | Cas concernés | Proposition | Propriétaire de la correction |
|---|---|---|---|---|---|
| | | | | | |

## 10. Historique des revues

| Version | Date | Période | Décision | Pièce (journal) |
|---|---|---|---|---|
| 1.0 | | | | |

## Décision attendue
Décider : continuer, corriger, étendre ou arrêter — ou demander les relevés manquants ; confirmer les règles de décision par défaut.
```

## B. Lignes de journal

Une par décision, avec le cas et la version de 95. Une correction d'un livrable du portefeuille s'écrit aussi :

```markdown
- 2027-01-12 · cas-saisie-commandes · 95-mesure, première lecture : « corriger » décidé par la direction commerciale · « adoption à 72 %, maintenance à 6 h par mois ; formation de la seconde équipe, relecture du modèle ; nouvelle lecture le 2027-02-09 »
- 2027-02-09 · cas-saisie-commandes · 95-mesure version 1.1 : « continuer » décidé par la direction commerciale · « seuils respectés deux lectures de suite ; extension à rediscuter à la revue de juin »
- 2027-06-08 · cas-saisie-commandes · 95-mesure version 1.2 : « étendre » décidé par la direction commerciale · « la seconde équipe entre par chiffrer-rentabilite avec les valeurs observées »
- 2027-03-09 · cas-saisie-commandes · 95-mesure : « arrêter » décidé par la direction commerciale · « retrait par les actions A-12 à A-15 de 90-mise-en-service ; retour à l'option 0 »
- 2027-01-14 · découverte · 03-chiffrage corrigé (version 1.1 : part du temps libéré réemployée observée à 35 % au lieu de 50 % pour le cas saisie des commandes) · confirmé par la direction générale
```

## C. Pièges fréquents

| Piège | Comment le repérer | Correction |
|---|---|---|
| Gain annoncé sur des exécutions réussies | « 3 000 exécutions » sans résultat côté métier | relever le résultat métier ; les exécutions restent une source d'activité |
| Périodes qui ne se ressemblent pas | départ en milieu de mois, mesure en fin de mois ; hiver contre été | même rythme, même saison, volume corrigé ; sinon « a contribué à » |
| Moyenne de quelques points | « 4,5 minutes » sans le nombre d'observations | écrire n, le minimum et le maximum |
| Adoption mesurée par les comptes ouverts | « 90 % de l'équipe a un accès » | occurrences passées par le dispositif ÷ occurrences totales |
| Adoption appliquée deux fois | un terme déjà observé en exploitation est multiplié par le taux | appliquer le taux au nombre d'occurrences, pas aux résultats déjà observés |
| Temps libéré compté en euros sans usage | « 40 h libérées » et aucun usage constaté | ne compter que la part réemployée observée ; le reste est de la valeur non financière |
| Maintenance oubliée | un gain net sans ligne de maintenance | heures notées × taux de celui qui la fait |
| Temps humain incomplet | on compte le temps de traitement sans la relecture, ni la supervision, ni les exceptions | temps complet, et recherche du travail déplacé ailleurs |
| Exclusions décidées après coup | les mauvaises semaines deviennent « atypiques » | règles écrites avant la lecture ; résultat avec et sans |
| Estimation réécrite | 50 modifié pour coller au réel | 50 intact ; l'écart s'écrit ici |
| Mesure de départ unique prise pour la référence | une seule séance de départ comparée à une moyenne | la re-mesure sur plusieurs occurrences d'avant le pilote, et les deux écrites |
| Gain du pilote extrapolé | « gain annuel » calculé sur un mois de pilote | `[F]` pour la période et le périmètre du pilote ; la suite est `[E]` |
| Version non validée mesurée | la version en service diffère du registre de 90 | marquer la période, écrire l'incident au journal, demander au propriétaire de garder ou de défaire par une `A-xx` validée avant |
| Échecs silencieux ignorés | seules les alertes sont comptées | échantillon lu par un humain, classé par mode de découverte |
| Décision sans date de re-mesure | « corriger » sans prochaine lecture | action, rôle, date, relevés attendus |
| Personne évaluée | une ligne par personne dans l'adoption | par rôle, en occurrences |
| Mesure faite par celui qui y gagne | l'équipe qui a construit fournit seule les chiffres | relevés tirés des systèmes de l'entreprise, ou par un rôle qui n'a pas construit |
