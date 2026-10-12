# Formules, unités et exemple de calcul

Ouvrir ce fichier pour : rendre un terme `[F]`, choisir l'unité de facturation d'un outil, intégrer la
montée en charge, construire les scénarios et le point mort, ou relire un calcul complet. La méthode
et les modèles de livrable sont dans `SKILL.md`.

## 1. Les termes, leur statut de départ, et comment les rendre `[F]`

| Terme | Statut de départ | Comment le rendre `[F]` |
|---|---|---|
| Occurrences par mois | `[F]` si comptées, sinon `[H]` | compter sur un cycle complet du processus (un mois au moins, davantage s'il est saisonnier) |
| Minutes gagnées par occurrence | `[H]` | chronométrer le temps actuel et le temps avec le dispositif sur des cas réels, difficiles compris, relecture et corrections humaines comprises |
| Part du temps libéré réemployée | `[H]` | faire nommer l'usage par le responsable de l'équipe, puis vérifier qu'il a lieu |
| Coût horaire chargé | `[F]` si fourni par l'entreprise (finance, ressources humaines), sinon `[H]` | demander le coût chargé par rôle (salaire, charges, frais généraux) ; jamais le salaire d'une personne |
| Erreurs évitées par mois, coût d'une erreur | `[H]` | compter erreurs et reprises sur une période ; chiffrer leur traitement (temps, remboursement, pénalité) |
| Autres gains (délai, chiffre d'affaires) | `[H]` | nommer le mécanisme et le taux ; compter la marge, pas le chiffre d'affaires |
| Taux d'adoption | `[H]` | relever l'usage réel pendant le pilote |
| Jours, taux journalier, devis | `[F]` si devis daté, `[H]` sinon | demander le devis ou le taux interne |
| Abonnements | `[F]` avec la date du tarif | relever la page de tarifs ou le contrat |
| Exécutions, modèles d'IA | `[E]` : volume × tarif unitaire | tester un échantillon représentatif pour mesurer ce que consomme une occurrence |
| Heures de maintenance | `[H]` | à défaut de mesure, une fourchette large, relevée ensuite |

Les lignes de résultat (gain brut, gain net, délai de retour) sont toujours `[E]`.

## 2. Le gain brut en détail

- **Heures libérées** = occurrences par mois × minutes gagnées ÷ 60. Une heure libérée ne devient une
  heure payée que si elle sert : c'est la part réemployée.
- **Usages crédibles du temps libéré** : absorber une hausse de volume sans embauche ; supprimer des
  heures supplémentaires ou un renfort temporaire ; consacrer le temps à une tâche de valeur nommée,
  dont l'effet est lui-même estimé. Du temps dilué dans l'agenda ne compte pas en euros : il reste
  une valeur de capacité, écrite à côté du calcul.
- **Erreurs évitées** : ce qu'elles coûtent à traiter (temps de reprise, geste commercial,
  remboursement, pénalité), pas leur gravité ressentie.
- **Autres gains** : un délai raccourci vaut quelque chose par un mécanisme précis (moins d'abandons,
  encaissement plus tôt) et un taux, tous deux `[H]`. Compter la marge, jamais le chiffre d'affaires.
- **Pas de double compte** : un même effet (par exemple le temps de traitement) ne se compte pas à la
  fois en heures libérées et en délai raccourci.
- **Adoption** : le taux s'applique à chaque ligne de gain qui dépend de l'usage.

## 3. Les coûts en détail

**Construction.** Jours × taux journalier (ou devis), plus les coûts uniques annexes : formation,
nettoyage ou migration de données, temps interne du pilote et de la recette. Le pilote est un coût,
pas un préalable gratuit.

**Fonctionnement.** Il dépend de l'unité de facturation de l'outil, à rapprocher de la forme du
traitement (beaucoup d'occurrences à peu d'étapes, ou peu d'occurrences à beaucoup d'étapes). Le
recalculer au volume du scénario haut : si le volume varie entre scénarios, il varie avec lui.

| Unité de facturation | Ce qui est compté | Piège |
|---|---|---|
| Par utilisateur ou par poste | les personnes ayant un accès | payé même si peu utilisé |
| Par exécution | un traitement complet, quel que soit son nombre d'étapes | les relances et boucles multiplient les exécutions |
| Par tâche ou par action | chaque étape | un traitement de dix étapes coûte dix unités |
| Par crédit | un nombre de crédits variable selon l'opération | lire la table de consommation, pas le prix du crédit |
| Par volume de texte traité (modèles d'IA) | la longueur des entrées et des sorties | la longueur réelle des documents change la facture : tester sur un échantillon |

**Maintenance.** Toujours présente, même quand l'outil est géré par un fournisseur. Elle couvre la
surveillance des échecs, les corrections quand un service tiers change, le renouvellement des accès,
l'adaptation quand le processus évolue, la formation des nouveaux arrivants et la revue périodique
de la qualité. Plus le processus est instable, plus elle monte.

**Trois lectures du coût, jamais mélangées.** *Payé* : devis, abonnements, usage facturé, aux
tarifs datés. *Mobilisé* : heures des équipes de l'entreprise (pilote, recette, formation,
maintenance interne), sans facture mais réelles. *Optimisé* : remise, volume ou mutualisation non
signés ; il ne figure que dans le scénario haut, jamais dans le central tant qu'il n'est pas obtenu.
Un outil déjà en place a un coût marginal faible, pas nul : la décision se prend sur le coût
marginal, et le coût complet reste affiché à côté. Un changement d'offre ou de licence imposé par le
projet est, lui, un coût du projet.

## 4. Montée en charge et délai de retour

Le gain n'atteint pas son régime établi dès le premier mois. Poser un coefficient par mois (la part
du régime établi atteinte, `[H]`, à caler sur le plan de déploiement) ; le manque à gagner, exprimé
en mois de gain brut, est `m = somme des (1 − coefficient)`. Fonctionnement et maintenance courent
dès le premier mois, sauf engagement contraire : le manque à gagner se mesure donc sur le gain brut.

```text
délai de retour (mois) = ( coût de construction + gain brut × m ) ÷ gain net mensuel
```

Cette forme est exacte quand le retour intervient après la montée en charge ; sinon, cumuler mois par
mois. Sans montée en charge (`m = 0`), on retrouve coût de construction ÷ gain net mensuel.

## 5. Scénarios, sensibilité et point mort

1. **Sensibilité.** Pour chaque hypothèse `[H]` porteuse, noter une valeur basse et une valeur haute
   plausibles (celles que juge possibles la personne qui connaît le terrain, pas le pire imaginable).
   Bouger chaque hypothèse seule, les autres restant au central, et relever l'écart de gain net.
   Retenir les deux ou trois qui écartent le plus.
2. **Scénarios.** Bas : ces hypothèses à leur valeur basse, ensemble. Haut : à leur valeur haute.
   Central : la meilleure estimation. Les autres termes restent au central.
3. **Point mort.** Gain brut minimal pour un retour en `H` mois (douze par défaut), avec `C` le coût
   de construction, `F` le fonctionnement plus la maintenance mensuels et `m` le manque à gagner de
   la montée en charge (section 4) :

   ```text
   gain brut minimal = ( C + H × F ) ÷ ( H − m )
   ```

   Résoudre ensuite pour l'hypothèse visée, les autres restant au central. Le seuil de rentabilité
   mensuelle est plus bas : gain brut = `F` ; en dessous, le dispositif coûte chaque mois plus qu'il
   ne rapporte et ne se rembourse jamais. Écrire le résultat en phrase : « reste rentable, retour en
   douze mois, tant que le temps gagné dépasse N minutes par occurrence ».

## 6. Mesurer : avant et après

- **Avant le déploiement** : relever les termes `[H]`, dans l'ordre de leur sensibilité, avec la
  méthode qui servira après (même comptage, même chronométrage), en nommant qui mesure, comment et à
  quelle date. Sans mesure de départ, aucun gain ne pourra être déclaré observé.
- **Après** : relire les mêmes termes de la même façon, plus l'usage réel (adoption), les coûts
  réels (factures), les heures de maintenance réelles et les incidents. Écrire l'écart avec
  l'estimation, remplacer `[E]` par `[F]` là où l'observation existe, dater la mise à jour.
- Les indicateurs et leurs seuils de correction, d'alerte et d'arrêt se définissent dans la
  spécification (`rediger-cahier-des-charges`) ; le rythme des revues et l'action à chaque seuil se
  fixent dans le plan de déploiement (`planifier-deploiement`).

## 7. Exemple de calcul — nombres fictifs, à ne reprendre dans aucune mission

Cas imaginaire : saisie des bons de commande reçus par courriel. Tous les montants sont inventés.

| Terme | Valeur centrale | Basse–haute | Statut |
|---|---|---|---|
| Occurrences par mois | 1 000 | — | `[H]` : à compter sur un mois |
| Minutes gagnées par occurrence | 6 | 3–8 | `[H]` : à chronométrer, relecture comprise |
| Part du temps libéré réemployée | 50 % | 25–80 % | `[H]` : à faire nommer par le responsable de l'équipe |
| Coût horaire chargé | 50 € | — | `[H]` : à confirmer par la direction financière |
| Erreurs évitées par mois · coût d'une erreur | 20 · 25 € | — | `[H]` |
| Taux d'adoption | 80 % | 60–90 % | `[H]` : à relever au pilote |
| Construction | 12 jours × 600 € + 10 h de formation × 50 € = 7 700 € | — | `[F]` devis daté pour 7 200 € ; `[H]` pour la formation |
| Fonctionnement par mois | 100 € d'abonnement + 20 € d'exécutions + 30 € de modèle d'IA = 150 € | — | `[F]` tarif daté pour 100 € ; `[E]` pour le reste |
| Maintenance par mois | 3 h × 50 € = 150 € | — | `[H]` |
| Montée en charge | 25 %, 50 %, 75 % puis 100 % | — | `[H]` : donc `m` = 1,5 mois |

Calcul central : 1 000 × 6 ÷ 60 = 100 heures libérées ; 50 % réemployées = 50 heures × 50 € = 2 500 € ;
plus 20 × 25 € = 500 € d'erreurs évitées ; × 80 % d'adoption = **gain brut 2 400 €** `[E]`. Gain net =
2 400 − 150 − 150 = **2 100 €** `[E]`. Retour en régime établi : 7 700 ÷ 2 100 = 3,7 mois. Avec la
montée en charge : (7 700 + 2 400 × 1,5) ÷ 2 100 = **5,4 mois** `[E]` (vérifié mois par mois : le cumul
devient positif au sixième mois).

| | Bas | Central | Haut |
|---|---|---|---|
| Minutes · réemploi · adoption | 3 · 25 % · 60 % | 6 · 50 % · 80 % | 8 · 80 % · 90 % |
| Gain brut par mois | 675 € | 2 400 € | 5 250 € |
| Gain net par mois | 375 € | 2 100 € | 4 950 € |
| Délai de retour, montée en charge comprise | 23,2 mois | 5,4 mois | 3,1 mois |
| Maintenance ÷ gain brut | 22 % | 6 % | 3 % |

Sensibilité du gain net (2 100 € au central), une hypothèse à la fois : part réemployée de 25 à 80 %
→ 1 100 à 3 300 € (écart 2 200 €) ; minutes gagnées de 3 à 8 → 1 100 à 2 767 € (écart 1 667 €) ;
adoption de 60 à 90 % → 1 500 à 2 400 € (écart 900 €). Les trois restent dans les scénarios.

Point mort, retour en douze mois, montée en charge comprise : gain brut minimal = (7 700 + 12 × 300)
÷ (12 − 1,5) ≈ 1 076 €. Les autres hypothèses au central, le cas reste rentable en douze mois tant que
le temps gagné dépasse environ **2 minutes** par occurrence, ou tant qu'au moins **17 %** du temps
libéré est réemployé.

Lecture : le central passe nettement, le bas non, et l'écart tient à des hypothèses `[H]` qu'une
mesure courte peut lever (chronométrer des cas réels, faire nommer l'usage du temps libéré).
Recommandation de départ : **mesurer d'abord**, puis revenir au calcul avec les valeurs relevées.
Valeur non financière, non convertie : moins de ressaisie fastidieuse, traitement plus rapide des
commandes.

## 8. Erreurs fréquentes

- Compter toutes les heures libérées comme de l'argent, sans usage nommé.
- Oublier la relecture humaine dans le temps « avec le dispositif ».
- Mettre la maintenance à zéro parce que l'outil est géré par un fournisseur.
- Mélanger coût marginal et coût complet, ou glisser une remise non signée dans le central.
- Compter le même effet deux fois (heures libérées et délai raccourci).
- Compter le chiffre d'affaires au lieu de la marge.
- Extrapoler un volume depuis une semaine atypique ; reprendre une moyenne de marché à la place du
  coût de l'entreprise ; laisser un tarif sans date.
- Lire le gain sur un horizon trop long : le processus et les outils auront changé avant.
