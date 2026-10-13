> **Source fictive.** Relevé simulé pour l'exemple du pack consultant-ia. Aucune personne, aucun chiffre et aucune entreprise réels : des compteurs et des durées, par rôle.

# Relevé du lundi 2026-11-16 · pilote, lundi 1, en parallèle

Mode (`60-specification.md` §13) : la gestionnaire clients mène la séance à la main selon la procédure unique et envoie ses propres courriels ; le flux prépare ses brouillons dans la boîte partagée, rien ne part du flux. L'étape 8 est désactivée ce jour-là (T-19). Durées notées par la gestionnaire clients ; compteurs lus par le responsable financier dans l'onglet « compteurs » du classeur du dispositif ; opérations lues au compteur de la plateforme.

## 1. Séance à la main (référence du jour)

| Phase | Minutes |
|---|---|
| É1 Exporter la liste | 12 |
| É2 Chercher dans le suivi | 36 |
| É5 Rédiger et envoyer | 56 |
| É6 Noter et contrôler | 17 |
| Total | 121 |

63 factures à traiter ; 28 relances envoyées par la gestionnaire clients (hors comptes clés) ; 4 comptes clés préparés pour le responsable financier. Cette séance ne compte pas pour l'indicateur IND-03 du pilote.

## 2. Ce que le flux a proposé (lancé à 10 h 12, après 10 h)

| Compteur | Valeur |
|---|---|
| Fichier du jour lu (Q-16) | 63 lignes lues sur 63, aucune erreur de lecture |
| Propositions | 36, dont 4 comptes clés |
| Écartées par motif | payée 9 · déjà relancée 6 · en litige 7 (22) |
| Au-delà de J+60 | 2 |
| « À traiter à la main » | 3 (adresse non plausible 2 ; historique contradictoire 1) |
| Total | 36 + 22 + 2 + 3 = 63 |
| Liste prête | 1 min 49 s après le lancement |
| Brouillons créés | 36, supprimés à 11 h 40 par l'interrupteur (essai A-11) |

## 3. Tableau des écarts, huit lignes, toutes expliquées

| # | Écart entre le flux et la séance à la main | Explication |
|---|---|---|
| 1 à 5 | 5 propositions du flux que la gestionnaire clients n'a pas faites | factures sous 15 € écartées à la main par sa règle personnelle ; le seuil est le point EF-05 de la seconde phase |
| 6 | 1 proposition du flux pour une facture déjà payée | paiement reçu lundi matin, après le rapprochement du vendredi ; vu à la main au contrôle par exception ; limite connue (`20-diagnostic.md` §7) |
| 7 et 8 | 2 factures « à traiter à la main » que la gestionnaire clients a relancées | adresse corrigée à la main puis relance envoyée ; la troisième (historique contradictoire) a été écartée par les deux voies : pas d'écart |

Contrôle : 32 propositions hors comptes clés = 28 relances envoyées + 5 sous 15 € + 1 payée ce matin − 2 factures « à la main » relancées = 32. Les 4 comptes clés sont identiques des deux côtés.

## 4. Essais en conditions réelles

| Essai | Heure | Résultat |
|---|---|---|
| Refus d'envoi du compte de service sur la vraie boîte (A-10) | 08 h 40 | refusé ; tentative au journal de la boîte ; un brouillon de test vers l'adresse interne de la finance, supprimé |
| Alerte de silence (flux non lancé à 10 h) | 10 h 00 | reçue par le responsable financier à 10 h 01 |
| Message d'avertissement de l'étape 6 | 10 h 14 | reçu par la gestionnaire clients |
| Interrupteur « Suspendre » (A-11) | coché 11 h 30 | brouillons supprimés au passage de 11 h 40 ; décoché à 11 h 45 |

## 5. Autres relevés de la semaine

- Réclamations après relance (support, semaine du 2026-11-16) : 3.
- Opérations consommées par la plateforme du 2026-11-16 au 2026-11-22 : 240.
- Alertes : 1 (silence, essayée). Incidents : aucun.

## 6. Indicateurs du jour

IND-02 : 0 (sans objet, rien n'est parti du flux). IND-04 : 0. IND-03 : non compté (séance à la main : 121 min). IND-08 : non compté (mode parallèle).
