# La matrice impact et vitesse

Méthode inspirée de `impact-speed-prioritization-matrix` (MichaelRochonnn, dépôt sans licence) ; idée publique reprise, texte réécrit ici.

## Quand la prendre

Quand `02-portefeuille.md` compte plus de trois cas, ou que les moyens du client sont limités, ou qu'il veut un premier résultat vite. À l'étape « Classer » de `decouvrir-cas-usage`, avant de recommander les trois cas à creuser.

## Les étapes

1. **Noter l'impact** : le gain mensuel `[E]` de la colonne « Valeur » (durée × volume), en heures par mois. Il est « fort » s'il atteint au moins la médiane des gains du portefeuille, « faible » sinon.
2. **Noter la vitesse** : le temps pour livrer un premier résultat utilisable, pas tout le projet, en semaines. « Rapide » : quatre semaines au plus. « Lente » : plus. Le délai se lit sur la dépendance la plus lente (données à rassembler, accès à obtenir, règles à fixer, validation à attendre) et part de la colonne « Facilité ». Il porte le statut `[H]` ou `[E]` : un délai n'est jamais `[F]` avant la mise en service.
3. **Placer chaque cas** :

   | | Rapide | Lente |
   |---|---|---|
   | **Impact fort** | gagner d'abord | planifier |
   | **Impact faible** | petit gain facile | laisser |

4. **Ordonner : ce qui rapporte vite d'abord.** Gagner d'abord, puis le petit gain facile, puis planifier, puis laisser ; dans une même case, le plus gros gain en tête. Un cas dont une donnée manque est « à classer » : il n'entre pas dans les trois.
5. **Justifier en une ligne par cas**, dans l'ordre du classement :
   `<cas> : gain <heures> h par mois [E] (fort ou faible) · vitesse <semaines> semaines (rapide ou lente) · <case> · pourquoi : <la raison>`.
   Un écart à l'ordre par défaut s'écrit dans la ligne, avec sa raison.
6. **Les trois proposés** sont les trois premiers de cette liste. La matrice ne remplace pas les classes de `02` : « Gains rapides » correspond à « gagner d'abord » et au petit gain facile, « Projets » à « planifier ».

## Exemple (fictif)

Un cabinet comptable de dix personnes, quatre cas. Gains : 35, 28, 14 et 50 heures par mois ; médiane 31,5 heures.

```text
1. Tri des e-mails entrants : gain 35 h par mois [E] (fort) · vitesse 3 semaines [H] (rapide) · gagner d'abord · pourquoi : règles stables, boîte partagée déjà accessible.
2. Relances de factures : gain 28 h par mois [E] (faible) · vitesse 1 semaine [H] (rapide) · petit gain facile · pourquoi : la liste des impayés existe déjà dans l'outil de facturation.
3. Comptes rendus de rendez-vous : gain 14 h par mois [E] (faible) · vitesse 1 semaine [H] (rapide) · petit gain facile · pourquoi : aucun accès à obtenir.
4. Reporting mensuel clients : gain 50 h par mois [E] (fort) · vitesse 8 semaines [H] (lente) · planifier · pourquoi : données dans trois outils, à rassembler d'abord ; le plus gros gain, mais pas dans les trois.
```

## Ce qu'elle rend

La liste d'une ligne par cas, dans `02-portefeuille.md` sous le tableau de la vue d'ensemble, et les trois cas proposés qui en sortent. Le gain mensuel reste un plafond que `chiffrer-rentabilite` réduit.
