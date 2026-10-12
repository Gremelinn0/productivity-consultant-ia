---
name: planifier-deploiement
description: >-
  Quand des cas d'usage sont retenus et qu'il faut dire par où commencer ou comment les mettre en
  service (« par quoi on commence ? », « quelle feuille de route ? », « comment on le déploie et on
  s'assure que l'équipe s'en sert ? ») → ordonner un portefeuille en feuille de route (valeur,
  facilité, risque, prérequis, jalons) ou détailler un cas en plan de déploiement (lots courts,
  pilote, recette, adoption, exploitation, mesure), puis le soumettre à un pré-mortem avant de
  s'engager. Dernière étape des deux portes du pack consultant-ia, après le chiffrage. Triggers :
  « feuille de route », « roadmap », « plan de déploiement », « plan de mise en œuvre », « par où
  commencer », « pilote », « mise en production », « conduite du changement », « adoption »,
  « pré-mortem », « rollout plan », « change management ».
metadata:
  scope: "l'ordre de mise en œuvre d'un portefeuille de cas retenus, ou le chemin d'un cas spécifié jusqu'à un dispositif utilisé, entretenu et mesuré"
  owns: "la feuille de route (priorités, ordre, prérequis, dépendances, responsables par rôle, jalons, indicateurs), le plan de déploiement (lots, pilote, recette, mise en production, adoption, exploitation, revue des indicateurs, communication) et le pré-mortem"
  consumes: "mission/00-contexte.md, 02-portefeuille.md et 03-chiffrage.md (feuille de route) ; mission/cas-<slug>/20-diagnostic.md, 30-exigences.md, 40-solutions.md, 50-rentabilite.md et 60-specification.md (plan de déploiement) ; mission/sources/"
---

# Planifier le déploiement

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/04-feuille-de-route.md` (portefeuille) ou
> `mission/cas-<slug>/70-plan.md` (un cas). Preuve : le décideur valide le plan et le lancement du
> premier lot — ou de la feuille de route et des premiers cas — et la décision s'inscrit dans
> `mission/journal.md`. Contrôle de forme : le modèle est complet (cinq rubriques pour la feuille de
> route, huit pour le plan), chaque lot compte trois à six étapes vérifiables, les six questions
> d'adoption ont une réponse ou un `?`, le pré-mortem rend un verdict, chaque nombre a son statut
> `[F]`, `[H]` ou `[E]`. Exemple de référence : `examples/` du pack. **Boucle** : aucune.

## Ce que cette compétence résout

Une bonne solution ne se déploie pas toute seule : un dispositif que personne ne reprend, que
l'équipe contourne ou que rien ne mesure devient un coût. Cette compétence ordonne d'abord les cas
retenus pour que les premiers réussissent vite et visiblement, puis décrit, pour chaque cas, le
chemin jusqu'à un dispositif utilisé, entretenu et mesuré.

Deux modes : la **feuille de route** (porte « aucun besoin ») ordonne un portefeuille, le **plan de
déploiement** (porte « besoin connu ») détaille un cas spécifié ; un pré-mortem attaque chacun.

Résultat attendu : un plan que le décideur peut valider et lancer — premier lot ou premiers cas —,
avec ce qu'on ne fait pas et ce qui arrêterait le projet.

## Stratégie

1. **Commencer petit, là où la valeur est forte et l'effort faible.** Trois à cinq cas pour la
   première vague, idéalement un par équipe : des résultats visibles tôt légitiment la suite, et
   chaque équipe compte une personne qui a vu le dispositif marcher.
2. **Ordonner par valeur, facilité et risque, pas par insistance.** L'ordre devient explicable : on
   peut dire pourquoi un cas passe avant un autre.
3. **Les prérequis avant le calendrier.** Une donnée absente, un accès à ouvrir, un processus à
   standardiser sont des tâches de la feuille de route, avec responsable et date, pas des retards.
4. **Un indicateur que l'entreprise suit déjà** pour chaque cas de la feuille de route (délai, volume,
   taux d'erreur, satisfaction) : pas de tableau de bord à bâtir, et la mesure de départ existe.
5. **Dire ce qu'on ne fait pas, avec la raison.** Un item qu'on ne nomme pas revient à chaque réunion.
6. **Des lots courts, dont chaque étape se vérifie.** Trois à six étapes ; chacune dit ce que le
   lecteur constate, sans avoir à croire l'auteur. Le plan ne déclare rien « fait » : l'avancement se
   lit sur les preuves.
7. **Casser le plan avant de s'y engager.** Le pré-mortem tient l'échec pour acquis et en cherche les
   causes, au moment le moins cher pour changer de direction. Un modèle de langage approuve volontiers
   ce qu'on lui soumet : il faut lui demander explicitement de démolir.

## Étapes

1. **Choisir le mode et lire ce qui existe.** `02-portefeuille.md` et `03-chiffrage.md` présents, des
   cas retenus sans ordre → feuille de route (lire aussi `00-contexte.md`). `60-specification.md`
   d'un cas présent → plan de ce cas (lire aussi `30-exigences.md`, `40-solutions.md` : condition
   d'arrêt et repli, `50-rentabilite.md` : hypothèses `[H]`, mesure de départ, maintenance
   supposée). La spécification définit déjà recette, critères de pilote, indicateurs (identifiants,
   seuils) et propriétaire de la maintenance : le plan les reprend sans les réécrire et y ajoute
   dates, responsables, rythme de revue et actions aux seuils. En cas d'écart avec la feuille de
   route, c'est elle qu'on corrige.
2. **Feuille de route — noter, choisir, ordonner.** Reprendre la facilité et le risque de
   `02-portefeuille.md` (haut / moyen / bas, avec leur raison) et la valeur de `03-chiffrage.md`
   (gain net central et fourchette) ; combler ce qui manque. Choisir trois à cinq premiers cas, forte
   valeur et faible effort (les « gains rapides »), idéalement un par équipe ; s'il n'y en a pas trois,
   le dire et commencer par le prérequis qui en débloque. Ordonner en vagues avec prérequis,
   dépendances, responsable par rôle, jalon et indicateur métier déjà suivi (mesure de départ
   comprise), puis écrire ce qu'on ne fait pas maintenant et la condition pour le rouvrir.
3. **Plan — lots et pilote.** Lots courts de trois à six étapes vérifiables, avec « ce qu'on ne fait
   pas dans ce lot » ; au-delà de six, scinder ; le premier lot relève la mesure de départ et lève
   les prérequis. Pilote : périmètre réduit (qui, quel volume), dates, critères de poursuite et d'arrêt
   repris de la spécification, hypothèses `[H]` de `50-rentabilite.md` à confirmer, décideur de la
   suite — continuer, corriger ou arrêter —, le tout écrit avant de commencer.
4. **Plan — recette et mise en production.** Tests et critères d'acceptation repris de
   `60-specification.md` ; le plan ajoute le côté humain : qui recette, sur des données réelles ou
   fidèlement reconstituées ; quel jour et dans quel ordre on bascule (progressivement ou d'un bloc) ;
   qui déclenche le retour arrière, sur quel signal, et comment on vérifie que l'ancienne méthode a
   repris.
5. **Plan — adoption et exploitation.** Répondre aux six questions de la rubrique 4 du modèle, ou les
   marquer `?` avec le rôle qui doit trancher. Propriétaire et suppléant (cf. spécification) ; heures de
   maintenance cohérentes avec `50-rentabilite.md` ; procédure d'une page, essayée par quelqu'un qui
   ne l'a pas écrite ; alerte sur l'échec et sur le silence ; comptes de l'entreprise, non personnels.
6. **Plan — protocole de mesure et communication.** Reprendre chaque indicateur de la spécification
   par son identifiant, sans redéfinir ses seuils, et fixer ce qui revient au plan : qui le relit
   (rôle), à quel rythme, et l'action déclenchée à chaque seuil — correction, alerte, arrêt avec
   retour arrière. Communication : qui est informé de quoi et quand, le pourquoi avant le quoi, en
   disant aussi ce qui disparaît avec l'ancienne méthode.
7. **Pré-mortem, dans les deux modes.** Écrire la thèse en une phrase falsifiable, puis : « dans six
   mois, ce projet a échoué : racontez pourquoi ». Raconter les histoires d'échec plausibles
   (adoption, qualité des données, processus qui change, outil ou fournisseur qui change, dérive des
   coûts, panne silencieuse, départ du responsable), chacune avec son signal d'alerte précoce, sa
   parade et sa condition d'arrêt (partir de celle de `40-solutions.md`). Classer les objections :
   bloquante, à mitiger, écartée mais nommée. Verdict : **engager**, **durcir** (parades intégrées)
   ou **pivoter** (un bloquant réel). Ouvrir `references/pre-mortem.md` pour le déroulé, les familles
   d'échec et le gabarit.
8. **Relire, puis finir par la décision attendue.** Toute formule en suspens (« on verra », « à
   définir ») devient une action, une hypothèse `[H]` avec son confirmateur, ou une question dans
   « Décision attendue ». Suite : chaque cas de la feuille de route entre par `cadrer-besoin`, le plan
   se lance par son premier lot. Quand le décideur tranche, ajouter une ligne à `mission/journal.md`.

## Le livrable

Modèle de `mission/04-feuille-de-route.md` (portefeuille, porte « aucun besoin ») :

```markdown
# Feuille de route — <entreprise ou périmètre>

Date · Décideur (rôle) · Rédigé par · Sources : 02-portefeuille, 03-chiffrage

## 1. Les cas, notés
| Cas | Équipe | Valeur (gain net central, fourchette) `[E]` | Facilité | Risque | Rang |
Principe d'ordre en une phrase : ce qui fait passer un cas avant un autre, et combien démarrent ensemble.

## 2. La séquence
| Vague | Cas | Prérequis | Dépend de | Responsable (rôle) | Jalon `[H]` | Indicateur déjà suivi · mesure de départ |

## 3. Prérequis à lever d'abord
Ce qui manque (donnée, accès, processus à standardiser), pour quels cas, qui le lève, pour quelle date.

## 4. Ce qu'on ne fait pas maintenant
| Cas ou chantier | Pourquoi pas maintenant | Se rouvre si |

## 5. Pré-mortem
Thèse · histoires d'échec retenues · signaux d'alerte · conditions d'arrêt · verdict.

## Décision attendue
Valider l'ordre, les cas de la première vague et leurs responsables, puis lancer le premier cas : il
entre par `cadrer-besoin`.
```

Modèle de `mission/cas-<slug>/70-plan.md` (plan de déploiement, porte « besoin connu ») :

```markdown
# Plan de déploiement — <titre court du cas>

Date · Responsable du cas (rôle) · Rédigé par · Sources : 30-exigences, 50-rentabilite, 60-specification

## 1. Objectif et critères de réussite
Repris du besoin et des exigences, avec leur mesure de départ.

## 2. Lots
### Lot 1 — <nom> (durée `[H]`)
| # | Étape | Responsable (rôle) | Preuve que c'est fait | Dépend de |
Ce qu'on ne fait pas dans ce lot : …

## 3. Pilote, recette et mise en production
Pilote : périmètre · dates · critères de poursuite et d'arrêt (de la spécification) · hypothèses `[H]`
à confirmer · décideur de la suite. Recette : qui accepte, sur quelles données. Mise en production :
jour et ordre de bascule · retour arrière (qui, signal, vérification) · interrupteur.

## 4. Adoption (une réponse, un rôle, une échéance par question — ou `?`)
1. Qui reprendra le dispositif, avec quel niveau d'autonomie ?
2. Quels gestes l'équipe doit-elle savoir faire sans le consultant ?
3. Quels rôles ont besoin d'une formation, d'un guide, d'une vidéo ou d'une documentation technique ?
4. Quels accès, propriétaires de comptes et procédures de secours faut-il transmettre ?
5. Comment vérifier que l'équipe a compris et sait corriger une erreur courante ?
6. Quel support après la transmission, et qu'est-ce qui relève d'une nouvelle mission ?

## 5. Exploitation
Propriétaire et suppléant (rôles, de la spécification) · maintenance : qui, rythme, heures `[H]` · procédure d'une page · comptes et accès à transmettre · alertes.

## 6. Protocole de mesure (indicateurs et seuils définis dans la spécification, rubrique 14)
| Indicateur (identifiant de 60-specification) | Relu par (rôle) | Rythme de la revue | Action au seuil de correction | Action au seuil d'alerte | Action au seuil d'arrêt |

## 7. Communication
| Public | Message (le pourquoi d'abord) | Canal | Moment |

## 8. Pré-mortem
Thèse · histoires d'échec retenues · signaux · parades · conditions d'arrêt · verdict · version durcie.

## Décision attendue
Valider le plan et lancer le premier lot.
```

Lignes de journal, au moment où le décideur tranche :

```markdown
- 2026-11-04 · découverte · 04-feuille-de-route validée par le comité de direction · « première vague : un cas par équipe ; le cas des achats attend la donnée fournisseurs »
- 2026-11-18 · cas-saisie-commandes · 70-plan validé par la direction commerciale · « pilote sur une équipe, arrêt si l'adoption reste sous le seuil convenu »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Trois à cinq cas pour la première vague | des résultats visibles tôt valent plus qu'une couverture large ; au-delà, rien ne se termine | lancer tout le portefeuille d'un coup | l'entreprise a les équipes et les prérequis pour mener davantage de cas en parallèle |
| Critères du pilote, indicateurs et seuils repris de la spécification par leur identifiant ; décision de continuer ou d'arrêter écrite avant de commencer | deux jeux de critères ou de seuils finissent par diverger, et une décision prise après coup se prend sur l'enthousiasme | réécrire critères et seuils dans le plan, ou un pilote sans critères | jamais : sans critères écrits, ce n'est pas un pilote |
| Le pré-mortem fait partie du plan, dans les deux modes | c'est le moment le moins cher pour changer de direction | un pré-mortem seulement sur demande | le plan tient en un lot réversible sans effet sur d'autres équipes : une demi-page suffit |
| L'adoption se traite par six questions, pas par un programme de conduite du changement | une équipe qui reprend le dispositif a besoin de réponses concrètes ; un programme complet dépasse la mission | un volet conduite du changement détaillé | le déploiement touche une grande partie de l'entreprise : on le propose comme mission distincte |

## Frontières

- Gains, coûts et hypothèses `[H]` à confirmer → `chiffrer-rentabilite` (le plan les reprend, il ne les
  recalcule pas). Tri et portefeuille → `decouvrir-cas-usage` ; chaque cas lancé →
  `cadrer-besoin`.
- Exigences et spécification (recette, critères de pilote, indicateurs et seuils, propriétaire de la
  maintenance) → `rediger-cahier-des-charges` ; choix de l'option → `concevoir-solution` ; processus
  actuel et ses mesures → `auditer-processus` ; état de la mission et journal → `router-mission-ia`.
- Construire, installer, former et mesurer à la place de l'entreprise : hors du pack.
- Facultatif, s'ils sont installés : `change-request` et `runbook` (plugin `operations`) pour mettre
  en forme les rubriques 3 et 5 ; `router-consulting-strategy` pour le contre-cas d'une feuille de
  route stratégique. Ne dire qu'on les a utilisés que s'ils ont réellement été appelés.

## Preuves restantes

- Éprouvée sur la mission fictive de `examples/` (les deux modes).
- NON MESURÉ sur une mission réelle : le premier déploiement dira si trois à six étapes par lot et
  six questions d'adoption suffisent, et si le pré-mortem nomme les échecs qui surviennent vraiment.
  Le pack ne relit pas le protocole de mesure après déploiement : c'est l'entreprise qui mesure.
- Sources et crédits : pré-mortem, méthode de Gary Klein (« Performing a Project Premortem », Harvard
  Business Review, 2007), écriture individuelle avant partage et relance aux jalons adaptées de gcamilo,
  « management-consulting » (MIT, https://github.com/gcamilo/management-consulting) ; retour arrière,
  communication et procédure d'exploitation inspirés de `change-request` et `runbook`, plugin
  `operations` d'Anthropic (Apache-2.0, https://github.com/anthropics/knowledge-work-plugins) ;
  propriétaire nommé, interrupteur, alerte sur le silence, comptes non personnels adaptés d'Eric Risco,
  « automation-strategy » (MIT, https://github.com/ericrisco/rsc-harness).
