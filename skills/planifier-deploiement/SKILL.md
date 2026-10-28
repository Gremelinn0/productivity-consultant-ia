---
name: planifier-deploiement
description: >-
  Quand des cas d'usage sont retenus et qu'il faut dire par où commencer ou comment les mettre en
  service (« par quoi on commence ? », « quelle feuille de route ? », « quel plan pour le déployer et
  s'assurer que l'équipe s'en sert ? ») → ordonner un portefeuille en feuille de route (valeur,
  facilité, risque, prérequis, socle commun, jalons, simplifications d'abord) ou détailler un cas en
  plan de déploiement (lots courts, porte, pilote, recette, adoption, exploitation, mesure), puis le
  soumettre à un pré-mortem avant de s'engager. Dernière étape de décision des deux portes du pack
  consultant-ia, après le chiffrage : le plan se lit avant de construire, et son exécution (pilote,
  bascule) est dans `piloter-mise-en-service`. Triggers : « feuille de route », « roadmap », « plan de
  déploiement », « plan de mise en œuvre », « par où commencer », « plan de pilote », « plan de mise en
  production », « plan d'adoption », « pré-mortem », « rollout plan », « change management plan ».
metadata:
  scope: "l'ordre de mise en œuvre d'un portefeuille de cas retenus, ou le chemin d'un cas spécifié jusqu'à un dispositif utilisé, entretenu et mesuré"
  owns: "la feuille de route (priorités, ordre, vague 0 des simplifications, prérequis, dépendances, responsables par rôle, jalons, indicateurs), le plan de déploiement (lots dont celui des simplifications, porte, pilote, recette, mise en production, adoption, exploitation, revue des indicateurs, communication) et le pré-mortem"
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
> d'adoption ont une réponse ou un `?`, le pré-mortem rend un verdict avec son compte, chaque nombre a
> son statut `[F]`, `[H]` ou `[E]` (définis dans `ARCHITECTURE.md`). Exemple de référence : `examples/` du
> pack. **Boucle** : aucune.

> ❓ **Une question pour l'entreprise sort de la base de questions** (`mener-entretien-ia/references/base-questions/`, un fichier par sujet ; ici essai-et-mise-en-service et transmission) :
> lire d'abord le bloc du sujet, ne poser que ce qui manque, puis y ranger ce qui manquait (`entretien.py ajouter`).

## Ce que cette compétence résout

Une bonne solution ne se déploie pas toute seule : un dispositif que personne ne reprend, que
l'équipe contourne ou que rien ne mesure devient un coût. Cette compétence ordonne d'abord les cas
retenus pour que les premiers réussissent vite et visiblement, puis décrit, pour chaque cas, le
chemin jusqu'à un dispositif utilisé, entretenu et mesuré. Quand la solution recommandée passe par une
porte (standardiser d'abord, construire ensuite), le plan des simplifications et le constat de la porte
sont les siens.

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
   standardiser sont des tâches de la feuille de route, avec responsable et date, pas des retards. Une
   simplification sans construction (supprimer, standardiser, vérifier) est une action de la vague 0, ou du
   premier lot du plan : responsable, date, pièce. Elle se décide au journal quand elle ne modifie aucun
   outil ; quand elle en modifie un, c'est une action `A-xx` de `piloter-mise-en-service`, validée à part.
4. **Un indicateur que l'entreprise suit déjà** pour chaque cas de la feuille de route (délai, volume,
   taux d'erreur, satisfaction) : pas de tableau de bord à bâtir, et la mesure de départ existe. Une action
   de la vague 0 n'en a pas toujours : on écrit « aucun indicateur suivi » et la mesure de départ de ce
   qu'on supprime.
5. **Dire ce qu'on ne fait pas, avec la raison.** Un item qu'on ne nomme pas revient à chaque réunion.
6. **Des lots courts, dont chaque étape se vérifie.** Trois à six étapes ; chacune dit ce que le
   lecteur constate, sans avoir à croire l'auteur. Le plan ne déclare rien « fait » : l'avancement se
   lit sur les preuves. Les dates et les durées sont des propositions `[H]` que le décideur confirme en
   validant.
7. **Citer, jamais recopier.** Le plan reprend les critères du pilote et les indicateurs `IND-xx` par leur
   identifiant (rubrique 13 de la spécification pour le pilote, rubrique 14 pour la production) : deux jeux de
   valeurs finissent par diverger. Les seuils du pilote et ceux de la production sont distincts, et le plan le dit.
8. **Casser le plan avant de s'y engager.** Le pré-mortem tient l'échec pour acquis et en cherche les
   causes, au moment le moins cher pour changer de direction. Un modèle de langage approuve volontiers
   ce qu'on lui soumet : il faut lui demander explicitement de démolir.

## Étapes

1. **Choisir le mode et lire ce qui existe.** `02-portefeuille.md` et `03-chiffrage.md` présents, des
   cas retenus sans ordre → feuille de route (lire aussi `00-contexte.md`). `60-specification.md`
   d'un cas présent → plan de ce cas (lire aussi `30-exigences.md`, `40-solutions.md` : porte, condition
   d'arrêt et repli, `50-rentabilite.md` : hypothèses `[H]`, mesure de départ, maintenance supposée). La
   spécification définit déjà recette, critères de pilote, indicateurs (identifiants, seuils) et propriétaire
   de la maintenance : le plan les reprend sans les réécrire et y ajoute dates, responsables, rythme de revue
   et actions aux seuils. Si la mise en plan révèle un trou ou un écart dans un livrable validé (une
   spécification muette sur un mode, une feuille de route qui contredit une valeur), on le corrige par une
   version datée et une ligne « correction » au journal (`ARCHITECTURE.md`), puis le plan cite le § et la
   version. Une échéance déjà passée à la date du plan se redate dans le plan, avec l'ancienne date : ce n'est
   pas une correction.
2. **Feuille de route — noter, choisir, ordonner.** Reprendre la facilité et le risque de
   `02-portefeuille.md` (haut / moyen / bas, avec leur raison ; un « à classer » reçoit sa note ici) et la
   valeur de `03-chiffrage.md` (gain net central et fourchette) ; combler ce qui manque. Mettre en vague 0 les
   actions sans construction (éliminer, simplifier, vérifier). Choisir trois à cinq premiers cas, forte valeur
   et faible effort (les « gains rapides »), idéalement un par équipe ; s'il n'y en a pas trois, le dire et
   commencer par le prérequis qui en débloque. Ordonner en vagues avec prérequis (un renvoi court à la
   rubrique 3, qui porte le détail daté), dépendances, responsable par rôle, jalon et indicateur métier déjà
   suivi (mesure de départ comprise), puis écrire ce qu'on ne fait pas maintenant et la condition pour le
   rouvrir. Écrire aussi le **socle commun** des cas retenus, en tête de la rubrique 3 : les plateformes
   retenues ou envisagées `[H]`, qui les exploite, les règles de sécurité communes (comptes, droits, secrets,
   lieu des données). Ce qui se lève une fois pour tous les cas ne se refait pas cas par cas.
3. **Plan — lots et pilote.** Lots courts de trois à six étapes vérifiables, avec « ce qu'on ne fait pas
   dans ce lot » ; au-delà de six, scinder. Le premier lot relève la mesure de départ, lève les prérequis et
   porte les simplifications du diagnostic (`20-diagnostic.md` §7), avec la re-mesure qui nourrit la porte.
   Quand plusieurs mesures et accords doivent précéder la porte, deux lots se chevauchent : le dire, et dire ce
   qui dépend des deux. Numéroter les étapes une fois pour tout le plan. Écrire la charge des personnes
   pendant les lots (heures par rôle, de `50-rentabilite.md`), en disant si les séances habituelles ou celles
   du pilote y sont comprises. Pilote : périmètre réduit (qui, quel volume), dates, critères de poursuite, de
   prolongation et d'arrêt cités de la spécification (rubrique 13) et signés sur une fiche avant de commencer,
   hypothèses `[H]` de `50-rentabilite.md` à confirmer, décideur de la suite — continuer, prolonger ou arrêter.
4. **Plan — porte, recette et mise en production.** La porte de `40-solutions.md` §10 devient une étape
   datée qui la constate : une fiche, une ligne par condition avec sa pièce, la mesure avec son agrégation
   (moyenne, minimum, chaque occurrence) telle que la solution l'a écrite, et ce qui se passe si une condition est
   « non » (la construction ne démarre pas, l'option 0 reste en place). Une décision sans livrable (porte
   constatée, fin de pilote, bascule) s'inscrit au journal avec sa pièce. Recette : tests et critères repris de
   `60-specification.md` ; le plan ajoute qui recette (pas celui qui construit), sur des données réelles ou
   fidèlement reconstituées. Mise en production : quel jour et dans quel ordre on bascule ; qui déclenche le
   retour arrière, sur quel signal, et comment on vérifie que l'ancienne méthode a repris. Le plan prévoit,
   il n'exécute pas : les actions, le feu vert et la bascule se tiennent dans `90-mise-en-service.md`.
5. **Plan — adoption et exploitation.** Répondre aux six questions de la rubrique 4 du modèle, ou les
   marquer `?` avec le rôle qui doit trancher. Propriétaire et suppléant (cf. spécification) ; heures de
   maintenance cohérentes avec `50-rentabilite.md` ; fiche d'une page, essayée par quelqu'un qui ne l'a pas
   écrite ; alerte sur l'échec et sur le silence ; comptes de l'entreprise, non personnels.
6. **Plan — protocole de mesure et communication.** Reprendre chaque `IND-xx` de la spécification par son
   identifiant, sans redéfinir ses seuils, et fixer ce qui revient au plan : qui le relit (rôle), à quel rythme,
   et l'action déclenchée à chaque seuil — correction, alerte, arrêt avec retour arrière. Pendant le pilote,
   l'arrêt est celui de la rubrique 13 ; après la bascule, celui de la rubrique 14. Communication : qui est
   informé de quoi et quand, le pourquoi avant le quoi, en disant aussi ce qui disparaît avec l'ancienne méthode.
7. **Pré-mortem, dans les deux modes.** Écrire la thèse en une phrase falsifiable, puis : « dans six
   mois, ce projet a échoué : racontez pourquoi ». Raconter les histoires d'échec plausibles
   (adoption, qualité des données, processus qui change, outil ou fournisseur qui change, dérive des
   coûts, panne silencieuse, départ du responsable), chacune avec son signal d'alerte précoce, sa
   parade et sa condition d'arrêt (partir de celle de `40-solutions.md`). Classer les objections :
   bloquante, à mitiger, écartée mais nommée. Verdict rendu sur la première version du plan, avec son compte
   (n parades manquantes sur m histoires) : **engager** (aucune parade manquante), **durcir** (chaque parade
   manquante s'écrit comme une étape, un test ou un seuil du plan), **pivoter** (un bloquant réel, ou une parade
   qui change le cas, l'option ou le périmètre). Les parades ajoutées portent « (pré-mortem n° k) ». Sans rôle
   de l'entreprise, il est « rédigé par le consultant seul » et le plan prévoit l'étape où chaque rôle écrit
   seul ses raisons d'échec. Ouvrir `references/pre-mortem.md` pour le déroulé, les familles d'échec et le gabarit.
   Pour arbitrer l'ordre des priorités (étape 2) ou le verdict, appeler `router-consulting-strategy` (lentilles
   priorisation, risques et parades) ; le livrable reste celui de cette étape.
8. **Relire, puis finir par la décision attendue.** Toute formule en suspens (« on verra », « à
   définir ») devient une action, une hypothèse `[H]` avec son confirmateur, ou une question dans
   « Décision attendue ». Suite : chaque cas de la feuille de route entre par `cadrer-besoin` ; le plan
   se lance par son premier lot, puis `construire-solution` ouvre la construction quand la porte est
   constatée ou sans objet (une option 0 seule passe directement à `piloter-mise-en-service`). Quand le
   décideur tranche, ajouter une ligne à `mission/journal.md`.

## Le livrable

Le modèle complet, ses consignes de remplissage, le gabarit du pré-mortem et les lignes de journal sont dans
`references/modeles.md` : l'ouvrir pour rédiger. Les titres ci-dessous sont ceux du modèle.

Squelette de `mission/04-feuille-de-route.md` (portefeuille, porte « aucun besoin ») :

```markdown
# Feuille de route — <entreprise ou périmètre>
Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle) · Rédigé par · Sources : 02-portefeuille, 03-chiffrage
## 1. Les cas, notés — valeur, facilité, risque, rang, principe d'ordre
## 2. La séquence — vague 0 des actions sans construction, puis les vagues ; prérequis en renvoi court
## 3. Socle commun et prérequis à lever d'abord — plateformes, exploitants, règles de sécurité ; le détail daté
## 4. Ce qu'on ne fait pas maintenant
## 5. Pré-mortem
## Décision attendue
```

Squelette de `mission/cas-<slug>/70-plan.md` (plan de déploiement, porte « besoin connu ») :

```markdown
# Plan de déploiement — <titre court du cas>
Date · Demandeur (rôle) · Responsable du cas (rôle) · Décideur du plan (rôle) · Rédigé par · Sources : 30-exigences, 40-solutions, 50-rentabilite, 60-specification (version lue)
## 1. Objectif et critères de réussite
## 2. Lots — trois à six étapes vérifiables, dates en propositions [H]
## 3. Porte, pilote, recette et mise en production
## 4. Adoption — six questions, une réponse, un rôle, une échéance, ou ?
## 5. Exploitation
## 6. Protocole de mesure — les IND-xx de la spécification
## 7. Communication
## 8. Pré-mortem
## Décision attendue
```

Lignes de journal, au moment où le décideur tranche ; les décisions sans livrable (porte constatée, fin de
pilote, bascule) citent la pièce qui les prouve :

```markdown
- 2026-11-04 · découverte · 04-feuille-de-route validée par le comité de direction · « première vague : un cas par équipe ; le cas des achats attend la donnée fournisseurs »
- 2026-11-18 · cas-saisie-commandes · 70-plan validé par la direction commerciale · « pilote sur une équipe, arrêt si l'adoption reste sous le seuil convenu »
- 2026-11-24 · cas-saisie-commandes · porte constatée par le responsable des opérations · « sept conditions remplies, fiche de porte jointe »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Trois à cinq cas pour la première vague | des résultats visibles tôt valent plus qu'une couverture large ; au-delà, rien ne se termine | lancer tout le portefeuille d'un coup | l'entreprise a les équipes et les prérequis pour mener davantage de cas en parallèle |
| Critères du pilote et indicateurs cités par leur identifiant, jamais recopiés ; décision de continuer, prolonger ou arrêter écrite avant de commencer | deux jeux de critères ou de seuils finissent par diverger, et une décision prise après coup se prend sur l'enthousiasme | réécrire critères et seuils dans le plan, ou un pilote sans critères | jamais : sans critères écrits, ce n'est pas un pilote |
| Les simplifications sont des actions de la vague 0, ou du premier lot : responsable, date, pièce | sans elles, une solution « standardiser d'abord » n'a aucun plan, et la porte n'a rien à constater | les laisser en annexe du diagnostic, sans suivi | l'entreprise mène seule ses simplifications et en fournit la pièce : le plan ne garde que la porte |
| Le pré-mortem fait partie du plan, dans les deux modes ; son verdict se rend sur la première version | c'est le moment le moins cher pour changer de direction ; celui qui écrit les parades connaît déjà le verdict | un pré-mortem seulement sur demande, ou un verdict rendu sur la version déjà durcie | le plan tient en un lot réversible sans effet sur d'autres équipes : une demi-page suffit |
| L'adoption se traite par six questions, pas par un programme de conduite du changement | une équipe qui reprend le dispositif a besoin de réponses concrètes ; un programme complet dépasse la mission | un volet conduite du changement détaillé | le déploiement touche une grande partie de l'entreprise : on le propose comme mission distincte |
| Une échéance passée se redate dans le plan ; un livrable amont ne se corrige par version que s'il contredit une valeur ou une décision | les dates sont des propositions `[H]` : les versionner noierait les vraies corrections | corriger chaque date amont par une nouvelle version | une date amont engage un tiers (contrat, échéance de l'éditeur) : elle est corrigée et tracée |

## Frontières

- Gains, coûts et hypothèses `[H]` à confirmer → `chiffrer-rentabilite` (le plan les reprend, il ne les
  recalcule pas). Tri et portefeuille → `decouvrir-cas-usage` ; chaque cas lancé →
  `cadrer-besoin`.
- Exigences et spécification (recette, critères de pilote, indicateurs et seuils, propriétaire de la
  maintenance) → `rediger-cahier-des-charges` ; choix de l'option et définition de la porte →
  `concevoir-solution` ; processus actuel, ses mesures et ses simplifications → `auditer-processus` ; état de
  la mission et journal → `router-mission-ia`.
- Construire en essai → `construire-solution` ; recetter → `tester-solution` ; mettre en service (actions sur
  les outils, feu vert, bascule, adoption réalisée, transmission) → `piloter-mise-en-service` ; relire les
  relevés après déploiement → `mesurer-gains`. Ici on planifie et on cite ; on n'exécute pas.
- Pour mettre en forme le retour arrière, la communication et l'exploitation : `COMPAGNONS.md` du pack,
  ligne « Mettre en service ». On ne dit s'en être servi que si on l'a réellement appelé.
- Hors du pack : former ou exploiter à la place de l'entreprise.

## Preuves restantes

- Éprouvée sur la mission fictive du 12/10/2026 (`examples/`, les deux modes), qui a relevé 94 frictions
  dans le pack ; celles qui touchent la feuille de route et le plan (vague 0, porte, lots en parallèle,
  indicateurs, pré-mortem, journal) sont corrigées ici.
- NON MESURÉ sur une mission réelle : le premier déploiement dira si trois à six étapes par lot et
  six questions d'adoption suffisent, si le critère de verdict du pré-mortem départage bien durcir et
  pivoter, et si le pré-mortem nomme les échecs qui surviennent vraiment. Le protocole de mesure du plan est
  relu après déploiement par `mesurer-gains`, qui dépend des relevés de l'entreprise.
- Sources et crédits : le pré-mortem suit la méthode de Gary Klein (« Performing a Project Premortem »,
  Harvard Business Review, 2007) ; les autres inspirations (écriture individuelle avant partage, relance aux
  jalons, retour arrière, communication, procédure d'exploitation, propriétaire nommé, interrupteur, alerte
  sur le silence, comptes non personnels) sont créditées dans la section « Sources et crédits » du
  `README.md`, et les compagnons de cette étape dans `COMPAGNONS.md`.
