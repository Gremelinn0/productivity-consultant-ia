# Modèle de la fiche solutions

À ouvrir pour rédiger `mission/cas-<slug>/40-solutions.md`. Les titres et numéros de rubrique sont ceux du
squelette de `SKILL.md`. Les chiffres des exemples sont fictifs. Les phrases en italique sous un titre sont des
consignes de remplissage : elles disparaissent du document rendu.

Règles de remplissage :

- Chaque nombre porte son statut, ceux d'`ARCHITECTURE.md` : `[F]` fait (devis ou page d'éditeur datés, relevé du
  diagnostic, décision énoncée par son détenteur), `[H]` hypothèse (avec le rôle qui la confirme), `[E]` estimation
  (calcul montré). Toute capacité ou tout prix de plateforme est daté (« lu le … sur la page de l'éditeur ») ou `[H]`.
- Des rôles, jamais des noms de personnes.
- En-tête : demandeur, valideur et décideur quand ils diffèrent. Le décideur peut dépendre du montant de l'option
  retenue (seuils d'engagement de l'entreprise) : écrire la règle qui le désigne, et le rôle qui en découle.
- Tableaux : toujours la ligne de séparation `|---|` sous l'en-tête.
- Un niveau par étape dans la rubrique 4 : le plus prudent. Une étape qui mêle un acte irréversible (envoyer) et un
  acte automatique sans risque (consigner) reçoit « préparée puis validée », et le dit dans « Pourquoi ».
- Les questions ouvertes portent un identifiant `Q-xx` numéroté une fois pour tout le cas, à la suite de
  `30-exigences.md`.
- Un renvoi cite le livrable, le § et, si le livrable a été corrigé, la version lue.

## Le modèle

```markdown
# Solutions — <titre court>

Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle, ou la règle qui le désigne selon le montant de l'option retenue) · Rédigé par · Exigences lues : 30-exigences du <date>, version <n>

## 1. Recommandation
**Option retenue** : <numéro et nom>, construite par <interne · éditeur · recrutement · indépendant · prestataire>.
**Porte** : la condition qui ouvre la construction (rubrique 10), ou « aucune ».
**Trois raisons porteuses** : 1. … 2. … 3. …
**Ce qui doit être vrai** : chaque condition avec la personne qui peut la confirmer `[H]`. Un seuil qui ne se calcule
qu'au business case s'écrit « seuil fixé par le point mort de 50-rentabilite » : la fiche est validée avant le chiffre,
puis la porte (rubrique 10) et la spécification le reprennent.
**Contre-argument le plus fort** : …
**Ce qui ferait changer d'avis** : …
**Condition d'arrêt** : le signal observable, avec son seuil, qui fait arrêter ou revenir au repli.
**Option de repli** : <option>, et pourquoi elle vient en second.

## 2. Faut-il automatiser ?
| Facteur | Valeur | Statut et source |
|---|---|---|
| Fréquence | | |
| Temps gagné par occurrence | | |
| Taux d'erreur à la main | | |
| Stabilité du processus | | |

Verdict : automatiser · standardiser d'abord · assister seulement · ne rien construire — et pourquoi.
« Standardiser d'abord » : option 0 seule, ou option à construire retenue sous une porte (rubrique 10).

## 3. Le chemin le plus simple
La question, la réponse, ce qu'on supprime ou simplifie avant tout. L'option 0, précisément : ce qui change, ce
qu'elle règle des exigences, ce qu'elle ne règle pas.

## 4. Où l'humain reste dans la boucle
| Étape du processus cible | Niveau (automatisée · préparée puis validée · humaine) | Pourquoi | Rôle qui valide |
|---|---|---|---|
| | | | |

## 5. Les options examinées
| N° | Famille | Retenue pour la matrice ? | Pourquoi |
|---|---|---|---|
| 0 | Ne rien construire | | |
Huit lignes, de 0 (ne rien construire) à 7 (hybride). Pour chaque option retenue : en quoi elle consiste, qui la
construit, ce qui existe déjà et se réutilise, ce qui a été vérifié (où, quand) ou `[H]`. Sans accès aux pages
des éditeurs, la recherche s'écrit « non vérifiée » `[H]` et passe en rubrique 9.

## 6. Matrice
Éliminatoires : exigence Indispensable non couverte · contrainte ferme violée (outil imposé, budget plafond,
lieu des données). L'option 0 n'est jamais éliminée par la couverture : sa couverture se lit « fonction assurée
à la main », avec l'écart de temps ou de risque noté. Une option éliminée garde sa colonne, titrée « (éliminée) »,
avec « non évalué » dans ses cellules et son motif dans cette ligne.

| Critère | Option A | Option B | Option C |
|---|---|---|---|
| Couverture des exigences | | | |
Une colonne par option, et deux pour une même option si deux profils de constructeur sont plausibles (coût,
délai et maintenance changent). Neuf lignes : couverture des exigences · coût de construction · coût de
fonctionnement (unité facturée × volume) · maintenance · fiabilité et risque · sécurité et lieu des données ·
dépendance et portabilité · compétences internes pour maintenir · délai. Cellule : favorable · acceptable ·
défavorable, une raison courte, le statut du chiffre.

## 7. L'option de repli
Même grille de lecture que l'option retenue : raisons, conditions, contre-argument.

## 8. Plateforme ou code
Seulement si une option passe par une plateforme sans code : unité de facturation, volume, ordre de
grandeur du coût mensuel `[E]`, page de l'éditeur lue (date) ou `[H]`, façon d'en sortir.

## 9. À vérifier avant de signer
| Hypothèse `[H]` | Qui la confirme | Avant quand |
|---|---|---|
| | | |

## 10. Porte
Seulement si l'option est retenue sous condition (standardiser, puis construire) ; sinon « sans objet ». L'option 0
s'applique dès maintenant ; la construction attend que la condition soit constatée.

| Condition de démarrage | Mesure (qui, comment) | Agrégation | Seuil | Date au plus tôt | Constatée par |
|---|---|---|---|---|---|
| | | moyenne des occurrences · minimum · chaque occurrence | | | |

Ce qui se fait tant que la porte est fermée (option 0, préparation de la spécification et du devis) et ce qui ne se
dépense pas. La porte se constate avec les autres conditions de la rubrique 1, avant toute signature.

## 11. Questions ouvertes
*Statut : « ouverte, échéance <date> » ou « répondue le <date> », avec la réponse et son statut.*

| ? | Question | Rôle qui répond | Statut |
|---|---|---|---|
| Q-xx | | | |

## Décision attendue
Choisir l'option retenue, le repli ou l'option 0 (ne rien construire), et dire qui construit.
```

## La porte, en trois lignes

- **Quand** : le verdict de la rubrique 2 est « standardiser d'abord » et une option à construire reste la meilleure
  une fois le processus stabilisé.
- **Quoi** : une condition qu'on peut constater sur une pièce (une mesure relevée, un accord écrit), jamais une
  intention. Elle écrit son agrégation : « la moyenne des trois lundis conformes laisse au moins N min » n'est pas
  « chaque lundi laisse au moins N min » ni « le pire lundi ».
- **Après** : `planifier-deploiement` la reprend (étape datée avec sa pièce), `rediger-cahier-des-charges` la reprend
  en rubrique 1 de la spécification. Elle n'est pas un pilote : elle précède la construction, le pilote suit la recette.
