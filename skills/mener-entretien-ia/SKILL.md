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
  `mission/sources/entretien-<rôle>-<date>.md` aux statuts [F]/[H]/[E], contrôlée. Tient aussi la base de
  questions par sujet (une mission de bout en bout, du premier échange au bilan, et chaque objectif, du
  support client à la prospection) : toute question à poser à une entreprise en part, et ce qui manquait y est rangé.
  Porte aussi l'agent d'entretien en ligne : devant un visiteur, sans consultant avant l'entretien, il choisit ses
  questions dans la base (douze au plus, jamais en dehors), affiche un plan et des réponses à cliquer, rend un
  compte rendu à son propre schéma (pistes comprises) et, pour le visiteur, un bilan écrit dans sa langue que la page
  affiche et envoie par e-mail à qui le demande.
  Outil du pack consultant-ia, appelé par decouvrir-cas-usage, cadrer-besoin et auditer-processus ; ne possède
  aucune étape. Triggers : « entretien guidé par IA », « entretien asynchrone », « questionnaire envoyé au
  client », « prépare les questions pour son objectif », « fais-moi les questions pour », « quelles questions
  poser à », « base de questions », « range cette question », « interview bot », « AI-led interview »,
  « agent d'entretien en ligne », « consigne en ligne », « audit en ligne d'un visiteur ».
metadata:
  scope: "un entretien du pack mené par écrit par une IA, sans le consultant, et sa note dans mission/sources/ ; la base de questions par sujet ; l'agent d'entretien en ligne d'un visiteur, qui choisit ses questions dans la base et lui rend son bilan"
  owns: "la base de questions (references/base-questions/, un fichier par sujet, guides fixes compris), la consigne de l'intervieweur, le schéma du compte rendu, le choix et la préparation du questionnaire, le contrôle et le rendu de la note et de sa transcription ; l'agent en ligne (sa méthode, sa consigne, le schéma de son compte rendu, le bilan du visiteur, sa note)"
  consumes: "ce que le consultant ou la session de l'entreprise a pu lire ; la conversation menée ; les règles d'entretien de decouvrir-cas-usage/references/guides-entretien.md"
---

# Mener un entretien guidé par IA

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/sources/entretien-<rôle>-<date>.md` et sa transcription
> `….transcription.md`. Preuve : `python skills/mener-entretien-ia/scripts/entretien.py note` refuse tout compte
> rendu qui enfreint les règles (une réponse par question dans l'ordre, ouverture dite, `[F]` fondé, `[H]` avec qui
> confirme, `[E]` avec son calcul, aucune adresse ni numéro) ; la transcription sort adresses et numéros retirés.
> Un questionnaire préparé sans objectif écrit, sans validation, ou de plus de douze questions est refusé.
> La base de questions : `entretien.py verifier` refuse un doublon dans toute la base, un préfixe pris deux fois,
> une ligne sans décision ou sans « D'abord », un index périmé, une compétence lectrice sans son rappel en tête, une
> consigne en ligne de plus de 60 000 caractères. L'agent en ligne : `entretien.py consigne-en-ligne` écrit sa ligne
> (consigne, schéma, sujets) et affiche la taille de la consigne ; `note` accepte son compte rendu (guide `en-ligne`),
> fusionne les entrées d'un même numéro de question, y recopie le bilan du visiteur (section « Bilan remis à la
> personne »), et refuse une question absente de la base, plus de douze questions différentes, une adresse ou un numéro,
> un prix dans une piste, un `bilan_visiteur` absent ou vide. Les cinq règles qu'a demandées le premier essai en ligne
> (douze questions, la question d'ouverture comprise ; un plan qui ne se récrit pas ; deux réponses d'un audit ; une
> seule chose par message ; une fin sans les moyens) et les deux du bilan (un message final court qui renvoie au bilan ;
> un bilan écrit pour la personne) sont écrites dans la méthode et dans la consigne, et des essais rougissent quand
> l'une manque.
> Essais : `python -m unittest discover -s skills/mener-entretien-ia/tests`. **Boucle** : aucune.

> ❓ **Une question pour l'entreprise sort de la base de questions** (`references/base-questions/`, un fichier par
> sujet, index `README.md`) : lire d'abord le bloc du sujet, ne poser que ce qui manque, puis y ranger ce qui
> manquait (`entretien.py ajouter` ; un sujet absent : `entretien.py creer-sujet`).

> 🌐 **Devant un visiteur en ligne, sans consultant avant l'entretien, l'agent choisit ses questions dans la base,
> jamais en dehors** : douze au plus, d'abord celles qui se posent à la personne, jamais ce que la page a déjà demandé.
> Avec un client du consultant, c'est un questionnaire préparé et validé. Méthode : `references/agent-en-ligne.md`.

## Ce que cette compétence résout

Les guides d'entretien du pack supposent un consultant en face : il pose, il relance, il note. Quand la personne
n'a qu'un quart d'heure ici ou là, ou qu'elle est à six fuseaux horaires, l'entretien n'a pas lieu, ou il se
réduit à un formulaire qui rend « ça dépend » et aucun chiffre. Cette compétence fait mener l'entretien par une IA,
à l'écrit, au rythme de la personne : elle pose les mêmes questions que le consultant, relance comme lui quand une
réponse est vague, et rend une note au format du pack, que le consultant relit avant de s'en servir.

Résultat attendu : une note d'entretien que `cadrer-besoin`, `auditer-processus` ou `decouvrir-cas-usage`
lisent comme n'importe quelle autre, avec ses citations mot pour mot et des nombres dont le statut est juste.

## Stratégie

1. **Les questions ne s'écrivent qu'une fois, dans la base.** Un fichier par sujet (`references/base-questions/`),
   chaque question avec la décision qu'elle sert ; les guides fixes en sont des blocs, et le script les y lit. Une
   question corrigée dans la base l'est partout ; chaque entretien enrichit la même base. Aucun questionnaire recopié.
2. **Ne demander que ce qui manque.** Un entretien qui redemande ce que l'entreprise a déjà écrit lasse la
   personne et coûte des réponses. Avant d'ouvrir, l'agent lit tout ce qui lui est accessible, ne pose pas ce qui
   est établi, fait confirmer ce qui est incertain, et vise l'objectif écrit. Une méthode, deux modes : en
   ligne, l'agent n'a lu que les sources du consultant et le site ; en local, la session de l'entreprise lit
   aussi ses dossiers et ses outils. Même questionnaire, même consigne, même note.
3. **L'IA recueille, elle ne conseille pas.** Pas de prix, d'outil, de délai ni de promesse ; une question posée au
   consultant est notée pour lui. C'est la règle « Ne rien promettre » des guides, tenue sans lui. L'agent en ligne
   n'avance des pistes qu'après la validation du récapitulatif, dans le bilan qu'il remet au visiteur, au conditionnel,
   sans prix, délai ni outil.
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
   mesurer). Les guides `besoin` (le socle du cadrage, CA01 à CA08) et `processus` (les huit questions
   d'automatisation, AP01 à AP08) servent quand rien n'a pu être lu avant. Un questionnaire par entretien et par rôle.
   Un visiteur en ligne, sans consultant avant l'entretien, n'a pas de questionnaire : voir la variante de l'agent en
   ligne, après l'étape 8.
2. **Préparer le questionnaire de l'objectif** : c'est ce qui fait la valeur de l'entretien. Lire tout ce qui est
   accessible (la demande, `mission/sources/`, le site, et en local les dossiers et outils de l'entreprise), en
   commençant par les traces de l'outil du processus quand un accès en lecture existe (`auditer-processus`,
   étape 2) : l'entretien confirme ce qu'elles montrent et cherche le reste, il ne fait pas ressaisir ce qu'on
   peut lire. Prendre le bloc du sujet dans la base (`references/base-questions/<sujet>.md`, index `README.md`)
   et le cadrage (`cadrage`) quand le sujet ne le pose pas dans ses mots ; un sujet absent s'ouvre dans la base.
   Puis trancher chacune : réponse sûre → elle ne se pose pas (« Déjà établi ») ; incertaine → elle se fait
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
   consultant le range, ou l'écarte : `entretien.py ajouter --sujet <sujet> --partie <n> --question "…" --decide "…"`
   (il refuse un doublon de toute la base et donne le numéro suivant), puis `entretien.py verifier`.
8. **Relire la note** comme le consultant relirait la sienne : ce qui est `[H]` reste à confirmer, les questions
   ouvertes partent dans le message de suite, et la note alimente l'étape qui l'a demandée.

### Variante : l'agent en ligne (un visiteur, sans consultant avant l'entretien)

Personne ne peut préparer ni valider le questionnaire d'un visiteur : l'agent choisit ses questions dans la base, douze
au plus, jamais en dehors. La méthode (le sujet, les douze questions, les réponses à cliquer, le plan, la fin, les
interdits) est `references/agent-en-ligne.md`.

1. `python …/entretien.py consigne-en-ligne --sortie ligne.json` écrit la ligne que l'hôte garde : `titre`, `guide`
   (`en-ligne`), `consigne` (la méthode condensée de `references/consigne-en-ligne.md`, l'index des sujets et toutes les
   questions de la base), `schema_compte_rendu` (`references/compte-rendu-en-ligne.schema.json`) et `questionnaire`. La
   taille de la consigne s'affiche.
2. L'hôte ajoute son contexte (la porte d'entrée, le sujet, les réponses de la page, les liens), définit les outils
   `afficher` (son `message` est obligatoire : tout ce que la personne lit passe par lui) et `terminer_entretien`, et
   mène la conversation. À la fin, il affiche le `bilan_visiteur` du compte rendu sous le dernier message et l'envoie par
   e-mail à qui le demande.
3. `python …/entretien.py note --compte-rendu cr.json --transcription messages.json --sortie mission/sources` écrit la
   note, de même structure que les autres, avec en plus « Pistes », « Bilan remis à la personne » (le bilan recopié tel
   quel, dans la langue de la personne) et « Pour la base de questions ». Rien n'y est `[F]`. Les entrées d'un même
   numéro de question s'y fusionnent, dans l'ordre.

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
`references/consigne-intervieweur.md`. Celui de l'agent en ligne suit `references/compte-rendu-en-ligne.schema.json` :
la note garde les mêmes sections, plus « Pistes » (constat, piste, prochaine étape), « Bilan remis à la personne » et
« Pour la base de questions ».

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
| Avec un client du consultant : un questionnaire préparé et validé, puis seulement ouvert | ce que l'agent croit savoir lui est lu ; une erreur dans « Déjà su » se dit à la personne | laisser l'IA choisir ses questions en direct | jamais, pour un client |
| En ligne, devant un visiteur : l'agent choisit ses questions dans la base, jamais en dehors | aucun consultant avant l'entretien, donc personne pour préparer ni valider un questionnaire ; la base est déjà relue et chaque question porte sa décision ; douze au plus, jamais ce que la page a demandé | un questionnaire préparé par visiteur (aucun relecteur) ; des questions inventées en direct | une question hors base a servi : elle y entre, relue par le consultant, puis l'agent peut la choisir |
| Douze questions au plus | un entretien écrit long s'abandonne ; le reste a sa place dans la séance d'observation ou l'audit | tout le module | une seule personne détient tout et le demande : deux entretiens, pas un long |
| En ligne, tout ce que la personne lit passe par `afficher.message` | le modèle range en bloc de réflexion vide le texte écrit avant un appel d'outil : un message écrit à côté de l'outil n'atteint pas la personne | un texte libre avant l'appel d'outil | un hôte qui montre aussi le texte écrit hors d'un appel d'outil |
| La note fusionne les entrées d'un même numéro de question, sans refuser le compte rendu | un entretien réel a rendu SC05 deux fois (une question reprise) : refuser la note privait le consultant du compte rendu du visiteur ; la consigne demande pourtant une seule entrée par numéro, et le plafond de douze compte les numéros différents | refuser le doublon (le contrôle d'avant) | deux réponses qui se contredisent sous un même numéro : la fusion cacherait un compte rendu faux |
| En ligne, les douze questions se comptent comme le visiteur les compte, la question d'ouverture comprise | l'ouverture promet douze questions : le premier essai (28/10) en a posé quatorze et a dit « Dernière question » à la quatorzième | ne compter que les questions de la base venues après l'ouverture ; laisser la fin à l'appréciation de l'agent | un hôte qui affiche le compte à côté du plan |
| En ligne, un plan affiché ne se récrit plus : seules les étapes « à venir » bougent, et « fait » veut dire demandé | le premier essai a laissé une étape « en cours » disparaître sans passer à « fait », en a renommé une trois fois et a fini sur un plan tout vert dont une étape n'avait jamais été demandée | un plan que l'agent ajuste librement à chaque tour (la règle d'avant) | jamais pour une étape en cours ou faite |
| En ligne, un audit demande toujours ce qui casserait si le volume doublait (EQ14) et l'objectif (DI01), avant les questions moins décisives | le premier essai n'a demandé ni l'un ni l'autre : le visiteur a ajouté l'objectif lui-même au récapitulatif, et la base n'avait aucune question sur le volume | les laisser au choix de l'agent parmi douze | la personne les a déjà données, ou la page les a demandées |
| En ligne, un message demande une seule chose, et les pistes de la fin disent un résultat, jamais le moyen | deux messages du premier essai demandaient deux choses, et les réponses à cliquer n'en couvraient qu'une ; la fin parlait d'« une automatisation ou un agent » : au visiteur, on parle du résultat | des messages à double question ; des pistes qui nomment l'agent, l'automatisation ou la plateforme | jamais pour le visiteur : le consultant choisit le moyen |
| En ligne, le visiteur repart avec un bilan écrit pour lui, dans sa langue (`bilan_visiteur`, champ obligatoire) ; le message final reste court | un visiteur qui a répondu pendant dix minutes repart avec quelque chose à garder : son récapitulatif validé et de une à trois pistes dites comme des résultats, sans compte ni prix ; la page l'affiche sous le message et l'envoie par e-mail à qui le demande | dire les pistes dans le message final (elles se perdent dans la conversation) ; un bilan en français pour tous ; refuser la note d'un visiteur dont le bilan dépasse les limites d'affichage (le consultant perdrait son compte rendu) | un hôte sans écran ni e-mail pour le bilan, ou un visiteur qui n'en veut pas |
| Une méthode, deux modes (en ligne, local) | seul l'accès aux données change ; deux méthodes divergeraient | un agent local à part | jamais |
| Une base de questions par sujet, guides fixes compris | une question vit à un seul endroit ; chaque entretien, audit ou rendez-vous enrichit la même base au lieu de réinventer ses questions | une liste dans chaque compétence (guides, cadrage, modules par objectif, jusqu'au 28/10/2026) | jamais |

## Frontières

- Quand poser quelles questions, combien et comment noter les réponses → `decouvrir-cas-usage` (règles des
  entretiens, séance d'enregistrement), `cadrer-besoin` (étape 3), `auditer-processus` (étapes 2 et 9). Les
  questions elles-mêmes vivent ici, dans la base. Ce qui est propre à une mission (le questionnaire préparé) vit
  dans `mission/sources/`.
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
- Agent en ligne : la consigne, le schéma, le contrôle du compte rendu et la note sont éprouvés par les essais du script,
  sur un compte rendu fictif. NON MESURÉ sur un vrai visiteur : si douze questions sont trop, si les réponses à cliquer
  orientent, si le plan se lit à côté de la conversation, combien vont jusqu'au récapitulatif. La consigne reprend toute
  la base : elle grossit avec elle, et `verifier` s'arrête à 60 000 caractères (au-delà, charger les sujets à la demande).
- Premier essai de l'agent en ligne (28/10/2026, un faux visiteur, quinze tours) : cinq défauts relevés (douze questions
  promises et quatorze posées ; un plan récrit sous les yeux du visiteur, fini tout vert ; un objectif jamais demandé ; deux
  choses demandées dans un message ; une fin qui parle d'automatisation et d'agent). La version 0.8.2 y répond par cinq
  règles écrites dans la méthode et dans la consigne, gardées par des essais. NON MESURÉ après correction : un second essai
  dira si le modèle tient le compte, le plan et la fin.
- Bilan du visiteur (version 0.8.3) : le schéma, la consigne, le contrôle et la note sont éprouvés par les essais du
  script, sur un compte rendu fictif en anglais ; retirer la phrase du message final de la consigne fait rougir l'essai
  qui la garde. NON MESURÉ avec le modèle : s'il écrit le bilan dans la langue de la personne, sans moyen ni prix, dans
  les limites d'affichage (1 200 et 300 caractères, trois pistes), et s'il garde le message final court.
- Le `message` obligatoire de `afficher` et la fusion d'une question reprise sont éprouvés par les essais du script ; un
  entretien réel les a motivés (un texte perdu hors de l'outil, SC05 revenu deux fois), aucun second entretien ne les a
  encore mesurés.
