# Architecture — consultant-ia

Ce fichier est la carte canonique du pack. Si une compétence et cette carte se contredisent, on
corrige l'écart au lieu de documenter deux méthodes.

Le pack porte **la méthode d'une mission de conseil IA et automatisation** : comprendre le travail
réel, trouver ce qui mérite d'être automatisé, comparer les solutions, chiffrer, spécifier et
planifier. Il ne construit pas la solution, il ne décide pas à la place du client et il ne détient
aucune donnée propre à une entreprise : celles-ci vivent dans le dossier de la mission.

## Les trois statuts d'un nombre

Ils sont définis ici, une seule fois. Chaque compétence qui écrit un nombre le rappelle en une ligne
et renvoie à cette définition ; les guides d'entretien aussi.

| Statut | Sens | À écrire à côté |
|---|---|---|
| `[F]` fait | observé, appuyé par une pièce, ou décision ou contrainte énoncée par son détenteur (la source est l'entretien ou la pièce). Une valeur proposée puis acceptée à la validation devient `[F]` | la source : la pièce, l'entretien, ou la ligne du journal qui consigne l'accord |
| `[H]` hypothèse | déclaré de mémoire, supposé, ou paramètre choisi (seuil, jeu d'essai) | le rôle qui peut la confirmer |
| `[E]` estimation | calculée à partir de `[F]` et de `[H]` | le calcul, montré |

Une durée chronométrée sur une seule occurrence est `[F]` pour cette occurrence et `[H]` comme durée
typique. Un nombre sans statut est une erreur, pas un style.

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
| Découvrir | `decouvrir-cas-usage` | brancher le contexte, cartographier les tâches, les trier en cinq issues, rendre un portefeuille de cas classés |
| Cadrer | `cadrer-besoin` | reformuler le besoin, vérifier que c'est le bon problème, fixer périmètre, contraintes et critères de succès, nommer le dossier du cas |
| Auditer | `auditer-processus` | décrire le processus actuel, le mesurer, trouver les goulets et leurs causes, simplifier avant d'automatiser |
| Spécifier | `rediger-cahier-des-charges` | mode **exigences** (avant le choix, sans solution) et mode **spécification** (PRD de la solution retenue, indicateurs et seuils compris) |
| Concevoir | `concevoir-solution` | décider s'il faut automatiser, comparer de vraies options (y compris ne rien construire), recommander, poser une porte quand il faut standardiser avant de construire |
| Chiffrer | `chiffrer-rentabilite` | ordre de grandeur d'un portefeuille ou business case d'une option, hypothèses visibles, scénarios |
| Planifier | `planifier-deploiement` | feuille de route d'un portefeuille ou plan de déploiement d'un cas : simplifications, porte, pilote, adoption, rythme des revues d'indicateurs, pré-mortem |

Aucune compétence ne refait le travail d'une autre ligne. Si une responsabilité a un propriétaire
ci-dessus, on l'appelle.

## Le dossier de mission — l'état vit une seule fois

Tout livrable s'écrit dans `mission/` à la racine du dossier de travail. Le routeur dérive l'état
de ce dossier à chaque appel ; aucun fichier d'état ne déclare « fait ».

```text
mission/
  journal.md                 décisions humaines, datées (qui a tranché quoi), corrections, clôture
  sources/                   ce que l'entreprise fournit : documents, exports, transcriptions
  00-contexte.md             porte 2 : fiche entreprise, sources branchées et manquantes
  01-cartographie-taches.md  porte 2 : une ligne par tâche observée, puis le tri
  02-portefeuille.md         porte 2 : cas d'usage classés, décision attendue
  03-chiffrage.md            porte 2 : ordre de grandeur des gains et des coûts par cas
  04-feuille-de-route.md     porte 2 : ordre de mise en œuvre du portefeuille
  cas-<slug>/                un dossier par besoin traité par la porte 1
    10-besoin.md
    20-diagnostic.md
    30-exigences.md
    40-solutions.md          dont la porte, quand on standardise avant de construire
    50-rentabilite.md
    60-specification.md
    70-plan.md
```

Un besoin traité seul par la porte 1 n'a que `journal.md` et son dossier `cas-<slug>/`.

## Les règles communes — chaque compétence les applique

1. **Chaque nombre porte son statut** (`[F]`, `[H]` ou `[E]`, définis plus haut).
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

## Les conventions communes

- **Le nom d'un cas.** `cadrer-besoin` fixe le slug une seule fois : deux à quatre mots, sans accent
  (`relances-factures`). Le dossier s'appelle `cas-<slug>` ; le routeur, le journal et tous les
  renvois le reprennent tel quel.
- **Les rôles d'un livrable.** L'en-tête distingue le demandeur, le valideur du livrable et le
  décideur quand ils diffèrent. Quand un seul rôle tient les trois, une seule mention suffit.
- **Les identifiants.** `EF` exigence fonctionnelle, `ENF` non fonctionnelle, `CA` critère
  d'acceptation, `T` test, `R` risque, `IND` indicateur, `Q` question ouverte. Chaque série est
  numérotée une fois pour tout le cas : `Q-07` désigne la même question de 30 à 70.
- **Corriger un livrable déjà validé.** On ne réécrit pas en silence. Le livrable prend une version
  datée, avec son motif, dans son en-tête (« Version 1.1, précisée le 2026-10-12 : seuil ramené à
  trois jours ouvrés ») et `journal.md` reçoit une ligne « correction ». L'étape qui trouve un trou en
  amont le corrige ainsi, puis en informe le valideur du livrable corrigé.
- **Les renvois.** Un renvoi cite le livrable et le § ; si le livrable a été corrigé, il cite aussi la
  version lue (« 60-specification §13, v1.1 »). Sans version, il vise la version 1.
- **Les seuils.** Un indicateur a un identifiant `IND-xx` ; ses seuils de production vivent à un
  seul endroit, le protocole de la spécification. Les seuils du pilote sont distincts, et dits tels.

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

- Éprouvé sur une mission fictive complète (`examples/`, déroulée le 12 octobre 2026), qui a relevé
  94 frictions, corrigées dans cette version ; pas encore sur une mission réelle.
- Les étapes construire, tester, déployer et mesurer après déploiement ne sont pas dans le pack : elles
  viendront dans une version suivante. Le pack s'arrête à la spécification et au plan.
- Le chiffrage ne vaut que par ses mesures d'entrée : sans temps mesurés, il reste une fourchette.
- La découverte dépend de ce que l'entreprise branche et des entretiens ; le pack n'observe pas le
  travail tout seul.
- L'adoption par les équipes tient dans le plan (responsables, formation, communication), pas dans
  une méthode dédiée.
- La recherche de l'existant (pages des éditeurs, modèles publics) suppose un accès au moment du
  choix ; sans accès, elle s'écrit « non vérifiée » et le pack le dit.
- En français seulement.

## Documentation canonique

1. **Ce fichier** — architecture, contrats, règles et conventions communes.
2. **`router-mission-ia`** — comportement de la porte et état en direct.
3. Chaque compétence — la méthode de sa responsabilité.
4. **README** — présentation et installation.
5. `examples/` — une mission fictive déroulée par les deux portes, jamais une source de méthode.
