---
name: chiffrer-rentabilite
description: >-
  Quand on se demande si une automatisation ou un agent IA vaut son coût (« est-ce rentable ? »,
  « combien ça coûte, combien ça rapporte ? ») → chiffrer gains et coûts avec des hypothèses
  visibles : un ordre de grandeur par cas pour classer un portefeuille, ou un business case en trois
  scénarios pour décider d'une option, maintenance comprise. Étape de chiffrage des deux portes du
  pack consultant-ia, après le tri des cas (porte « aucun besoin ») ou la comparaison des solutions
  (porte « besoin connu »). Triggers : « chiffrer », « rentabilité », « ROI », « business case »,
  « retour sur investissement », « délai de retour », « payback », « analyse coûts-bénéfices »,
  « est-ce que ça vaut le coup », « TCO », « cost-benefit ».
metadata:
  scope: "le chiffrage de cas d'automatisation ou d'IA : ordre de grandeur de chaque cas d'un portefeuille, ou business case d'une option retenue et de son option de repli"
  owns: "gains, coûts de construction, de fonctionnement et de maintenance, délai de retour, trois scénarios, point mort, valeur non financière nommée, valeurs à relever avant et après déploiement"
  consumes: "mission/02-portefeuille.md et 01-cartographie-taches.md (porte aucun besoin) ; mission/cas-<slug>/10-besoin.md, 20-diagnostic.md et 40-solutions.md (porte besoin connu) ; mission/sources/ (tarifs, devis, coût horaire chargé)"
---

# Chiffrer la rentabilité

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/03-chiffrage.md` (ordre de grandeur) ou
> `mission/cas-<slug>/50-rentabilite.md` (business case). Preuve : le décideur tranche — y aller, ne
> pas y aller ou mesurer d'abord — et la décision s'inscrit dans `mission/journal.md`. Contrôle de
> forme : le modèle est complet (cinq rubriques pour l'ordre de grandeur, sept pour le business case),
> chaque nombre a son statut `[F]`, `[H]` ou `[E]`, la ligne de maintenance est présente, et un
> business case porte trois scénarios et un point mort. Exemple de référence : `examples/` du pack.
> **Boucle** : aucune.

## Ce que cette compétence résout

Le gain annoncé d'une automatisation est la partie visible d'un calcul ; ce qui le fait mentir, ce
sont les lignes oubliées : maintenance, coût à plein volume, équipe qui ne s'en sert qu'à moitié,
temps libéré sans usage. Ce chiffrage pose le calcul complet, avec des hypothèses contestables une
à une.

Il travaille à deux niveaux. L'**ordre de grandeur** (porte « aucun besoin ») donne à chaque cas d'un
portefeuille des fourchettes qui suffisent à classer et à choisir ceux qui méritent une étude. Le
**business case** (porte « besoin connu ») compare l'option retenue et son option de repli en trois
scénarios, et dit où la décision bascule.

Résultat attendu : un tableau ou une fiche où chaque nombre dit d'où il vient, et une
recommandation — y aller, ne pas y aller ou mesurer d'abord — que le décideur peut renverser.

## Stratégie

1. **Deux niveaux, deux précisions.** Un portefeuille se classe avec des fourchettes larges : chiffrer
   finement un cas qui sera peut-être écarté est du temps perdu. Une décision d'investissement
   demande l'inverse. Un ordre de grandeur ne se présente jamais comme un business case.
2. **Chaque terme porte son statut.** `[F]` fait observé, avec sa source ; `[H]` hypothèse, avec qui
   peut la confirmer ; `[E]` estimation calculée. Tout résultat est `[E]` : il hérite de la
   fragilité de son terme le plus faible, et le livrable le dit.
3. **Le coût complet, avec la ligne qu'on oublie.** Construction, fonctionnement et maintenance
   figurent toujours, même pour un outil du marché : sans la maintenance, l'erreur va dans le sens
   qui rassure.
4. **Du temps gagné n'est de l'argent que s'il est réemployé.** On dit ce que devient le temps
   libéré ; sans usage nommé, il compte comme valeur non financière, pas comme euros. Même règle pour
   l'adoption : si seule une partie de l'équipe s'en sert, on ne compte que cette part du gain.
5. **Des fourchettes et un point mort, pas un chiffre.** Trois scénarios qui font varier les deux ou
   trois hypothèses les plus incertaines, et le seuil où la décision bascule (« reste rentable tant
   que le temps gagné dépasse N minutes par occurrence »). Le décideur voit ce qu'il parie.
6. **Estimé n'est pas mesuré.** On décide vite sur des estimations à la louche, puis on les corrige
   avec le réel : mesure de départ définie avant le déploiement, valeurs relues après.
7. **La valeur non financière se nomme, elle ne se convertit pas.** Qualité, risque, satisfaction,
   délai client : écrits à côté du calcul, pas transformés en euros, qui auraient l'air d'un fait.

## Étapes

1. **Choisir le niveau.** Un portefeuille à trier (`mission/02-portefeuille.md`) → ordre de grandeur.
   Un cas dont `40-solutions.md` désigne une option retenue et une option de repli → business case,
   qui fait alors foi pour ce cas même s'il a déjà un ordre de grandeur (resté comme trace du tri).
2. **Lire ce qui existe.** Volumes, temps, erreurs : `01-cartographie-taches.md` ou
   `20-diagnostic.md` ; critères de succès et mesure de départ : `10-besoin.md` ; options :
   `40-solutions.md` ; tarifs, devis, coût horaire : `mission/sources/`. Un `[H]` recopié reste `[H]`.
3. **Fixer les paramètres communs** : coût horaire chargé par rôle (`[F]` s'il vient de l'entreprise,
   sinon `[H]` avec son confirmateur ; jamais une moyenne de marché), base HT ou TTC (la même
   partout), taux d'adoption, montée en charge, horizon de lecture (douze mois, vingt-quatre au plus :
   au-delà, le processus et les outils auront changé).
4. **Poser les gains et les coûts** avec les formules suivantes. Chaque terme d'entrée est `[F]` ou
   `[H]` ; chaque ligne de résultat est `[E]`.

   ```text
   gain brut mensuel      = ( occurrences/mois × minutes gagnées ÷ 60 × part réemployée × coût horaire chargé
                              + erreurs évitées/mois × coût d'une erreur
                              + autres gains mensuels, chacun justifié ) × taux d'adoption
   coût de construction   = jours × taux journalier (ou devis) + coûts uniques annexes
   fonctionnement/mois    = abonnements + exécutions (selon l'unité de facturation) + modèles d'IA
   maintenance/mois       = heures de maintenance × coût horaire chargé
   gain net mensuel       = gain brut − fonctionnement − maintenance
   délai de retour (mois) = coût de construction ÷ gain net mensuel (+ manque à gagner de la montée en charge)
   ```

   Les « minutes gagnées » comptent la relecture humaine. Un autre gain (délai, chiffre d'affaires)
   se justifie par un mécanisme et se compte en marge. Ouvrir `references/formules.md` pour les
   unités de facturation, la montée en charge, le point mort et un exemple de calcul.
5. **Séparer trois lectures du coût** : payé (devis, abonnements) ; mobilisé (heures des équipes pour
   le pilote, la recette, la formation : sans facture, mais réelles) ; optimisé (remise ou volume
   non signés : scénario haut seulement). Un outil déjà en place coûte peu à la marge, pas rien :
   décider sur le coût marginal, afficher le coût complet. Tout tarif relevé porte sa date.
6. **Faire varier.** Ordre de grandeur : une fourchette bas–haut par cas. Business case : bouger
   chaque hypothèse seule pour repérer les deux ou trois qui déplacent le résultat, construire bas,
   central et haut avec elles, puis calculer le point mort (méthode en référence).
7. **Classer ou recommander.** Deux repères d'alerte (Eric Risco, voir « Preuves restantes » ; non
   mesurés ici) : un délai de retour au-delà d'environ douze mois rend le cas douteux ; une
   maintenance au-delà de 30 à 50 % du gain brut signale une charge, pas un outil. *Solide* : même le
   scénario bas passe les deux repères → recommander d'y aller. *À mesurer d'abord* : le central
   passe, le bas non, et une mesure courte peut lever l'hypothèse fragile. *Douteux* : le central ne
   passe pas. Si l'entreprise a ses propres critères d'investissement, on applique les siens.
8. **Définir la mesure** : avant le déploiement, les valeurs `[H]` à relever (comment, par qui) ;
   après, les valeurs à relire pour remplacer l'estimation par le réel. Indicateurs et seuils :
   `rediger-cahier-des-charges` (spécification) ; rythme des revues et action à chaque seuil :
   `planifier-deploiement`.
9. **Nommer la valeur non financière**, rédiger avec le modèle ci-dessous, finir par la décision
   attendue. Suite : `planifier-deploiement` (feuille de route) après un ordre de grandeur ;
   `rediger-cahier-des-charges` (mode spécification) après un business case « on y va ». Quand le
   décideur tranche, ajouter une ligne à `mission/journal.md`.

## Le livrable

Modèle de `mission/03-chiffrage.md` (ordre de grandeur, porte « aucun besoin ») :

```markdown
# Chiffrage — ordre de grandeur du portefeuille

Date · Décideur (rôle) · Rédigé par · Sources lues

## 1. Paramètres communs
| Paramètre | Valeur | Statut | Source, ou qui peut confirmer |
Coût horaire chargé par rôle · base HT ou TTC · taux d'adoption · montée en charge · horizon.

## 2. Un cas par ligne, en fourchettes bas–haut
| Cas | Gain brut/mois | Construction | Fonctionnement + maintenance/mois | Gain net/mois | Délai de retour | Hypothèse la plus fragile |
Tous les montants sont `[E]` ; la dernière colonne nomme le `[H]` dont dépend le cas.

## 3. Classement
Solides · À mesurer d'abord · Douteux — une ligne de raison par cas ; dans chaque groupe, par gain
net central décroissant.

## 4. Hypothèses à confirmer
| Hypothèse | Cas concernés | Qui peut la confirmer | Mesure courte proposée |

## 5. Hors chiffrage
Valeur non financière, non convertie (qualité, risque, satisfaction des équipes, délai client) et ce
qui n'est pas chiffré, avec la raison.

## Décision attendue
Pour chaque cas : y aller (il entre dans la feuille de route), mesurer d'abord, ou ne pas y aller.
```

Modèle de `mission/cas-<slug>/50-rentabilite.md` (business case, porte « besoin connu ») :

```markdown
# Rentabilité — <titre court du cas>

Date · Décideur (rôle) · Rédigé par · Options chiffrées (de `40-solutions.md`) : <retenue> / <repli>

## 1. Situation de référence
Ce que le processus coûte aujourd'hui : volumes, temps, erreurs repris de `20-diagnostic.md`.

## 2. Hypothèses et mesure
| Terme | Valeur centrale | Basse–haute plausible | Statut | Source, ou qui peut confirmer |
Puis : valeurs à relever avant le déploiement (qui, comment) et valeurs à relire après.

## 3. Calcul par option
| Ligne | Option retenue | Option de repli |
Gain brut/mois · construction · fonctionnement/mois · maintenance/mois · gain net/mois · délai de
retour. Puis les trois lectures du coût : payé · mobilisé · optimisé.

## 4. Trois scénarios et point mort
| | Bas | Central | Haut |
Hypothèses qui varient, avec leurs valeurs. Point mort : « reste rentable tant que … ».

## 5. Temps libéré et adoption
Ce que devient le temps libéré (usage nommé, part réemployée) · taux d'adoption · montée en charge.

## 6. Valeur non financière
Nommée, non convertie.

## 7. Recommandation
Y aller · ne pas y aller · mesurer d'abord : trois raisons au plus, et ce qui la renverserait.

## Décision attendue
Valider la recommandation — ou la corriger.
```

Lignes de journal, au moment où le décideur tranche :

```markdown
- 2026-10-21 · portefeuille · 03-chiffrage validé par la direction des opérations · « les cas solides sont retenus, celui qui dépend d'une hypothèse attend une mesure »
- 2026-10-28 · cas-saisie-commandes · 50-rentabilite : « mesurer d'abord » décidé par la direction commerciale · « relever le temps réel et nommer l'usage du temps libéré »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Fourchettes pour trier, trois scénarios pour décider | un portefeuille ne se chiffre pas au détail, une décision d'investissement ne se prend pas sur un ordre de grandeur | un seul niveau de détail pour tous les cas | le portefeuille ne compte qu'un ou deux cas : on passe directement au business case |
| La maintenance est une ligne obligatoire, même pour un outil du marché | c'est la ligne qu'on oublie, et l'omettre fausse le calcul dans le sens qui rassure | la fondre dans le fonctionnement sans la montrer | un engagement écrit d'un fournisseur couvre corrections et évolutions `[F]` : la ligne reste, réduite à la supervision interne |
| Le temps libéré sans usage nommé ne compte pas en euros | du temps qui se dilue dans l'agenda ne réduit aucune dépense et n'augmente aucune recette | compter toutes les heures au coût horaire chargé | le responsable de l'équipe nomme l'usage (volume absorbé sans embauche, heures supplémentaires évitées…) |
| La valeur non financière se nomme, sans équivalent en euros | un chiffre inventé a l'air d'un fait et fausse la comparaison | chiffrer la satisfaction ou le risque | l'entreprise dispose d'une valeur interne établie, par exemple le coût d'un incident passé `[F]` |
| Douze mois et 30 à 50 % sont des repères d'alerte, pas des seuils | ils viennent de la pratique d'un auteur, pas d'une mesure ; un cas un peu au-delà de douze mois peut être juste s'il est stratégique | un rejet automatique au-delà | l'entreprise a ses critères d'investissement : on applique les siens |
| Décider sur des estimations, puis corriger avec le réel | attendre des mesures complètes retarde une décision souvent réversible | exiger des mesures avant tout chiffrage | la décision est coûteuse ou difficile à défaire : « mesurer d'abord » devient la recommandation |

## Frontières

- Les temps, volumes et erreurs actuels, et leurs causes → `auditer-processus`.
- Le tri des cas et leur portefeuille → `decouvrir-cas-usage` ; les options à comparer et la
  recommandation de solution → `concevoir-solution`.
- Les exigences, la spécification, les indicateurs et leurs seuils → `rediger-cahier-des-charges`.
- L'ordre de mise en œuvre, les jalons, le rythme des revues et l'action à chaque seuil →
  `planifier-deploiement`.
- L'état de la mission et le journal des décisions → `router-mission-ia`.
- Facultatif : `router-consulting-strategy` (lentille « business case ») et `automation-strategy`
  (décision d'automatiser, choix de plateforme selon l'unité de facturation) s'ils sont installés
  dans la session. Ne dire qu'on les a utilisés que s'ils ont réellement été appelés.

## Preuves restantes

- Éprouvée sur la mission fictive de `examples/` (ordre de grandeur et business case).
- NON MESURÉ sur une mission réelle : le premier cas réel dira si les fourchettes tiennent, si
  l'entreprise fournit un coût horaire chargé, si les repères de douze mois et de 30 à 50 % aident le
  décideur, et quel écart sépare le gain estimé du gain relevé (le pack n'a pas de boucle de mesure
  après déploiement : c'est l'entreprise qui mesure).
- Sources et crédits : adapté d'Eric Risco, « automation-strategy » (licence MIT,
  https://github.com/ericrisco/rsc-harness) : formule de retour avec ligne de maintenance, repères de
  douze mois et de 30 à 50 % ; et de gcamilo, « management-consulting » (licence MIT,
  https://github.com/gcamilo/management-consulting) : fourchettes bas–central–haut, sensibilité,
  normes de preuve. Les exemples chiffrés de ces sources ne sont pas repris.
