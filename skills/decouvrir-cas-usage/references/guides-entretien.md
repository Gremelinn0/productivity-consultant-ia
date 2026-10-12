# Guides d'entretien et séance d'enregistrement

À ouvrir aux étapes 2, 3 et 4 de `decouvrir-cas-usage`. Trois outils : un guide pour la direction, un guide
pour les équipes, un protocole pour la séance où l'on enregistre le travail réel. Puis un modèle de note à
déposer dans `mission/sources/`.

## Règles communes

- **Dire l'objet en ouverture.** Par exemple : « Je cherche à comprendre comment le travail se passe
  aujourd'hui pour voir ce qui pourrait être simplifié. Je ne juge personne, et mes notes ne mentionnent
  que des rôles. » Sans cette phrase, on obtient la procédure officielle et non les contournements. La note
  l'enregistre en une ligne.
- **Une question à la fois**, puis un silence : les meilleures réponses viennent après la première. Une ligne
  des tableaux ci-dessous est un thème, dont les sous-questions se posent l'une après l'autre.
- **Demander l'occurrence réelle.** « La dernière fois, que s'est-il passé ? » vaut mieux que « en
  général, comment faites-vous ? ». Demander à voir l'objet : le rapport, le tableur, le courriel type.
- **Chiffrer avec un exemple, et noter le statut.** Les trois statuts `[F]`, `[H]` et `[E]` sont ceux de
  `ARCHITECTURE.md`, aucun autre : un temps ou un volume dit de mémoire se note `[H]`, avec la personne qui
  peut le confirmer ; la pièce montrée ou l'observation le rend `[F]`. Une règle ou une contrainte que son
  détenteur énonce (budget, interdit, critère d'investissement) est `[F]`, sa source est l'entretien.
- **Garder les contradictions.** Si la direction et l'équipe ne décrivent pas le même processus, écrire
  les deux versions avec leur source : l'écart est souvent le vrai sujet.
- **Ne rien promettre.** Ne pas annoncer qu'une tâche sera automatisée ni qu'un poste évoluera :
  l'entretien recueille, il ne décide pas, et une promesse fausserait les réponses suivantes.
- **Citer mot pour mot ce qui sert de demande.** Une phrase que la direction ou une équipe prononce et qui
  résume ce qu'elle attend est notée telle quelle : `cadrer-besoin` la reprendra entre guillemets, et une
  citation doit figurer dans une note de `mission/sources/`.
- **Version courte (20 minutes)** quand le temps manque : la semaine type, la tâche qu'on voudrait ne plus
  faire, les informations recopiées d'un outil à l'autre. Ces trois questions suffisent à repérer des
  candidats ; elles ne suffisent pas à les mesurer.

## Guide direction (environ 45 minutes)

À mener en premier, avant de rédiger `00-contexte.md` : ses réponses (objectifs, contraintes, budget, essais
passés) remplissent la fiche entreprise.

| # | Thème | Question | Alimente |
|---|---|---|---|
| 1 | Objectifs | Quels sont les deux ou trois résultats que l'entreprise doit atteindre cette année ? | la valeur des cas, le choix des équipes |
| 2 | Temps | Où le temps de l'entreprise part-il le plus, sans rapporter autant qu'il le devrait ? | les signaux, les équipes à écouter |
| 3 | Disparition | Quelle tâche pourrait disparaître demain sans que personne ne la regrette ? | l'issue « Éliminer » |
| 4 | Priorités | Si un seul sujet devait s'améliorer d'ici six mois, lequel ? Qu'est-ce qui ne doit surtout pas changer ? | le classement, le périmètre |
| 5 | Contraintes | Quelles données ne doivent jamais quitter l'entreprise ? Quelles règles (contrats, conformité, clients) encadrent le travail ? Quels outils sont imposés ? | `00` (contraintes), « Limites » des fiches |
| 6 | Budget | Quel ordre de grandeur de budget envisagez-vous, et pour quoi : un essai, une première phase, un déploiement ? Qui décide à partir de quel montant ? | la classe « Projets », le décideur des livrables |
| 7 | Déjà essayé | Qu'avez-vous déjà essayé (outils, essais d'IA, automatisations) ? Qu'en reste-t-il, qu'est-ce qui a été abandonné, et pourquoi ? | « Déjà disponible », les freins d'adoption |
| 8 | Équipes et accès | Quelles équipes écouter en premier ? Peut-on observer et enregistrer leur travail, et quels documents ou outils peut-on consulter ? | `00` (autorisations), le plan des entretiens |
| 9 | Décision | Qui décide des cas à lancer, et sur quels critères ? | la décision attendue, les parties prenantes |
| 10 | Clôture | Qu'est-ce que je n'ai pas demandé et qu'il faudrait savoir ? | les questions ouvertes |

## Guide équipes (45 à 60 minutes)

À mener avec une équipe à la fois, de préférence avec deux personnes qui font la même tâche : leurs écarts
alimentent le test de stabilité d'`auditer-processus`. Quand une seule personne fait la tâche, ou que sa
suppléante n'est pas disponible, le dire dans la note : la question 9 repose alors sur un récit croisé, les deux
versions sont gardées, la suppléante est notée « non observée » et une séance avec elle est proposée.

| # | Thème | Question | Colonne de `01` alimentée |
|---|---|---|---|
| 1 | Semaine type | Racontez-moi votre dernière semaine, jour par jour : qu'avez-vous fait ? | Tâche, Déclencheur |
| 2 | Répétitif | Qu'avez-vous fait plusieurs fois cette semaine à peu près de la même façon ? | Fréquence ; les candidats à l'automatisation |
| 3 | Temps et volume | La dernière fois, combien de temps cela a-t-il pris pour une unité (une relance, un ticket) ? Combien d'unités par mois ? À quelle fréquence ? Pouvez-vous me montrer un exemple récent ? | Durée par occurrence (par unité), Volume (par mois), Fréquence, avec leur statut |
| 4 | Outils et données | Quels outils ouvrez-vous pour cette tâche, dans quel ordre, et que cherchez-vous dans chacun ? | Outils, Données |
| 5 | Copier-coller | Y a-t-il des informations que vous recopiez d'un outil à l'autre, ou que vous saisissez deux fois ? | Passages, Erreurs / reprises |
| 6 | Validations | Qui doit donner son accord avant que ce soit terminé, et combien de temps attendez-vous ? | Passages entre équipes |
| 7 | Erreurs et reprises | Que se passe-t-il quand cela se passe mal ? Qu'est-ce qu'il faut refaire, et à quelle fréquence ? | Erreurs / reprises |
| 8 | Exceptions | Dans quels cas la tâche ne se passe-t-elle pas comme d'habitude ? Qui décide alors, et comment ? | Stabilité des règles ; l'issue « Garder » |
| 9 | Règles | Les règles sont-elles écrites quelque part ? Un collègue qui fait la même tâche la fait-il de la même façon ? | Stabilité des règles ; l'issue « Simplifier d'abord » |
| 10 | Ne plus faire | Si vous pouviez ne plus jamais faire une seule chose, laquelle ? Que feriez-vous avec du temps en plus ? | l'issue « Éliminer », la valeur, l'adoption |
| 11 | Clôture | Qui d'autre pourrait m'en parler ? Qu'est-ce que je n'ai pas demandé ? | d'autres sources, les questions ouvertes |

## Séance d'enregistrement du travail réel

C'est la source la plus riche : on voit ce que les gens font, pas ce qu'ils disent faire. Le pack n'enregistre
rien lui-même ; le consultant et l'entreprise organisent la séance, la session lit la transcription.

**Préparer**
1. Choisir trois à cinq tâches parmi celles repérées en entretien : les plus fréquentes, les plus longues,
   ou celles dont les récits divergent.
2. Obtenir l'accord de la direction et de chaque personne enregistrée, selon les règles internes de
   l'entreprise (protection des données, représentants du personnel si elle en a). Dire où l'enregistrement
   est conservé et qui peut le voir.
3. Écarter ou masquer les données sensibles : préférer un cas de test, ou masquer les informations sur des
   personnes avant d'enregistrer.
4. Prévoir 30 à 60 minutes, avec une occurrence réelle de chaque tâche et non une démonstration idéale. Une
   tâche plus longue que la séance (une séance hebdomadaire de plusieurs heures) s'enregistre entière, seule
   dans la séance : on ne l'échantillonne pas, on garde de la transcription un extrait et un relevé
   d'horodatages par phase.

**Pendant**
- La personne fait la tâche comme d'habitude et commente à voix haute ce qu'elle regarde, ce qu'elle
  cherche, pourquoi elle choisit ceci plutôt que cela. L'observateur ne corrige pas et ne conseille pas.
- Les questions viennent à la fin de chaque tâche : « Qu'est-ce qui vous a fait choisir ceci ? »,
  « Qu'auriez-vous fait si… ? ».
- Noter le temps par étape, les attentes, les retours en arrière, les outils ouverts.

**Après**
1. Transcrire, retirer noms et données personnelles, puis déposer le texte dans
   `mission/sources/seance-<équipe>-<date>.md`. L'enregistrement brut reste chez l'entreprise.
2. Reporter les tâches observées dans `01-cartographie-taches.md`, source « observation, <équipe>,
   <date> ». Une durée chronométrée sur une occurrence est `[F]` pour cette occurrence et `[H]` comme durée
   typique tant qu'on n'a pas plusieurs occurrences (`ARCHITECTURE.md`).
3. Noter ce qu'on n'a pas vu (fin de mois, cas rares, exceptions, suppléante) et le demander en entretien.

## Modèle de note d'entretien

Fichier `mission/sources/entretien-<rôle>-<date>.md` :

```markdown
# Entretien — <rôle>, <équipe> · <date> · <durée>

Mené par · Guide utilisé : direction, équipes ou version courte · Personnes présentes (rôles)

## Ce qui a été dit
Ouverture : l'objet de l'entretien est dit (une ligne). Puis, par thème du guide, ce qui a été répondu, avec les
citations utiles mot pour mot. Statuts de `ARCHITECTURE.md` : `[F]` ce qu'une pièce ou une observation appuie,
ou une règle énoncée par son détenteur · `[H]` ce qui est dit de mémoire, avec qui peut le confirmer.

## Tâches citées (à reporter dans 01)
| Tâche | Fréquence | Durée | Volume | Outils | Statut, et qui confirme |
|---|---|---|---|---|---|
| | | | | | |

## Pièces remises
Document, export, organigramme : ce qui a été remis, et le nombre qu'il rend `[F]`.

## Écarts avec d'autres sources
Ce qui contredit un document, un autre entretien ou une observation.

## Documents ou accès promis

## Questions restées ouvertes
```
