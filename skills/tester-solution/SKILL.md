---
name: tester-solution
description: >-
  Quand la solution est construite en version gelée (étape 80) et qu'il faut savoir si elle fait ce que
  la spécification exige avant de la confier à de vrais utilisateurs (« teste la solution », « fais la
  recette », « est-elle prête pour le pilote ? », « go / no-go ») → exécuter, preuves à l'appui, le test
  de chaque critère d'acceptation (cas limites, erreurs, doublons, reprise, permissions) ; saboter une
  fois les tests qui comptent ; évaluer à part la partie IA sur un jeu étiqueté (cas courants,
  difficiles, injections, abstentions), seuils pris dans la spécification ; dire dans quel environnement
  chaque résultat a été obtenu ; rendre un verdict : prêt, prêt avec réserves, pas prêt. Étape 85 du
  pack consultant-ia, après la construction. Triggers : « recette », « tester la solution », « exécuter
  les critères d'acceptation », « plan de test », « jeu d'évaluation », « evals », « golden set », « injection de
  prompt », « LLM-as-judge », « défauts », « UAT », « acceptance testing ».
metadata:
  scope: "la preuve qu'une version gelée de la solution fait ce que la spécification exige, dans un environnement d'essai, avec un verdict pour le pilote"
  owns: "la couverture et l'exécution de la recette (tests ajoutés à la suite de ceux de 60), les preuves, le sabotage, le registre des défauts (D-xx, une seule série par cas : trouvés en recette, en pilote ou en exploitation), le jeu d'évaluation de l'IA (EV-xx) et son analyse, l'échelle des environnements, le verdict pour le pilote (trois libellés exacts)"
  consumes: "60-specification (version lue : critères, tests, seuils du pilote, rôle de l'IA), 30-exigences §9, 80-construction et son dossier (version gelée, essai, données, écarts, fiche), mission/journal.md"
---

# Tester la solution

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/85-recette.md` (et, au besoin, le dossier
> facultatif `85-recette/` pour les preuves longues et le jeu d'évaluation). Preuve : un rôle métier prononce
> la recette sur les preuves, le décideur autorise ou non le pilote, et les deux décisions s'inscrivent dans
> `mission/journal.md`. Contrôle de forme : le document porte les dix rubriques du modèle ; chaque critère
> d'acceptation de `30-exigences` §9 a un test et chaque test un critère ; chaque test est « exécuté » avec
> sa preuve (commande ou procédure, sortie, date, version) ou « prévu », jamais « réussi » sans exécution ;
> l'attendu est écrit avant l'exécution ; les tests qui protègent le grave ont été sabotés puis rétablis ;
> chaque défaut (trouvé en recette, en pilote ou en exploitation) a un `D-xx`, une gravité et un re-test ; le verdict est
> exactement « prêt », « prêt avec réserves » ou « pas prêt » ; si la solution comprend de l'IA, le jeu
> `EV-xx`, les seuils pris dans `60-specification` (fixés avant) et les résultats par catégorie sont écrits,
> sinon « sans objet » avec la raison ; chaque résultat dit son environnement ; chaque nombre a son statut
> `[F]`, `[H]` ou `[E]` (définis dans `ARCHITECTURE.md`). Exemple de référence : `examples/` du pack
> (cas fictif : recette de la maquette jouée, sabotages compris). **Boucle** : aucune.

## Ce que cette compétence résout

Un dispositif qui « a l'air de marcher » le jour de la démonstration se découvre en production : un
événement reçu deux fois, un plantage au mauvais moment, une réponse d'IA plausible et fausse, une règle qui
a changé sans que personne le dise. Cette compétence organise deux preuves qui ne se mélangent pas. La
recette dit, critère par critère, si le dispositif déterministe fait ce que la spécification exige.
L'évaluation dit, sur des cas étiquetés, dans quelle proportion et sur quelles catégories un composant d'IA
se trompe, et si c'est acceptable au regard de seuils écrits avant.

Résultat attendu : pour chaque critère, un test exécuté ou prévu avec sa preuve ; les défauts trouvés et
corrigés ; un verdict pour le pilote que le décideur peut suivre ou contredire en connaissance de cause,
avec, pour chaque résultat, l'environnement dans lequel il a été prouvé.

## Stratégie

1. **Deux preuves, jamais un seul tableau.** Une recette déterministe réussit ou échoue ; une IA réussit en
   proportion, par catégorie. Mêlées, « 95 % de tests réussis » cache la catégorie grave qui échoue.
   (A) La recette : formats, doublons, idempotence (rejouer ne double rien), reprise après plantage, délai
   dépassé, traitement partiel, retour arrière, lecture après écriture, permissions. (B) L'évaluation de
   l'IA : justesse, fidélité aux sources, usage des outils, injection, fuite de données, abstention quand
   il faut, coût, latence, acceptation humaine, non-régression.
2. **Exécuté ou prévu, rien entre les deux.** Un test exécuté a sa preuve : commande ou procédure, sortie,
   date, version. Un résultat jamais exécuté ne s'écrit pas « réussi » ; « ça marche », sans pièce, ne vaut
   pas exécution. Un critère qu'on ne peut pas prouver dans l'essai (système réel, charge réelle,
   comportement humain) est dit « à vérifier au pilote », avec la mesure qui le vérifiera.
3. **Chaque résultat dit son environnement.** Quatre niveaux : *non testé* ; *données synthétiques* (l'essai,
   sur des données fictives) ; *préproduction* (les outils du client en configuration d'essai, mêmes
   versions et connecteurs, comptes de test, effets externes simulés ou dirigés vers des cibles de test) ;
   *accepté par le client* (un rôle métier a vu les preuves et prononcé la recette, sur le niveau atteint,
   qu'il ne relève pas). Rien ne se teste en production : ce qui exige un outil réel est une action du
   pilote (règle 7, `ARCHITECTURE.md`).
4. **L'attendu s'écrit avant l'exécution, et vient de la spécification.** Recopier la sortie du dispositif
   comme résultat attendu fabrique un test qui approuve ce qu'il devait juger. L'attendu vient de `60` ou
   `30`, d'un relevé `[F]`, ou d'un calcul fait à côté.
5. **Un test qui n'a jamais échoué ne prouve rien.** On sabote une fois : une régression plausible dans une
   copie (retirer le contrôle de fraîcheur, la recherche de clé, un refus de droit) ; le test doit échouer ;
   on rétablit et on compare à l'empreinte de la version gelée. Obligatoire pour ce qui protège le grave.
   Un test qui a déjà échoué sur un vrai défaut a fait sa preuve.
6. **Les cas qui font mal d'abord.** Le cas limite critique de `60` §12, l'appel reçu deux fois, le
   plantage juste après une écriture, le processus instable (une règle change en cours de route), le
   changement non approuvé, la validation humaine contournée, la permission refusée. Le cas nominal passe
   presque toujours : les dispositifs cassent ailleurs.
7. **Des seuils écrits avant, pris dans la spécification.** Pour l'IA comme pour le pilote : ceux de `60`
   §4 et §13. Un seuil fixé après avoir vu le résultat ne protège de rien. Un seuil absent est un trou de
   `60` : le décideur le fixe avant la passe (`[H]` daté, `[F]` une fois accepté) et `60` est corrigé par
   une version datée.
8. **Le jeu d'évaluation est à part et s'use.** Étiqueté par un humain avant l'exécution, jamais utilisé
   pour régler les consignes ; dès qu'il a servi à corriger, ses cas passent en mise au point et un
   nouveau lot confirme. Un petit jeu ne prouve pas un petit taux d'erreur : zéro erreur sur n cas
   autorise « moins de 3/n environ » `[E]` (règle de trois), pas « zéro ».
9. **Un juge automatique n'est pas une vérité.** Il aide à lire beaucoup de sorties, mais ne devient un
   critère d'arrêt qu'après calibrage contre une vérité humaine : échantillon relu à la main, accord par
   catégorie, désaccords relus, seuil d'accord fixé avant. Avant, c'est un indicateur.
10. **Celui qui construit ne prononce pas la recette.** Quand le même acteur construit et teste, le
    document le dit en tête : l'indépendance repose alors sur l'attendu écrit d'avance, l'état remis à
    zéro avant chaque test, le sabotage et le prononcé d'un rôle métier.

## Étapes

1. **Lire ce qui existe et décider de ce qui se teste.** `60-specification` (version lue : §4 rôle de l'IA,
   §12 tests et cas limite critique, §13 seuils du pilote), `30-exigences` §9, `80-construction` et son
   dossier, le journal. Rien n'a été construit parce que l'option 0 seule est retenue : pas de recette, le
   dire et passer à `piloter-mise-en-service`. Si `80` n'est pas validé « prêt pour la recette », le dire :
   tester une version qui bouge ne prouve rien. La recette porte sur la phase construite (`80` rubrique 1) ; les critères des
   phases suivantes sont écrits « hors phase », pas « réussis ». Y a-t-il de l'IA (`60` §4) ? Oui →
   partie B ; non → « sans objet », raison écrite.
2. **Figer l'objet testé.** Version et empreinte de `80`, environnement d'essai (son nom), données
   (provenance), état de départ (remise à zéro), qui exécute, quel rôle métier prononcera la recette, et si
   constructeur et testeur sont le même acteur (le dire en tête). Les accès de préproduction viennent du
   client ; le pack ne s'en procure aucun.
3. **Établir la couverture.** Table critère → tests : chaque CA de `30` §9 a un test, chaque test sert un
   CA, une EF ou une ENF ; orphelins signalés dans les deux sens. Compléter par les familles de risque
   (`references/methodes-de-test.md`, partie 1) ; les tests ajoutés continuent la numérotation de `60`
   (T-20…), avec leur raison. Un manque qui révèle un trou de `60` → version datée de `60` et ligne
   « correction » au journal (`ARCHITECTURE.md`).
4. **Écrire l'attendu avant d'exécuter**, avec sa source (rubrique de `60` ou `30`, relevé `[F]`, calcul
   indépendant).
5. **Exécuter et garder les preuves.** Une passe = une version testée. Par test : résultat (réussi ·
   échoué · prévu · à vérifier au pilote), commande ou procédure, sortie, date, environnement atteint.
   Preuve courte dans le document, longue dans `85-recette/`. Une exécution faite par le client ou le
   constructeur compte si sa pièce est reçue et nommée. Un test qui change de résultat sans changement de
   version est un défaut du test ou du dispositif, pas un test à rejouer jusqu'au vert.
6. **Saboter.** Pour le cas limite critique et chaque test qui protège un effet irréversible, une validation
   humaine, le dédoublonnage ou les permissions : une régression plausible dans une copie, le test doit
   échouer, puis on rétablit et on compare l'empreinte. Un test saboté qui reste vert est invalide : le
   réécrire, recommencer (`references/methodes-de-test.md`, partie 5).
7. **Tenir le registre des défauts.** `D-xx` (défaut trouvé en recette, en pilote ou en exploitation ; une
   seule série par cas, définie dans `ARCHITECTURE.md`) : où il a été trouvé, test source ou relevé, gravité
   (bloquant · majeur · mineur, critères en partie B de `references/modeles.md`), cause, correction. La
   correction se fait par `construire-solution` (nouvelle version), puis nouvelle passe : le test échoué,
   ceux de la tranche touchée, le sabotage si un garde-fou a bougé. Un défaut trouvé en pilote ou en
   exploitation (par `piloter-mise-en-service` ou `mesurer-gains`) prend le numéro suivant, est marqué
   « pilote » ou « exploitation » et suit la même boucle, avant toute nouvelle action en 90, hors les mesures d'attente
   (`A-xx` de confinement). Un défaut laissé ouvert n'est « accepté » que par une décision écrite du décideur, au journal.
8. **Évaluer l'IA (partie B), seulement s'il y en a.** `references/evaluation-ia.md` : seuils de `60`
   (avant), jeu `EV-xx` (cas du jeu d'évaluation) étiqueté, exécution avec modèle et consignes versionnés,
   erreurs par catégorie et gravité, relecture humaine, juge calibré s'il y en a un, coût, latence,
   acceptation humaine, non-régression. Résultats par catégorie, jamais une moyenne.
9. **Dire ce qui ne se prouve pas ici.** Critères prévus pour le pilote avec leur mesure (`IND-xx`) ou leur
   action (`A-xx`, action sur un outil réel du registre de `90-mise-en-service`) ; hypothèses `[H]` de `50`
   que la recette ne confirme pas ; niveau d'environnement atteint par critère.
10. **Rendre le verdict, puis la décision attendue.** Le verdict s'écrit avec exactement l'un de ces trois
    libellés, que `90-mise-en-service` lit tels quels : « prêt », « prêt avec réserves », « pas prêt ». Ni
    « presque prêt » ni « prêt sous conditions » : la nuance va dans les réserves. *Prêt* : tout critère
    Indispensable exécuté et réussi sur la version gelée, cas limite critique compris ; chaque sabotage a
    fait échouer son test puis a été rétabli ; aucun défaut ouvert ; si de l'IA, chaque seuil atteint,
    catégorie par catégorie. *Prêt avec réserves* : aucun défaut bloquant ouvert ; les défauts majeurs ou
    mineurs ouverts, les critères Importants ou Souhaitables prévus ou une catégorie d'IA non critique sous
    son seuil sont acceptés un à un par le décideur, chacun devenant une condition du pilote (rôle, date,
    signal). *Pas prêt* : un critère Indispensable échoué ou non exécutable, le cas limite critique échoué,
    un sabotage sans effet, un défaut bloquant ouvert, un seuil non atteint sur une catégorie grave
    (injection suivie, action hors liste, fuite de données), un secret ou une donnée personnelle dans la
    livraison, un interrupteur ou un retour arrière non prouvés. Un critère Indispensable laissé au pilote
    ne permet « prêt » que si le mode du pilote (`60` §13) empêche tout effet réel tant qu'il n'est pas
    vérifié. Le verdict dit ses niveaux d'environnement (« 9 critères sur 10 en préproduction, 1 sur
    données synthétiques »). Proposer `piloter-mise-en-service`. Deux lignes au journal : la recette
    prononcée (rôle métier), le pilote autorisé ou non (décideur). Un défaut bloquant trouvé après le feu vert rend « pas
    prêt » la version en service : le verdict est relu au journal (« verdict relu : pas prêt pour la version en service »)
    jusqu'à la passe qui recette la correction.

## Le livrable

Le modèle complet, la gravité des défauts, les critères du verdict, les lignes de journal et les pièges sont
dans `references/modeles.md` : l'ouvrir pour rédiger. Les titres ci-dessous sont ceux du modèle.

Squelette de `mission/cas-<slug>/85-recette.md` :

```markdown
# Recette — <titre court>
Date · Version testée (80, empreinte) · Environnement d'essai (nom) · Spécification lue (version) · Exécutée par · Prononcée par (rôle métier) · Décideur du pilote (rôle) · Rédigé par · Version
Constructeur et testeur : <deux acteurs distincts | le même acteur : indépendance assurée par …>
Mode : recette déterministe + <évaluation de l'IA | évaluation de l'IA sans objet : aucun modèle n'intervient (60 §4)>
## 1. Objet testé — version, empreinte, essai, données, état de départ, tests de 60 et tests ajoutés
## 2. Couverture — critère → tests ; orphelins dans les deux sens
## 3. Passes — version testée, date, tests joués, résultats, environnement atteint
## 4. Résultats et preuves — un test par ligne : attendu et sa source, résultat, preuve, environnement
## 5. Familles de risque — doublons, reprise, permissions… : couvert, en partie, non (pourquoi)
## 6. Sabotage — test, régression, échec constaté, rétablissement vérifié
## 7. Défauts — D-xx, trouvé en (recette · pilote · exploitation), gravité, correction, re-test, état
## 8. Évaluation de l'IA — seuils, jeu EV-xx, résultats par catégorie, erreurs, juge ; ou « sans objet » et la raison
## 9. Ce qui ne se prouve pas ici — vérifié au pilote par quelle mesure ou quelle action
## 10. Verdict pour le pilote — « prêt » · « prêt avec réserves » · « pas prêt », l'un des trois tel quel ; niveaux atteints ; réserves
## Décision attendue
```

Lignes de journal, au moment où le rôle métier prononce puis où le décideur tranche (exemples fictifs) :

```markdown
- 2026-11-13 · cas-relances-factures · 85-recette prononcée par la gestionnaire clients et le responsable financier · « dix critères de la première phase exécutés, neuf en préproduction et un sur données synthétiques ; sabotages faits »
- 2026-11-13 · cas-relances-factures · pilote autorisé par le responsable financier · « verdict : prêt avec réserves (une réserve : un défaut mineur ouvert, condition au premier lundi) »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Deux preuves séparées, recette et évaluation d'IA | une recette réussit ou échoue ; une IA réussit en proportion et par catégorie ; mêlées, la moyenne cache la catégorie grave | un seul tableau de tests | la solution n'a aucune IA : la partie B est « sans objet » |
| Attendu écrit avant l'exécution | recopier la sortie fabrique un test qui approuve ce qu'il devait juger | résultat attendu déduit de la sortie | jamais |
| Sabotage des tests qui protègent le grave | un test jamais échoué ne prouve rien | faire confiance au vert | le test a déjà échoué sur un vrai défaut : il a fait sa preuve |
| Seuils pris dans 60 et fixés avant | un seuil réglé sur le résultat ne protège de rien | ajuster le seuil au score obtenu | seuil absent de 60 : le décideur le fixe avant la passe |
| Juge automatique seulement calibré | un juge non mesuré blanchit ou noircit les résultats sans qu'on le sache | utiliser le juge tel quel | accord mesuré au-dessus du seuil fixé, sur ce type de cas |
| Ce qui ne se prouve pas dans l'essai est dit « au pilote » | « réussi » sans exécution est la faute que cette étape existe pour éviter | compter ces critères comme réussis | jamais |
| Verdict à trois libellés exacts, aux critères décidables | « presque prêt » ne se décide pas, et `90-mise-en-service` lit les libellés tels quels | un score global ; un verdict nuancé | le décideur demande un classement : on le fournit en plus |

## Frontières

- Les exigences, critères d'acceptation, tests prévus et seuils → `rediger-cahier-des-charges` ; un trou
  trouvé en recette y retourne par version datée.
- Construire, corriger un défaut, livrer une nouvelle version → `construire-solution`.
- Le pilote, la bascule, l'adoption et toute action sur un outil réel, y compris tester dans l'outil réel →
  `piloter-mise-en-service`, avec le retour arrière de chaque action.
- Mesurer les gains et suivre la qualité en exploitation → `mesurer-gains` (les `IND-xx` se lisent en
  exploitation, pas ici).
- Le choix de l'option → `concevoir-solution` ; le calendrier et le choix des recetteurs →
  `planifier-deploiement` ; l'état de la mission et le journal → `router-mission-ia`.
- Tests propres à une plateforme → `COMPAGNONS.md` du pack.
- Un « pas prêt » qui remet l'option en cause renvoie à `concevoir-solution`, par le routeur
  (`router-mission-ia`).

## Preuves restantes

- Rédigée le 12/10/2026 d'après le contrat de l'étape 85. Essayée une fois, sur la mission fictive de `examples/` :
  43 tests exécutés sur la maquette (25 de 60 §12, 18 ajoutés), deux passes (39 réussis, puis 43 sur 43), 17
  sabotages tous détectés puis rétablis, verdict « prêt avec réserves » (cinq réserves). D-01 et D-02 viennent des
  documents, D-03 à D-06 de la logique, tous trouvés par les tests. D-07, trouvé ensuite en exploitation par la
  lecture d'un échantillon, était un trou de la spécification que des tests écrits depuis elle ne voyaient pas :
  la même version est relue « pas prêt pour la version en service » (ligne au journal). Passes 3 et 4 (plateforme) simulées ; tests écrits par le
  constructeur. Le témoin du balayage des secrets se compose à l'exécution : aucun fichier ne porte le texte d'une forme de clé réelle.
- Non essayée : la partie B (jeu étiqueté, règle de trois, juge), « sans objet » dans l'exemple.
- NON MESURÉ : si dix rubriques et le sabotage ciblé suffisent à une vraie recette ; si les critères du
  verdict départagent bien « prêt avec réserves » et « pas prêt » ; si la passe qui suit la correction d'un
  défaut d'exploitation (passe 5, proposée) se déroule comme écrit ; si la règle de trois et un jeu de
  quelques dizaines de cas donnent des seuils d'IA tenables ; combien de temps coûte le calibrage d'un juge.
- Sources et crédits : méthodes générales (test de mutation, jeu de référence étiqueté, règle de trois,
  accord entre évaluateurs, relecture après écriture). Les compagnons par plateforme sont crédités dans
  `COMPAGNONS.md`, jamais copiés ici. Réécrit avec nos mots.
