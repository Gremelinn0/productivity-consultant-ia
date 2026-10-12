---
name: auditer-processus
description: >-
  Quand un besoin est cadré et qu'il faut comprendre comment le travail se fait vraiment avant de
  décider quoi que ce soit (« comment ça se passe aujourd'hui ? », « où perd-on du temps ? », « est-ce
  prêt à être automatisé ? ») → décrire le processus actuel, le mesurer, trouver goulets et
  gaspillages, remonter à des causes sur lesquelles on peut agir, tester sa stabilité, trier chaque
  étape (éliminer, automatiser, déléguer à l'IA, garder) et fixer ce qu'il faut simplifier ou
  standardiser avant toute automatisation. Deuxième étape de la porte « besoin connu » du pack
  consultant-ia, après cadrer-besoin ; alimente rediger-cahier-des-charges (mode exigences).
  Triggers : « audit de processus », « cartographier le processus », « process mapping », « où
  perd-on du temps », « goulet d'étranglement », « avant d'automatiser », « le processus est-il
  stable », « process audit ».
metadata:
  scope: "un processus nommé et cadré, de la description de l'existant au diagnostic, avant tout choix de solution"
  owns: "le diagnostic : carte du processus actuel, mesures, goulets, causes, test de stabilité, tri par étape, simplifications à faire d'abord, opportunités classées"
  consumes: "mission/cas-<slug>/10-besoin.md ; mission/sources/ ; la fiche du cas dans mission/02-portefeuille.md et ses lignes de 01-cartographie-taches.md ; les réponses des personnes qui font le travail"
---

# Auditer le processus

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/20-diagnostic.md`. Preuve : le demandeur valide
> les causes à traiter et les simplifications à faire avant toute automatisation, et la décision
> s'inscrit dans `mission/journal.md`. Contrôle de forme : le diagnostic porte ses neuf rubriques, chaque
> étape a son issue, chaque nombre son statut `[F]`, `[H]` ou `[E]`. Exemple de référence : `examples/`
> du pack. **Boucle** : aucune.

## Ce que cette compétence résout

Une fiche besoin dit ce qu'on veut obtenir ; elle ne dit pas comment le travail se fait aujourd'hui. Un processus
décrit de mémoire donne la version théorique, celle des procédures, pas celle des contournements — or c'est le
travail réel qu'il faudra transformer. Automatiser la version théorique construit un outil qui ne colle pas au
travail ; automatiser un processus instable donne un chaos automatisé, avec une facture de maintenance.

Cette compétence décrit le processus tel qu'il se déroule, le mesure, repère où le temps et la qualité se perdent,
remonte aux causes, et dit ce qu'il faut supprimer, simplifier ou standardiser avant de penser à automatiser.
Résultat attendu : un diagnostic qui permet de décider quelles causes traiter et quelles simplifications faire
d'abord.

## Stratégie

1. **Observer plutôt que se faire raconter.** L'enregistrement d'une personne qui fait la tâche (vidéo ou partage
   d'écran, avec son accord) montre ce qu'on omet par habitude : contrôles informels, copier-coller, fichiers « à
   côté ». Ces contournements sont l'information ; aucune procédure écrite ne les contient.
2. **Mesurer avant de changer.** Sans point de départ, aucun gain ne se démontre. Chaque nombre porte son statut ;
   ce qui n'est pas mesuré se dit, avec le moyen de le mesurer.
3. **Chercher des causes, pas des coupables.** On demande « pourquoi » jusqu'à une cause sur laquelle on peut agir,
   et on nomme sa nature (processus, organisation, donnée ou outil) : elle dit qui peut agir. Les personnes ne sont
   jamais jugées ; on écrit des rôles.
4. **Tester la stabilité avant de parler d'automatisation.** Si trois personnes font la tâche de trois façons, ou si
   les règles ne sont écrites nulle part, on standardise d'abord : automatiser le chaos donne un chaos automatisé.
5. **Supprimer, simplifier, standardiser — puis automatiser.** Les simplifications passent avant les
   automatisations, même quand leur gain est plus petit : elles conditionnent le reste.
6. **Un diagnostic n'est pas une solution.** On classe des opportunités, on ne choisit pas l'outil : la comparaison
   des options appartient à `concevoir-solution`, qui doit pouvoir conclure qu'il ne faut rien construire.

## Étapes

1. **Lire ce qui existe** : `10-besoin.md` (périmètre, critères de succès, mesures de départ connues),
   `mission/sources/` et, si le cas vient de la porte découverte, sa fiche dans `02-portefeuille.md` et ses lignes
   de `01-cartographie-taches.md`. Ne pas redemander ce qui s'y trouve.
2. **Choisir la source de la description**, par ordre de préférence : l'enregistrement d'une personne qui fait
   réellement la tâche (transcription déposée dans `mission/sources/`, protocole dans `decouvrir-cas-usage`) ; un
   entretien sur la dernière occurrence réelle (« la dernière fois que… ») ; une procédure écrite, notée `[H]`
   « théorique » tant qu'elle n'est pas confrontée au réel. Observer deux personnes quand c'est possible : leurs
   écarts nourrissent le test de stabilité.
3. **Décrire le processus** : étapes (un verbe, un objet), rôle, outil, entrées et sorties, passages de main,
   attentes, points de décision, exceptions. Ajouter un schéma Mermaid si le flux comporte des branches. Faire
   relire la description par une personne qui fait le travail, pas seulement par son responsable.
4. **Mesurer** : volume, fréquence, temps par étape, délai total comparé au temps de travail effectif, taux d'erreur
   ou de reprise (part des occurrences qui reviennent à une étape précédente), temps d'attente. Séparer cas simples
   et cas complexes : une moyenne cache la variabilité. Si rien n'est mesuré, écrire comment le faire — chronométrer
   un échantillon d'occurrences, compter pendant une semaine, demander un export. Cette mesure de départ précède
   tout changement.
5. **Repérer goulets et gaspillages** : ressaisie, copier-coller entre outils, attente de validation, contrôles en
   double, recherche d'information, rapports manuels, exceptions traitées au cas par cas. Les situer sur une étape
   et leur donner un coût `[E]` quand les mesures le permettent. Un délai fait d'attente ne se réduit pas en
   automatisant le travail qui l'entoure.
6. **Remonter aux causes** : demander « pourquoi » jusqu'à une cause sur laquelle quelqu'un peut agir, puis
   l'étiqueter processus, organisation, donnée ou outil. Une cause d'organisation (« personne ne tient la liste »)
   ne se règle pas avec un outil.
7. **Tester la stabilité** avec les quatre questions de la rubrique 5. Une réponse négative ne bloque pas le
   diagnostic : elle fait de la standardisation la première opportunité — écrire la procédure unique, la tester à la
   main sur quelques occurrences, re-mesurer, puis seulement automatiser.
8. **Trier chaque étape en quatre issues**, avec les critères de la découverte (fréquence, coût, valeur, risque si
   ça se trompe) :
   - **Éliminer** : prend du temps, apporte peu, personne ne remarquerait sa disparition ;
   - **Automatiser** : même schéma à chaque fois, relie plusieurs outils, règles stables ;
   - **Déléguer à l'IA** : processus clair, résultat contrôlable ; l'IA prépare ou exécute, un humain valide si
     nécessaire ;
   - **Garder** : jugement, relation, négociation, décision importante ; l'IA peut préparer, comparer, challenger,
     sans porter la responsabilité.

   Pas de « Automatiser » si le test de stabilité est négatif. Une étape irréversible ou à fort impact (envoi vers
   l'extérieur, paiement, suppression, décision sur une personne) reste sous validation humaine : l'automatisation
   prépare, un humain valide.
9. **Poser les huit questions d'automatisation qui manquent**, en une seule fois, après avoir cherché la réponse
   dans le besoin, les sources et l'observation :
   1. Quel événement déclenche le processus, et quel résultat doit-il produire ?
   2. Quelles étapes sont stables et répétitives, lesquelles exigent une décision humaine ?
   3. Quels systèmes, comptes et droits faut-il lire ou modifier ?
   4. Quel volume, quelle fréquence, quel niveau de criticité ?
   5. Quelles erreurs sont acceptables, lesquelles doivent bloquer, et qui alerter ?
   6. Quelles données sensibles, règles de conformité ou validations humaines doivent encadrer l'IA ?
   7. Quel cas limite doit absolument fonctionner avant de généraliser ?
   8. Qui maintiendra automatisations, prompts, modèles et accès après livraison ?

   Une réponse manquante devient une hypothèse `[H]` avec la personne qui peut la confirmer. Ces réponses sont
   l'entrée de `rediger-cahier-des-charges` (mode exigences).
10. **Classer les opportunités.** Chaque opportunité (supprimer, simplifier, standardiser, configurer un outil déjà
    en place, automatiser, déléguer à l'IA) reçoit une valeur (gain mensuel `[E]` tiré des mesures de l'étape 4),
    une facilité (données disponibles, règles stables, accès aux outils, peu d'exceptions) et un risque, notés haut,
    moyen ou bas avec une raison d'une ligne, puis une classe :
    - **Gains rapides** : valeur notable, facilité haute, risque bas ou couvert par une validation ;
    - **Projets** : valeur haute mais facilité moyenne ou basse, ou risque qui impose des garde-fous ;
    - **À creuser** : une donnée manquante empêche de classer — écrire laquelle et qui la fournit ;
    - **À écarter** : valeur faible, risque disproportionné ou besoin déjà couvert — écrire la raison.
11. **Rédiger, puis s'arrêter sur la décision.** Remplir le modèle et finir par la décision attendue. Quand le
    demandeur valide, ajouter une ligne à `mission/journal.md`, puis proposer `rediger-cahier-des-charges` en mode
    exigences.

## Le livrable

Modèle de `mission/cas-<slug>/20-diagnostic.md` :

```markdown
# Diagnostic — <processus>

Date · Demandeur (rôle) · Rédigé par · Source de la description : observation, entretien ou procédure

## 1. Le processus tel qu'il se fait
| Étape | Rôle | Outil | Entrées | Sorties | Passage de main ou attente | Décision ou exception |

Schéma Mermaid facultatif. Dire quelle source a servi, en rôles.

## 2. Mesures
| Mesure | Valeur | Statut | Source, ou comment la mesurer |
|---|---|---|---|
| Volume (exemple fictif) | 120 dossiers par mois | `[H]` | responsable de l'équipe ; à confirmer par un export |

À mesurer : volume · fréquence · temps par étape · délai total · taux d'erreur ou de reprise · temps d'attente.
Statuts : `[F]` fait observé, avec sa source · `[H]` hypothèse, avec qui peut la confirmer · `[E]` estimation calculée.

## 3. Goulets et gaspillages
| Étape | Nature (ressaisie, attente, double contrôle…) | Effet | Coût `[E]` |

## 4. Causes
| Goulet | Pourquoi (la chaîne) | Cause actionnable | Nature : processus, organisation, donnée ou outil |

## 5. Stabilité
| Question | Réponse | Source |
|---|---|---|
| Le processus se fait-il pareil à chaque fois ? | | |
| Les règles de décision sont-elles écrites ? | | |
| Deux personnes ou plus le font-elles de la même façon ? | | |
| Les étapes, les outils ou les règles vont-ils changer bientôt ? | | |

Verdict : stable (le tri peut conclure à l'automatisation) ou à standardiser d'abord.

## 6. Tri des étapes
| Étape | Issue | Pourquoi | Garde-fou ou validation humaine |

## 7. À simplifier et à standardiser d'abord
Liste ordonnée, avant toute automatisation : ce qu'on supprime, ce qu'on simplifie, ce qu'on écrit comme
procédure unique. Pour chacun : l'effet attendu `[E]` et la mesure qui le vérifiera.

## 8. Les huit questions d'automatisation
| Question | Réponse | Statut |

## 9. Opportunités classées
| Opportunité | Valeur (gain mensuel `[E]`) | Facilité | Risque | Classe |

## Décision attendue
Choisir les causes à traiter et les simplifications à faire avant toute automatisation — ou les corriger.
```

Ligne de journal, au moment où le demandeur tranche :

```markdown
- 2026-10-21 · cas-relances-factures · 20-diagnostic validé par la direction financière · « on supprime le double contrôle, puis on écrit la procédure unique avant d'automatiser »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Observer d'abord, interroger ensuite | un processus décrit de mémoire est la version théorique ; les contournements n'apparaissent qu'à l'écran | un questionnaire adressé au responsable | personne ne peut être enregistré ou le cas est trop rare : entretien sur la dernière occurrence, nombres en `[H]` |
| Mesure de départ avant toute recommandation | sans point de départ, aucun gain ne se démontre | estimer d'abord, mesurer plus tard | le processus est trop rare pour un échantillon : estimation assumée, marquée `[H]` |
| Test de stabilité avant tout « Automatiser » | automatiser un processus instable fige le chaos et coûte en maintenance | automatiser puis corriger | l'entreprise impose l'automatisation : le risque est écrit dans le diagnostic, la décision est la sienne |
| Causes classées par nature (processus, organisation, donnée, outil) | la nature dicte qui peut agir ; un problème de donnée ne se règle pas par un outil | une liste plate de problèmes | jamais |
| Huit questions posées seulement quand elles manquent | ne pas redemander ce que le besoin ou les sources disent | un questionnaire complet et systématique | le besoin vient d'une source pauvre : les huit passent en questions ouvertes |
| Le diagnostic classe, il ne choisit pas l'outil | choisir ici fermerait les options avant leur comparaison | proposer l'outil dès l'audit | jamais : la comparaison appartient à `concevoir-solution` |

## Frontières

- Le besoin, son périmètre et ses critères de succès → `cadrer-besoin`. Aucun besoin nommé → `decouvrir-cas-usage`.
- Les exigences que la solution doit satisfaire → `rediger-cahier-des-charges` (mode exigences), qui reçoit ce
  diagnostic.
- La décision d'automatiser, la comparaison d'options et le choix d'une plateforme → `concevoir-solution`.
- Le gain et le coût → `chiffrer-rentabilite` ; le calendrier → `planifier-deploiement`.
- L'état de la mission et le journal des décisions → `router-mission-ia`.
- Facultatif : si les compétences `process-optimization` et `process-doc` (plugin `operations`) ou
  `automation-strategy` sont installées, elles peuvent servir de contre-lecture. Ne dire qu'on les a utilisées que
  si elles ont réellement été appelées.

## Preuves restantes

- Éprouvée sur la mission fictive de `examples/`.
- NON MESURÉ sur une mission réelle : le premier cas réel dira si le diagnostic reste lisible quand le processus
  compte beaucoup d'étapes, si le test de stabilité à quatre questions suffit et si les neuf rubriques sont toutes
  utiles.
- Sources et crédits : la description du processus et l'analyse des gaspillages s'inspirent de
  `process-optimization` et `process-doc`, plugin `operations` d'Anthropic (Apache-2.0,
  https://github.com/anthropics/knowledge-work-plugins) ; le test de stabilité et le garde-fou humain s'inspirent de
  `automation-strategy` d'Eric Risco (MIT, https://github.com/ericrisco/rsc-harness). Méthode réécrite avec nos
  mots, aucun passage repris.
