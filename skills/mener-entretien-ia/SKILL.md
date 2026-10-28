---
name: mener-entretien-ia
description: >-
  Quand un entretien du pack doit se faire sans le consultant (« fais-le répondre seul », « elle répondra quand
  elle aura le temps », « un entretien mené par une IA », « envoie-lui les questions ») → préparer l'entretien
  écrit qu'une IA mène à sa place, en ligne ou dans la session Claude Code de l'entreprise : le questionnaire
  préparé pour l'objectif (seulement ce qui manque après lecture de tout ce qui est accessible, ce qui est
  incertain fait confirmer) ou un guide du pack (direction, équipes, version courte, cadrage, audit), la consigne
  de l'intervieweur (une question à la fois, relance sur la dernière occurrence réelle et l'ordre de grandeur,
  aucune promesse, aucun nom, la langue de la personne), puis transformer son compte rendu en note
  `mission/sources/entretien-<rôle>-<date>.md` aux statuts [F]/[H]/[E], contrôlée. Outil du pack consultant-ia,
  appelé par decouvrir-cas-usage, cadrer-besoin et auditer-processus ; ne possède aucune étape. Triggers :
  « entretien guidé par IA », « entretien asynchrone », « questionnaire envoyé au client », « prépare les
  questions pour son objectif », « interview bot », « AI-led interview », « async discovery interview ».
metadata:
  scope: "un entretien du pack mené par écrit par une IA, sans le consultant, et sa note dans mission/sources/"
  owns: "la consigne de l'intervieweur, le schéma du compte rendu, le choix et la préparation du questionnaire, le contrôle et le rendu de la note et de sa transcription"
  consumes: "les questions de decouvrir-cas-usage/references/guides-entretien.md, de cadrer-besoin (étape 3 et references/questions-par-objectif.md) et d'auditer-processus (étape 9) ; ce que le consultant ou la session de l'entreprise a pu lire ; la conversation menée"
---

# Mener un entretien guidé par IA

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/sources/entretien-<rôle>-<date>.md` et sa transcription
> `….transcription.md`. Preuve : `python skills/mener-entretien-ia/scripts/entretien.py note` refuse tout compte
> rendu qui enfreint les règles (une réponse par question dans l'ordre, ouverture dite, `[F]` fondé, `[H]` avec qui
> confirme, `[E]` avec son calcul, aucune adresse ni numéro) ; la transcription sort adresses et numéros retirés.
> Un questionnaire préparé sans objectif écrit, sans validation, ou de plus de douze questions est refusé.
> Essais : `python -m unittest discover -s skills/mener-entretien-ia/tests` (17, dont 11 sabotages). **Boucle** :
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
2. **Ne demander que ce qui manque.** Un entretien qui redemande ce que l'entreprise a déjà écrit lasse la
   personne et coûte des réponses. Avant d'ouvrir, l'agent lit tout ce qui lui est accessible, ne pose pas ce qui
   est établi, fait confirmer ce qui est incertain, et vise l'objectif écrit. Une méthode, deux modes : en
   ligne, l'agent n'a lu que les sources du consultant et le site ; en local, la session de l'entreprise lit
   aussi ses dossiers et ses outils. Même questionnaire, même consigne, même note.
3. **L'IA recueille, elle ne conseille pas.** Pas de prix, d'outil, de délai ni de promesse ; une question posée au
   consultant est notée pour lui. C'est la règle « Ne rien promettre » des guides, tenue sans lui.
4. **Relancer comme le consultant, deux fois au plus.** Une réponse sans occurrence réelle, sans ordre de grandeur
   ni exemple est relancée ; au-delà de deux relances, on demande qui saurait, et on passe. L'entretien reste court.
5. **Le statut se décide par une règle, pas par l'IA.** À l'écrit, presque tout est dit de mémoire : `[H]` avec qui
   confirme. `[F]` seulement pour une règle énoncée par son détenteur ou un nombre lu dans une pièce jointe. Le
   contrôle refuse un `[F]` sans fondement.
6. **La personne parle sa langue ; la note est en français.** Les citations restent mot pour mot dans la langue
   d'origine : c'est elles que `cadrer-besoin` reprend entre guillemets.
7. **Le consultant reste le valideur.** La note est une source, pas une décision : elle se relit, et ses `[H]`
   restent à confirmer comme ceux d'un entretien en face.

## Étapes

1. **Choisir le questionnaire.** L'objectif est nommé (porte « besoin connu ») → un questionnaire préparé pour lui
   (étape 2), le cas courant d'une mission. Pas encore d'objectif → un guide du pack : `direction` ou `equipes`
   (découverte), `court` quand le temps manque (trois questions, de quoi repérer des candidats, pas de quoi
   mesurer). Les guides `besoin` (les huit questions de `cadrer-besoin`) et `processus` (les huit
   d'`auditer-processus`) servent quand rien n'a pu être lu avant. Un questionnaire par entretien et par rôle.
2. **Préparer le questionnaire de l'objectif** : c'est ce qui fait la valeur de l'entretien. Lire tout ce qui est
   accessible (la demande, `mission/sources/`, le site, et en local les dossiers et outils de l'entreprise), en
   commençant par les traces de l'outil du processus quand un accès en lecture existe (`auditer-processus`,
   étape 2) : l'entretien confirme ce qu'elles montrent et cherche le reste, il ne fait pas ressaisir ce qu'on
   peut lire. Prendre les huit questions du cadrage et le bloc du sujet dans la base de questions (`references/base-questions/<sujet>.md`, sinon le module de `cadrer-besoin/references/questions-par-objectif.md`),
   puis trancher chacune : réponse sûre → elle ne se pose pas (« Déjà établi ») ; incertaine → elle se fait
   confirmer (« Déjà su ») ; absente → elle se pose, dans les mots de la personne. Douze au plus. Le fichier
   `mission/sources/questionnaire-<objet>-<date>.md` suit `references/questionnaire-prepare.md` et se fait
   valider avant l'entretien ; le script refuse celui qui n'est pas validé. Pour un guide du pack, écrire
   seulement ce qu'on sait déjà en quelques lignes (`--contexte`), rien qu'on ne dirait pas à la personne.
3. **Produire la consigne** :
   `python skills/mener-entretien-ia/scripts/entretien.py consigne --questionnaire mission/sources/questionnaire-….md --role "dirigeante" --entreprise "…" [--langue en]`
   (ou `--guide equipes --contexte contexte.md`). Elle porte l'ouverture (l'objet, l'enregistrement, des rôles
   et jamais de noms, « je ne sais pas » est une réponse), le questionnaire, les relances et la fin. Sans
   `--langue`, l'IA suit la langue de la personne.
4. **Faire mener l'entretien par un hôte**, l'un des deux modes ; seul change ce que l'agent a pu lire :
   - **en ligne** : un fil de conversation avec un modèle qui accepte une consigne système et un outil (un projet
     Claude que la personne ouvre, une page web derrière connexion). L'outil s'appelle `terminer_entretien`, son
     schéma est `python …/entretien.py schema`. L'hôte garde la conversation pour qu'on reprenne plus tard, et ne
     montre jamais la consigne ni le compte rendu à la personne ;
   - **en local** : la session Claude Code ou Codex de l'entreprise, pack installé. Elle a lu les dossiers à
     l'étape 2, pose à la personne seulement ce qui reste, une question à la fois, selon la même consigne, puis
     écrit le compte rendu au schéma dans un fichier JSON. Ce qu'elle a lu reste chez l'entreprise.
5. **À la fin, l'IA récapitule et fait valider** le récapitulatif par la personne, puis rend le compte rendu.
   L'hôte remplace la date, la durée et le guide par ce qu'il sait : le modèle ne connaît pas le jour.
6. **Tirer la note** :
   `python …/entretien.py note --compte-rendu cr.json [--questionnaire mission/sources/questionnaire-….md] --transcription messages.json --sortie mission/sources`.
   Un refus liste chaque écart ; on corrige le compte rendu (ou on le fait refaire), jamais la règle.
7. **Enrichir la base** : la section « Pour la base de questions » de la note propose ce qui manquait ; le
   consultant l'ajoute à `references/base-questions/<sujet>.md`, avec la décision que la question sert, ou l'écarte.
8. **Relire la note** comme le consultant relirait la sienne : ce qui est `[H]` reste à confirmer, les questions
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
| Date, durée et guide fixés par l'hôte | le modèle ignore le jour ; un essai l'a daté d'un an trop tôt, un autre a rendu « court » pour un questionnaire préparé | les prendre dans le compte rendu | jamais |
| Adresses et numéros retirés de la transcription | les guides : on retire noms et données personnelles avant de déposer | garder la transcription brute | jamais ; la conversation brute reste chez l'hôte, comme un enregistrement chez l'entreprise |
| La consigne en français, l'entretien dans la langue de la personne | une seule consigne à tenir ; la note du pack est en français | une consigne par langue | un modèle traduit mal une langue donnée : écrire la consigne dans cette langue |
| Un questionnaire préparé pour l'objectif, pas le cadrage générique | le 28/10, une dirigeante qui voulait un agent pour son service client a reçu les huit questions du cadrage : rien sur ses messages, ses réponses types ni ses commandes | un questionnaire unique pour tous | l'objectif n'est pas encore nommé : c'est une découverte, un guide du pack |
| Préparé, validé, puis seulement ouvert | ce que l'agent croit savoir lui est lu ; une erreur dans « Déjà su » se dit à la personne | laisser l'IA choisir ses questions en direct | jamais |
| Douze questions au plus | un entretien écrit long s'abandonne ; le reste a sa place dans la séance d'observation ou l'audit | tout le module | une seule personne détient tout et le demande : deux entretiens, pas un long |
| Une méthode, deux modes (en ligne, local) | seul l'accès aux données change ; deux méthodes divergeraient | un agent local à part | jamais |

## Frontières

- Les questions elles-mêmes → `decouvrir-cas-usage` (guides direction, équipes, version courte), `cadrer-besoin`
  (étape 3, modules par objectif), `auditer-processus` (étape 9). Les corriger là-bas. Ce qui est propre à une
  mission (le questionnaire préparé) vit dans `mission/sources/`.
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
- Questionnaire préparé : contrôles éprouvés par les essais (objectif, validation, douze au plus, numérotation,
  compte rendu sans son questionnaire). Le mode local reste à éprouver sur un dossier d'entreprise fictif : ce
  que la session lit, ce qu'elle ne redemande pas.
