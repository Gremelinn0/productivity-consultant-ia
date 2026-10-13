# Rentabilité — Relances de factures échues

2026-10-08 · Demandeur, valideur et décideur : direction générale (critère d'investissement : retour en 18 mois au plus sur le scénario central `[F]`, entretien direction) · Rédigé par : consultant IA · Options chiffrées (de `40-solutions.md`, version 1) : 4 retenue, après 0 / 0 repli
Version 1.1, précisée le 2026-10-16 : la rubrique 2 renvoie la relecture après le pilote à `95-mesure.md`, où le réel s'écrit à côté de cette estimation, qui reste intacte. Aucun nombre ne change.

## 1. Situation de référence

Ce que le processus coûte aujourd'hui (`20-diagnostic.md`).

- 96 relances par mois `[F]`. Une séance de 156 min chaque lundi `[F]`, une occurrence ; 4 séances par mois `[E]`. Soit 10,4 h par mois et 322 € `[E]` à 31 € de l'heure `[F]`.
- Dont 76 min de contrôles à la main par séance, soit 49 % `[E]`.
- 13 réclamations après relance par mois `[F]` : au plus 3,0 h d'agent et 88 € par mois `[E]` (13 × 14 min `[H]` × 29 € `[F]`).
- 210 factures échues pour 118 500 € HT au 2026-08-28 `[F]`, dont 33 factures de plus de 35 jours pour 30 900 € HT `[E]`. C'est une exposition de trésorerie, pas un gain (rubrique 6).
- Référence après l'option 0 : séance de 115 min `[E]`. L'option 4 suit l'option 0 : elle est jugée sur ce qu'elle apporte au-dessus de ce niveau.

## 2. Hypothèses et mesure

| Terme | Valeur centrale | Basse–haute plausible | Statut | Source, ou qui peut confirmer |
|---|---|---|---|---|
| Critère d'investissement | retour en 18 mois au plus, sur le scénario central | — | `[F]` | entretien direction (`03-chiffrage.md` §1) |
| Relances par mois | 96 | — | `[F]` | export de facturation, mai à juillet 2026 |
| Séances par mois | 4 | — | `[E]` | 96 relances ÷ 24 relances par séance |
| Minutes gagnées par séance, apport de l'option 4 | 83 | 58–100 | `[E]` au central (115 − 32, temps résiduel supposé `[H]`) ; bas et haut `[H]` | gestionnaire clients : re-mesure, puis pilote |
| Part du temps libéré réemployée | 80 % | 60–100 % | `[H]` | direction générale : usage nommé en rubrique 5 |
| Taux d'adoption | 90 % | 80–100 % | `[H]` | à relever au pilote |
| Erreurs évitées par mois, apport de l'option 4 | 2 | 0–4 | `[H]` | responsable du support : classer les 13 réclamations d'un mois par motif |
| Coût d'une erreur | 6,77 € | — | `[E]` (14 min `[H]` × 29 € `[F]` ÷ 60) | responsable du support |
| Coût horaire chargé | gestionnaire clients 31 € · agent 29 € · comptable 34 € · responsable financier 52 € · responsable du support 38 € | — | `[F]` | entretien finance (tableau de paie) |
| Construction, option 4, première phase | 1 348 € = 900 € payé (2 jours × 450 €) + 448 € mobilisés (6 h × 31 € + 3 h × 52 € + 2 h × 34 € + 1 h × 38 €) | — | `[H]` | direction générale : devis daté attendu le 2026-10-09 |
| Fonctionnement, option 4 | 20 € par mois | — | `[H]` | tarif de la plateforme non lu, à dater |
| Maintenance, option 4 | 1 h par mois, soit 31 € | 0,5–2 h | `[H]` | responsable financier |
| Construction, option 0 | 383 € mobilisés (3 h × 52 € + 5 h × 31 € + 1 h × 34 € + 1 h × 38 €) | — | `[H]` | responsable financier |
| Maintenance, option 0 | 0,5 h par mois du responsable financier, soit 26 € | — | `[H]` | responsable financier |
| Montée en charge | 50 %, 75 %, puis 100 % ; m = 0,75 mois | — | `[H]` | à caler sur `70-plan.md` |
| Base et horizon | hors taxes ; 12 mois de lecture, 24 au plus | — | convention | — |

**À relever avant le déploiement**, dans l'ordre de sensibilité. 1. Minutes gagnables : chronométrer les phases É1, É2, É5 et É6 sur trois lundis consécutifs, avec un horodatage par facture (gestionnaire clients). Leur total, en moyenne sur les trois lundis, doit être au moins égal à 112 min `[E]` (80 gagnables + 32 résiduelles `[H]`, voir le point mort). 2. Usage du temps libéré : la direction générale le nomme avec une échéance, le responsable financier compte les appels passés. 3. Heures de maintenance : estimation écrite de l'indépendant, à comparer à 1 h. 4. Devis et tarif de la plateforme, datés. 5. Motif des 13 réclamations d'un mois (responsable du support).

**À relire après**, de la même façon, dans `95-mesure.md` (`mesurer-gains`), à partir des quatre lundis du pilote puis des relevés de production : minutes avec le dispositif, adoption, appels passés, heures de maintenance réelles, coût de la plateforme, factures reçues, réclamations. Le réel s'écrit à côté de l'estimation de ce document, qui reste intacte, avec l'écart ; un gain n'est un fait qu'en `95-mesure.md`.

## 3. Calcul par option

| Ligne | Option retenue : 4 après 0 | Option de repli : 0 seule | Apport de l'option 4 |
|---|---|---|---|
| Gain brut/mois | 221 € | 85 € | 136 € |
| Construction (payé + mobilisé) | 1 731 € = 900 € payé + 831 € mobilisés | 383 € = 0 € payé + 383 € mobilisés | 1 348 € = 900 € payé + 448 € mobilisés |
| Fonctionnement/mois | 20 € | 0 € | 20 € |
| Maintenance/mois | 57 € | 26 € | 31 € |
| Gain net/mois | 144 € | 59 € | 85 € |
| Délai de retour, montée en charge comprise | 13,2 mois | 7,5 mois | 17,1 mois |
| Délai de retour, payé seul | 7,4 mois | sans objet : rien n'est payé | 11,8 mois |

Tous les montants sont `[E]`, arrondis à l'euro ; les délais sont calculés sur les valeurs non arrondies. La colonne « Option retenue » additionne l'option 0 et l'apport de l'option 4, avant arrondi.

Calcul central de l'apport de l'option 4. Heures libérées : 83 min × 4 séances ÷ 60 = 5,5333 h. Valeur du temps : 5,5333 h × 31 € = 171,53 €, dont 80 % réemployés = 137,23 €. Erreurs évitées : 2 × 6,7667 € = 13,53 €. Gain brut : (137,23 + 13,53) × 90 % d'adoption = 135,68 €, soit 136 €. Gain net : 135,68 − 20 − 31 = 84,68 €, soit 85 €. Délai : (1 348 + 135,68 × 0,75) ÷ 84,68 = 17,1 mois. Payé seul : (900 + 135,68 × 0,75) ÷ 84,68 = 11,8 mois.

Calcul central de l'option 0. Heures libérées : 41 min × 4 ÷ 60 = 2,7333 h. Valeur du temps : 2,7333 h × 31 € = 84,73 €, dont 80 % réemployés = 67,79 €. Erreurs évitées : 4 × 6,7667 € = 27,07 €. Gain brut : (67,79 + 27,07) × 90 % = 85,37 €, soit 85 €. Gain net : 85,37 − 26 = 59,37 €, soit 59 €. Délai : (383 + 85,37 × 0,75) ÷ 59,37 = 7,5 mois.

Total de l'option retenue. Gain brut : 85,37 + 135,68 = 221,05 €. Coûts mensuels : 20 € de fonctionnement + 26 € + 31 € de maintenance = 77 €. Gain net : 221,05 − 77 = 144,05 €. Construction : 383 + 1 348 = 1 731 €. Délai : (1 731 + 221,05 × 0,75) ÷ 144,05 = 13,2 mois. Payé seul : (900 + 221,05 × 0,75) ÷ 144,05 = 7,4 mois.

Lecture. La décision se prend sur la dernière colonne : l'option 0 est engagée et rentable, la question est de savoir si l'option 4 se rembourse par ce qu'elle ajoute. Le total (13,2 mois) paraît meilleur parce que l'option 0 coûte peu ; il ne doit pas masquer l'apport (17,1 mois). Le délai « payé seul » dit ce que la direction sort de sa poche (11,8 mois pour l'apport) ; le délai complet porte la décision, parce que les heures des équipes sont réelles même sans facture.

Écart avec `03-chiffrage.md`. La ligne « Relances » de 03 donnait 190 € de gain brut et un retour en 15,1 mois au central. L'écart tient à deux choses : les minutes (5,2 par relance en tout ici, répartis en 1,7 par les simplifications et 3,5 par la construction selon `20-diagnostic.md` §9, contre 4,2 au central de 03) et la construction (2 jours pour la première phase au lieu de 3). 03 est précisé par sa version 1.1 du 2026-09-30 ; `50-rentabilite.md` fait foi pour ce cas.

Trois lectures du coût. Payé : 900 € pour l'option retenue, 0 € pour le repli. Mobilisé : 831 € (383 + 448) contre 383 €. Optimisé : aucun, rien n'est signé.

## 4. Trois scénarios et point mort

Sensibilité du gain net de l'apport (85 € au central), une hypothèse à la fois, les autres au central ; les écarts se calculent sur les valeurs non arrondies. Minutes de 58 à 100 : de 47 à 110 € (écart 62 €). Part réemployée de 60 à 100 % : de 54 à 116 € (écart 62 €). Maintenance de 2 h à 0,5 h par mois : de 54 à 100 € (écart 47 €). Adoption de 80 à 100 % : de 70 à 100 € (écart 30 €). Erreurs évitées de 0 à 4 : de 73 à 97 € (écart 24 €). Les trois premières font les scénarios ; adoption et erreurs évitées restent au central.

| Apport de l'option 4 | Bas | Central | Haut |
|---|---|---|---|
| Minutes · réemploi · maintenance | 58 · 60 % · 2 h | 83 · 80 % · 1 h | 100 · 100 % · 0,5 h |
| Gain brut par mois | 77 € | 136 € | 198 € |
| Gain net par mois | −5 € | 85 € | 163 € |
| Délai de retour, montée en charge comprise | ne se rembourse pas | 17,1 mois | 9,2 mois |
| Maintenance ÷ gain brut | 81 % | 23 % | 8 % |

Tous les montants sont `[E]`, arrondis à l'euro. Le bas est sous le seuil de rentabilité mensuelle : son gain brut (77 €) ne couvre pas 82 € de coûts mensuels (20 € de fonctionnement et 62 € de maintenance).

Point mort, retour en 18 mois (critère de la direction), montée en charge comprise : gain brut minimal = (1 348 + 18 × 51) ÷ (18 − 0,75) = 131,36 €, soit environ 131 € `[E]`. Les autres hypothèses restant au central, l'apport reste rentable en 18 mois tant que (seuils arrondis) :
- la construction retire au moins environ 80 min par séance (le central en retire 83) ;
- au moins 77 % du temps libéré est réemployé (central : 80 %) ;
- au moins 87 % des séances passent par le dispositif (central : 90 %) ;
- la maintenance ne dépasse pas 1,1 h par mois (central : 1 h) ;
- le devis reste sous 975 € payé, soit 2,2 jours (central : 900 €).

Sous 26 min par séance, le dispositif coûte chaque mois plus qu'il ne rapporte et ne se rembourse jamais. Au repère de 12 mois du pack, il faudrait environ 109 min par séance : seul le haut le tient (9,2 mois).

Repères d'alerte du pack. Le central dépasse le repère de 12 mois (17,1) mais respecte le critère de la direction (18), qui prime. La maintenance pèse 23 % du gain brut au central, 81 % au bas, au-dessus du repère de 30 à 50 %.

Option de repli (0), mêmes méthodes : bas 16,5 mois, central 7,5 mois, haut 4,8 mois `[E]` (réemploi 60, 80, 100 % ; adoption 80, 90, 100 % ; erreurs évitées 2, 4, 6 `[H]`). Même son bas passe le critère de 18 mois.

## 5. Temps libéré et adoption

- **Temps libéré.** 2,7 h par mois par l'option 0 et 5,5 h par l'apport de l'option 4 au central, soit 8,3 h `[E]`.
- **Usage nommé.** 1. Appeler les clients en retard de plus de 35 jours : 33 factures au 2026-08-28 `[E]`. La direction le veut et constate qu'« aujourd'hui, personne ne le fait » `[F]`. 2. Absorber 10 % d'activité en plus sans embauche `[F]` : à environ 106 relances par mois `[E]`, la séance passerait à environ 172 min sans rien changer, à environ 127 min après l'option 0 et à environ 35 min avec l'option 4 `[E]`.
- **Part réemployée.** 80 % au central `[H]`. La direction générale la confirme en nommant le premier mois d'appels et leur nombre ; sans cela, on lit le bas (60 %).
- **Adoption.** 90 % au central `[H]` : part des séances tenues avec le dispositif, pannes, suppléance et fin de mois compris. À relever au pilote.
- **Montée en charge.** 50 % le premier mois, 75 % le deuxième, 100 % ensuite ; m = 0,75 mois `[H]`, à caler sur le pilote de `70-plan.md`.

## 6. Valeur non financière

Nommée, non convertie. Trésorerie : 118 500 € HT de factures échues, dont 30 900 € HT en retard de plus de 35 jours `[E]`. Relation client : moins de relances à des clients qui ont payé ou qui sont en litige. Capacité : tenir 10 % d'activité en plus sans embauche. Qualité : fin des numéros de facture oubliés dans un courriel. Sérénité de la gestionnaire clients : moins de vérification (« la moitié de mon lundi » `[H]`).

## 7. Recommandation

Mesurer d'abord, pour l'option 4. Classement selon le critère de la direction (18 mois sur le central) : l'option 0, déjà engagée, est solide, puisque même son bas passe (16,5 mois `[E]`) ; l'apport de l'option 4 est à mesurer d'abord, puisque son central passe (17,1 mois) et que son bas ne se rembourse pas. « Mesurer d'abord » n'empêche pas de préparer la spécification et le devis : la mesure est au calendrier (trois lundis, porte de `40-solutions.md` §10) et seule la construction attend la porte.

Trois raisons :
1. Le central de l'apport passe de peu (17,1 mois contre 18) et le bas ne rembourse jamais.
2. Quatre hypothèses `[H]` sont proches de leur seuil : 83 min contre 80, 80 % contre 77 %, 90 % contre 87 %, 1 h de maintenance contre 1,1 h.
3. La mesure courte existe et suit déjà le calendrier : trois lundis sous la procédure unique, l'usage du temps libéré nommé, le devis daté.

Ce qui la renverserait :
- Vers « y aller » : la re-mesure confirme au moins 80 min gagnables par séance (phases É1, É2, É5, É6 d'au moins 112 min au total), le devis reste sous 975 € payé et la direction générale nomme l'usage du temps libéré. Ou la direction générale applique son critère (18 mois au central) et décide d'y aller dès maintenant : la construction attendrait la mesure, mais la spécification et le devis seraient prêts. Sa décision s'inscrit alors au journal.
- Vers « ne pas y aller » : moins de 80 min gagnables, un devis au-dessus de 975 €, ou plus de 1,1 h de maintenance par mois. On s'arrête alors à l'option 0.

## Décision attendue

Valider la recommandation — ou la corriger.
