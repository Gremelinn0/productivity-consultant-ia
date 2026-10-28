# Questionnaire préparé pour un objectif

Quand l'objectif de la mission est nommé, l'entretien ne pose pas un questionnaire générique : il pose les
questions **qui manquent** pour cet objectif, dans les mots de la personne. Ce fichier donne la méthode et le
modèle ; `scripts/entretien.py` lit le questionnaire (guide `prepare`) et refuse celui qui ne respecte pas le
modèle.

## La méthode, avant d'ouvrir l'entretien

1. **L'objectif en une phrase**, à l'infinitif et dans les mots du client : « mettre en place un agent qui
   réponde aux demandes des clients de la boutique ». Toutes les questions le servent.
2. **Lire tout ce qui est accessible, en lecture seule** : la demande, les notes de `mission/sources/`, les
   échanges, le site de l'entreprise. En local (la session de l'entreprise, le pack installé), aussi ses
   dossiers, exports et outils déjà branchés : la boîte de support, le CRM, le back-office. Noter ce qu'on a lu.
3. **Prendre les questions candidates** : les huit de `cadrer-besoin` (étape 3), puis le module de l'objectif
   dans `cadrer-besoin/references/questions-par-objectif.md`, puis, si le processus est déjà nommé, les huit
   d'`auditer-processus` (étape 9).
4. **Trancher chaque candidate avec ce qu'on a lu** :
   - la réponse est sûre (une pièce, une règle dite par son détenteur) → la question ne se pose pas ; le fait
     va dans « Déjà établi », avec sa source ;
   - la réponse existe mais reste incertaine (dite de mémoire, ancienne, de seconde main, tirée du site) → la
     question se pose avec « Déjà su » : l'IA dit ce qu'on a noté et la personne confirme ou corrige ;
   - rien → la question se pose, réécrite pour cette personne : ses clients, ses outils, ses mots ; jamais
     le jargon du pack.
5. **Douze questions au plus**, les plus décisives d'abord : celles qui changent le périmètre, le coût ou les
   conditions de réussite. Le reste attend la séance d'observation ou l'audit, et se dit dans « Pas dans cet
   entretien ».
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
- Une question qui a changé le cadrage, le coût ou la réussite d'une mission rejoint son module (règle
  « Ajouter une question » de `questions-par-objectif.md`), réécrite sans le nom du client.
