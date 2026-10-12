---
name: cadrer-besoin
description: >-
  Quand une demande d'automatisation ou d'IA arrive formulée comme une solution ou une envie
  (« on veut un chatbot », « automatiser les relances », « un agent pour le support ») → la
  reformuler, vérifier que c'est le bon problème, puis fixer décision, périmètre, contraintes et
  critères de succès dans une fiche besoin d'une page que le demandeur valide. Première étape de la
  porte « besoin connu » du pack consultant-ia. Triggers : « cadrer le besoin », « audit du
  besoin », « expression du besoin », « recueil du besoin », « on veut automatiser », « on veut un
  agent IA », « needs assessment », « problem framing ».
metadata:
  scope: "un besoin nommé par un client ou une équipe, avant tout diagnostic, chiffrage ou choix de solution"
  owns: "la fiche besoin : demande citée, reformulation, vrai problème, décision à prendre, parties prenantes, périmètre, contraintes, critères de succès, inconnues"
  consumes: "la demande telle qu'exprimée ; mission/sources/ ; la ligne du cas dans mission/02-portefeuille.md quand il vient de la porte découverte"
---

# Cadrer le besoin

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/10-besoin.md`. Preuve : le demandeur
> valide la reformulation, et la décision s'inscrit dans `mission/journal.md`. Contrôle de forme :
> la fiche porte les dix rubriques du modèle et chaque nombre a son statut `[F]`, `[H]` ou `[E]`.
> Exemple de référence : `examples/` du pack. **Boucle** : aucune.

## Ce que cette compétence résout

Une demande arrive presque toujours sous la forme d'une solution : « il nous faut un chatbot ».
La construire telle quelle, c'est parier que le demandeur a déjà fait le diagnostic. Ce cadrage
remonte de la solution demandée au problème qu'elle doit régler, et pose ce qu'il faut savoir avant
d'auditer ou de chiffrer quoi que ce soit.

Résultat attendu : une fiche d'une page dans laquelle le demandeur reconnaît son besoin, et qui dit
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
   par une supposition coûte un projet. On marque `[H]` ce qui est supposé et on continue.
5. **Rester court.** Une page. Le détail du processus appartient à l'audit, les exigences au cahier
   des charges.

## Étapes

1. **Lire ce qui existe** : la demande, `mission/sources/`, et, si le cas vient de la porte
   découverte, sa fiche dans `mission/02-portefeuille.md`. Ne pas reposer une question dont la
   réponse est déjà là.
2. **Ouvrir le dossier du cas** : `mission/cas-<slug>/`, avec un slug court tiré du besoin
   (`relances-factures`, `support-niveau-1`). Créer `mission/journal.md` s'il n'existe pas.
3. **Poser les questions qui manquent, en une seule fois**, les plus décisives d'abord. Le socle
   tient en huit questions :
   - Quel résultat concret doit être obtenu pour que la mission soit considérée comme réussie ?
   - Quelle est la situation actuelle, et qu'est-ce qui ne fonctionne pas assez bien aujourd'hui ?
   - Quel périmètre est prioritaire, et qu'est-ce qui doit rester explicitement hors périmètre ?
   - Qui décide, qui valide et qui utilisera réellement le dispositif ?
   - Quelles informations, données, accès ou disponibilités peuvent être fournis ?
   - Quel budget est prévu, et couvre-t-il un pilote, une première phase ou la production complète ?
   - Quel calendrier est souhaité : une charge de travail, une date butoir, des jours consécutifs ?
   - Quelles contraintes de sécurité, de conformité, de propriété des données ou d'outils s'imposent ?

   Au premier contact, deux questions au plus : seulement celles qui changent le périmètre, le coût
   ou les conditions de réussite. Les questions de diagnostic détaillé attendent l'audit.
4. **Si une réponse manque**, écrire l'hypothèse provisoire, la marquer `[H]` avec la personne qui
   peut la confirmer, et continuer. On ne bloque que si la décision dépend entièrement de cette
   inconnue.
5. **Rédiger la fiche** avec le modèle ci-dessous.
6. **Vérifier que c'est le bon problème** : la solution demandée règle-t-elle le problème posé ?
   une solution plus simple le réglerait-elle (supprimer une étape, configurer un outil déjà en
   place) ? le problème vient-il d'ailleurs (processus, organisation, donnée) ? Écrire la réponse,
   même quand elle conforte la demande.
7. **Finir par la décision attendue**, puis proposer l'étape suivante : `auditer-processus`. Quand
   le demandeur valide, ajouter une ligne à `mission/journal.md`.

## Le livrable

Modèle de `mission/cas-<slug>/10-besoin.md` :

```markdown
# Besoin — <titre court>

Date · Demandeur (rôle) · Rédigé par

## 1. La demande, telle qu'exprimée
> « … » (citation exacte, source : entretien, courriel, ticket)

## 2. Reformulation
Une ou deux phrases que le demandeur doit pouvoir signer.

## 3. Symptôme, problème, solution demandée
| Symptôme observé | Problème supposé | Solution demandée |

## 4. Décision à prendre
Ce que la mission doit permettre de décider, et par qui.

## 5. Parties prenantes
Rôles : qui décide, qui valide, qui utilise, qui est touché. Aucun jugement sur les personnes.

## 6. Périmètre
Dedans · Dehors (explicitement).

## 7. Contraintes
Budget, calendrier, outils imposés, données, sécurité, conformité.

## 8. Critères de succès
Chaque critère est mesurable et porte sa mesure de départ si elle est connue ; sinon « à mesurer
avant tout lancement ».

## 9. Ce qu'on sait, ce qu'on suppose, ce qu'on ignore
`[F]` faits avec leur source · `[H]` hypothèses avec qui peut les confirmer · `?` questions ouvertes.

## 10. Est-ce le bon problème ?
Réponse argumentée, y compris l'alternative la plus simple envisagée.

## Décision attendue
Valider la reformulation, le périmètre et les critères de succès — ou les corriger.
```

Ligne de journal, au moment où le demandeur tranche :

```markdown
- 2026-10-14 · cas-relances-factures · 10-besoin validé par la direction financière · « on garde le périmètre France »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Une page, pas un dossier | le détail du processus appartient à l'audit ; un cadrage long retarde la décision | un questionnaire exhaustif dès le départ | le besoin couvre plusieurs processus distincts : on ouvre alors un cas par processus |
| Questions groupées, envoyées en une fois | un aller-retour par question épuise le demandeur | l'entretien question par question | l'échange a lieu en direct : on peut alors suivre le fil de la conversation |
| Hypothèse marquée plutôt qu'attente | une mission ne s'arrête pas faute d'une réponse secondaire | bloquer jusqu'à la réponse | la décision dépend entièrement de l'inconnue |
| La solution demandée reste écrite | elle dit ce que le demandeur imagine, et c'est une information | la remplacer par « le vrai besoin » | jamais : on la garde, même écartée |

## Frontières

- Le processus actuel, ses mesures et ses causes → `auditer-processus`.
- Les exigences détaillées → `rediger-cahier-des-charges`.
- Aucun besoin nommé (« où l'IA peut-elle nous aider ? ») → `decouvrir-cas-usage`.
- L'état de la mission et le journal des décisions → `router-mission-ia`.
- Facultatif : quand la demande est une décision d'affaires ambiguë (marché, offre, investissement)
  et que `router-consulting-strategy` est installé dans la session, il peut structurer cette
  décision. Ne dire qu'on l'a utilisé que s'il a réellement été appelé.

## Preuves restantes

- Éprouvée sur la mission fictive de `examples/`.
- NON MESURÉ sur une mission réelle : le premier cas réel dira si huit questions suffisent ou s'il
  manque une rubrique.
