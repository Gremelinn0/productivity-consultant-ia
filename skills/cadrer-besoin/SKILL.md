---
name: cadrer-besoin
description: >-
  Quand une demande d'automatisation ou d'IA arrive formulée comme une solution ou une envie
  (« on veut un chatbot », « automatiser les relances », « un agent pour le support ») → la
  reformuler, vérifier que c'est le bon problème, puis fixer décision, périmètre, contraintes et
  critères de succès dans une fiche besoin courte que le demandeur valide, et donner son nom au
  dossier du cas. Première étape de la porte « besoin connu » du pack consultant-ia. Triggers :
  « cadrer le besoin », « audit du besoin », « expression du besoin », « recueil du besoin », « on
  veut automatiser », « on veut un agent IA », « needs assessment », « problem framing ».
metadata:
  scope: "un besoin nommé par un client ou une équipe, avant tout diagnostic, chiffrage ou choix de solution"
  owns: "la fiche besoin : demande citée, reformulation, vrai problème, décision à prendre, parties prenantes, périmètre, contraintes, critères de succès, inconnues ; le nom du dossier du cas"
  consumes: "la demande telle qu'exprimée ; mission/sources/ ; la ligne du cas dans mission/02-portefeuille.md quand il vient de la porte découverte"
---

# Cadrer le besoin

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/10-besoin.md`. Preuve : le demandeur
> valide la reformulation, et la décision s'inscrit dans `mission/journal.md`. Contrôle de forme :
> la fiche porte les dix rubriques du modèle, le dossier un nom de deux à quatre mots, et chaque
> nombre son statut `[F]`, `[H]` ou `[E]` (définis dans `ARCHITECTURE.md`). Exemple de référence :
> `examples/` du pack. **Boucle** : aucune.

> ❓ **Une question pour l'entreprise sort de la base de questions** (`mener-entretien-ia/references/base-questions/`, un fichier par sujet) :
> lire d'abord le bloc du sujet, ne poser que ce qui manque, puis y ranger ce qui manquait (`entretien.py ajouter`).

## Ce que cette compétence résout

Une demande arrive presque toujours sous la forme d'une solution : « il nous faut un chatbot ».
La construire telle quelle, c'est parier que le demandeur a déjà fait le diagnostic. Ce cadrage
remonte de la solution demandée au problème qu'elle doit régler, et pose ce qu'il faut savoir avant
d'auditer ou de chiffrer quoi que ce soit.

Résultat attendu : une fiche courte dans laquelle le demandeur reconnaît son besoin, et qui dit
quelle décision la suite de la mission doit permettre.

## Stratégie

1. **Partir des mots du demandeur.** On cite la demande telle quelle, puis on la reformule. Si la
   reformulation le surprend, c'est elle qui est fausse, pas lui.
2. **Séparer le symptôme, le problème et la solution demandée.** « Les relances partent en retard »
   est un symptôme ; « personne n'a la liste à jour des factures échues » est le problème ; « un
   agent qui relance » est la solution demandée. La suite du pack travaille sur le problème.
3. **Nommer la décision.** Un cadrage sert à décider : lancer un projet, choisir entre deux pistes,
   renoncer. Si aucune décision n'est attendue, l'écrire : la mission est alors exploratoire.
4. **Rendre visible ce qu'on ignore.** Une inconnue écrite coûte une question ; une inconnue comblée
   par une supposition coûte un projet. On marque `[H]` ce qui est supposé et on continue. Chaque nombre
   porte son statut : `[F]` fait (pièce, entretien, ou accord inscrit au journal), `[H]` hypothèse (avec le
   rôle qui la confirme), `[E]` estimation (calcul montré) ; définitions dans `ARCHITECTURE.md`.
5. **Rester court.** Dix rubriques, quelques lignes chacune. Le détail du processus appartient à
   l'audit, les exigences au cahier des charges.
6. **Donner un seul nom au cas.** Le slug fixé ici sert de nom de dossier à toute la suite : le routeur, le
   journal et les renvois le reprennent tel quel.

## Étapes

1. **Lire ce qui existe** : la demande, `mission/sources/`, et, si le cas vient de la porte
   découverte, sa fiche dans `mission/02-portefeuille.md`. Ne pas reposer une question dont la
   réponse est déjà là.
2. **Fixer le nom, puis ouvrir le dossier du cas.** Le slug tient en deux à quatre mots tirés du besoin,
   sans accent (`relances-factures`, `support-niveau-1`) ; pour un cas venu de la découverte, on part du
   nom de sa fiche. Créer `mission/cas-<slug>/` ; le slug ne change plus. Créer `mission/journal.md`
   s'il n'existe pas.
3. **Poser en un seul message les questions qui manquent**, les plus décisives d'abord. Le socle tient en
   huit questions, dans la base de questions (`mener-entretien-ia/references/base-questions/cadrage.md`, CA01 à
   CA08) : le résultat attendu, la situation actuelle, le périmètre, qui décide et qui utilisera, ce qui peut
   être fourni, le budget, le calendrier, les contraintes. La base dit quelle rubrique du modèle chacune nourrit.

   Au premier contact, le message ne contient que deux questions : celles qui changent le périmètre, le
   coût ou les conditions de réussite. Les questions de diagnostic détaillé attendent l'audit. **Un cas
   venu de la porte découverte ne reçoit aucune question reposée** : les réponses sont dans
   `02-portefeuille.md` et `mission/sources/`, et une rubrique sans réponse prend un `?`. Les questions
   posées et les réponses reçues se déposent dans `mission/sources/` (note d'échange datée) ; la fiche les cite.

   **L'entretien de l'objectif.** Quand l'objectif relève d'un sujet de la base (service client, prospection,
   CRM, données, reporting, contenu, transmission ; l'index : `base-questions/README.md`), on prépare l'entretien
   avec les questions qui manquent de ce seul sujet, réécrites dans les mots de la personne, après avoir lu
   soi-même les traces de l'outil quand il est lisible (`auditer-processus`, étape 2). Un sujet absent s'ouvre
   dans la base avec la première question qui a servi (`entretien.py creer-sujet`). Mené par
   écrit par une IA, en ligne ou dans la session de l'entreprise, c'est `mener-entretien-ia` (questionnaire
   préparé) ; sa note entre dans `mission/sources/` comme celle d'un entretien en direct.
4. **Si une réponse manque**, écrire l'hypothèse provisoire, la marquer `[H]` avec la personne qui
   peut la confirmer, et continuer. On ne bloque que si la décision dépend entièrement de cette
   inconnue. Une valeur que le rédacteur propose (une cible, un seuil) reste `[H]` jusqu'à la validation ;
   acceptée, elle devient `[F]` et sa source est la ligne du journal.
5. **Rédiger la fiche** avec le modèle ci-dessous. La citation de la rubrique 1 figure mot pour mot dans une
   note de `mission/sources/` ; sinon la demande est reformulée, sans guillemets, et la fiche le dit.
6. **Vérifier que c'est le bon problème** : la solution demandée règle-t-elle le problème posé ?
   une solution plus simple le réglerait-elle (supprimer une étape, configurer un outil déjà en
   place) ? le problème vient-il d'ailleurs (processus, organisation, donnée) ? Écrire la réponse,
   même quand elle conforte la demande.
7. **Finir par la décision attendue**, puis proposer l'étape suivante : `auditer-processus`. Quand
   le demandeur valide, ajouter une ligne à `mission/journal.md`, avec les valeurs qu'il accepte.

## Le livrable

Modèle de `mission/cas-<slug>/10-besoin.md` :

```markdown
# Besoin — <titre court>

Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle) · Rédigé par
Un seul rôle quand c'est le même (« Demandeur, valideur et décideur : … »).

## 1. La demande, telle qu'exprimée
> « … » (citation exacte, présente telle quelle dans une note de `mission/sources/` : entretien, courriel, ticket)

## 2. Reformulation
Une ou deux phrases que le demandeur doit pouvoir signer.

## 3. Symptôme, problème, solution demandée
| Symptôme observé | Problème supposé | Solution demandée |
|---|---|---|
| | | |

## 4. Décision à prendre
Ce que la mission doit permettre de décider, et par qui.

## 5. Parties prenantes
Rôles : qui décide, qui valide, qui utilise, qui est touché. Aucun jugement sur les personnes.

## 6. Périmètre
Dedans · Dehors (explicitement).

## 7. Contraintes
Budget, calendrier, outils imposés, données, sécurité, conformité.

## 8. Critères de succès
Chaque critère est mesurable et porte sa mesure de départ avec son statut si elle est connue ; sinon « à
mesurer avant tout lancement ». Une cible proposée par le rédacteur est `[H]` ; acceptée à la validation,
elle devient `[F]`, source : la ligne du journal.

## 9. Ce qu'on sait, ce qu'on suppose, ce qu'on ignore
`[F]` faits avec leur source · `[H]` hypothèses avec qui peut les confirmer · `?` questions ouvertes.

## 10. Est-ce le bon problème ?
Réponse argumentée, y compris l'alternative la plus simple envisagée.

## Décision attendue
Valider la reformulation, le périmètre et les critères de succès — ou les corriger.
```

Ligne de journal, au moment où le demandeur tranche :

```markdown
- 2026-10-14 · cas-relances-factures · 10-besoin validé par la direction financière · « on garde le périmètre France ; cibles de la rubrique 8 acceptées »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Une fiche courte, pas un dossier | le détail du processus appartient à l'audit ; un cadrage long retarde la décision | un questionnaire exhaustif dès le départ | le besoin couvre plusieurs processus distincts : on ouvre alors un cas par processus, chacun avec son nom |
| Questions groupées, envoyées en une fois | un aller-retour par question épuise le demandeur | l'entretien question par question | l'échange a lieu en direct : on peut alors suivre le fil de la conversation |
| Hypothèse marquée plutôt qu'attente | une mission ne s'arrête pas faute d'une réponse secondaire | bloquer jusqu'à la réponse | la décision dépend entièrement de l'inconnue |
| La solution demandée reste écrite | elle dit ce que le demandeur imagine, et c'est une information | la remplacer par « le vrai besoin » | jamais : on la garde, même écartée |
| Le nom du dossier se fixe ici, une fois | deux noms pour un cas font deux dossiers et un état faux | laisser chaque étape nommer le cas | jamais |
| Une valeur proposée puis acceptée devient `[F]` | la validation est une décision de son détenteur ; la source est la ligne du journal | la garder `[H]` à vie | la valeur dépend d'une mesure à venir : elle reste `[H]` jusqu'à la mesure |

## Frontières

- Le processus actuel, ses mesures et ses causes → `auditer-processus`.
- Les exigences détaillées → `rediger-cahier-des-charges`.
- Aucun besoin nommé (« où l'IA peut-elle nous aider ? ») → `decouvrir-cas-usage`.
- L'état de la mission et le journal des décisions → `router-mission-ia`.
- Seulement quand la demande est elle-même une décision d'affaires ambiguë (marché, offre,
  investissement) : appeler `router-consulting-strategy`, qui structure cette décision et ne possède
  aucun livrable. Pour un besoin ordinaire, cette étape ne l'appelle pas.

## Preuves restantes

- Éprouvée sur la mission fictive du 12/10/2026 (`examples/`), qui a relevé 94 frictions ; celles qui
  touchent la fiche besoin sont corrigées ici.
- NON MESURÉ sur une mission réelle : le premier cas réel dira si huit questions suffisent ou s'il
  manque une rubrique, et si dix rubriques restent lisibles quand le demandeur n'a presque rien écrit.
