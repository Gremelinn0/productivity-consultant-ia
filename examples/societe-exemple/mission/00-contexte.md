# Contexte — Société Exemple (toute l'entreprise, cinq équipes)

2026-08-31 · Demandeur et valideur : direction générale · Rédigé par : consultant IA (exemple fictif)

## 1. Fiche entreprise

- **Activité** : distributeur B2B de fournitures de bureau (papeterie, consommables d'impression, petit mobilier).
- **Taille et équipes (rôles)** : 40 personnes `[F]` : direction 3, ventes 10, finance 4, support client 8, logistique 15 (organigramme remis à l'entretien direction).
- **Outils en place** : un tableur partagé, une messagerie, un outil de tickets, un logiciel de facturation qui porte aussi les commandes et les clients (entretien direction).
- **Données et où elles vivent** : commandes, factures et clients dans le logiciel de facturation ; tickets dans l'outil de tickets ; suivi des relances et suivi des expéditions dans le tableur partagé (entretien direction).
- **Objectifs** : absorber 10 % d'activité en plus l'an prochain sans embauche `[F]` (entretien direction) ; alléger la trésorerie, que les retards de paiement pèsent ; que les équipes cessent de ressaisir les mêmes informations.
- **Contraintes** : les données clients restent dans l'Union européenne ; accord de la direction générale au-delà de 3 000 € par projet et pour tout coût récurrent de plus de 100 € par mois `[F]` ; critère d'investissement de la direction : retour en 18 mois au plus sur le scénario central `[F]` ; pas de changement de logiciel de facturation avant la décision de renouvellement de mars 2027 ; aucun poste supprimé (toutes ces contraintes : entretien direction).
- **Déjà essayé** : en 2024, les relances automatiques du logiciel de facturation ont été activées, puis coupées : elles écrivaient à des clients qui avaient déjà payé, environ trois plaintes `[H]` (le responsable financier peut confirmer).
- **Porte choisie** : découverte. La demande est « où l'IA peut-elle nous aider ? » ; la direction cite six irritants mais ne désigne aucun processus à traiter en priorité.

## 2. Sources branchées et autorisations obtenues

| Source | Nature (fichier, outil connecté, entretien, observation) | Date | Autorisation (qui, quand, périmètre) |
|---|---|---|---|
| Entretien direction (cadrage) | entretien | 2026-08-27 | direction générale, 2026-08-27 : objectifs, priorités, contraintes, budget, essais passés |
| Export des tickets, résumé de mai à juillet 2026 | fichier déposé dans `sources/` | 2026-08-28 | responsable du support, 2026-08-28 : catégories, volumes, dates ; aucun message, aucun nom |
| Export de facturation et suivi des relances, résumé de mai à juillet 2026 | fichier déposé dans `sources/` | 2026-08-28 | responsable financier, 2026-08-28 : volumes et âges des factures ; aucun nom de client |
| Outils connectés à la session | inventaire | 2026-08-31 | aucun outil connecté dans la session : rien à autoriser, rien lu |
| Entretien finance | entretien | 2026-09-02 | responsable financier, 2026-08-31 : semaine type, tâches, volumes, coûts horaires |
| Entretien support | entretien | 2026-09-03 | responsable du support, 2026-08-31 : semaine type, tâches, volumes |
| Séance d'enregistrement : relances de factures | observation : partage d'écran commenté à voix haute | 2026-09-07 | direction générale et responsable financier, 2026-08-31 ; gestionnaire clients d'accord le 2026-08-31 ; noms de clients masqués dans la transcription |

## 3. Sources manquantes

- **Entretiens avec les ventes et la logistique.** Non prévus dans cette phase. Ils empêchent de mesurer leurs tâches : durées, volumes et règles resteront en `[H]` (déclarés par la direction), et aucun de leurs cas ne pourra être classé autrement que « À creuser ». Peuvent les fournir : le responsable des ventes, le responsable logistique.
- **Procédure écrite de relance et modèles de courriel.** La direction dit qu'ils existent ; ils ne sont pas déposés. Ils empêchent de comparer la procédure théorique à la pratique observée. Peut les fournir : le responsable financier.
- **Fonctions du logiciel de facturation** (relances, rapprochement bancaire). Ni documentation ni réponse de l'éditeur : on ne sait pas ce qui existe déjà. Peut les fournir : le responsable financier, qui administre l'outil.
- **Observation du travail du support.** Non prévue ; les durées du support seront déclarées, pas observées. Peut la rendre possible : le responsable du support.
- **Devis ou tarifs de prestataires.** Aucun ; tous les coûts de construction resteront des hypothèses. Peut les demander : la direction générale, après la décision de creuser un cas.

## Décision attendue

Confirmer les sources à brancher et les équipes à écouter — ou les corriger.
