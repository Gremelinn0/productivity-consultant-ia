# Modèle du diagnostic

À ouvrir pour rédiger `mission/cas-<slug>/20-diagnostic.md`. Les titres et numéros de rubrique sont ceux du
squelette de `SKILL.md`. Les chiffres de l'exemple sont fictifs. Les phrases en italique sous un titre sont des
consignes de remplissage : elles disparaissent du document rendu.

Règles de remplissage :

- Chaque nombre porte son statut, ceux d'`ARCHITECTURE.md` : `[F]` fait (relevé, pièce, observation, ou règle
  énoncée par son détenteur), `[H]` hypothèse (avec le rôle qui peut la confirmer), `[E]` estimation (calcul
  montré).
- Des rôles, jamais des noms de personnes.
- En-tête : demandeur, valideur et décideur quand ils diffèrent ; un seul rôle quand c'est le même.
- Tableaux : toujours la ligne de séparation `|---|` sous l'en-tête.
- Un diagnostic validé qui doit changer prend une version datée et une ligne « correction » au journal.

## Le modèle

```markdown
# Diagnostic — <processus>

Date · Demandeur (rôle) · Valideur (rôle) · Rédigé par · Source de la description : observation, entretien ou procédure · Relue par (rôle, date)

## 1. Le processus tel qu'il se fait
*Une ligne par étape (un verbe, un objet), les étapes hors périmètre comprises : le processus se décrit en
entier, puis la rubrique 6 les marque « hors périmètre ». Dire quelle source a servi, en rôles, ce qui n'a pas été
observé, et qui a relu la description (une personne qui fait le travail, pas seulement son responsable).*

| Étape | Rôle | Outil | Entrées | Sorties | Passage de main ou attente | Décision, exception ou variante |
|---|---|---|---|---|---|---|
| | | | | | | |

*Dans la dernière colonne : la règle de décision, l'exception et ce que l'on fait quand elle arrive, la variante
(ce qui change d'une personne, d'un client ou d'un cas à l'autre).*

*Schéma Mermaid facultatif.*

## 2. Mesures
*Une ligne par mesure et par statut : une mesure dérivée qui mêle `[F]` et `[E]` prend deux lignes. Une durée
chronométrée sur une seule occurrence est `[F]` pour cette occurrence ; la durée typique est `[H]` tant qu'on n'a
pas plusieurs occurrences. Ce qui n'est pas mesuré se dit, avec le moyen de le mesurer.*

| Mesure | Valeur | Statut | Source, ou comment la mesurer |
|---|---|---|---|
| Volume (exemple fictif) | 120 dossiers par mois | `[H]` | responsable de l'équipe ; à confirmer par un export |

*À mesurer : volume · fréquence · temps par étape · délai total · taux d'erreur ou de reprise · temps d'attente.
Statuts : ceux d'`ARCHITECTURE.md`.*

## 3. Goulets et gaspillages
| Étape | Nature (ressaisie, attente, double contrôle…) | Effet | Coût `[E]` |
|---|---|---|---|
| | | | |

## 4. Causes
*Une nature par cause : la dominante (processus, organisation, donnée ou outil). Deux natures qui appellent
deux acteurs font deux lignes.*

| Goulet | Pourquoi (la chaîne) | Cause actionnable | Nature : processus, organisation, donnée ou outil |
|---|---|---|---|
| | | | |

## 5. Stabilité
| Question | Réponse | Source |
|---|---|---|
| Le processus se fait-il pareil à chaque fois ? | | |
| Les règles de décision sont-elles écrites ? | | |
| Deux personnes ou plus le font-elles de la même façon ? | | |
| Les étapes, les outils ou les règles vont-ils changer bientôt ? | | |

*Si une seule personne a été observée, la réponse à la troisième question repose sur le récit des autres : le
dire, garder les deux versions, noter l'autre personne « non observée ».*

Verdict : stable (le tri peut conclure à l'automatisation) ou à standardiser d'abord.

## 6. Tri des étapes
*Cinq issues : Éliminer · Simplifier d'abord · Automatiser · Déléguer à l'IA · Garder (critères : fréquence, coût,
valeur, risque si ça se trompe). Pas d'« Automatiser » si le verdict de la rubrique 5 est « à standardiser
d'abord » : une étape mécanique et stable en soi reçoit alors « Simplifier d'abord », avec l'issue visée après
la nouvelle mesure. Une étape hors périmètre reçoit « hors périmètre », sans issue.*

| Étape | Issue | Pourquoi | Garde-fou ou validation humaine |
|---|---|---|---|
| | | | |

## 7. À simplifier et à standardiser d'abord
*Liste ordonnée, avant toute automatisation : ce qu'on supprime, ce qu'on simplifie, ce qu'on écrit comme
procédure unique. Pour chacun : l'effet attendu `[E]` quand il y a un gain de temps ; sinon la mesure de qualité
qui le vérifiera et sa cible `[H]` (par exemple l'accord de deux personnes sur dix cas, ou le nombre de règles non
écrites) ; la mesure ; l'échéance proposée `[H]`. Le plan de simplification (qui fait quoi, quand) appartient à
`planifier-deploiement`, qui reprend cette liste.*

*Puis le mode opératoire du processus cible (la procédure du métier, pas la fiche d'exploitation du dispositif, qui
s'écrit plus tard en 80), quand le verdict de la rubrique 5 est « à standardiser d'abord » ou qu'une procédure
unique est retenue : une page que la personne qui fait le travail peut suivre sans la lire deux fois.*

| Étape cible | Rôle | Exceptions et conduite à tenir | Variantes (gardée · supprimée, pourquoi) | Indicateur de suivi |
|---|---|---|---|---|
| | | | | |

## 8. Les huit questions d'automatisation
*Chercher la réponse dans le besoin, les sources et l'observation avant de demander ; écrire la source dans la
cellule Réponse.*

| Question | Réponse, avec sa source | Statut |
|---|---|---|
| | | |

## 9. Opportunités classées
*Quatre classes : Gains rapides · Projets · À creuser · À écarter. Une opportunité sans gain direct qui conditionne
une autre (procédure unique, liste des comptes clés) porte la classe de celle qu'elle conditionne, notée « valeur
indirecte : elle conditionne <n> ».*

| Opportunité | Valeur (gain mensuel `[E]`) | Facilité | Risque | Classe |
|---|---|---|---|---|
| | | | | |

*Lecture, sous le tableau : (1) le gain partagé entre ce que retirent les simplifications et ce que retire
l'automatisation en plus, sans compter deux fois les mêmes minutes ; (2) les opportunités qui portent sur les mêmes
étapes et ne s'additionnent pas. Si ce partage contredit l'ordre de grandeur de `03-chiffrage.md`, celui-ci est
corrigé par une version datée.*

## Décision attendue
Choisir les causes à traiter et les simplifications à faire avant toute automatisation — ou les corriger.
```
