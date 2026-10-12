# Modèles — ordre de grandeur et business case

À ouvrir pour rédiger : la partie A pour `mission/03-chiffrage.md` (ordre de grandeur, porte « aucun besoin »), la
partie B pour `mission/cas-<slug>/50-rentabilite.md` (business case, porte « besoin connu »). Les titres et
numéros de rubrique sont ceux des squelettes de `SKILL.md`. Les formules, les unités de facturation, les arrondis et
un exemple de calcul sont dans `formules.md`. Les phrases en italique sous un titre sont des consignes de
remplissage : elles disparaissent du document rendu.

Règles de remplissage :

- Chaque terme porte son statut, ceux d'`ARCHITECTURE.md` : `[F]` fait (devis ou tarif datés, relevé, décision
  énoncée par son détenteur), `[H]` hypothèse (avec le rôle qui peut la confirmer), `[E]` estimation. Tout résultat
  est `[E]`.
- En-tête : demandeur, valideur et décideur quand ils diffèrent ; un seul rôle quand c'est le même.
- Montants à l'euro, durées à la minute, délais de retour au dixième de mois ; les dérivés se calculent sur les
  valeurs non arrondies (`formules.md`, section 8). Un tableau dont les valeurs sont arrondies le dit dans sa légende.
- Tableaux : toujours la ligne de séparation `|---|` sous l'en-tête.
- Un livrable validé qui doit changer prend une version datée et une ligne « correction » au journal.

## A. Ordre de grandeur — modèle de `mission/03-chiffrage.md`

```markdown
# Chiffrage — ordre de grandeur du portefeuille

Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle) · Rédigé par · Sources lues
*Cas chiffrés : ceux que la validation de 02-portefeuille a décidé de creuser. Les cas mis en attente ou écartés ne le
sont pas, et le document le dit.*

## 1. Paramètres communs
*Coût horaire chargé par rôle · base HT ou TTC · taux d'adoption · part du temps libéré réemployée · montée en
charge · horizon · critère d'investissement de l'entreprise, s'il existe (il remplace alors les repères du pack,
dans la même logique de classement).*

| Paramètre | Valeur | Statut | Source, ou qui peut confirmer |
|---|---|---|---|
| | | | |

## 2. Un cas par ligne, en fourchettes bas–haut
*Tous les montants sont `[E]`. Format de chaque cellule : bas–haut (central). Trois hypothèses communes font
varier les cas : minutes gagnées, part réemployée, adoption ; les autres termes restent au central. Pas de
classement de sensibilité ici : il est réservé au business case. La dernière colonne nomme le `[H]` dont dépend
le cas. Le calcul de chaque ligne se montre sous le tableau.*

| Cas | Gain brut/mois | Construction | Fonctionnement + maintenance/mois | Gain net/mois | Délai de retour | Hypothèse la plus fragile |
|---|---|---|---|---|---|---|
| | | | | | | |

## 3. Classement
*Solides · À mesurer d'abord · Douteux — une ligne de raison par cas ; dans chaque groupe, par gain net central
décroissant.*

## 4. Hypothèses à confirmer
| Hypothèse | Cas concernés | Qui peut la confirmer | Mesure courte proposée |
|---|---|---|---|
| | | | |

## 5. Hors chiffrage
*Valeur non financière, non convertie (qualité, risque, satisfaction des équipes, délai client) et ce qui n'est pas
chiffré, avec la raison.*

## Décision attendue
Pour chaque cas : y aller (il entre dans la feuille de route), mesurer d'abord, ou ne pas y aller.
```

## B. Business case — modèle de `mission/cas-<slug>/50-rentabilite.md`

```markdown
# Rentabilité — <titre court du cas>

Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle) · Rédigé par · Options chiffrées (de `40-solutions.md`) : <retenue> / <repli>

## 1. Situation de référence
*Ce que le processus coûte aujourd'hui : volumes, temps, erreurs repris de `20-diagnostic.md`. Quand une option
en suit une autre (simplifications, puis construction), la référence de la seconde est l'état après la première.*

## 2. Hypothèses et mesure
| Terme | Valeur centrale | Basse–haute plausible | Statut | Source, ou qui peut confirmer |
|---|---|---|---|---|
| | | | | |

*Puis : valeurs à relever avant le déploiement (qui, comment) et valeurs à relire après.*

## 3. Calcul par option
*Colonnes : option retenue, option de repli et, quand l'option retenue suit une autre, une colonne « apport de
l'option » (ce que la seconde apporte au-dessus de la première). Le gain se répartit explicitement entre les deux,
comme dans `20-diagnostic.md` §9, sans compter deux fois les mêmes minutes ; la décision se lit sur l'apport. Puis
les trois lectures du coût : payé · mobilisé · optimisé. Le délai de retour compte le payé et le mobilisé ; le
délai « payé seul » s'affiche à côté. Si `03-chiffrage.md` existe pour ce cas, une phrase explique l'écart avec
lui (phases, hypothèses) ; si l'écart révèle un trou de `03`, celui-ci est corrigé par une version datée.*

| Ligne | Option retenue | Option de repli | Apport de l'option |
|---|---|---|---|
| Gain brut/mois | | | |
| Construction (payé + mobilisé) | | | |
| Fonctionnement/mois | | | |
| Maintenance/mois | | | |
| Gain net/mois | | | |
| Délai de retour, montée en charge comprise | | | |
| Délai de retour, payé seul | | | |

## 4. Trois scénarios et point mort
*Sensibilité d'abord : chaque hypothèse seule, les autres au central ; retenir les deux ou trois qui écartent le plus
(elles peuvent différer de celles de `03-chiffrage.md` ; `50` fait foi). Un scénario bas dont le gain net est négatif
s'écrit « ne se rembourse pas » et se dit sous le seuil de rentabilité mensuelle.*

| | Bas | Central | Haut |
|---|---|---|---|
| Hypothèses qui varient | | | |
| Gain brut par mois | | | |
| Gain net par mois | | | |
| Délai de retour | | | |

*Point mort : « reste rentable tant que … », pour le critère de l'entreprise s'il existe, et pour les repères du
pack à titre d'alerte.*

## 5. Temps libéré et adoption
*Ce que devient le temps libéré (usage nommé, part réemployée) · taux d'adoption · montée en charge.*

## 6. Valeur non financière
*Nommée, non convertie.*

## 7. Recommandation
*Y aller · ne pas y aller · mesurer d'abord : trois raisons au plus, et ce qui la renverserait. Le classement suit
le critère de l'entreprise s'il existe (solide : le bas passe ; à mesurer d'abord : le central passe, le bas non ;
douteux : le central ne passe pas). Le décideur peut renverser la recommandation : sa décision s'inscrit au journal.*

## Décision attendue
Valider la recommandation — ou la corriger.
```

## C. Lignes de journal

Une par décision, avec l'étiquette « découverte » pour `03-chiffrage.md` (jamais « portefeuille ») :

```markdown
- 2026-10-21 · découverte · 03-chiffrage validé par la direction des opérations · « les cas solides sont retenus, celui qui dépend d'une hypothèse attend une mesure »
- 2026-10-28 · cas-saisie-commandes · 50-rentabilite : « mesurer d'abord » décidé par la direction commerciale · « relever le temps réel et nommer l'usage du temps libéré »
- 2026-11-05 · découverte · 03-chiffrage corrigé (version 1.1 : le central de la ligne « Saisie » réunit deux effets que le diagnostic sépare) · confirmé par la direction des opérations
```
