# Architecture — consultant-ia

Ce fichier est la carte canonique du pack. Si une compétence et cette carte se contredisent, on
corrige l'écart au lieu de documenter deux méthodes.

Le pack porte **la méthode d'une mission de conseil IA et automatisation** : comprendre le travail
réel, trouver ce qui mérite d'être automatisé, comparer les solutions, chiffrer, spécifier et
planifier. Il ne construit pas la solution, il ne décide pas à la place du client et il ne détient
aucune donnée propre à une entreprise : celles-ci vivent dans le dossier de la mission.

## Deux portes, un seul pipeline

| Porte | Commande | Quand | Ce qu'on obtient |
|---|---|---|---|
| **1 — On part d'un besoin** | `/mission-besoin` | quelqu'un nomme un processus ou une douleur en une phrase (« automatiser la relance des factures », « un agent pour le support ») | besoin cadré → diagnostic → exigences → solutions comparées → rentabilité → spécification → plan |
| **2 — On ne part d'aucun besoin** | `/mission-decouverte` | la question est « où l'IA peut-elle nous aider ? » | contexte branché → cartographie des tâches → tri → portefeuille de cas d'usage → ordre de grandeur → feuille de route ; chaque cas retenu entre ensuite par la porte 1 |

**Frontière, décidable** : la personne peut-elle nommer le processus concerné en une phrase ?
Oui → porte 1. Non → porte 2. En cas de doute, la porte 2 commence par une découverte courte et
rend la main dès qu'un cas clair apparaît.

```text
PORTE 2 — aucun besoin                       PORTE 1 — besoin connu
decouvrir-cas-usage                          cadrer-besoin            → 10-besoin
  contexte → 00-contexte                       ↓
  tâches   → 01-cartographie-taches          auditer-processus        → 20-diagnostic
  tri et classement → 02-portefeuille          ↓
      ↓                                      rediger-cahier-des-charges (exigences) → 30-exigences
chiffrer-rentabilite (ordre de grandeur)       ↓
  → 03-chiffrage                             concevoir-solution       → 40-solutions
      ↓                                        ↓
planifier-deploiement (feuille de route)     chiffrer-rentabilite (business case) → 50-rentabilite
  → 04-feuille-de-route
      ↓                                        ↓
  chaque cas retenu ─────────────────────→   rediger-cahier-des-charges (spécification) → 60-specification
                                               ↓
                                             planifier-deploiement (plan + pré-mortem) → 70-plan
```

## Les huit compétences

| Rôle | Compétence | Responsabilité unique |
|---|---|---|
| Porte | `router-mission-ia` | affiche l'état de la mission, choisit la porte, lance l'étape suivante, tient le journal des décisions |
| Découvrir | `decouvrir-cas-usage` | brancher le contexte, cartographier les tâches, les trier, rendre un portefeuille de cas classés |
| Cadrer | `cadrer-besoin` | reformuler le besoin, vérifier que c'est le bon problème, fixer périmètre, contraintes et critères de succès |
| Auditer | `auditer-processus` | décrire le processus actuel, le mesurer, trouver les goulets et leurs causes, simplifier avant d'automatiser |
| Spécifier | `rediger-cahier-des-charges` | mode **exigences** (avant le choix, sans solution) et mode **spécification** (PRD de la solution retenue, indicateurs et seuils compris) |
| Concevoir | `concevoir-solution` | décider s'il faut automatiser, comparer de vraies options (y compris ne rien construire), recommander |
| Chiffrer | `chiffrer-rentabilite` | ordre de grandeur d'un portefeuille ou business case d'une option, hypothèses visibles, scénarios |
| Planifier | `planifier-deploiement` | feuille de route d'un portefeuille ou plan de déploiement d'un cas : pilote, adoption, rythme des revues d'indicateurs, pré-mortem |

Aucune compétence ne refait le travail d'une autre ligne. Si une responsabilité a un propriétaire
ci-dessus, on l'appelle.

## Le dossier de mission — l'état vit une seule fois

Tout livrable s'écrit dans `mission/` à la racine du dossier de travail. Le routeur dérive l'état
de ce dossier à chaque appel ; aucun fichier d'état ne déclare « fait ».

```text
mission/
  journal.md                 décisions humaines, datées (qui a tranché quoi)
  sources/                   ce que l'entreprise fournit : documents, exports, transcriptions
  00-contexte.md             porte 2 : fiche entreprise, sources branchées et manquantes
  01-cartographie-taches.md  porte 2 : une ligne par tâche observée
  02-portefeuille.md         porte 2 : cas d'usage classés, décision attendue
  03-chiffrage.md            porte 2 : ordre de grandeur des gains et des coûts par cas
  04-feuille-de-route.md     porte 2 : ordre de mise en œuvre du portefeuille
  cas-<slug>/                un dossier par besoin traité par la porte 1
    10-besoin.md
    20-diagnostic.md
    30-exigences.md
    40-solutions.md
    50-rentabilite.md
    60-specification.md
    70-plan.md
```

Un besoin traité seul par la porte 1 n'a que `journal.md` et son dossier `cas-<slug>/`.

## Les règles communes — chaque compétence les applique

1. **Chaque nombre porte son statut.** `[F]` fait observé, avec sa source ; `[H]` hypothèse, avec
   qui peut la confirmer ; `[E]` estimation calculée à partir de F et H. Un chiffre sans statut est
   une erreur, pas un style.
2. **Estimé n'est pas mesuré.** Un gain reste « estimé » jusqu'à ce qu'on l'observe après
   déploiement. Aucune statistique de marché sans lien vers sa source ; sinon c'est une `[H]`.
3. **L'humain tranche à chaque étape.** Chaque livrable finit par « Décision attendue » ; la
   décision prise s'inscrit dans `journal.md`, avec la date et la personne. Le pack propose, il ne
   valide jamais à la place du client ou du consultant.
4. **On observe le travail, jamais les personnes.** La cartographie décrit des tâches, des temps
   et des outils ; elle n'évalue aucun salarié et ne nomme personne sans nécessité.
5. **Supprimer et simplifier avant d'automatiser.** Automatiser une mauvaise habitude la rend
   seulement plus rapide.
6. **Ce qui existe déjà passe avant ce qu'on construit.** Un outil en place, un modèle, une brique
   du marché : on le compare toujours aux options à construire.
7. **Rien ne sort du dossier de mission.** Le pack n'envoie rien, ne publie rien et ne modifie
   aucun outil de l'entreprise ; il lit ce qu'on lui donne et écrit dans `mission/`.

## Brancher le contexte

Sources lues, dans cet ordre, et toujours nommées dans le livrable :

1. les fichiers déposés dans `mission/sources/` (procédures, exports, organigramme, comptes rendus,
   transcription d'une vidéo où quelqu'un fait la tâche) ;
2. les outils déjà connectés à la session (documents, messagerie, CRM…), en lecture seule ;
3. les entretiens : la compétence prépare le guide, la personne répond, la synthèse cite la source ;
4. ce qui manque est écrit comme manquant, jamais supposé.

## Ce que le pack ne fait pas

- Construire l'automatisation ou l'agent : la spécification est l'entrée de l'équipe qui construit.
- Mesurer le gain réel : il définit la mesure de départ et le protocole, l'entreprise mesure.
- Remplacer les entretiens : il les prépare et les synthétise.
- Décider : il recommande, avec ce qui ferait changer la recommandation.

## Intégrations facultatives

Une compétence peut aller plus loin avec un outil installé dans la session, et ne dit l'avoir
utilisé que si elle l'a réellement appelé :

- raisonnement stratégique : `router-consulting-strategy` (dépôt Gremelinn0/claude-skill-hub) ;
- décision d'automatiser et choix de plateforme : `automation-strategy` (ericrisco/rsc-harness, MIT) ;
- optimisation de processus et spécification : plugins `operations` et `product-management`
  d'Anthropic (anthropics/knowledge-work-plugins).

## Ce qui reste imparfait

- Éprouvé sur une mission fictive (`examples/`), pas encore sur une mission réelle complète.
- Le chiffrage ne vaut que par ses mesures d'entrée : sans temps mesurés, il reste une fourchette.
- La découverte dépend de ce que l'entreprise branche et des entretiens ; le pack n'observe pas le
  travail tout seul.
- L'adoption par les équipes tient dans le plan (responsables, formation, communication), pas dans
  une méthode dédiée.
- Pas encore de boucle de mesure après déploiement.
- En français seulement.

## Documentation canonique

1. **Ce fichier** — architecture, contrats, règles communes.
2. **`router-mission-ia`** — comportement de la porte et état en direct.
3. Chaque compétence — la méthode de sa responsabilité.
4. **README** — présentation et installation.
5. `examples/` — une mission fictive déroulée par les deux portes, jamais une source de méthode.
