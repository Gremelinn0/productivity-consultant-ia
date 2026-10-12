# Besoin — Relances de factures échues

2026-09-24 · Demandeur, valideur et décideur : direction générale · Rédigé par : consultant IA

## 1. La demande, telle qu'exprimée

> « Il faut automatiser les relances, mais pas comme en 2024. » (direction générale, entretien direction du 2026-08-27, point 4)

## 2. Reformulation

Les relances de factures échues doivent partir au bon moment, vers les bons clients et seulement quand elles sont justifiées, avec un humain qui valide chaque envoi. Le but est de soulager la trésorerie sans refaire l'erreur de 2024.

## 3. Symptôme, problème, solution demandée

| Symptôme observé | Problème supposé | Solution demandée |
|---|---|---|
| Des relances partent à des clients qui ont déjà payé ou qui sont en litige : 13 réclamations par mois `[F]` (export des tickets). La séance du lundi dure 156 min `[F]`, dont 76 min de contrôles à la main `[E]` (35 + 32 + 9). | La finance relance sur une liste qui n'est pas à jour : les paiements sont rapprochés le jeudi, les litiges ne sont connus que du support, trois règles ne sont écrites nulle part `[H]` (le responsable financier peut le confirmer). | « Automatiser les relances » : réactiver ou construire une relance automatique. |

## 4. Décision à prendre

Faut-il automatiser les relances, et par quelle voie : régler le processus seul, configurer le logiciel en place, ou construire ? Décide : la direction générale au-delà de 3 000 € ou de 100 € de coût récurrent par mois `[F]`, le responsable financier en deçà. Le responsable financier valide dans tous les cas le contenu des relances.

## 5. Parties prenantes

- Décide : la direction générale. Valide : le responsable financier (la finance), le responsable du support (la colonne « litige »).
- Utilise : la gestionnaire clients, qui prépare et envoie les relances ; la comptable, qui la remplace et fait le lettrage.
- Touchés : les agents du support (réclamations), les commerciaux (réponses sur les litiges), les clients.

## 6. Périmètre

- **Dedans** : les relances de niveaux 1, 2 et 3 (J+7, J+21, J+35), pour tous les clients, comptes clés compris avec la validation du responsable financier ; la préparation de la liste, des brouillons et du suivi ; les règles écrites ; le lettrage avant la séance ; la colonne « litige ».
- **Dehors** : le téléphone et le courrier recommandé au-delà de J+60 ; le contentieux ; le changement du logiciel de facturation ; les avoirs et gestes commerciaux ; tout envoi sans validation humaine ; les autres cas du portefeuille.

## 7. Contraintes

- Budget : accord de la direction générale au-delà de 3 000 € par projet et 100 € par mois de coût récurrent `[F]` ; retour en 18 mois au plus sur le scénario central `[F]` (entretien direction). Pour ce cas, pilote et première phase sous 3 000 € `[H]` (la direction générale peut le confirmer).
- Calendrier : plan validé avant le 2026-10-16 `[H]` ; dispositif en service avant la décision de renouvellement du logiciel de mars 2027 `[H]` (la direction générale peut les confirmer).
- Outils imposés : le logiciel de facturation (jusqu'à la décision de mars 2027), le tableur partagé, la messagerie.
- Données et sécurité : tout reste dans l'Union européenne ; les coordonnées des contacts clients sont des données personnelles à limiter ; aucun envoi sans validation humaine (règle de la direction, entretien direction).

## 8. Critères de succès

- Réclamations après relance : au plus 7 par mois `[F]` (cible proposée, acceptée par la direction générale : journal du 2026-09-24). Mesure de départ : 13 par mois `[F]` (export des tickets).
- Durée de la séance du lundi : sous 60 min `[F]` (cible proposée, acceptée par la direction générale : journal du 2026-09-24). Mesure de départ : 156 min `[F]` (séance du 2026-09-07, une seule occurrence).
- Envois validés par un humain : 100 % `[F]` (règle de la direction, entretien direction). Aujourd'hui tout est envoyé à la main.
- Temps libéré réemployé à appeler les clients en retard de plus de 35 jours : nombre d'appels par mois, à mesurer avant tout lancement (aucun appel régulier aujourd'hui selon la direction `[H]`). Stock de départ : 33 factures `[E]` (22 + 11, export de facturation).

## 9. Ce qu'on sait, ce qu'on suppose, ce qu'on ignore

Aucune question n'est reposée : le cas vient de la porte découverte, et les réponses sont dans `02-portefeuille.md` et `mission/sources/`. Ce qui manque est marqué `?`.

- `[F]` 96 relances par mois (export de facturation). Séance du 2026-09-07 : 61 factures à traiter, 24 relances envoyées, 37 écartées dont 9 déjà payées (séance). 13 réclamations après relance par mois (export des tickets). Module de relances automatiques présent et désactivé ; 210 factures échues pour 118 500 € HT au 2026-08-28 (export de facturation).
- `[H]` Environ trois plaintes en 2024 (responsable financier). Le module n'exclut peut-être ni litiges, ni comptes clés, ni petits montants (responsable financier, en lisant la documentation). Environ 25 comptes clés (responsable financier). Une suppléante qui relance dès J+3, non observée (gestionnaire clients). Enveloppe et calendrier du cas (direction générale).
- `?` Quel seuil de montant retenir : 15 € observé, « pas de seuil » déclaré ? (responsable financier). Qui tient la liste des comptes clés ? (responsable financier). Combien de jours séparent en moyenne une relance du paiement ? Non mesuré (responsable financier). Pourquoi le module de 2024 a-t-il écrit à des clients qui avaient payé ? (responsable financier).

## 10. Est-ce le bon problème ?

En partie. Automatiser telle quelle la relance reproduirait 2024. La séance du lundi montre pourquoi : le lettrage se fait le jeudi, la relance le lundi, et 9 factures sur 61 étaient déjà payées `[F]`. Trois voies plus simples sont à essayer avant toute construction, sans aucun outil : lettrer avant la séance, écrire le seuil de montant, la liste des comptes clés et la règle des litiges, partager les litiges du support avec la finance par une colonne. L'automatisation garde un sens pour les contrôles qui subsistent après cela (recherche dans le suivi, export, rédaction), mais sa taille dépend de ce que la simplification enlève déjà : l'audit le mesure. Le problème est d'abord de processus et de données (ordre du lettrage, litiges invisibles), ensuite d'outil. L'alternative la plus simple envisagée est de ne rien construire et de standardiser ; son gain n'est pas encore mesuré.

## Décision attendue

Valider la reformulation, le périmètre et les critères de succès — ou les corriger.
