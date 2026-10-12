---
name: decouvrir-cas-usage
description: >-
  Quand une entreprise veut savoir où l'IA peut l'aider sans pouvoir nommer un processus (« où
  peut-on utiliser l'IA chez nous ? », « on perd du temps mais on ne sait pas où », « trouvez-nous
  des cas d'usage ») → brancher le contexte, cartographier les tâches réelles des équipes, les trier
  en quatre issues (éliminer, automatiser, déléguer à l'IA, garder) et rendre un portefeuille de cas
  d'usage classés, avec la décision : quels cas creuser. Porte « on ne part d'aucun besoin » du pack
  consultant-ia ; chaque cas retenu entre ensuite par la porte « besoin connu », à partir de
  cadrer-besoin. Triggers : « où l'IA peut nous aider », « découverte de cas d'usage », « use case
  discovery », « cartographier les tâches », « portefeuille de cas d'usage », « par où commencer
  avec l'IA », « opportunités d'automatisation », « AI opportunity assessment ».
metadata:
  scope: "une entreprise ou une équipe qui ne nomme aucun besoin précis, du contexte au portefeuille de cas d'usage classés, avant tout cadrage, diagnostic détaillé ou choix de solution"
  owns: "le contexte branché, la cartographie des tâches, le tri en quatre issues, les fiches de cas d'usage et leur classement, les guides d'entretien"
  consumes: "mission/sources/ ; les outils connectés à la session, en lecture seule et avec autorisation ; les réponses aux entretiens ; mission/journal.md"
---

# Découvrir les cas d'usage

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/00-contexte.md`, `mission/01-cartographie-taches.md` et
> `mission/02-portefeuille.md`. Preuve : le décideur choisit les cas à creuser, et la décision s'inscrit
> dans `mission/journal.md`. Contrôle de forme : la cartographie porte ses douze colonnes et l'issue de
> chaque tâche, chaque fiche de cas ses douze rubriques, chaque nombre son statut `[F]`, `[H]` ou `[E]`.
> Exemple de référence : `examples/` du pack. **Boucle** : aucune.

## Ce que cette compétence résout

« Où l'IA peut-elle nous aider ? » n'est pas un besoin, c'est une question sur un travail que l'entreprise ne voit
plus : la direction parle d'objectifs, les équipes de leurs journées, et personne ne met les deux côte à côte. Cette
compétence part du travail réel : elle branche ce que l'entreprise fournit, recense les tâches, décide pour chacune
si elle doit disparaître, être automatisée, confiée à l'IA ou rester humaine, puis rend une liste courte de cas
d'usage classés.

Résultat attendu : trois documents (contexte, cartographie, portefeuille) et une décision — quels cas creuser. Pas
de solution choisie, pas de chiffrage fin.

## Stratégie

1. **Partir du travail, pas de l'outil.** Un cas d'usage décrit un résultat métier reproductible (« les relances de
   factures échues partent à temps »), jamais un produit ni un workflow ; sinon le portefeuille se remplit de
   technologies qui cherchent un problème.
2. **Interroger le travail, pas les personnes.** On demande ce qui se passe, on écrit des rôles plutôt que des noms,
   on ne juge personne : quelqu'un qui se sent évalué cache ses contournements, et ce sont eux qui révèlent les
   meilleures pistes.
3. **Observé avant déclaré, déclaré avant supposé.** Un enregistrement du travail vaut mieux qu'un entretien, qui
   vaut mieux qu'un document, qui vaut mieux qu'une intuition. Chaque ligne dit d'où elle vient ; une tâche sans
   source n'entre pas dans la cartographie.
4. **Trier avant de construire.** Éliminer, automatiser, déléguer à l'IA, garder — on pose les questions dans cet
   ordre, car automatiser une mauvaise habitude la rend seulement plus rapide. Ce qui existe déjà (outil en place,
   modèle, brique du marché) passe avant ce qu'on construit.
5. **Un ordre de grandeur suffit, et une liste courte se décide.** On compare des cas, on ne promet pas de gains :
   estimé n'est pas mesuré, chaque nombre garde son statut. Trois à cinq cas à faible effort et forte valeur,
   idéalement un par équipe, valent mieux que quarante idées : chaque équipe voit un gain proche et adopte la suite.

## Étapes

1. **Vérifier la porte, puis ouvrir le dossier.** La personne peut-elle nommer le processus en une phrase ? Oui →
   `cadrer-besoin` : la découverte ne retarde pas ce qui est déjà clair. Non, ou doute → découverte courte, qui rend
   la main dès qu'un cas clair apparaît. Créer `mission/`, `mission/sources/` et `mission/journal.md` s'ils
   manquent.
2. **Brancher le contexte, dans cet ordre**, en nommant chaque source dans `00-contexte.md` :
   - les fichiers déposés dans `mission/sources/` (procédures, exports, organigramme, comptes rendus,
     transcriptions) ;
   - les outils déjà connectés à la session, inventoriés d'après les outils réellement disponibles et sans rien lire
     d'abord. Autorisation explicite de l'entreprise, source par source (qui, quand, quel périmètre), puis lecture
     seule. Minimiser les données personnelles : lire catégories, objets, volumes et dates des tickets plutôt que
     les messages des personnes, ne rien copier de nominatif ;
   - puis les entretiens et l'observation (étapes 3 et 4).

   Ce qui manque s'écrit comme manquant. Sans aucune source, s'arrêter à `00-contexte.md` et au guide d'entretien :
   on ne devine pas les tâches. Faire valider `00` (sources, équipes à écouter).
3. **Mener les entretiens** : la direction d'abord (objectifs, ce qui coûte le plus de temps, priorités,
   contraintes, budget, essais passés), puis les équipes (semaine type, tâches répétitives, volumes, outils,
   copier-coller, validations, erreurs, exceptions, ce qu'elles voudraient ne plus faire). Questions, version
   courte, modèle de note : `references/guides-entretien.md`, à adapter aux équipes et aux outils déjà repérés. Si
   la session ne mène pas l'entretien, remettre le guide au consultant et lire sa note, déposée dans
   `mission/sources/`.
4. **Proposer la séance d'enregistrement, la source la plus riche** : des personnes font réellement leurs tâches
   pendant qu'on enregistre (vidéo ou partage d'écran) en commentant à voix haute, avec leur accord et celui de la
   direction ; la transcription est déposée dans `mission/sources/`. Le pack n'enregistre rien lui-même (protocole :
   `references/guides-entretien.md`).
5. **Chercher les signaux** dans les sources : demandes récurrentes, rapports faits à la main, copier-coller entre
   outils, tableurs utilisés comme base de données, validations par courriel, double saisie. Un signal n'est pas une
   tâche : il dit où poser la question.
6. **Cartographier (`01`).** Une ligne par tâche, douze colonnes, chaque ligne avec sa source ; chaque nombre porte
   `[F]` (fait observé, avec sa source), `[H]` (hypothèse, avec qui peut la confirmer) ou `[E]` (estimation
   calculée). Fusionner une tâche décrite par deux sources, puis faire relire le tableau par les équipes : s'y
   reconnaissent-elles ?
7. **Trier chaque tâche en quatre issues**, en pesant quatre critères — la **fréquence**, le **coût** (temps et
   argent par occurrence), la **valeur** (ce que la tâche apporte), le **risque si ça se trompe** — et écrire
   pourquoi :

   | Issue | Quand | Ce qu'on en fait |
   |---|---|---|
   | **Éliminer** | prend du temps, apporte peu, personne ne remarquerait sa disparition | souvent le gain le plus rapide : on supprime, on ne construit rien |
   | **Automatiser** | même schéma à chaque fois, relie plusieurs outils, règles stables | on construit une fois, puis on surveille |
   | **Déléguer à l'IA** | processus clair, résultat contrôlable | l'IA prépare ou exécute, un humain valide si nécessaire |
   | **Garder** | jugement, relation, négociation, décision importante | l'IA peut préparer, comparer, challenger, sans porter la responsabilité |

   Des règles floues ne donnent pas « Automatiser » : on simplifie d'abord. Faire valider `01`.
8. **Formuler les cas d'usage (`02`).** Chaque tâche « Automatiser » ou « Déléguer à l'IA » devient une fiche ; une
   tâche « Garder » seulement si l'IA y prépare, compare ou challenge sans décider (la fiche nomme qui décide).
   Dédoublonner : même déclencheur + même transformation + même résultat + même responsable = un seul cas ; secteur,
   canal ou outil différents = variantes ; données, validation, contraintes réglementaires ou résultat économique
   différents = cas séparés. `references/catalogue-cas-usage.md` rappelle les pistes de chaque fonction :
   aide-mémoire, pas preuve — une piste qu'aucune tâche de `01` ne fonde reste une hypothèse `[H]`.
9. **Classer.** *Valeur* : ordre de grandeur du gain mensuel `[E]` = fréquence × durée × volume (exemple de calcul,
   fictif : 4 fois par mois × 10 minutes × 30 relances = 20 heures par mois, un plafond que le chiffrage réduira).
   *Facilité* (données disponibles, règles stables, accès aux outils, peu d'exceptions) et *risque si ça se trompe*
   se notent haut, moyen ou bas, avec une raison d'une ligne que `planifier-deploiement` reprendra. Un cas n'est pas
   plus facile que sa donnée la moins accessible ; un risque haut n'écarte pas le cas, il impose une validation
   humaine. Quatre classes :
   - **Gains rapides** : valeur notable, facilité haute, risque bas ou couvert par une validation ;
   - **Projets** : valeur haute mais facilité moyenne ou basse, ou risque qui impose des garde-fous ;
   - **À creuser** : une donnée manquante empêche de classer — écrire laquelle et qui la fournit ;
   - **À écarter** : valeur faible, risque disproportionné ou besoin déjà couvert — écrire la raison.
10. **Recommander, puis s'arrêter sur la décision.** Recommander trois à cinq cas à faible effort et forte valeur,
    idéalement un par équipe concernée, et dire ce qui ferait changer cette recommandation. À chaque validation
    (`00`, `01`, `02`), ajouter une ligne à `mission/journal.md`. Proposer ensuite `chiffrer-rentabilite` (ordre de
    grandeur → `03-chiffrage.md`), `planifier-deploiement` (feuille de route → `04-feuille-de-route.md`), puis
    `cadrer-besoin` pour chaque cas retenu, depuis sa fiche.

## Le livrable

Trois documents dans `mission/`. Modèle de `00-contexte.md` :

```markdown
# Contexte — <entreprise ou périmètre>

Date · Demandeur (rôle) · Rédigé par

## 1. Fiche entreprise
Activité · taille et équipes concernées (rôles) · outils en place · données disponibles et où elles
vivent · objectifs · contraintes (sécurité, conformité, budget, calendrier) · ce qui a été essayé.

## 2. Sources branchées et autorisations obtenues
| Source | Nature (fichier, outil connecté, entretien, observation) | Date | Autorisation (qui, quand, périmètre) |

## 3. Sources manquantes
Ce qui manque, ce que cela empêche de conclure, qui peut le fournir.

## Décision attendue
Confirmer les sources à brancher et les équipes à écouter — ou les corriger.
```

Modèle de `01-cartographie-taches.md` :

```markdown
# Cartographie des tâches — <périmètre>

## 1. Les tâches
| Équipe | Tâche | Déclencheur | Fréquence | Durée par occurrence | Volume | Outils | Données | Passages entre équipes | Erreurs / reprises | Stabilité des règles | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Finance | Relancer les factures échues (exemple fictif) | échéance dépassée | 4 fois par mois `[H]` | 10 min `[H]` | 30 relances `[F]` | tableur, courriel | factures, coordonnées | vente → finance | relances en double `[H]` | règles écrites `[F]` | entretien finance ; export |

## 2. Le tri
| Tâche | Issue | Fréquence | Coût | Valeur | Risque si ça se trompe | Pourquoi cette issue |

## Décision attendue
Confirmer que la cartographie ressemble au travail réel, que les équipes s'y reconnaissent et que le tri tient — ou le corriger.
```

Modèle de `02-portefeuille.md` :

```markdown
# Portefeuille de cas d'usage — <périmètre>

## 1. Vue d'ensemble
| Cas | Équipe(s) | Valeur (gain mensuel `[E]`) | Facilité | Risque | Classe (raison si « À écarter ») |

## 2. Fiches
### <Nom du cas> — <classe>
- **Résultat** : une phrase.
- **Pour qui** : rôle.
- **Problème** : une phrase.
- **Déclencheur** : l'événement qui lance le processus.
- **Entrées** : 3 à 6 données ou objets.
- **Ce que fait le système** : 3 à 7 étapes.
- **Sorties** : 1 à 4 résultats, dans l'outil métier.
- **Valeur** : temps, revenu, coût, risque ou qualité ; gain mensuel `[E]` avec son calcul.
- **Limites et validation humaine** : cas ambigus, qui valide, contraintes.
- **Preuve** : observé (ligne de `01`, source) · déclaré · hypothèse `[H]` (qui peut la confirmer).
- **Déjà disponible** : outil en place, modèle, brique du marché, rien.

## Recommandation et décision attendue
À éliminer d'abord, sans IA : les tâches triées « Éliminer », et qui peut décider de les supprimer.
Trois à cinq cas à faible effort et forte valeur, idéalement un par équipe. Ce qui ferait changer
cette recommandation : … Quels cas creuser : pour chacun, creuser, mettre en attente ou écarter.
```

Ligne de journal, au moment où le décideur tranche (une par document validé) :

```markdown
- 2026-10-07 · découverte · 02-portefeuille validé par la direction générale · « on creuse trois cas : relances de factures, tri du support, comptes rendus de rendez-vous »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Quatre issues, « Éliminer » en tête | beaucoup de gains rapides n'exigent aucune technologie, et automatiser une mauvaise habitude la fige | ne chercher que ce qui est automatisable | l'entreprise vient de simplifier ses processus : « Éliminer » peut rester vide, on l'écrit |
| Cartographier des tâches, pas des postes ni des personnes | une carte de personnes se lit comme une évaluation et fait cacher les contournements | un organigramme noté « potentiel IA » par poste | jamais |
| Observation et entretiens plutôt qu'un questionnaire général | chacun décrit la procédure, pas ses contournements | un formulaire envoyé à tous les salariés | l'enregistrement est refusé ou impossible : entretiens seuls, durées et volumes en `[H]` |
| Ordre de grandeur, pas de business case | classer demande de comparer, pas de promettre ; le détail appartient à `chiffrer-rentabilite` | un business case complet par cas dès la découverte | un seul cas intéresse la direction : la porte « besoin connu » le chiffre |
| Trois à cinq cas recommandés | une liste courte se décide, et chaque équipe voit un gain proche | classer et défendre tous les cas trouvés | la direction veut une couverture exhaustive : le portefeuille reste long, la recommandation reste courte |

## Frontières

- Un processus nommé en une phrase, un besoin exprimé → `cadrer-besoin` (porte « besoin connu »), puis le détail du
  processus : étapes, mesures, causes → `auditer-processus`.
- L'ordre de grandeur des gains et des coûts → `chiffrer-rentabilite` ; l'ordre de mise en œuvre →
  `planifier-deploiement` ; les exigences et la comparaison de solutions d'un cas → `rediger-cahier-des-charges`,
  `concevoir-solution`. L'état de la mission et le journal des décisions → `router-mission-ia`.
- Facultatif : les outils connectés à la session (documents, messagerie, tickets, CRM) ne servent qu'en lecture ; ne
  dire qu'on a lu une source que si l'outil a réellement été appelé.

## Preuves restantes

- Éprouvée sur la mission fictive de `examples/`.
- NON MESURÉ sur une mission réelle : le premier cas réel dira si les douze colonnes suffisent, si le tri en quatre
  issues est assez fin et si trois à cinq cas est le bon nombre.
- Sources et crédits : la forme de l'entretien s'inspire de `smb-onboard`, plugin `small-business` d'Anthropic
  (Apache-2.0, https://github.com/anthropics/knowledge-work-plugins). Méthode réécrite, aucun passage repris.
