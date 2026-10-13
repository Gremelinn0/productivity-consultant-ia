> **Source fictive.** Relevé simulé pour l'exemple du pack consultant-ia. Aucune personne, aucun chiffre et aucune entreprise réels : des compteurs et des durées, par rôle.

# Relevé du lundi 2026-11-30 · pilote, lundi 3, fin de mois (première mesure de la pointe)

Mode : préparation avec validation (lot suivant sous A-15, plafond de 60 relances, comptes clés compris). Durées notées par la gestionnaire clients ; compteurs lus par le responsable financier ; opérations lues au compteur de la plateforme.

## 1. Séance

| Phase | Minutes |
|---|---|
| Dépôt de l'extraction et lancement | 4 |
| Lecture de la liste, des motifs et des « à traiter à la main » | 9 |
| Relecture, corrections, suppressions et envois des brouillons | 43 |
| Fin de séance : compteurs, file des échecs, historique | 8 |
| Total | 64 |

Pendant l'attente de 9 minutes décrite ci-dessous, la gestionnaire clients a relu les brouillons déjà créés : ce temps est compté en relecture, il n'est pas perdu.

## 2. Compteurs du dispositif

| Compteur | Valeur |
|---|---|
| Factures dans l'extraction | 81 (61 le 2026-09-07 : pointe de fin de mois, +33 %) |
| Propositions | 52, dont 6 comptes clés ; sous le plafond de 60 |
| Écartées par motif | payée 10 · déjà relancée 7 · en litige 6 (23) |
| Au-delà de J+60 | 2 |
| « À traiter à la main » | 4 |
| Total | 52 + 23 + 2 + 4 = 81 |
| Liste prête | 3 min 12 s, interruption non comprise |
| Brouillons hors comptes clés relus | 46 : 37 envoyés · 9 supprimés (7 sous 15 € ; 2 factures payées le matin même) · dont 5 envoyés après correction |
| Comptes clés | 6 brouillons ; envoyés par le responsable financier le 2026-12-01 |
| Lignes d'historique écrites par l'étape 8 | 37 ; aucune alerte « identifiant introuvable » |
| File des échecs | vide en fin de séance |

## 3. Incidents

| Heure | Ce qui s'est passé | Ce qui l'a rattrapé |
|---|---|---|
| 09 h 31 | double clic sur « Lancer » : une seconde exécution demandée alors que la première tourne | refus « une exécution est déjà en cours », rien créé en double (T-12, T-30) |
| 09 h 47 | l'éditeur redémarre la plateforme pendant la création des brouillons : 17 brouillons créés, 35 à créer ; aucun message d'erreur, l'exécution s'arrête | la gestionnaire clients voit 17 brouillons au lieu de 52 à 09 h 52 et relance à 09 h 56 : les 17 brouillons déjà présents sont adoptés, 35 sont créés, aucun doublon, une ligne « réconcilié » au journal (T-15b, T-29) |

Ni l'un ni l'autre n'est un défaut : le comportement est celui de la spécification. Aucun `D-xx`.

## 4. Indicateurs du jour

IND-02 : 0. IND-03 : 64 min. IND-04 : 0. IND-05 : (9 supprimées + 5 corrigées) ÷ 52 propositions = 26,9 %. IND-08 : 1 séance sur 1 (gestionnaire clients).

## 5. Autres relevés

- Réclamations après relance (support, semaine du 2026-11-30) : 3.
- Opérations consommées le lundi 2026-11-30 : 286 (mois de novembre) ; du mardi 1er au vendredi 4 décembre : 21 (mois de décembre).
- Temps du responsable financier : lecture des compteurs et des alertes 6 min ; validation des 6 comptes clés le 2026-12-01, 14 min.
