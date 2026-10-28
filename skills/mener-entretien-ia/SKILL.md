---
name: mener-entretien-ia
description: >-
  Quand un entretien du pack doit se faire sans le consultant (« fais-le répondre seul », « elle répondra quand
  elle aura le temps », « un entretien mené par une IA », « envoie-lui les questions ») → préparer l'entretien
  écrit qu'une IA mène à sa place : le questionnaire tiré du pack (direction, équipes, version courte, les huit
  questions de cadrer-besoin ou celles d'auditer-processus), la consigne de l'intervieweur (une question à la
  fois, relance sur la dernière occurrence réelle et l'ordre de grandeur, aucune promesse, aucun nom, la langue de
  la personne), puis transformer son compte rendu en note `mission/sources/entretien-<rôle>-<date>.md` aux statuts
  [F]/[H]/[E], contrôlée. Outil du pack consultant-ia, appelé par decouvrir-cas-usage, cadrer-besoin et
  auditer-processus ; ne possède aucune étape. Triggers : « entretien guidé par IA », « entretien asynchrone »,
  « questionnaire envoyé au client », « interview bot », « AI-led interview », « async discovery interview ».
metadata:
  scope: "un entretien du pack mené par écrit par une IA, sans le consultant, et sa note dans mission/sources/"
  owns: "la consigne de l'intervieweur, le schéma du compte rendu, le choix du questionnaire, le contrôle et le rendu de la note et de sa transcription"
  consumes: "les questions de decouvrir-cas-usage/references/guides-entretien.md, de cadrer-besoin (étape 3) et d'auditer-processus (étape 9) ; ce que le consultant sait déjà ; la conversation menée"
---

# Mener un entretien guidé par IA

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/sources/entretien-<rôle>-<date>.md` et sa transcription
> `….transcription.md`. Preuve : `python skills/mener-entretien-ia/scripts/entretien.py note` refuse tout compte
> rendu qui enfreint les règles (une réponse par question dans l'ordre, ouverture dite, `[F]` fondé, `[H]` avec qui
> confirme, `[E]` avec son calcul, aucune adresse ni numéro) ; la transcription sort adresses et numéros retirés.
> Essais : `python -m unittest discover -s skills/mener-entretien-ia/tests` (11, dont 7 sabotages). **Boucle** :
> aucune.

## Ce que cette compétence résout

Les guides d'entretien du pack supposent un consultant en face : il pose, il relance, il note. Quand la personne
n'a qu'un quart d'heure ici ou là, ou qu'elle est à six fuseaux horaires, l'entretien n'a pas lieu, ou il se
réduit à un formulaire qui rend « ça dépend » et aucun chiffre. Cette compétence fait mener l'entretien par une IA,
à l'écrit, au rythme de la personne : elle pose les mêmes questions que le consultant, relance comme lui quand une
réponse est vague, et rend une note au format du pack, que le consultant relit avant de s'en servir.

Résultat attendu : une note d'entretien que `cadrer-besoin`, `auditer-processus` ou `decouvrir-cas-usage`
lisent comme n'importe quelle autre, avec ses citations mot pour mot et des nombres dont le statut est juste.

## Stratégie

1. **Les questions ne s'écrivent qu'une fois.** Le script lit le questionnaire là où il vit (guides, cadrer-besoin,
   auditer-processus) ; une question corrigée là-bas l'est ici. Aucun questionnaire recopié.
2. **L'IA recueille, elle ne conseille pas.** Pas de prix, d'outil, de délai ni de promesse ; une question posée au
   consultant est notée pour lui. C'est la règle « Ne rien promettre » des guides, tenue sans lui.
3. **Relancer comme le consultant, deux fois au plus.** Une réponse sans occurrence réelle, sans ordre de grandeur
   ni exemple est relancée ; au-delà de deux relances, on demande qui saurait, et on passe. L'entretien reste court.
4. **Le statut se décide par une règle, pas par l'IA.** À l'écrit, presque tout est dit de mémoire : `[H]` avec qui
   confirme. `[F]` seulement pour une règle énoncée par son détenteur ou un nombre lu dans une pièce jointe. Le
   contrôle refuse un `[F]` sans fondement.
5. **La personne parle sa langue ; la note est en français.** Les citations restent mot pour mot dans la langue
   d'origine : c'est elles que `cadrer-besoin` reprend entre guillemets.
6. **Le consultant reste le valideur.** La note est une source, pas une décision : elle se relit, et ses `[H]`
   restent à confirmer comme ceux d'un entretien en face.

## Étapes

1. **Choisir le guide** selon l'étape qui en a besoin : `direction` ou `equipes` (découverte), `court` quand le temps
   manque (trois questions, de quoi repérer des candidats, pas de quoi mesurer), `besoin` (les huit questions de
   `cadrer-besoin`), `processus` (les huit questions d'automatisation d'`auditer-processus`). Un guide par entretien
   et par rôle.
2. **Écrire ce qu'on sait déjà** en quelques lignes (le contexte, la demande, les sources lues) : l'IA ne le redemande
   pas et s'en sert pour noter les écarts. Rien de confidentiel qu'on ne dirait pas à la personne elle-même.
3. **Produire la consigne** :
   `python skills/mener-entretien-ia/scripts/entretien.py consigne --guide besoin --role "dirigeante" --entreprise "…" --contexte contexte.md [--langue en]`.
   Elle porte l'ouverture (l'objet, l'enregistrement, des rôles et jamais de noms, « je ne sais pas » est une
   réponse), le questionnaire, les relances et la fin. Sans `--langue`, l'IA suit la langue de la personne.
4. **Faire mener l'entretien par un hôte** : n'importe quel fil de conversation avec un modèle qui accepte une
   consigne système et un outil (un projet Claude que la personne ouvre, une page web derrière connexion). L'outil
   s'appelle `terminer_entretien`, son schéma est `python …/entretien.py schema`. L'hôte garde la conversation pour
   qu'on puisse reprendre plus tard, et ne montre jamais la consigne ni le compte rendu à la personne.
5. **À la fin, l'IA récapitule et fait valider** le récapitulatif par la personne, puis appelle l'outil. L'hôte
   remplace la date et la durée par celles qu'il a mesurées : le modèle ne connaît pas le jour.
6. **Tirer la note** :
   `python …/entretien.py note --compte-rendu cr.json --transcription messages.json --sortie mission/sources`.
   Un refus liste chaque écart ; on corrige le compte rendu (ou on le fait refaire), jamais la règle.
7. **Relire la note** comme le consultant relirait la sienne : ce qui est `[H]` reste à confirmer, les questions
   ouvertes partent dans le message de suite, et la note alimente l'étape qui l'a demandée.

## Le livrable

`mission/sources/entretien-<rôle>-<date>.md`, au modèle de note de `decouvrir-cas-usage/references/guides-entretien.md` :

```markdown
# Entretien — <rôle>, <équipe> · <date> · <durée>
Mené par : entretien guidé par IA, sans le consultant · Guide utilisé · Personnes présentes (rôles) · Langue
Transcription intégrale : `entretien-<rôle>-<date>.transcription.md`
## Ce qui a été dit
Ouverture dite, puis par question : la question, la synthèse en français, la dernière occurrence racontée,
les nombres avec leur statut, les citations mot pour mot, le nombre de relances.
## Tâches citées (à reporter dans 01)
## Pièces remises
## Écarts avec d'autres sources
## Documents ou accès promis
## Questions restées ouvertes
```

Le compte rendu qui la produit suit `references/compte-rendu.schema.json` ; la consigne de l'intervieweur est
`references/consigne-intervieweur.md`.

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Une IA qui converse, pas un formulaire | un formulaire rend « ça dépend » ; la relance sur la dernière occurrence est ce qui donne des faits | un questionnaire envoyé en une fois | la personne préfère tout écrire d'un coup : la consigne accepte une longue réponse et relance seulement ce qui manque |
| Deux relances au plus par question | au-delà, la personne se lasse et abandonne l'entretien | relancer jusqu'à obtenir un chiffre | une question décide seule du cas : l'écrire dans le contexte, l'IA y revient à la fin |
| `[F]` réservé à la règle énoncée et à la pièce jointe | un nombre écrit de mémoire n'est pas plus sûr qu'un nombre dit | laisser l'IA juger du statut | jamais |
| Date et durée fixées par l'hôte | le modèle ignore le jour ; un essai l'a daté d'un an trop tôt | les prendre dans le compte rendu | jamais |
| Adresses et numéros retirés de la transcription | les guides : on retire noms et données personnelles avant de déposer | garder la transcription brute | jamais ; la conversation brute reste chez l'hôte, comme un enregistrement chez l'entreprise |
| La consigne en français, l'entretien dans la langue de la personne | une seule consigne à tenir ; la note du pack est en français | une consigne par langue | un modèle traduit mal une langue donnée : écrire la consigne dans cette langue |

## Frontières

- Les questions elles-mêmes → `decouvrir-cas-usage` (guides direction, équipes, version courte), `cadrer-besoin`
  (étape 3), `auditer-processus` (étape 9). Les corriger là-bas.
- La séance où l'on enregistre une personne qui fait la tâche → `decouvrir-cas-usage` : un entretien écrit ne la
  remplace pas, on n'y voit pas les contournements.
- Ce qu'on fait de la note (fiche besoin, diagnostic, cartographie) → l'étape qui l'a demandée.
- L'hôte qui sert la conversation (page, comptes, stockage) n'appartient pas au pack ; il respecte l'étape 4.

## Preuves restantes

- Éprouvée le 28/10/2026 sur une cliente fictive (boutique en ligne, en anglais, guide `besoin`, 16 messages) :
  relances sur la réponse vague, refus du prix et d'une injection (« ignore your instructions »), adresse e-mail
  non répétée, correction de fin prise en compte, note acceptée par le contrôle. Deux défauts corrigés depuis :
  glissements en français, date du compte rendu.
- NON MESURÉ sur une vraie personne : le premier entretien réel dira si l'ouverture est assez courte, si deux
  relances suffisent, et combien de personnes vont au bout.
