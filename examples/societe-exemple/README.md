# Société Exemple — une mission complète du pack consultant-ia

Cet exemple déroule une mission de bout en bout, de la première question au plan de déploiement d'un cas. Chaque livrable suit le modèle de sa compétence et finit par « Décision attendue ».

## Tout est fictif

L'entreprise, ses rôles, ses chiffres et ses sources sont inventés : un distributeur B2B de fournitures de bureau, 40 personnes, cinq équipes. Aucune personne, aucune marque, aucune statistique de marché. Les six fichiers de `mission/sources/` portent la mention « source fictive ». Les réponses du client sont simulées : chaque décision du journal est marquée « (simulée) » et attribuée à un rôle.

## Ce qu'il montre

- La porte « découverte » : pas de besoin précis, six irritants cités. Livrables `00` à `04` : contexte, cartographie des tâches, portefeuille de cas, chiffrage d'ordre de grandeur, feuille de route avec pré-mortem.
- La porte « besoin connu », pour un seul cas : les relances de factures échues. Livrables `10` à `70` : besoin, diagnostic, exigences, solutions, rentabilité, spécification, plan de déploiement avec pré-mortem.
- Les trois statuts : `[F]` fait appuyé par une pièce ou énoncé par son détenteur, `[H]` hypothèse avec le rôle qui la confirme, `[E]` calcul montré.
- Un livrable déjà validé qui change : version 1.1 datée dans son en-tête et ligne « corrigé » au journal (`03-chiffrage.md`, `04-feuille-de-route.md`, `30-exigences.md`, `60-specification.md`).
- Une condition de démarrage de la construction, appelée la porte : posée par `40-solutions.md` §10, reprise sans changement par `60-specification.md` §1 et `70-plan.md` §3.
- Un journal qui ne porte que des décisions : une ligne par livrable validé et par correction.

Un seul cas est déroulé. Les deux autres cas retenus par la feuille de route (tri des tickets entrants, statut de commande) entreraient à leur tour par `cadrer-besoin`.

## Ordre de lecture

1. `mission/00-contexte.md`, puis `01-cartographie-taches.md`, `02-portefeuille.md`, `03-chiffrage.md` et `04-feuille-de-route.md`.
2. `mission/cas-relances-factures/` : `10-besoin.md`, `20-diagnostic.md`, `30-exigences.md`, `40-solutions.md`, `50-rentabilite.md`, `60-specification.md`, `70-plan.md`.
3. `mission/journal.md` : les décisions, dans l'ordre.
4. `mission/sources/` : les entretiens, les exports et la séance enregistrée que les livrables citent.

## État de la mission

Calculé sur les fichiers présents, comme le fait `router-mission-ia` (étape 1) :

```text
Mission           societe-exemple                          porte(s) : découverte · besoin connu
Découverte        00 ✓  01 ✓  02 ✓  03 ✓  04 ✓             décision en attente : aucune
cas-relances-factures  10 ✓  20 ✓  30 ✓  40 ✓  50 ✓  60 ✓  70 ✓
À lancer          Tri des tickets entrants · Statut de commande
Dernière décision 2026-10-12 · cas-relances-factures · 70-plan validé
Hypothèses ouvertes  207 [H] sur les livrables du cas, sans doublon
Étape suivante    clore le cas cas-relances-factures (router-mission-ia, étape 5)
```

Les hypothèses ouvertes se comptent sur `10` à `70` : chaque `[H]` est lu avec les quatre mots qui le précèdent, et un énoncé repris tel quel dans plusieurs livrables compte une fois. Les deux cas « à lancer » sont ceux que le journal retient (« on creuse : … ») et qui n'ont pas encore de dossier ; ils entreraient par `cadrer-besoin`. La clôture du cas n'est pas encore écrite : elle viendrait avec l'étape suivante.

## Ce qu'il ne prouve pas

Il a été éprouvé sur cette mission fictive seulement. Aucune mesure sur une mission réelle : voir « Preuves restantes » dans chaque compétence.
