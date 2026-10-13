# Mesure — Relances de factures échues

2027-01-13 · Demandeur : direction générale · Valideur et décideur : direction générale (critère d'investissement de `50-rentabilite.md`) ; relevés remis par le responsable financier · Rédigé par : consultant IA · Version 1.2 · Période mesurée : du 2026-12-14 au 2027-01-10, quatre lundis (trois avec le flux, un à la main), équipe finance, flux 1.1, règles R1 puis R1.1 · Sources : `20-diagnostic.md` (version 1.1), `50-rentabilite.md` (version 1.1), `60-specification.md` §14 (version 1.4), `70-plan.md` §6 (version 1.2), `90-mise-en-service.md` (version 1.2), `85-recette.md` (version 1.4)
Lecture : première lecture — relevés reçus le 2027-01-11. La version 1.0 du 2026-12-15 était la demande de relevés (aucune donnée) ; les règles d'exclusion de la rubrique 1 y ont été écrites avant toute lecture. La version 1.2 du 2027-01-13 corrige la rubrique 4 : le retour s'écrit « pas de retour » tant que le gain net est négatif, par la seule formule de 50 §4, sans régime corrigé ; elle écrit aussi l'incident de A-17 comme tel (rubriques 1 et 7). Les relevés, le gain net observé et la décision ne changent pas.
Ce document compare, sur la période du 2026-12-14 au 2027-01-10, ce que le flux a rapporté et coûté à l'estimation de `50-rentabilite.md` (apport de l'option 4). Le réel s'écrit ici ; `50-rentabilite.md` garde l'estimation sur laquelle la décision d'y aller a été prise le 2026-10-08.

**Ce qui est réel, ce qui est simulé.** Simulés : les relevés (pièces fictives de `mission/sources/`), les rôles et leurs décisions (lignes « simulée » du journal) ; aucun chiffre n'est un résultat réel hors de l'exemple fictif. Réel : le calcul. Chaque nombre de ce document vient de `95-mesure/calculs-v1.2.py` (bibliothèque standard seule, entrées recopiées des relevés avec leur pièce), exécuté le 2026-10-13 avec Python 3.14.6 ; la sortie est `95-mesure/calculs-v1.2.txt`. Les dates de la mission suivent le calendrier fictif de `70-plan.md`, la date d'exécution du calcul est celle de la machine (deux horloges, comme en `85-recette.md`).

## 1. Données reçues et leurs limites

| Relevé | Rôle qui l'a relevé | Période | Méthode | Dépôt (`mission/sources/…`) | Comparable au départ ? | Statut |
|---|---|---|---|---|---|---|
| Trois lundis de départ : durée par phase, factures, relances | gestionnaire clients | 2026-10-12, 10-19, 10-26 | chronométrage horodaté par facture, phases É1, É2, É5, É6 | `releves-de-depart-2026-10-27.md` | c'est le départ : après les simplifications, avant le flux | `[F]` n = 3, minimum 111 min, maximum 119 min |
| Quatre lundis de production : durée, factures, relances, comptes clés | gestionnaire clients ; comptable le 2026-12-28 | 2026-12-14 à 2027-01-04 | durée du premier dépôt à la dernière note | `releve-mensuel-2027-01-11.md` §1 | oui pour la séance entière et le nombre de relances ; non phase par phase (les phases du flux n'ont ni le nom ni le contenu de É1, É2, É5, É6) | `[F]` n = 3 avec le flux (55 à 62 min), 1 à la main |
| Compteurs du dispositif | responsable financier, lecture du classeur | trois lundis avec le flux | onglet « compteurs » | `releve-mensuel-2027-01-11.md` §2 | pas de départ : le dispositif n'existait pas | `[F]` comme activité, jamais comme gain |
| Opérations et factures de la plateforme | responsable financier | novembre, décembre, janvier au 10 | facture et compteur de l'éditeur | `releve-mensuel-2027-01-11.md` §3 | oui : même tarif que la page lue le 2026-10-21 | `[F]` |
| Maintenance et incidents | gestionnaire clients, responsable financier | quatre semaines | notes d'intervention du classeur | `releve-mensuel-2027-01-11.md` §4 | pas de départ ; 50 §2 : 1 h par mois `[H]` | `[F]` (heures notées) |
| Réclamations après relance, par motif | responsable du support | quatre semaines | classement par motif (méthode de Q-07) | `releve-mensuel-2027-01-11.md` §5 | oui : 13 par mois `[F]` ; même période de l'an passé non relevée | `[F]` |
| Appels aux retards de plus de 35 jours ; stock | responsable financier | période ; extraction du 2027-01-04 | décompte à la main ; extraction de S1 | `releve-mensuel-2027-01-11.md` §5 | oui : départ du 2026-10-27 | `[F]` |
| Lecture de 54 cas | comptable | relances du 2026-12-14 au 2027-01-10 | tirage fait par le responsable financier avant la lecture ; lecture hors dispositif | `lecture-echantillon-2027-01-11.md` | sans objet : pas de départ | `[F]` pour n = 54 ; 2 échecs sur 30 au tirage au hasard |
| Construction : facture et heures notées | responsable financier | — | facture payée ; heures notées par rôle | `releve-mensuel-2027-01-11.md` §6 | oui : 50 §2 | `[F]` |

Version en service pendant la période : flux 1.1 ; règles R1 jusqu'au 2026-12-14 à 10 h 12, R1.1 ensuite. Dernière version validée au registre de 90 : flux 1.1 (A-06), règles R1.1 (A-18) → identique. Une différence a existé du 2026-12-11 (modèle du niveau 2 corrigé hors registre : incident, A-17 annulée) au 2026-12-14 à 10 h 12 (approbation de R1.1, A-18) : aucune exécution n'a eu lieu dans l'intervalle, le garde-fou a refusé celle de 09 h 32 (rubrique 7). La période est **comparable**.
Règles d'exclusion écrites le 2026-12-15 (version 1.0), avant la lecture. (1) Un lundi mené à la main parce que la plateforme est indisponible compte dans le volume et dans l'adoption (IND-08 : « pannes comprises ») ; il est exclu du calcul des minutes gagnées par relance, faute de comparaison. (2) L'attente causée par un refus du garde-fou n'entre pas dans la durée de la séance, qui court du premier dépôt à la dernière note ; elle entre dans les incidents. (3) Aucun lundi n'est écarté pour sa durée, sa pointe de fin de mois ou la saison des fêtes ; la saison est nommée comme limite (le départ date d'octobre, aucune période de l'an passé n'est relevée). (4) La première période après la bascule est une montée en charge (50 §2 : 50 %, 75 %, 100 %, m = 0,75 mois `[H]`) : elle ne se lit pas comme un régime établi et compte dans le retour constaté. (5) Le résultat se montre avec et sans l'accident : rubriques 4 et 7.

**Demande de données** pour la lecture du 2027-02-08 (période du 2027-01-11 au 2027-02-07, lundis 2027-01-11, 01-18, 01-25 et 02-01). Mêmes règles d'exclusion, reconduites sans changement.

| Ce qu'on relève | Pour quel `IND-xx` ou terme de 50 | Méthode (celle du départ) | Période | Rôle qui relève | Dépôt et format | Pour le | Exclusions écrites d'avance |
|---|---|---|---|---|---|---|---|
| Les quatre lundis, comme le 2027-01-11 : durée, factures, relances, comptes clés, compteurs | IND-03, IND-05, IND-08, volume | même fiche de relevé | 2027-01-11 à 2027-02-07 | gestionnaire clients (comptable si elle tient le lundi) ; responsable financier pour les compteurs | `releve-mensuel-2027-02-08.md`, mêmes tableaux | 2027-02-08 | règles (1) à (5) |
| Le motif de chaque brouillon supprimé : sous 15 €, payée, litige, autre | IND-05, seuil de 15 € (EF-05) | une colonne « motif » dans l'onglet « compteurs » | idem | gestionnaire clients | idem | idem | — |
| Chaque appel aux retards de plus de 35 jours : date, durée, qui appelle | IND-07, part réemployée | décompte à la main | idem | gestionnaire clients appelle, responsable financier compte | idem | idem | un appel ne compte que s'il vise une facture de plus de 35 jours |
| Facture et opérations de la plateforme, janvier | IND-09, fonctionnement | facture de l'éditeur | janvier | responsable financier | idem | idem | — |
| Heures de maintenance et de supervision, avec le motif : changement de règle, défaut, lecture | IND-10, maintenance | notes d'intervention | idem | gestionnaire clients, responsable financier | idem | idem | — |
| Lecture d'échantillon : 30 cas au hasard tirés avant la lecture, les réclamations, les comptes clés et le niveau 3 | qualité (IND-11 proposé, rubrique 9) | tirage par le responsable financier, lecture par la comptable | relances de la période | comptable | `lecture-echantillon-2027-02-08.md` | idem | — |
| Réclamations par motif et par semaine ; même période de l'an passé si le support la retrouve | IND-01 | classement du support | idem | responsable du support | idem | idem | — |
| Temps de traitement d'une réclamation (14 min `[H]`) | coût d'une erreur (50 §2) | chronométrage de chaque réclamation de la période | idem | responsable du support | idem | idem | — |

## 2. Indicateurs

Seuils de 60 §14 (version 1.4), cités. Autres changements de la période : aucun changement de règle de relance (R1.1 ne corrige qu'un accent), pas d'embauche, pas de nouveau client majeur connu ; saison des fêtes (factures à traiter : 64, 60, 52, 75). Le départ de la durée (114,3 min) est la re-mesure faite après les simplifications et avant la construction (`20-diagnostic.md` §9) : l'écart ci-dessous est donc celui de la construction seule.

| Famille | `IND-xx` | Propriétaire · méthode | Départ | Observé | Écart au départ | Seuils (cités) | Position |
|---|---|---|---|---|---|---|---|
| Volume | terme de 50 §2 | gestionnaire clients · export et compteurs | 96 par mois `[F]` ; 24,3 relances par lundi (3 lundis) `[F]` | 116 relances hors comptes clés en 4 lundis (29,0 par lundi) et 19 comptes clés `[F]` | +21 % contre les 96 de 50 ; +19 % contre les trois lundis de départ (97,3 pour quatre) | — | contexte : le gain se compare par relance |
| Temps humain complet | IND-03 Durée de la séance | gestionnaire clients · minutes par séance | 156 min (2026-09-07) `[F]` ; 114,3 min sur 3 lundis, 4,70 min par relance `[F]` | 58,3 min sur 3 lundis (55 à 62), 1,94 min par relance `[F]` ; la séance à la main du 2026-12-28 : 118 min, 4,54 min par relance, hors comparaison | −56,0 min par séance (−49 %) ; −2,75 min par relance (−59 %) | correction > 60 min ; alerte > 115 min ; arrêt > 156 min deux lundis de suite | dans les seuils, de peu (le lundi 12-14 : 62 min) |
| Temps humain complet | validation des comptes clés (pas d'`IND`) | responsable financier · minutes | non chronométrée au départ (É7, `20-diagnostic.md` §1) | 10 min par lundi (11, 9, 8, 12) `[F]` | non comparable : aucun départ | — | écart non déclaré ; la lecture des compteurs (6 min par lundi) est comptée en rubrique 4 |
| Erreurs | IND-01 Réclamations après relance | responsable du support · compte par motif | 13 par mois `[F]`, soit 13,5 pour 100 relances | 8 en 4 semaines, soit 5,9 pour 100 relances envoyées `[F]` ; motifs : montant contesté 4, facture en double 2, acompte non déduit 1, autre 1, relance à tort 0 | −5 | correction > 7 par mois ; alerte > 13 ; arrêt > 13 deux mois de suite | correction (8 > 7), sous l'alerte |
| Erreurs | IND-02 Relances parties à tort | gestionnaire clients · colonne « à tort » | 9 par mois `[F]` (7 payées, 2 en litige : Q-07) | 0 `[F]` | −9 | alerte : un cas ; arrêt : deux cas dans la semaine | dans les seuils |
| Erreurs | IND-04 Relances envoyées sans validation | responsable financier · comptage | 0 `[F]` | 0 sur 105 relances du flux `[F]` | 0 | alerte et arrêt : un cas | dans les seuils |
| Qualité | IND-05 Part retirée ou corrigée | gestionnaire clients · propositions supprimées ou modifiées | aucun départ `[H]` | 26,6 % (34 sur 128 ; par lundi 24,4 ; 27,5 ; 27,7) `[F]` | — | correction > 10 % ; alerte > 20 % ; arrêt > 30 % deux lundis de suite | alerte |
| Qualité | aucun : trou de 60 §14 | comptable · échantillon lu (rubrique 6) | aucun départ | 3 échecs sur 54 cas lus, dont 2 sur 30 au tirage au hasard ; 0 par alerte `[F]` | — | aucun seuil écrit | trou de 60 : IND-11 proposé (rubrique 9) |
| Satisfaction | — | non relevée : aucun départ, aucune enquête demandée ; les remarques spontanées (un accent, les petits montants) sont dans les messages | | | | | |
| Adoption active | IND-08 Séances menées avec le dispositif | responsable financier (mesure : gestionnaire clients) · séances ÷ séances tenues | 90 % supposé `[H]` | 3 séances sur 4 = 75 % (77,6 % des relances) ; 100 % sans le lundi de panne `[F]` | — | correction < 90 % ; alerte < 87 % ; arrêt < 60 % deux mois de suite | alerte |
| Coûts d'usage | IND-09 Coût de la plateforme | responsable financier · facture et opérations | 20 € pour 600 opérations `[H]` | novembre 20 € (957 opérations) ; décembre 35 € (1 069, palier Équipe depuis le 12-24) `[F]` ; janvier : 351 au 10, environ 1 390 `[E]` | +15 € | correction > 20 € ; alerte > 24 € ; arrêt > 24 € deux mois de suite | décembre : alerte ; janvier `[E]` : arrêt de 60 §14 à la facture de janvier |
| Maintenance | IND-10 Heures par mois | responsable financier (mesure : gestionnaire clients) · notes du classeur | 1 h par mois `[H]` | 1,5 h (gestionnaire clients 0,7 h ; responsable financier 0,8 h) `[F]` | +0,5 h | correction > 1 h ; alerte > 1,1 h ; arrêt > 2 h deux mois de suite | alerte |
| Incidents | rubrique 6 | — | — | 2 incidents, 62,27 € de reprise `[F]` | — | — | — |
| Contexte | IND-06 Stock de plus de 35 jours | responsable financier · extraction de S1 | 31 factures, 29 400 € HT (2026-10-12) `[F]` | 29 factures, 27 300 € HT (2027-01-04) `[F]` | −2 factures ; −2 100 € HT | correction > 33 deux relevés de suite ; alerte > 40 | dans les seuils ; « a contribué à » (saison, gros clients) |
| Contexte | IND-07 Appels aux retards | responsable financier · décompte à la main | 0 appel (2026-10-12 au 10-26) `[F]` | 4 appels, 88 min (22 min en moyenne) `[F]` ; 29 factures concernées, nombre de clients non relevé | +4 | correction : moins de la moitié des clients concernés appelés dans le mois ; alerte : aucun appel | correction (4 appels contre 12 nommés par la direction générale) |

## 3. Business case terme par terme

| Terme (50 §2) | Estimé : bas · central · haut | Observé (période · statut) | Position | Écart au central |
|---|---|---|---|---|
| Relances par mois | 96 `[F]` | 116 hors comptes clés en 4 lundis `[F]` | terme sans éventail | +20 (+21 %) |
| Séances par mois | 4 `[E]` | 4, dont 3 avec le flux `[F]` | — | 0 |
| Minutes gagnées, par relance (par séance de 24) | 2,42 · 3,46 · 4,17 (58 · 83 · 100) | 2,75 (66,1) `[F]` | entre le bas et le central | −0,70 min (−20 %) |
| Part du temps libéré réemployée | 60 · 80 · 100 % `[H]` | 35,5 % `[F]` : 88 min d'appels pour 247,9 min libérées | sous le bas | −44,5 points |
| Taux d'adoption | 80 · 90 · 100 % `[H]` | 75 % des séances, 77,6 % des relances `[F]` | sous le bas | −15 points (séances) |
| Erreurs évitées par mois, apport | 0 · 2 · 4 `[H]` | 1 `[E]` : 13 → 8 réclamations, dont 4 attribuées à l'option 0 par 50 `[H]` | entre le bas et le central | −1 |
| Coût d'une erreur | 6,77 € `[E]` | non relevé (14 min `[H]` × 29 €) | — | — |
| Construction, option 4, première phase | 1 348 € = 900 payé + 448 mobilisés `[H]` | 1 593 € = 900 (facture) + 693 (heures notées) `[F]` | terme sans éventail | +245 € (+18 %) |
| Fonctionnement par mois | 20 € `[H]` | 35 € (facture de décembre, palier Équipe) `[F]` | terme sans éventail | +15 € |
| Maintenance par mois | 0,5 · 1 · 2 h (15,50 · 31 · 62 €) `[H]` | 1,5 h = 63,30 € `[F]` | entre le central et le haut de l'éventail en heures, côté scénario bas du gain | +0,5 h (+32,30 €) |
| Montée en charge | 50 %, 75 %, 100 % ; m = 0,75 mois `[H]` | gain brut de la première période : 52,23 €, soit 38 % de 136 € `[E]` ; une période ne suffit pas à lire m | non lue (règle 4) | — |
| Termes absents de 50 | supervision, incidents | supervision 20,80 € ; incidents 62,27 € `[F]` | — | ajoutés en rubrique 4 |

Hypothèses `[H]` de 50 §2 levées par ce relevé : la part réemployée, le taux d'adoption, la construction, le fonctionnement et la maintenance de l'option 4. Restent ouvertes : les minutes au bas et au haut, l'attribution des erreurs évitées, le coût d'une erreur, la construction et la maintenance de l'option 0, la montée en charge.

| Condition du point mort (50 §4, retour en 18 mois) | Seuil | Observé | Passe ? |
|---|---|---|---|
| Minutes retirées par séance de 24 relances | au moins 80 (50) ; au moins 84 avec la construction réelle ; au moins 127 avec les coûts relevés `[E]` | 66,1 `[F]` | non |
| Part du temps libéré réemployée | au moins 77 % | 35,5 % | non |
| Séances menées avec le dispositif | au moins 87 % | 75 % | non |
| Maintenance | au plus 1,1 h par mois | 1,5 h | non |
| Devis payé | au plus 975 € | 900 € | oui |
| Fonctionnement (70 §5 : limite de 24 € par mois) | au plus 24 € | 35 € | non |

Point mort recalculé (`chiffrer-rentabilite`, `formules.md` §6, H = 18, m = 0,75). Gain brut minimal : 131,36 € dans 50 ; 145,57 € avec la construction réelle (1 593 €) et les coûts de 50 ; 216,63 € avec la construction réelle et les coûts relevés (fonctionnement 35 €, maintenance 63,30 €, supervision 20,80 €, hors incidents). Observé : 52,23 €. Le point mort de 18 mois ne tient dans aucun cas.

## 4. Gain et coûts réels

Mêmes formules que 50 (`formules.md` §2 à §4), valeurs observées. Les 90 relances passées par le dispositif sont déjà l'adoption : elle n'est pas réappliquée. Les écarts sont calculés sur les valeurs non arrondies ; la « période » compte quatre semaines, soit les quatre séances que 50 appelle un mois.

| Ligne | Estimé (50, central, apport) | Observé | Écart | Statut |
|---|---|---|---|---|
| Gain brut par mois | 135,68 € | 52,23 € | −83,45 € (−62 %) | `[E]` : les erreurs évitées restent `[E]` |
| dont temps libéré réemployé | 123,50 € | 45,47 € | −78,03 € | `[F]` |
| dont erreurs évitées | 12,18 € | 6,77 € | −5,41 € | `[E]` |
| Construction payée (facture) | 900 € | 900 € | 0 | `[F]` |
| Construction mobilisée (heures notées) | 448 € | 693 € | +245 € | `[F]` |
| Fonctionnement par mois : abonnement | 20,00 € | 35,00 € | +15,00 € | `[F]` |
| Coûts d'usage par mois | sans objet : aucun modèle, les opérations sont dans l'abonnement | 0 € | — | — |
| Maintenance par mois | 31,00 € (1 h) | 63,30 € (1,5 h) | +32,30 € | `[F]` |
| Supervision (ligne ajoutée : absente de 50) | non estimée | 20,80 € (24 min du responsable financier) | +20,80 € | `[F]` |
| Incidents | non estimés | 62,27 € (deux incidents) | +62,27 € | `[F]` |
| Gain net par mois | 84,68 € | −129,13 € | −213,82 € | `[E]` ; −135,90 € `[F]` sans compter les erreurs évitées |
| Retour : constaté (cumul réel), projeté `[E]` (formule de 50 §4) ou « pas de retour » | 17,1 mois (apport) ; 13,2 mois (option retenue, 4 après 0) | **pas de retour** : le gain net observé est négatif (−129,13 € ; −66,87 € sans les incidents) et le cumul est de −129 € après une période | — | `[E]` |

Calcul montré (`95-mesure/calculs-v1.2.txt`).
- Minutes. Départ : 343 min ÷ 73 relances = 4,699 min par relance (3 lundis). Production : 175 min ÷ 90 relances = 1,944 min. Gain : 2,754 min par relance, soit 66,1 min pour une séance de 24 relances. Contrôle croisé : les quatre lundis réels ont duré 293 min ; faits entièrement à la main au rythme du départ ils auraient duré 545,0 min, soit 252,0 min de moins, contre 247,9 min calculées pour le flux seul. La séance à la main du 2026-12-28 (4,54 min par relance, contre 4,70) confirme que la méthode de repli n'a pas dérivé : le départ reste un bon témoin.
- Temps libéré. 90 × 2,754 ÷ 60 = 4,131 h, soit 128,07 € à 31 €. Les 88 min d'appels (4 appels de 22 min) sont 35,5 % de ces heures, en admettant qu'elles aient été prises sur le temps libéré : 128,07 × 0,355 = 45,47 € `[F]`. Le reste, 2,665 h (82,60 €), est du temps libéré non réemployé : valeur non financière, zéro euro de gain.
- Erreurs. 13 → 8 réclamations par période : 5 de moins ; 50 en attribue 4 à l'option 0 `[H]`, il en reste 1 pour l'option 4 : 1 × 6,77 € = 6,77 € `[E]`.
- Gain brut : 45,47 + 6,77 = 52,23 € `[E]`. Coûts : 35,00 + 63,30 (0,7 h × 31 + 0,8 h × 52) + 20,80 (24 min × 52 ÷ 60) + 62,27 (15,60 + 20,67 + 26,00) = 181,37 €. Gain net : 52,23 − 181,37 = **−129,13 €** `[E]`.
- Construction réelle : 900 + 693 (8 h × 31 + 5,5 h × 52 + 3 h × 34 + 1,5 h × 38) = 1 593 €. Seuil de rentabilité mensuelle : le gain brut (52,23 €) ne couvre pas fonctionnement plus maintenance (98,30 €, ou 119,10 € avec la supervision) : sur cette période le dispositif coûte plus qu'il ne rapporte.

**Avec et sans l'accident.** Période telle que relevée : −129,13 €. Sans les incidents (62,27 €) : −66,87 €. Dans les deux cas le gain net est négatif : le retour s'écrit « pas de retour », par la seule formule de 50 (`formules.md` §4 : `(construction payée + construction mobilisée + gain brut × m) ÷ gain net mensuel`), qui n'a pas de délai quand le gain net est nul ou négatif. La décision suit alors les cas du §5 de `mesure.md` (rubriques 7 et 8).

Coût de poursuite par mois `[E]`, tel que relevé et hors incidents : fonctionnement 35,00 € + maintenance 63,30 € + supervision 20,80 € = 119,10 €. Le gain brut observé (52,23 €) ne le couvre pas : il manque 66,87 € par période. Un appel de 22 min réemploie 22 ÷ 60 × 31 = 11,37 € de temps libéré : au volume et à l'adoption observés, le gain net serait nul à 87,7 % de réemploi du temps libéré (4,13 h, soit 11,3 appels de 22 min), c'est-à-dire environ 9,9 appels par période contre 4 relevés. Avec tout le temps libéré réemployé, il serait de +15,74 €, hors incidents : seuls un volume plus haut (la panne du 2026-12-28 a retiré un lundi du flux), des coûts plus bas (palier d'entrée, maintenance revenue vers 1 h) ou moins d'incidents l'augmenteraient davantage (décomposition de la rubrique 7). Les douze appels par mois nommés par la direction générale dépassent le temps libéré de la période.

## 5. Adoption et usage

| Rôle | Occurrences totales | Passées par le dispositif | Adoption active | Contournements constatés | Cause probable |
|---|---|---|---|---|---|
| Gestionnaire clients | 3 séances, 90 relances hors comptes clés | 3 séances, 90 relances | 100 % | aucun | — |
| Comptable | 1 séance, 26 relances | 0 | 0 % | la séance du 2026-12-28 menée à la main selon la fiche : repli prévu, pas un contournement | plateforme indisponible de 8 h à 14 h 30 |
| Ensemble (IND-08) | 4 séances, 116 relances | 3 séances, 90 relances | 75 % des séances, 77,6 % des relances | aucun tableur parallèle ni relance hors du flux (lecture du lundi soir du responsable financier) | la panne seule |

Usage du temps libéré : 4 appels en quatre semaines contre 12 par mois nommés par la direction générale le 2026-10-22 et le 2026-12-08, soit un tiers. Cause probable `[H]` : aucun créneau n'est réservé aux appels ; à confirmer par la gestionnaire clients.

## 6. Cas lus, échecs et incidents

Échantillon : 30 relances tirées au hasard dans la liste numérotée des 105 relances du flux (taille `[H]` d'une matinée de lecture), les 8 relances ayant donné lieu à réclamation, les 15 comptes clés et les 6 relances de niveau 3 ; 54 cas distincts après retrait des chevauchements ; tirage fait par le responsable financier avant la lecture ; lus par la comptable (elle n'a ni construit ni écrit la fiche) en 2 h 40, le 2027-01-11.

| Catégorie d'échec | Trouvés | par alerte | par lecture | par réclamation | Action |
|---|---|---|---|---|---|
| mauvaise valeur : montant (un acompte déjà reçu n'est pas déduit) | 3 | 0 | 2 | 1 | `D-07` inscrit en 85 (version 1.3) ; correction de 60 puis du flux ; mesures d'attente A-24 et A-25 (proposées) |
| autres catégories de la recette (mauvaise cible, oubli, doublon, hors règle, hors périmètre, retard) | 0 | — | — | — | — |

Taux d'échec dans l'échantillon aléatoire : 2 sur n = 30 (6,7 % ; fourchette de Wilson à 95 % : 1,8 à 21,3 % `[E]`). Part des échecs vus par une alerte : 0 sur 3. Échecs silencieux : 3. Le brouillon est conforme à l'extraction, qui ne porte que le montant hors taxes ; la personne qui relit ne peut pas voir l'écart avec le solde du logiciel de facturation. Contrôle à ajouter et à tester : T-42 en 85 à la correction, la lecture mensuelle d'un échantillon (IND-11) tout de suite ; une alerte n'est possible que si l'extraction porte le solde dû (Q-18). Les 7 autres réclamations lues sont conformes : 4 montants contestés sur le fond, 2 factures en double à la source, 1 adresse de facturation différente.

| Date | Ce qui s'est passé | Détecté par | Durée | Effet | Cause | `D-xx` · `R-xx` |
|---|---|---|---|---|---|---|
| 2026-12-14 | le flux refuse de s'exécuter à 09 h 32 | alerte « règles ou modèles modifiés hors de la version approuvée », 09 h 33 (T-22) | 40 min d'attente (09 h 34 à 10 h 14) | séance retardée ; aucune relance partie avec un texte non approuvé | le modèle du niveau 2 corrigé hors registre le 2026-12-11 (A-17 annulée, suite A-18) | aucun `D-xx` : le comportement est celui de 60 §4 ; incident du registre de 90 |
| 2026-12-28 | plateforme indisponible de 8 h à 14 h 30 (maintenance de l'éditeur annoncée le 12-21 à l'adresse de notification du compte, que personne ne lit) | vérification de 10 h de la fiche (la comptable : aucun brouillon) ; l'alerte de silence est portée par la plateforme et n'a pas pu partir | séance à la main décidée à 10 h 20 (limite : 10 h 30), 118 min | 26 relances et 4 comptes clés envoyés à la main ; 0,5 h du responsable financier | changement subi : avis de maintenance non lu | aucun `D-xx` ; `R-03` en partie |
| 2027-01-04 | une alerte « identifiant introuvable » : courriel envoyé avec l'objet modifié, ligne d'historique complétée à la main | alerte de l'étape 8 | quelques minutes, comprises dans la séance | aucun | objet modifié par la personne (T-23) | aucun `D-xx` : 60 §4 exige l'objet du brouillon |

Histoires du pré-mortem (70 §8, version 1.2) produites : n° 4 (modèle modifié sans date), le 12-14 ; signal qui a parlé : le garde-fou. N° 5 (coût de fonctionnement), en partie : 35 € en décembre ; signal : le quota de 1 000 opérations dépassé le 12-24, lu à la facture ; la parade, un relevé mensuel, ne couvrait pas un avis de maintenance envoyé à une adresse non lue. N° 7 (le flux ne s'est pas lancé), sous la forme d'une panne de la plateforme ; signal : la vérification de 10 h, pas l'alerte de silence, qui tombe avec la plateforme. N° 9 (temps libéré sans appels), en partie : 4 appels sur 12. N° 10 (petits montants, ajoutée le 2026-12-08) : IND-05 à 26,6 %. N° 11 (décision tardive de passer à la main, ajoutée le 2026-12-08) : évitée de justesse, décision à 10 h 20 pour une limite de 10 h 30. N° 8 (absence de la gestionnaire clients) : la comptable a tenu seule le lundi 12-28. Non produites : n° 1, 2, 3, 6. Histoire non prévue : une facture réglée en partie (D-07), à ajouter au pré-mortem comme n° 12 à la revue du 2027-02-08.

## 7. Cas difficiles

| Cas | Constaté ? | Constat | Conduite |
|---|---|---|---|
| Adoption nulle ou presque | non constaté | IND-08 à 75 %, en alerte (< 87 %), loin du seuil d'arrêt (< 60 % deux mois de suite) ; le seul lundi hors flux est la panne ; aucun contournement | relire à la prochaine période ; la comptable a déjà tenu un lundi avec le flux (pilote, lundi 4) |
| Gain net devenu négatif | constaté | −129,13 € sur la période contre +85 € estimés ; décomposition ci-dessous : le réemploi (−57 €) et les incidents (−62 €) pèsent le plus, les coûts d'exploitation (−68 €) et les minutes (−26 €) ensuite, le volume joue pour (+26 €) | une période, la montée en charge et deux accidents : ni accident isolé prouvé ni tendance ; la règle d'arrêt par défaut (deux périodes comparables de suite) n'est pas atteinte ; conduite : corriger (rubrique 8). Coût de poursuite par mois `[E]` : 119,10 € tel que relevé (35 + 63,30 + 20,80), hors incidents ; le retour s'écrit « pas de retour » |
| Changement non approuvé | constaté, suite décidée par A-18 ; un changement subi | (1) modèle du niveau 2 corrigé hors registre le 2026-12-11 (incident, A-17 annulée) : le garde-fou a refusé l'exécution du 2026-12-14 ; suite A-18, validée à 10 h 09 puis faite à 10 h 12 après T-08 et T-22 rejoués par l'indépendant (R1.1) ; la période reste comparable, aucune exécution n'ayant eu lieu entre la modification et le refus. (2) Maintenance de l'éditeur le 2026-12-28 : l'avis n'est arrivé à personne ; le lundi 2027-01-04 est conforme (aucun écart de comportement, la seule alerte attendue est celle de T-23) | rappeler que tout changement passe par une `A-xx` validée avant ; A-23 (adresse de notification) proposée ; aucun modèle d'IA concerné |

Décomposition du gain net, de l'estimation de 50 à l'observé, chaque terme remplacé par sa valeur observée dans cet ordre (l'ordre change la part de chacun, pas le total).

| Terme remplacé | Effet sur le gain net | Gain net après |
|---|---|---|
| 50, central | — | 84,68 € |
| volume : 96 → 116 relances hors comptes clés | +25,73 € | 110,41 € |
| adoption : 90 % → 77,6 % des relances | −22,26 € | 88,15 € |
| minutes : 3,46 → 2,75 par relance | −26,19 € | 61,96 € |
| réemploi : 80 % → 35,5 % | −56,99 € | 4,97 € |
| erreurs évitées : 2 → 1 | −3,73 € | 1,23 € |
| fonctionnement : 20 → 35 € | −15,00 € | −13,77 € |
| maintenance : 31 → 63,30 € | −32,30 € | −46,07 € |
| supervision : 0 → 20,80 € | −20,80 € | −66,87 € |
| incidents : 0 → 62,27 € | −62,27 € | −129,13 € |

Plusieurs termes sont en cause : le dispositif tient moins de minutes que prévu et coûte plus cher à faire tourner ; mais les deux plus gros écarts, le réemploi et les incidents, tiennent à un usage non organisé et à deux accidents, pas au calibrage.

## 8. Décision

Décision proposée : **corriger** — décidée par la direction générale le 2027-01-12 (simulée), avec une règle d'arrêt : si la lecture du 2027-02-08 donne un gain net observé négatif malgré les corrections, hors accident documenté, le flux s'arrête et l'on revient à l'option 0 par des actions de retrait en 90. Règles de décision par défaut `[H]` de `mesure.md` §6, confirmées par elle avec cette règle.
Trois raisons.
1. Une seule période, qui porte la montée en charge et deux accidents : le gain net est négatif (−129 € ; −67 € sans les incidents), mais la règle d'arrêt par défaut demande deux périodes comparables de suite.
2. Les causes sont nommées et réparables : le réemploi (4 appels sur 12 nommés), le palier de la plateforme (35 € au lieu de 20 €), les petits montants (IND-05 à 26,6 %), la facture réglée en partie (D-07), l'adresse de notification, la maintenance (1,5 h). Au volume et à l'adoption observés, le gain brut couvrirait les coûts relevés à environ 10 appels par période (rubrique 4) `[E]` ; le palier d'entrée, une maintenance revenue vers 1 h et l'absence d'incident abaisseraient ce seuil (décomposition de la rubrique 7).
3. Aucun seuil d'arrêt de 60 §14 n'est franchi à ce jour, et le dispositif tient ses deux promesses de fond : une séance de 58 min contre 114, et 0 relance à tort contre 9 par mois.
Ce qui la renverserait. Vers « arrêter » : un gain net négatif à la lecture du 2027-02-08 (règle ci-dessus) ; IND-09 : plus de 24 € deux mois de suite, ce que la facture de janvier produira si elle dépasse 1 000 opérations (environ 1 390 `[E]`) : 60 §14 demande alors de refaire le calcul de 50 §3 et de choisir entre l'option 3 et l'option 0, calcul que la direction générale a demandé pour le 2027-02-08 et dont la rubrique 4 est la première version ; une relance au montant faux partie après la consigne de A-24 (suspendre en attendant la correction). Vers « continuer » : un gain net positif hors accident sur la période du 2027-01-11 au 2027-02-07, avec les appels comptés (environ 10 par période au volume de cette période) et D-07 corrigé ou circonscrit.
Contre-cas le plus fort : arrêter dès maintenant. Il évite 119,10 € de coûts par mois tels que relevés `[E]`, et tant que le gain net est négatif il n'y a pas de retour à comparer au critère de 18 mois (« pas de retour »). Réponse : la construction (1 593 €) est dépensée ; ce qui compte est le gain net à venir, positif à partir d'environ 10 appels par période au volume observé ; les gains de l'option 0 ne dépendent pas du flux, ceux du flux (58 min contre 114, aucune relance à tort) s'arrêtent avec lui. Si la lecture du 2027-02-08 donne un gain net positif, le retour se calcule alors par la formule de 50 §4 sur les termes observés, et c'est à la direction générale de dire si elle maintient le critère de 18 mois pour un investissement déjà fait. `router-consulting-strategy` n'a pas été appelé : la décision suit les règles par défaut.

| Action | Rôle | Date | Passe par 90 (`A-xx`) ? |
|---|---|---|---|
| Confirmer les douze appels par mois, réserver un créneau le lundi après la séance, compter chaque appel (date, durée) | direction générale confirme ; gestionnaire clients appelle ; responsable financier compte | dès le lundi 2027-01-18 | non : aucun outil |
| Contenir D-07 par des mesures d'attente : consigne temporaire (A-24) et onglet « règlements partiels » (A-25) | responsable financier ; comptable | avant le lundi 2027-01-18 | oui : A-24, A-25 (proposées) |
| Corriger D-07 : 60 version 1.5 (cas « réglée en partie », IND-11), réponse à Q-18, flux 1.2, test T-42 et passe 5 de 85 | consultant IA (60, 80, 85) ; indépendant monte la plateforme | avant le 2027-02-08 | oui, à l'import de la version 1.2 : une `A-xx` nouvelle après la passe 5 |
| Passer la veille à 30 min et supprimer le passage de 17 h : environ 930 opérations par mois au lieu de 1 390 `[E]`, palier d'entrée dès février | responsable financier décide ; indépendant | après la passe 5 (T-06 en 30 min) | oui : A-22 (proposée) |
| Faire lire les avis de l'éditeur : adresse de notification vers un alias lu | responsable financier | dès validation | oui : A-23 (proposée) |
| Chiffrer le seuil de 15 € (EF-05) avec l'indépendant ; IND-05 passerait de 26,6 % à environ 12,5 % `[E]` | responsable financier avec l'indépendant | 2027-01-22 | non : un devis ; si accepté, 60 version 1.5, flux 1.2 et une `A-xx` |
| Relever le motif de chaque suppression de brouillon | gestionnaire clients | dès le lundi 2027-01-18 | non |
| Vérifier qu'un rappel de calendrier de 10 h, hors plateforme, est armé chez le responsable financier et la gestionnaire clients (Q-13) | responsable financier | 2027-01-18 | oui s'il est à créer |
| Refaire le calcul de 50 §3 avec le relevé de février et la facture de janvier ; ajouter l'histoire n° 12 au pré-mortem | consultant IA | 2027-02-08 | non |

Prochaine lecture : 2027-02-08 (revue du plan avant la décision de renouvellement du logiciel de facturation, `70-plan.md` étape 27) · relevés attendus : ceux de la demande de données de la rubrique 1.

## 9. Ce que la mesure change pour le portefeuille

| Paramètre ou décision | Supposé (document · version) | Observé | Cas concernés | Proposition | Propriétaire de la correction |
|---|---|---|---|---|---|
| Fonctionnement : un abonnement de compte, pas un coût de cas | 20 € relances, 20 € tri, 40 € statut (03 version 1.1 §1) | 35 € au palier Équipe pour environ 1 400 opérations par mois avec une veille toutes les 10 min ; les opérations de tous les espaces s'ajoutent sur le quota du compte (page de l'éditeur du 2026-10-21) | tri des tickets, statut de commande | refaire la ligne « fonctionnement » de 03 : un abonnement par compte, partagé par les cas montés sur la plateforme P ; estimer les opérations de chaque cas | `chiffrer-rentabilite` (03 version 1.2) |
| Part du temps libéré réemployée | 60 · 80 · 100 % (03 §1) | 35,5 % la première période, avec un usage nommé mais sans créneau réservé | tous | lire le bas de 03 comme optimiste pour un premier mois ; exiger, par cas, un usage nommé avec nombre, créneau et compteur avant la décision de construire | `chiffrer-rentabilite` |
| Adoption | 80 · 90 · 100 % (03 §1) | 75 % pannes comprises, 100 % hors panne | tous | garder le bas à 80 % ; mettre la panne de la plateforme dans le pré-mortem de chaque cas qui s'y monte | `chiffrer-rentabilite`, `planifier-deploiement` |
| Maintenance, supervision, incidents | maintenance 1 h (tri, relances), 2 h (statut) ; ni supervision ni incidents | 1,5 h dont 0,5 h de lecture de facture ; supervision 20,80 € ; incidents 62,27 € par période | tous | 1,5 h par cas au premier mois jusqu'à la lecture de février ; ajouter les lignes supervision (6 min par lundi du rôle qui lit) et incidents | `chiffrer-rentabilite` |
| Temps interne mobilisé | 448 € (50), 268 € (tri), 936 € (statut) | 693 € mesurés, +55 % | tri des tickets, statut de commande | majorer de 50 % `[H]` le temps interne mobilisé jusqu'à un second cas observé | `chiffrer-rentabilite` |
| Jalon de la vague 2 | statut de commande : décision de reprise le 2026-11-27 (04 version 1.2) | la vague 1 n'a décidé qu'un « corriger » le 2027-01-12 | statut de commande | repousser la reprise à la lecture du 2027-02-08 ; le cas reste « douteux » (25,8 mois) et sa condition de réouverture (construction sous 3 099 €) n'est pas touchée | `planifier-deploiement` (04 version 1.3) |
| Qualité lue sur échantillon | 60 §14 : IND-01 à IND-10, aucun indicateur de conformité | 3 échecs silencieux sur 54 cas lus | tri des tickets, statut de commande | ajouter IND-11 « conformité des sorties validées par une personne, sur un échantillon lu chaque mois » aux spécifications de chaque cas | `rediger-cahier-des-charges` (60 version 1.5) |

Les corrections de 03, 04 et 60 ne sont pas faites ici : chaque compétence propriétaire les écrit par version datée avec une ligne « corrigé » au journal, après confirmation de la direction générale.

## 10. Historique des revues

| Version | Date | Période | Décision | Pièce (journal) |
|---|---|---|---|---|
| 1.0 | 2026-12-15 | aucune donnée | demande de relevés et règles d'exclusion ; aucune décision de fond | journal du 2026-12-15 |
| 1.1 | 2027-01-12 | 2026-12-14 au 2027-01-10 | corriger, règle d'arrêt pour le 2027-02-08 (direction générale) | journal du 2027-01-12 ; `sources/messages-du-client-2026-11-11-au-2027-01-12.md` |
| 1.2 | 2027-01-13 | idem (relevés inchangés) | corriger, inchangé ; retour réécrit « pas de retour », régimes corrigés retirés, A-17 écrite comme incident (`95-mesure/calculs-v1.2.py`) | journal du 2027-01-13 |

## Décision attendue

Décision prise le 2027-01-12 (simulée) : corriger. Restent à la direction générale : confirmer la date de la prochaine lecture (2027-02-08) et dire, avant cette lecture, si le critère de 18 mois reste celui de la décision de continuer : tant que le gain net est négatif il n'y a pas de retour à lui comparer, la lecture du 2027-02-08 le calculera si le gain net devient positif. Au responsable financier, en 90 (version 1.2) : les actions A-22 à A-25 (A-24 et A-25 sont des mesures d'attente) et le maintien du flux en service sous D-07.
