# Modèles — contexte, cartographie et portefeuille

À ouvrir pour rédiger `00-contexte.md`, `01-cartographie-taches.md` et `02-portefeuille.md`. Les titres et
numéros de rubrique sont ceux des squelettes de `SKILL.md`. Les chiffres des exemples sont fictifs. Les
phrases en italique sous un titre sont des consignes de remplissage : elles disparaissent du document rendu.

Règles communes de remplissage :

- Chaque nombre porte son statut : `[F]` fait (pièce, observation, ou décision énoncée par son détenteur,
  avec sa source), `[H]` hypothèse (avec le rôle qui peut la confirmer), `[E]` estimation (calcul montré) ;
  définitions dans `ARCHITECTURE.md`. Un temps ou un volume dit de mémoire en entretien est `[H]`, même
  s'il paraît plausible.
- Des rôles, jamais des noms de personnes.
- En-tête de chaque document : `Date · Demandeur (rôle) · Valideur (rôle) · Rédigé par`. Quand un seul rôle
  tient les deux premiers, une seule mention suffit (« Demandeur et valideur : direction générale »).
- Un document validé qui doit changer prend une version datée et une ligne « correction » au journal
  (`ARCHITECTURE.md`). Passer une source de « à venir » à sa date réelle n'est pas une correction.
- Tableaux : toujours la ligne de séparation `|---|` sous l'en-tête.

## A. Mode d'emploi de `00-contexte.md`

```markdown
# Contexte — <entreprise ou périmètre>

Date · Demandeur (rôle) · Valideur (rôle) · Rédigé par

## 1. Fiche entreprise
*Activité · taille et équipes concernées (rôles) · outils en place · données disponibles et où elles vivent ·
objectifs · contraintes (sécurité, conformité, budget, calendrier) · ce qui a été essayé · porte choisie et
pourquoi. Objectifs, contraintes, budget et essais passés viennent de l'entretien de cadrage avec la
direction : une règle ou une contrainte énoncée par son détenteur est `[F]`, sa source est l'entretien.*

## 2. Sources branchées et autorisations obtenues
*Une ligne par source. Un entretien ou une séance prévus s'écrivent « à venir », avec leur date prévue ;
quand ils ont eu lieu, la ligne prend sa date réelle.*

| Source | Nature (fichier, outil connecté, entretien, observation) | Date | Autorisation (qui, quand, périmètre) |
|---|---|---|---|
| | | | |

## 3. Sources manquantes
*Ce qui manque, ce que cela empêche de conclure, qui peut le fournir.*

## Décision attendue
Confirmer les sources à brancher et les équipes à écouter — ou les corriger.
```

## B. Mode d'emploi de `01-cartographie-taches.md`

```markdown
# Cartographie des tâches — <périmètre>

Date · Demandeur (rôle) · Valideur (rôle) · Rédigé par

## 1. Les tâches
*Lecture des colonnes. Durée par occurrence : minutes pour une unité traitée (une relance, un ticket, un
rapport). Volume : unités par mois. Fréquence : le rythme (« chaque lundi, 4 séances par mois »). Temps
mensuel = durée × volume. Une tâche hebdomadaire compte 4 occurrences par mois : convention à dire. Un
nombre relevé dans un export ou chronométré en séance est `[F]` ; dit de mémoire en entretien, il est `[H]`
avec le rôle qui peut le confirmer ; calculé, il est `[E]`. Une durée chronométrée sur une seule occurrence
est `[F]` pour cette occurrence et `[H]` comme durée typique.*

| Équipe | Tâche | Déclencheur | Fréquence | Durée par occurrence | Volume | Outils | Données | Passages entre équipes | Erreurs / reprises | Stabilité des règles | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Finance | Relancer les factures échues (exemple fictif) | échéance dépassée | chaque lundi, 4 séances par mois `[E]` | 10 min par relance `[H]` | 120 relances par mois `[F]` | tableur, courriel | factures, coordonnées | vente → finance | relances en double `[H]` | règles écrites `[F]` | entretien finance ; export |

## 2. Écarts gardés et tâches non observées
*Quand deux sources ou deux personnes décrivent une tâche autrement, garder les deux versions avec leur
source : l'écart est souvent le vrai sujet. Une tâche décrite par plusieurs sources se fusionne en une ligne.
Dire ce qui n'a pas été observé (une personne, une période, un cas rare) et ce que cela empêche de conclure.*

## 3. Le tri
*Cinq issues, posées dans l'ordre : Éliminer · Simplifier d'abord · Automatiser · Déléguer à l'IA · Garder.
Pour une tâche qui naît d'un défaut d'information, écrire que « Éliminer la cause » est testé d'abord. Pour
« Simplifier d'abord », écrire l'issue visée après la nouvelle mesure. Coût par occurrence = durée × coût
horaire chargé du rôle, avec son statut.*

| Tâche | Issue | Fréquence | Coût | Valeur | Risque si ça se trompe | Pourquoi cette issue |
|---|---|---|---|---|---|---|
| | | | | | | |

## Décision attendue
Confirmer que la cartographie ressemble au travail réel, que les équipes s'y reconnaissent et que le tri tient — ou le corriger.
```

## C. Mode d'emploi de `02-portefeuille.md`

```markdown
# Portefeuille de cas d'usage — <périmètre>

Date · Demandeur (rôle) · Valideur (rôle) · Rédigé par

## 1. Vue d'ensemble
*Valeur = gain mensuel `[E]`, calculé comme durée × volume de `01-cartographie-taches.md` : un plafond
(100 % du temps actuel), que `03-chiffrage.md` réduira. Facilité et risque : haut, moyen ou bas, avec une
raison d'une ligne que `planifier-deploiement` reprendra ; « à classer » quand une donnée manque, en écrivant
la donnée et la personne qui la fournit (le cas est alors « À creuser »).*

| Cas | Équipe(s) | Valeur (gain mensuel `[E]`) | Facilité | Risque | Classe (raison si « À écarter ») |
|---|---|---|---|---|---|
| | | | | | |

## 2. Fiches
*Une fiche par tâche triée « Automatiser », « Déléguer à l'IA » ou « Simplifier d'abord » ; une tâche
« Garder » seulement si l'IA y prépare, compare ou challenge sans décider (la fiche nomme qui décide). Pour
« Simplifier d'abord », la fiche dit ce qu'on simplifie en premier ; facilité et risque se notent après
simplification.*

### <Nom du cas> — <classe>
- **Résultat** : une phrase.
- **Pour qui** : rôle.
- **Problème** : une phrase.
- **Déclencheur** : l'événement qui lance le processus.
- **Entrées** : 3 à 6 données ou objets.
- **Ce que fait le système** : 3 à 7 étapes.
- **Sorties** : 1 à 4 résultats, dans l'outil métier.
- **Valeur** : temps, revenu, coût, risque ou qualité ; gain mensuel `[E]` avec son calcul.
- **Limites et validation humaine** : cas ambigus, qui valide, contraintes.
- **Preuve** : observé ou appuyé par une pièce `[F]` (ligne de `01`, source) · déclaré de mémoire `[H]` (qui peut le confirmer).
- **Déjà disponible** : outil en place, modèle, brique du marché, rien.

## 3. Recommandation
*À éliminer d'abord, sans IA : les tâches triées « Éliminer » et les causes à supprimer avant d'automatiser,
avec qui peut décider de les supprimer. Trois à cinq cas à faible effort et forte valeur, idéalement un par
équipe. Ce qui ferait changer cette recommandation.*

## Décision attendue
Quels cas creuser : pour chacun, creuser, mettre en attente ou écarter. La ligne de journal nomme les cas à
creuser (« on creuse : … »), le routeur en tire la liste « à lancer ».
```

## D. Lignes de journal

Une ligne par document validé, avec l'étiquette de cas « découverte » (jamais « portefeuille » ni le nom d'un
document) :

```markdown
- 2026-10-02 · découverte · 00-contexte validé par la direction générale · « sources : trois entretiens, deux exports et une séance enregistrée »
- 2026-10-07 · découverte · 02-portefeuille validé par la direction générale · « on creuse : relances de factures, tri des tickets, statut de commande »
```
