# Questionnaire préparé pour un objectif

Quand l'objectif de la mission est nommé, l'entretien ne pose pas un questionnaire générique : il pose les
questions **qui manquent** pour cet objectif, dans les mots de la personne. Ce fichier donne la méthode et le
modèle ; `scripts/entretien.py` lit le questionnaire (guide `prepare`) et refuse celui qui ne respecte pas le
modèle.

## La méthode, avant d'ouvrir l'entretien

1. **L'objectif en une phrase**, à l'infinitif et dans les mots du client : « mettre en place un agent qui
   réponde aux demandes des clients de la boutique ». Toutes les questions le servent.
2. **Lire tout ce qui est accessible, en lecture seule** : la demande, les notes de `mission/sources/`, les
   échanges, le site de l'entreprise. Si l'outil du processus est lisible (accès accordé au consultant, ou en
   local la session de l'entreprise avec ses dossiers, exports et outils branchés : la boîte de support, le CRM,
   le back-office), relever d'abord ses traces comme le fait `auditer-processus` (étape 2) : volume, canaux,
   types, réponses, et ce qui n'arrive pas dans l'outil. Ce relevé passe en « Déjà établi » ; les questions ne
   portent plus que sur ce qu'il ne montre pas. Noter ce qu'on a lu.
3. **Partir de la base de questions du sujet** (`references/base-questions/<sujet>.md`, un fichier par sujet) :
   `python skills/mener-entretien-ia/scripts/entretien.py preparer --base support-client --objectif "…" --role "…" --sortie mission/sources/questionnaire-<objet>-<date>.md`
   écrit le brouillon avec toutes les questions du sujet (ou celles de `--garder SC02,SC05,…`), chacune avec son
   numéro de base et la décision qu'elle sert. On ne réécrit rien : on garde, on adapte les mots, on tranche
   (étape 4). Le cadrage (`cadrage`, CA01 à CA08) s'ajoute quand le sujet ne pose pas déjà ces questions dans
   ses mots ; l'automatisation d'un processus (`processus`) quand l'objectif en est une. Sans fichier pour le
   sujet : le cadrage et `processus`, puis le sujet s'ouvre dans la base avec les questions qui ont servi.
4. **Trancher chaque candidate avec ce qu'on a lu** :
   - la réponse est sûre (une pièce, une règle dite par son détenteur) → la question ne se pose pas ; le fait
     va dans « Déjà établi », avec sa source. Une pièce prouve ce qu'elle contient, pas qu'il n'y a rien d'autre :
     un export de la boîte ne dit rien d'un canal qui n'y arrive pas ;
   - la réponse existe mais reste incertaine (dite de mémoire, ancienne, de seconde main, tirée du site) → la
     question se pose avec « Déjà su » : l'IA dit ce qu'on a noté et la personne confirme ou corrige ;
   - rien → la question se pose, réécrite pour cette personne : ses clients, ses outils, ses mots ; jamais
     le jargon du pack.
5. **Douze questions au plus**, les plus décisives d'abord : celles qui changent le périmètre, le coût ou les
   conditions de réussite. Le reste attend la séance d'observation ou l'audit, et se dit dans « Pas dans cet
   entretien ». Quand plusieurs questions relèvent d'une autre personne (celle qui répond aux clients, celle qui
   tient la boutique), elles forment le questionnaire d'un second entretien, pour ce rôle.
6. **Faire valider** le questionnaire avant de l'ouvrir : le consultant ; en local sans consultant, la personne
   qui lance l'entretien. La ligne « Validé par » porte son rôle et la date ; sans elle, le script refuse.

Le même questionnaire sert en ligne (une page derrière connexion) et en local (la session Claude Code ou Codex
de l'entreprise) : seul change ce que l'agent a pu lire à l'étape 2. En direct, le consultant s'en sert comme
guide d'entretien.

## Le modèle

Fichier `mission/sources/questionnaire-<objet>-<date>.md` :

```markdown
# Questionnaire préparé — <objectif court> · <entreprise>

Objectif : <une phrase à l'infinitif, dans les mots du client>
Personne interrogée : <rôle> · Préparé le <date> par <rôle>
Validé par : <rôle>, le <date>
Lu pour le préparer : <la demande, les notes, le site, les exports… avec leur date>
Base : <sujet de la base> (<numéros gardés>)

## Déjà établi (on ne le redemande pas)

- <fait> (source : <pièce ou note>)

## Questions

| # | Thème | Question | Déjà su (à faire confirmer) | Alimente |
|---|---|---|---|---|
| 1 | <thème> | <la question, dans les mots de la personne> | <ce qu'on croit savoir, ou vide> | <rubrique de 10-besoin, colonne de 01, ou la donnée à réunir> |

## Pas dans cet entretien

- <ce qui attend la séance d'observation, l'audit ou une autre personne, et pourquoi>
```

Les questions portent les numéros 1 à n dans l'ordre ; le script leur donne les identifiants Q1 à Qn, que le
compte rendu reprend. La note d'entretien cite ce fichier ; `router-mission-ia` sait ainsi quel questionnaire
attend encore sa réponse.

## Règles

- Une question qui demande un document (export, modèle, politique écrite) dit aussi à qui l'envoyer : l'IA ne
  reçoit pas de pièce ; la promesse va dans « Documents ou accès promis ».
- Rien dans « Déjà su » qu'on ne dirait pas à la personne elle-même : l'IA le lui lit.
- Une question qui a changé le cadrage, le coût ou la réussite d'une mission rejoint son sujet dans la base,
  réécrite sans le nom du client (`base-questions/README.md`, « Enrichir la base » ; `entretien.py ajouter`).
- Ce questionnaire est celui d'un client du consultant. Un visiteur en ligne n'en a pas : personne ne peut le préparer
  ni le valider, et l'agent choisit ses questions dans la base, jamais en dehors (`agent-en-ligne.md`).
