# L'arbre de problèmes

Méthode inspirée de `mckinsey-issue-tree-structuring` (MichaelRochonnn, dépôt sans licence) ; idée publique reprise, texte réécrit ici.

## Quand la prendre

Quand la demande est large ou floue (« on perd du temps », « on veut plus de clients », « les devis sont trop lents ») ou que plusieurs causes sont possibles. Avant de choisir un cas, pour savoir où chercher d'abord. Pas besoin pour une demande déjà précise (« relancer les factures échues ») : la fiche besoin suffit.

## Les étapes

1. **Une question racine, en une phrase mesurable.** « Pourquoi un devis part-il en 6 jours au lieu de 2 ? » et non « les devis, c'est le bazar ». Si la personne ne peut pas la signer, on la reformule avec elle.
2. **Découper en 2 à 5 branches.** Deux tests, à faire à voix haute :
   - elles ne se recoupent pas : une même chose ne peut se ranger que dans une branche ;
   - elles couvrent tout : si chaque branche était réglée, la question serait réglée.

   Le plus sûr est de découper selon le déroulé réel du travail (de la demande au résultat) ou selon un total qu'on additionne (temps, euros, volume).
3. **Descendre d'un niveau seulement là où ça pèse.** Une branche sans poids ne se découpe pas.
4. **Peser chaque branche dans la même unité que la question** : heures par mois, jours de délai, euros. Chaque nombre porte son statut `[F]`, `[H]` ou `[E]` (`ARCHITECTURE.md`). Un poids inconnu s'écrit `?` avec qui le fournit ; on ne le devine pas.
5. **Retenir la branche qui pèse le plus**, la nommer, et écrire les autres « pas creusées » avec leur poids. Vérifier que la branche retenue est une cause et non un symptôme (on peut encore demander « pourquoi ? »).
6. **Écrire, pour chaque branche, ce qui la ferait tomber.** Une branche est une hypothèse `[H]` tant qu'elle n'a pas passé son test : le chiffre ou le fait qui la réfuterait, et qui peut le relever. « La collecte pèse 80 h par mois » tombe si un relevé de trois semaines montre moins de 60 h par mois, le poids de la branche suivante ; « la validation fait attendre » tombe si les devis validés le jour même sont aussi lents. Une branche dont on ne sait pas dire ce qui la réfuterait n'est pas encore une hypothèse, c'est une impression.

## Exemple (fictif)

Un bureau d'études de douze personnes : « nos devis sont trop lents ». Quarante devis par mois.

```text
Pourquoi un devis part-il en 6 jours au lieu de 2 ?
├─ Recueillir les infos du client : 2 h par devis, soit 80 h par mois [H]  ← retenue (tombe sous 60 h)
├─ Chiffrer : 1 h 30 par devis, soit 60 h par mois [H]
├─ Rédiger et mettre en forme : 1 h par devis, soit 40 h par mois [H]
└─ Valider et envoyer : 0 h de travail, mais 2 jours d'attente en moyenne [H]
```

Le poids du travail est dans la collecte (80 h). Le délai, lui, est dans la validation (2 jours d'attente) : deux questions racines, deux arbres. La personne choisit celle qu'elle veut régler ; ici « le temps de travail », donc la collecte.

## Ce qu'elle rend

Un petit arbre (liste indentée, trois niveaux au plus) et la branche retenue, dans la rubrique 10 de `10-besoin.md` (« Est-ce le bon problème ? ») ; la branche retenue nourrit le « Problème supposé » de la rubrique 3. Les branches non creusées restent écrites : elles disent ce qu'on a laissé de côté. Aucune rubrique n'est ajoutée à la fiche.
