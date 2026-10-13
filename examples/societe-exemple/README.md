# Société Exemple — une mission complète du pack consultant-ia

Cet exemple déroule une mission de bout en bout, de la première question à la mesure des gains d'un cas. Chaque livrable suit le modèle de sa compétence et finit par « Décision attendue ».

## Tout est fictif

L'entreprise, ses rôles, ses chiffres et ses sources sont inventés : un distributeur B2B de fournitures de bureau, 40 personnes, cinq équipes. Aucune personne, aucune marque, aucune statistique de marché. Les dix-sept fichiers de `mission/sources/` portent la mention « source fictive ». Les réponses du client sont simulées : chaque décision du journal est marquée « (simulée) » et attribuée à un rôle.

## Ce qui est réel, ce qui est simulé

À partir de l'étape 80, une partie de l'exemple est exécutée pour de bon. Les deux horloges ne se confondent pas : les dates de la mission (août 2026 à janvier 2027) sont fictives ; les exécutions ont eu lieu le 2026-10-13 sur la machine qui a produit l'exemple, avec Python 3.14.6 et la bibliothèque standard seule.

| | Réel (exécuté, rejouable) | Simulé (inventé, daté de la mission) |
|---|---|---|
| 80 construction | la maquette `flux_relances.py` du flux de relances (versions 1.0 et 1.1, gelées avec leur manifeste d'empreintes), ses doubles de classeur et de messagerie, ses contrôles de tranche, son balayage de secrets, l'essai du retour arrière | la plateforme sans code P, que la maquette remplace ; l'indépendant qui la monte |
| 85 recette | 43 tests, deux passes (39 réussis puis 43 sur 43), 17 sabotages tous détectés puis rétablis, balayage des pièces ; commandes en tête de `85-recette.md` | la passe 3 sur la plateforme (43 sur 43), la passe 4, le prononcé des deux rôles métier |
| 90 mise en service | rien : aucun outil réel n'est touché | les 25 actions `A-xx`, leurs validations et exécutions, le pilote, la bascule, l'adoption, la transmission |
| 95 mesure | le calcul : `95-mesure/calculs-v1.2.py` redonne chaque nombre du document, sortie dans `calculs-v1.2.txt` | les relevés de départ, du pilote et de production, la lecture d'échantillon (pièces de `mission/sources/`) et la décision |

Aucun chiffre de 90 ou de 95 n'est un résultat réel : ce sont des entrées inventées traitées par des calculs réels. Chaque livrable concerné le dit en tête.

## Ce qu'il montre

- La porte « découverte » : pas de besoin précis, six irritants cités. Livrables `00` à `04` : contexte, cartographie des tâches, portefeuille de cas, chiffrage d'ordre de grandeur, feuille de route avec pré-mortem.
- La porte « besoin connu », pour un seul cas : les relances de factures échues. Livrables `10` à `70` : besoin, diagnostic, exigences, solutions, rentabilité, spécification, plan de déploiement avec pré-mortem.
- De la construction à la mesure, sur le même cas. `80` : une maquette exécutable et sa fiche d'exploitation. `85` : une recette qui échoue d'abord (quatre tests en échec, quatre défauts de logique, deux défauts de document), puis réussit, avec ses sabotages ; un défaut de plus, D-07, trouvé en exploitation par la lecture d'un échantillon de cas, que des tests écrits depuis la spécification ne pouvaient pas voir. `90` : le registre des actions sur les outils réels avec leur retour arrière, le feu vert, le pilote, la bascule, l'adoption, la transmission. `95` : les relevés comparés au départ et au business case terme par terme, le gain net devenu négatif et décomposé, la décision « corriger » avec sa règle d'arrêt, ce que la mesure change pour le portefeuille.
- Les cas difficiles : un lancement reçu deux fois (T-12), un arrêt net au milieu de l'écriture (T-15, T-29, T-31), un changement non approuvé (T-22, puis un modèle corrigé hors registre : incident daté, A-17 annulée, suite en A-18), une adoption nulle et un gain net négatif (`95-mesure.md` §7).
- Les trois statuts : `[F]` fait appuyé par une pièce ou énoncé par son détenteur, `[H]` hypothèse avec le rôle qui la confirme, `[E]` calcul montré. Un gain n'est un fait qu'en `95`.
- Un livrable déjà validé qui change : version datée dans son en-tête et ligne « corrigé » au journal (`03-chiffrage.md`, `04-feuille-de-route.md`, `30-exigences.md`, `60-specification.md`, `70-plan.md`, `80-construction.md`, `90-mise-en-service.md`, `95-mesure.md`, la fiche d'exploitation en cinq révisions).
- Une condition de démarrage de la construction, appelée la porte : posée par `40-solutions.md` §10, reprise sans changement par `60-specification.md` §1 et `70-plan.md` §3.
- Un journal qui ne porte que des décisions : une ligne par livrable validé, par correction, par réponse à une question, par verdict relu, par lot d'actions validées, par feu vert, fin de pilote, bascule, transmission et lecture de la mesure, avec la pièce qui la prouve.

Un seul cas est déroulé. Les deux autres cas retenus par la feuille de route (tri des tickets entrants, statut de commande) entreraient à leur tour par `cadrer-besoin`.

## Ordre de lecture

1. `mission/00-contexte.md`, puis `01-cartographie-taches.md`, `02-portefeuille.md`, `03-chiffrage.md` et `04-feuille-de-route.md`.
2. `mission/cas-relances-factures/` : `10-besoin.md`, `20-diagnostic.md`, `30-exigences.md`, `40-solutions.md`, `50-rentabilite.md`, `60-specification.md`, `70-plan.md`, puis `80-construction.md` (avec `80-construction/` : fiche de montage, fiche d'exploitation, journal des versions, la livraison et ses données d'essai), `85-recette.md` (avec `85-recette/` : les programmes de test, les passes, les sabotages), `90-mise-en-service.md` et `95-mesure.md` (avec `95-mesure/` : le calcul).
3. `mission/journal.md` : les décisions, dans l'ordre.
4. `mission/sources/` : les entretiens, les exports et la séance enregistrée, puis les pièces de la mise en service et de la mesure (compte rendu de la passe 3, messages du client, relevés du pilote et de production, lecture d'échantillon) que les livrables citent.

Pour rejouer la partie réelle, depuis `mission/cas-relances-factures/85-recette/` : `python -X utf8 test_recette.py` (les 43 tests, une vingtaine de secondes) et `python -X utf8 sabotage.py` (les 17 sabotages) ; depuis `95-mesure/` : `python -X utf8 calculs-v1.2.py`. Les sorties rangées à côté sont celles de l'exécution du 2026-10-13 ; elles ne se réécrivent pas à chaque rejeu.

## État de la mission

Calculé sur les fichiers présents, comme le fait `router-mission-ia` (étape 1) :

```text
Mission           societe-exemple                          porte(s) : découverte · besoin connu
Découverte        00 ✓  01 ✓  02 ✓  03 ✓  04 ✓             décision en attente : aucune
cas-relances-factures  10 ✓  20 ✓  30 ✓  40 ✓  50 ✓  60 ✓  70 ✓  80 ✓  85 ✓  90 ✓  95 ✓
                  décision en attente : 80 fiche d'exploitation révision 5 · 85 version 1.4 (gravité de D-07) · 90 version 1.2 (actions A-22 à A-25, maintien du flux sous D-07)
À lancer          Tri des tickets entrants · Statut de commande
Dernière décision 2027-01-13 · cas-relances-factures · 95-mesure corrigé (version 1.2) : « pas de retour » tant que le gain net est négatif (direction générale)
Questions ouvertes  5 Q-xx sans réponse inscrite au journal
Étape suivante    95-mesure, revue du 2027-02-08 (« corriger » laisse le cas ouvert)
```

Les questions ouvertes se comptent sans jugement : les `Q-xx` citées par les livrables `10` à `95` (dix-huit, de Q-01 à Q-18) moins celles qu'une ligne du journal donne pour « répondue » (treize). Restent cinq : Q-02 (seuil de montant, seconde phase), Q-08 (règle de la comptable suppléante), Q-13 (alerte de silence sur un déclencheur distinct, à vérifier), Q-15 (indépendance du connecteur d'alerte) et Q-18 (solde dû dans l'export de S1). Les hypothèses `[H]` ne se comptent plus ; le routeur cite les plus lourdes à la clôture seulement, et ce cas n'est pas clos. Les deux cas « à lancer » sont ceux que le journal retient (« on creuse : … ») et qui n'ont pas encore de dossier ; ils entreraient par `cadrer-besoin`. Le journal n'a pas de bloc « Clôture » : « corriger » laisse le cas ouvert, le routeur ne le clôt pas.

## Ce qu'il ne prouve pas

Il a été éprouvé sur cette mission fictive seulement. Aucune mesure sur une mission réelle : un client réel remettra-t-il les relevés demandés, la lecture de cas tiendra-t-elle dans une matinée, les règles de décision par défaut départageront-elles aussi bien ? Voir « Preuves restantes » dans chaque compétence. La partie réelle (maquette et recette) éprouve la logique du flux et la méthode de test, pas une plateforme ni une équipe : l'auteur de la maquette est aussi celui des tests, et la plateforme sans code n'a jamais été touchée. Les décisions et les relevés de 90 et de 95 sont inventés par l'auteur de l'exemple : ils montrent la forme des livrables et la justesse des calculs, pas ce qu'une équipe réelle ferait.
