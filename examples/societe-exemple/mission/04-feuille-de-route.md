# Feuille de route — Société Exemple

2026-09-22 · Demandeur et valideur : direction générale · Rédigé par : consultant IA · Sources : `02-portefeuille.md`, `03-chiffrage.md` (et `00-contexte.md` pour les contraintes)
Version 1.1, précisée le 2026-10-12 : le seuil de retard de la colonne « litige » (pré-mortem, ligne 1) passe de 2 jours à 3 jours ouvrés, comme dans `60-specification.md` §10. Rien d'autre ne change.

Ce document ordonne les trois cas retenus et les actions sans construction, jusqu'au 2026-12-18.

## 1. Les cas, notés

| Cas | Équipe | Valeur (gain net central, fourchette) `[E]` | Facilité | Risque | Rang |
|---|---|---|---|---|---|
| Tri des tickets | Support | 220 € par mois (85–418 €) | haute : huit catégories écrites, règles peut-être dans l'outil `[H]` | bas : un ticket mal classé est repris par la permanence | 1 |
| Relances de factures échues | Finance | 139 € par mois (43–268 €) | moyenne après simplification : données accessibles ; trois règles à écrire et litiges invisibles de la finance, à traiter d'abord | haut : message à un client ; validation humaine avant tout envoi | 2 |
| Statut de commande | Support | 185 € par mois (18–406 €) | moyenne : suivi du transporteur saisi à la main, parfois périmé `[H]` | moyen : un statut faux se voit chez le client | 3 |

Principe d'ordre. Un cas passe avant un autre quand son chiffrage est meilleur (solide, puis à mesurer, puis douteux), puis quand sa facilité est plus haute. Le statut de commande passe après les relances malgré un gain net plus fort (185 € contre 139 €) : son délai de retour dépasse le critère de la direction (25,8 mois contre 18 `[E]`). Deux cas démarrent ensemble, de deux équipes différentes ; il n'y a qu'un gain rapide, donc pas de première vague de trois cas : on commence par les prérequis qui débloquent les relances.

## 2. La séquence

| Vague | Cas | Prérequis | Dépend de | Responsable (rôle) | Jalon `[H]` | Indicateur déjà suivi · mesure de départ |
|---|---|---|---|---|---|---|
| 0 (tout de suite, sans construction) | Supprimer le rapport hebdomadaire des ventes, par un test de quatre semaines | accord du responsable des ventes | — | direction générale | début le 2026-09-28 ; décision de supprimer le 2026-10-26 | aucun indicateur suivi · 3 h par mois `[E]` (45 min × 4 `[H]`) |
| 0 | Réduire le rapport mensuel de pilotage aux trois chiffres lus | accord de la direction générale sur les trois chiffres | — | responsable financier | première version courte le 2026-10-30 | aucun indicateur suivi · 8 h par rapport `[H]`, à relever le mois prochain |
| 0 | Vérifier si un avis d'expédition automatique existe | lecture de la documentation de l'éditeur | — | responsable financier | réponse le 2026-10-02 | tickets de statut · 480 par mois `[F]` |
| 1 | Relances de factures échues | voir 3 : règles de relance, lettrage, colonne « litige », comptes clés | colonne « litige » alimentée par le support | responsable financier | cadrage le 2026-09-24 ; plan validé avant le 2026-10-16 | réclamations après relance · 13 par mois `[F]` |
| 1 | Tri des tickets | voir 3 : règles d'affectation, outil lu ; mesure sur 50 tickets (pré-mortem n° 2) | — | responsable du support | cadrage le 2026-10-01 ; plan validé avant le 2026-10-23 | tickets non classés · 67 par mois, soit 5,4 % `[F]` |
| 2 | Statut de commande | voir 3 : avis d'expédition vérifié (vague 0), échantillon de 100 tickets de statut ; suivi du transporteur lisible sans saisie | vague 0 (avis d'expédition) ; décision de pilote de la vague 1 | responsable du support | décision de reprise le 2026-11-27 | tickets de statut · 480 par mois `[F]` |

## 3. Prérequis à lever d'abord

| Ce qui manque | Pour quels cas | Qui le lève | Pour quelle date `[H]` |
|---|---|---|---|
| Trois règles de relance écrites : seuil de montant, comptes clés, litiges | relances | responsable financier | 2026-10-09 |
| Lettrage fait avant la séance du lundi (changement de jour, sans outil) | relances | comptable et responsable financier | première application le lundi 2026-10-05 |
| Colonne « litige » dans le tableur partagé, alimentée chaque jour par le support | relances | responsable du support | 2026-10-05 |
| Liste écrite des comptes clés (environ 25 `[H]`) | relances | responsable financier | 2026-10-09 |
| Règles d'affectation par catégorie écrites ; documentation de l'outil de tickets lue | tri | responsable du support | 2026-09-30 |
| Mesure sur 50 tickets classés avec et sans proposition (minutes gagnées par ticket) | tri | responsable du support | 2026-10-16 |
| Documentation de l'éditeur du logiciel de facturation lue : relances, import bancaire, avis d'expédition | relances, statut de commande | responsable financier | 2026-10-02 |
| Devis daté d'un indépendant, sur la base des exigences | tri, relances | direction générale | 2026-10-09 |
| Échantillon de 100 tickets de statut (part avec réponse type et suivi à jour) | statut de commande | responsable du support, responsable logistique | 2026-11-20 |
| Entretiens courts avec le responsable des ventes et le responsable logistique | devis, réapprovisionnement (en attente) | direction générale | 2026-11-06 |

## 4. Ce qu'on ne fait pas maintenant

| Cas ou chantier | Pourquoi pas maintenant | Se rouvre si |
|---|---|---|
| Statut de commande | chiffrage douteux (25,8 mois contre 18 au central `[E]`) ; suivi du transporteur saisi à la main | un avis d'expédition automatique existe, ou le suivi devient lisible sans saisie et la construction complète passe sous environ 3 099 € `[E]` |
| Rapprochement des paiements | capacités du logiciel inconnues ; le retard de lettrage se règle d'abord sans outil | le responsable financier confirme que le logiciel importe un fichier bancaire, ou le lettrage reste en retard après la standardisation |
| Demandes de devis | volume et durée jamais mesurés (200 demandes et 10 min, `[H]`) | l'entretien court avec le responsable des ventes mesure plus de 30 h par mois de ressaisie |
| Réapprovisionnement | seuils et durée jamais mesurés (4 h par semaine, `[H]`) | l'entretien court avec le responsable logistique confirme 16 h par mois et des seuils stables |
| Aide à la réponse aux réclamations de facture | valeur faible (3,0 h par mois `[E]`) | les réclamations restent au-dessus de 13 par mois `[F]` quand les relances sont corrigées |
| Tournées de livraison | tâche à garder (jugement, contraintes de terrain non écrites) | le responsable logistique en fait la demande |
| Un troisième cas en même temps | trop de cas à la fois : aucun ne se termine (pré-mortem n° 3) | la vague 1 a passé sa décision de pilote |

## 5. Pré-mortem

Thèse attaquée : d'ici le 2026-12-18, deux dispositifs sont en service, le tri des tickets et les relances validées par un humain, utilisés par le support et la finance et mesurés sur des indicateurs déjà suivis, parce que les prérequis de la section 3 sont levés avant le 2026-10-09.
Contributions : rédigé par le consultant seul ; aucun rôle de l'entreprise n'a écrit ses propres raisons d'échec. Le plan de chaque cas prévoit l'étape où les rôles concernés les écrivent seuls avant le pilote.

| # | Histoire d'échec (au passé) | Vraisemblance | Gravité | Signal d'alerte précoce | Parade | Condition d'arrêt | Propriétaire (rôle) | Classement |
|---|---|---|---|---|---|---|---|---|
| 1 | La colonne « litige » n'a jamais été alimentée régulièrement : le support la remplissait quand il y pensait, et les relances ont continué de partir chez des clients en litige. | moyenne | haute | colonne vide ou en retard de plus de 3 jours ouvrés `[H]` | alimentation quotidienne inscrite comme ligne datée de la section 3, avec son propriétaire | colonne non à jour 3 lundis de suite `[H]` : le cas relances sort de la vague 1 | responsable du support | à mitiger |
| 2 | Le tri des tickets, choisi pour sa facilité, n'a presque rien apporté : l'outil classait déjà presque tout, ou la permanence ne se fiait pas aux propositions. | moyenne | moyenne | minutes gagnées mesurées sous 0,5 par ticket (le bas du chiffrage `[H]`) | mesure sur 50 tickets avant d'engager la construction (ligne ajoutée à la séquence ; durci) | minutes gagnées sous 0,5 par ticket : arrêter, ne rien construire | responsable du support | à mitiger |
| 3 | Les devis et le réapprovisionnement ont été lancés dès leurs entretiens faits : quatre cas ouverts, aucun terminé, un support saturé. | moyenne | haute | plus de deux cas en cours | limite de deux cas simultanés, inscrite en section 4 (durci) | tout nouveau départ suspendu tant que la vague 1 n'a pas décidé | direction générale | à mitiger |
| 4 | Le logiciel de facturation a été remplacé en mars 2027 : les relances, branchées sur ses fonctions, ont dû être refaites avant d'avoir remboursé leur construction. | basse | haute | décision de renouvellement à l'ordre du jour de la direction | construire sur des fichiers exportés plutôt que sur des fonctions du logiciel ; options de repli de `40-solutions.md` à garder à jour (durci) | adaptation estimée à plus de 30 % de la construction `[H]` : décider avant de payer | direction générale | à mitiger |

Écartées : retrait du soutien de la direction — la direction générale décide chaque vague et a posé elle-même la trésorerie en priorité.
Verdict : durcir — la thèse tient et aucune objection n'est bloquante, mais 3 parades manquaient sur 4 histoires retenues (n° 2, 3 et 4).
Version durcie : (a) ajouter à la séquence la mesure sur 50 tickets avant le tri (pré-mortem n° 2) ; (b) limiter à deux cas simultanés (section 4) (pré-mortem n° 3) ; (c) exiger de `40-solutions.md` une solution qui lit des fichiers exportés et reste portable, avec l'option de repli sans développement (pré-mortem n° 4).
À rejouer : à la décision de pilote de chaque cas de la vague 1 ; avant la décision de renouvellement du logiciel de facturation en mars 2027.

## Décision attendue

Valider l'ordre, les cas de la première vague et leurs responsables, puis lancer le premier cas : il entre par `cadrer-besoin`.
