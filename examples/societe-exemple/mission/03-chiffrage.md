# Chiffrage — ordre de grandeur du portefeuille

2026-09-18 · Demandeur, valideur et décideur : direction générale · Rédigé par : consultant IA · Sources lues : `01-cartographie-taches.md`, `02-portefeuille.md`, entretien finance (coûts horaires), entretien support, export de facturation, export des tickets
Version 1.1, précisée le 2026-09-30 : le central de la ligne « Relances » réunissait deux effets que le diagnostic sépare (note sous le tableau de la rubrique 2). Les chiffres ne changent pas.

Trois cas sont chiffrés : ceux que la direction a décidé de creuser en `02-portefeuille.md`. Les trois autres cas du portefeuille, mis en attente ou écartés, ne le sont pas.

## 1. Paramètres communs

| Paramètre | Valeur | Statut | Source, ou qui peut confirmer |
|---|---|---|---|
| Coût horaire chargé | agent de support 29 € · gestionnaire clients 31 € · responsable du support 38 € · comptable 34 € · responsable financier 52 € | `[F]` | entretien finance (tableau de paie) |
| Base | hors taxes, partout | convention | — |
| Taux d'adoption | bas 80 % · central 90 % · haut 100 % | `[H]` | responsables d'équipe ; à relever au pilote |
| Part du temps libéré réemployée | bas 60 % · central 80 % · haut 100 % | `[H]` | direction générale : appeler les retards de plus de 35 jours (33 factures au 2026-08-28 `[E]`, 22 + 11 dans l'export de facturation) et absorber la croissance ; responsable du support : former les agents |
| Montée en charge | 50 % le premier mois, 75 % le deuxième, 100 % ensuite ; manque à gagner m = 0,5 + 0,25 = 0,75 mois `[E]` | `[H]` | à caler sur le plan de déploiement |
| Horizon | 12 mois de lecture, 24 au plus | `[H]` | consultant, à confirmer par la direction générale |
| Critère d'investissement | retour en 18 mois au plus, sur le scénario central | `[F]` | entretien direction |
| Taux journalier d'un indépendant | 450 € | `[H]` | direction générale : aucun devis en source, à demander |
| Fonctionnement par mois | tri 20 € · relances 20 € · statut 40 € | `[H]` | non vérifié : aucun tarif de plateforme lu, à dater avant de signer |
| Maintenance par mois | tri 1 h · relances 1 h · statut 2 h | `[H]` | responsable du support, responsable financier |

Lecture. Le critère de la direction (18 mois sur le central) remplace le repère de 12 mois du pack dans la même logique de classement : *solide* quand le scénario bas le passe, *à mesurer d'abord* quand le central le passe et le bas non, *douteux* quand le central ne le passe pas. Le repère de 12 mois reste affiché comme alerte, avec celui de maintenance (30 à 50 % du gain brut).

## 2. Un cas par ligne, en fourchettes bas–haut

Tous les montants sont `[E]`, arrondis à l'euro ; les dérivés (gain net, délai) sont calculés sur les valeurs non arrondies. Chaque cellule s'écrit bas–haut (central). Les trois hypothèses qui varient d'un scénario à l'autre sont les minutes gagnées, la part réemployée et l'adoption ; les autres termes restent au central. La construction comprend le coût payé (jours × 450 €) et le temps interne mobilisé (heures × coût horaire).

| Cas | Gain brut/mois | Construction | Fonctionnement + maintenance/mois | Gain net/mois | Délai de retour | Hypothèse la plus fragile |
|---|---|---|---|---|---|---|
| Tri des tickets | 143–476 € (278 €) | 1 168 € = 900 € payé (2 jours) + 268 € mobilisé | 58 € = 20 € + 38 € | 85–418 € (220 €) | 15,1–3,7 mois (6,3) | minutes gagnées par ticket, de 0,5 à 0,8 `[H]` |
| Relances de factures échues | 94–319 € (190 €) | 1 950 € = 1 350 € payé (3 jours) + 600 € mobilisé | 51 € = 20 € + 31 € | 43–268 € (139 €) | 47,2–8,2 mois (15,1) | minutes gagnées par relance, de 3,2 à 5,2 `[H]`, et part réemployée |
| Statut de commande | 134–522 € (301 €) | 4 536 € = 3 600 € payé (8 jours) + 936 € mobilisé | 116 € = 40 € + 76 € | 18–406 € (185 €) | 263–12,1 mois (25,8) | part des tickets de statut qui ont une réponse type et un suivi à jour, de 40 à 75 % `[H]` |

Précision de la version 1.1 (2026-09-30). Pour les relances, le central de 4,2 min gagnées par relance réunit deux effets que `20-diagnostic.md` §9 sépare : 1,7 min viennent des simplifications, sans construction, et 3,5 min de la construction, soit 5,2 min au total, le haut de la fourchette. La ligne garde ses chiffres, qui restent un ordre de grandeur ; `50-rentabilite.md` fait foi pour ce cas.

Calculs (bas ; central ; haut). Heures libérées = occurrences × minutes gagnées ÷ 60. Gain brut = (heures libérées × part réemployée × coût horaire + erreurs évitées × coût d'une erreur) × adoption. Gain net = gain brut − fonctionnement − maintenance. Délai de retour = (construction + gain brut × 0,75) ÷ gain net.

- **Tri des tickets.** Occurrences : 1 230 par mois `[F]`. Minutes gagnées par ticket : 0,5 ; 0,65 ; 0,8 `[H]`. Heures libérées : 10,25 ; 13,33 ; 16,40 h. Valeur du temps à 29 € : 178,35 ; 309,14 ; 475,60 €. Gain brut après adoption : 142,68 ; 278,23 ; 475,60 €, soit 143 ; 278 ; 476 €. Gain net : 142,68 − 58 = 84,68 ; 278,23 − 58 = 220,23 ; 475,60 − 58 = 417,60 €, soit 85 ; 220 ; 418 €. Délai : (1 168 + 142,68 × 0,75) ÷ 84,68 = 15,1 ; (1 168 + 278,23 × 0,75) ÷ 220,23 = 6,3 ; (1 168 + 475,60 × 0,75) ÷ 417,60 = 3,7 mois. Temps interne mobilisé : 4 h × 38 € + 2 agents × 2 h × 29 € = 268 € `[H]`.
- **Relances.** Occurrences : 96 par mois `[F]`. Minutes gagnées par relance : 3,2 ; 4,2 ; 5,2 `[H]` (la durée actuelle est de 6,5 min `[H]`). Heures libérées : 5,12 ; 6,72 ; 8,32 h. Valeur du temps à 31 € : 95,232 ; 166,656 ; 257,920 €. Erreurs évitées : 13 réclamations par mois `[F]` × 25 % ; 50 % ; 70 % `[H]` = 3,25 ; 6,5 ; 9,1, à 6,7667 € chacune `[E]` (14 min × 29 € ÷ 60) = 21,992 ; 43,983 ; 61,577 €. Gain brut : (95,232 + 21,992) × 0,8 = 93,779 ; (166,656 + 43,983) × 0,9 = 189,575 ; 257,920 + 61,577 = 319,497 €, soit 94 ; 190 ; 319 €. Gain net : 93,779 − 51 = 42,779 ; 189,575 − 51 = 138,575 ; 319,497 − 51 = 268,497 €, soit 43 ; 139 ; 268 €. Délai : (1 950 + 93,779 × 0,75) ÷ 42,779 = 47,2 ; (1 950 + 189,575 × 0,75) ÷ 138,575 = 15,1 ; (1 950 + 319,497 × 0,75) ÷ 268,497 = 8,2 mois. Temps interne mobilisé : 8 h × 31 € + 4 h × 52 € + 2 h × 38 € + 2 h × 34 € = 600 € `[H]`.
- **Statut de commande.** Occurrences : 480 par mois `[F]`. Minutes gagnées par ticket : 1,2 ; 1,8 ; 2,25 `[H]` (40 % ; 60 % ; 75 % des 3 min actuelles `[H]`). Heures libérées : 9,6 ; 14,4 ; 18 h. Valeur du temps à 29 € : 167,04 ; 334,08 ; 522 €. Gain brut après adoption : 133,63 ; 300,67 ; 522 €, soit 134 ; 301 ; 522 €. Gain net : 133,63 − 116 = 17,63 ; 300,67 − 116 = 184,67 ; 522 − 116 = 406 €, soit 18 ; 185 ; 406 €. Délai : (4 536 + 133,63 × 0,75) ÷ 17,63 = 263 ; (4 536 + 300,67 × 0,75) ÷ 184,67 = 25,8 ; (4 536 + 522 × 0,75) ÷ 406 = 12,1 mois. Temps interne mobilisé : 8 h × 38 € + 2 agents × 8 h × 29 € + 4 h × 42 € = 936 € `[H]`.

## 3. Classement

- **Solides.** Tri des tickets. Le scénario bas passe le critère de 18 mois (15,1) et la maintenance pèse 27 % du gain brut bas `[E]` (38 ÷ 142,68). Le bas dépasse le repère d'alerte de 12 mois, le central non (6,3).
- **À mesurer d'abord.** Relances de factures échues. Le central passe (15,1 mois), le bas non (47,2 mois) ; la maintenance pèse 33 % du gain brut bas `[E]` (31 ÷ 93,78), dans la zone d'alerte. L'écart tient à des `[H]` qu'une mesure courte peut lever : une seconde séance chronométrée phase par phase, et le motif des 13 réclamations d'un mois. Le diagnostic de la porte « besoin connu » fournit cette mesure.
- **Douteux.** Statut de commande. Le central ne passe pas (25,8 mois contre 18) : la construction est lourde (8 jours et 936 € mobilisés) parce que le suivi du transporteur est saisi à la main. Le cas se rouvre si la construction complète tombe sous environ 3 099 € `[E]` (18 × 184,67 − 300,67 × 0,75), par exemple avec un avis d'expédition automatique ou un suivi lisible sans saisie.

## 4. Hypothèses à confirmer

| Hypothèse | Cas concernés | Qui peut la confirmer | Mesure courte proposée |
|---|---|---|---|
| Minutes gagnées par ticket (0,5 à 0,8) | tri | responsable du support | chronométrer 50 tickets classés avec et sans proposition, relecture comprise |
| Minutes gagnées par relance (3,2 à 5,2) | relances | gestionnaire clients | observer une seconde séance et chronométrer chaque phase |
| Part du temps libéré réemployée (60 à 100 %) | tous | direction générale, responsable du support | faire nommer l'usage et son échéance (appels aux retards de plus de 35 jours) |
| Part des réclamations évitées (25 à 70 %) | relances | responsable du support | classer par motif les 13 réclamations d'un mois |
| Part des tickets de statut avec réponse type et suivi à jour (40 à 75 %) | statut de commande | responsable du support, responsable logistique | échantillon de 100 tickets de statut |
| Avis d'expédition automatique possible | statut de commande | responsable financier | lire la documentation de l'éditeur du logiciel de facturation |
| Règles de classement automatiques dans l'outil de tickets | tri | responsable du support | lire la documentation de l'outil |
| Durée de construction en jours (2, 3, 8) et taux journalier | tous | direction générale, par un devis | demander un devis daté sur la base des exigences |
| Fonctionnement mensuel (20 € ; 20 € ; 40 €) | tous | direction générale | lire et dater la page de tarifs de la plateforme choisie |

## 5. Hors chiffrage

- **Valeur non financière, non convertie.** Trésorerie : 210 factures échues pour 118 500 € HT au 2026-08-28 `[F]` sont exposées, ce n'est pas un gain. Relation client : moins de relances à tort. Capacité : absorber 10 % d'activité sans embauche `[F]`. Délai de réponse du support.
- **Non chiffré, faute de mesure.** Rapprochement des paiements, demandes de devis, réapprovisionnement : mis en attente. Aide à la réponse aux réclamations : écartée.
- **Non chiffré, sans coût de construction.** La suppression du rapport hebdomadaire des ventes libérerait 3 h par mois `[E]`, soit 165 € si le temps est réemployé ; l'usage reste à nommer par le responsable des ventes.
- **Coûts hors calcul.** Formation au-delà du temps interne mobilisé ; licences d'outil non vérifiées.

## Décision attendue

Pour chaque cas : y aller (il entre dans la feuille de route), mesurer d'abord, ou ne pas y aller. Recommandation : tri des tickets, y aller ; relances de factures échues, mesurer d'abord, par le diagnostic ; statut de commande, ne pas y aller maintenant.
