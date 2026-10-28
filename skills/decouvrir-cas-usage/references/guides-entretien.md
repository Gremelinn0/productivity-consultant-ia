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
  faire, les informations recopiées d'un outil à l'autre (EQ01, EQ10, EQ05). Ces trois questions suffisent à repérer des
  candidats ; elles ne suffisent pas à les mesurer.

## Guide direction (environ 45 minutes)

À mener en premier, avant de rédiger `00-contexte.md` : ses réponses (objectifs, contraintes, budget, essais
passés) remplissent la fiche entreprise.

Les dix thèmes et leurs questions vivent dans la base de questions,
`mener-entretien-ia/references/base-questions/decouverte-direction.md` (DI01 à DI10), chacun avec ce
qu'il alimente : on les y corrige et on les y complète.

## Guide équipes (45 à 60 minutes)

À mener avec une équipe à la fois, de préférence avec deux personnes qui font la même tâche : leurs écarts
alimentent le test de stabilité d'`auditer-processus`. Quand une seule personne fait la tâche, ou que sa
suppléante n'est pas disponible, le dire dans la note : la question des règles (EQ09) repose alors sur un récit croisé, les deux
versions sont gardées, la suppléante est notée « non observée » et une séance avec elle est proposée.

Les onze thèmes et leurs questions vivent dans la base de questions,
`mener-entretien-ia/references/base-questions/decouverte-equipes.md` (EQ01 à EQ11), chacun avec la
colonne de `01` qu'il alimente : on les y corrige et on les y complète.

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

## Sans le consultant : l'entretien guidé par IA

Quand la personne ne peut pas donner le temps d'un entretien en direct, `mener-entretien-ia` fait poser ces mêmes
questions par écrit par une IA, avec les règles ci-dessus (une question à la fois, l'occurrence réelle, rien de
promis) ; sa note suit le modèle ci-dessous. Le script lit les questions dans la base : une question corrigée là
l'est partout. Quand l'objectif est déjà nommé, ce ne sont plus ces guides mais un questionnaire préparé pour
lui, tiré du sujet de l'objectif dans la même base.

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
