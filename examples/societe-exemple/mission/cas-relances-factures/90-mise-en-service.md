# Mise en service — Relances de factures échues

2027-01-13 · Demandeur : direction générale · Responsable du cas : responsable financier · Décideur de la mise en service : responsable financier (`60-specification.md` §13) · Rédigé par : consultant IA · Version 1.2 · Sources : `60-specification.md` (version 1.4), `70-plan.md` (version 1.2), `80-construction.md` (version 1.1, fiche d'exploitation révision 5), `85-recette.md` (version 1.4)
Version 1.0 du 2026-12-15 (transmission acceptée) ; version 1.1 du 2027-01-12 : actions A-22 à A-25 proposées à la suite de la première lecture de `95-mesure.md`, surveillance renforcée et rubrique 9 mises à jour. Version 1.2 du 2027-01-13 : A-17, faite hors registre le 2026-12-11, est annulée et écrite comme un incident daté (aucune action n'est faite sans validation antérieure, et rien ne se régularise après coup) ; sa suite est A-18, validée avant d'être faite ; A-24 et A-25 sont marquées « mesure d'attente ». Aucun chiffre ni aucune autre décision déjà inscrite ne change.
**Ce qui est réel, ce qui est simulé.** Tout ce document est simulé : aucun outil réel n'a été touché. Chaque validation, chaque exécution et chaque relevé est une pièce fictive de `mission/sources/` (messages du client, compte rendu de la passe 3, relevés du pilote et de la production), et chaque ligne du journal qui s'y rapporte est marquée « (simulée) ». Seules sont réelles, hors de l'exemple, l'exécution de la maquette et celle de sa recette (`80-construction.md`, `85-recette.md`).
Solution mise en service : le flux de relances `flux_relances` version 1.1, assemblé sur la plateforme P (espace « production ») ; règles R1, puis R1.1 depuis le 2026-12-14. Environnement réel : S1 (extraction déposée), S2 (tableur partagé, classeurs de pilotage et du dispositif), S3 (boîte partagée de la finance), plateforme P (`30-exigences.md` §6). Les dates prévues sont des propositions `[H]` que le décideur confirme ; une date réelle est un fait, avec sa pièce.

## 1. Point de départ

| Élément | Lu | Pièce (livrable § · version) | Conséquence |
|---|---|---|---|
| Verdict de la recette | prêt avec réserves, prononcé le 2026-11-13 par la gestionnaire clients et le responsable financier | `85-recette.md` §10 · version 1.1 ; journal du 2026-11-13 | les cinq réserves sont acceptées comme conditions du feu vert (ligne suivante) |
| Réserves | R1 passe 3 sur la plateforme · R2 Q-14, cadence et palier · R3 Q-16, fichier réel de S1 · R4 Q-17, dossier « Envoyés » · R5 CA-08 en version 1.2, liste d'accès aux comptes clés | `85-recette.md` §10 | **R1 fermée le 2026-11-13** : 43 tests sur 43, liste prête en 1 min 52 s (`sources/passe-3-plateforme-2026-11-13.md`). **R2 tranchée le 2026-11-13** par le responsable financier, direction générale informée (`sources/messages-du-client-2026-11-11-au-2027-01-12.md`). **R3 levée le 2026-11-16** : 63 lignes lues sur 63. **R4 levée le 2026-11-20** par la règle de classement A-13. **R5 : liste relue le 2026-11-18**, trois personnes ; le premier cas d'envoi hors validation arrête le pilote (aucun cas) |
| Défauts `D-xx` ouverts | au feu vert : aucun (D-01 à D-06 corrigés en recette) ; depuis le 2027-01-12 : D-07, trouvé en exploitation | `85-recette.md` §7 · version 1.3 | D-07 : aucune action ne le contourne avant sa correction par `construire-solution` puis sa passe de `tester-solution`, sauf les mesures d'attente A-24 et A-25 ; A-22 attend la passe 5 de `85-recette.md` ; verdict relu « pas prêt pour la version en service » (journal du 2027-01-12) |
| Porte (`40-solutions.md` §10) | constatée le 2026-10-27, sept conditions sur sept | journal du 2026-10-27 ; `sources/fiche-de-porte-2026-10-27.md` | rien à faire constater |
| Lot de simplifications seules (option 0) | non : l'option 4 est construite | `70-plan.md` · version 1.2 | le registre porte toutes les actions sur les outils réels |
| Écarts avec le plan | (1) A-01 et A-02 (étape 14 de `70-plan.md`) ont été faites le 2026-10-28, avant l'ouverture de ce registre : elles y figurent, avec une validation antérieure (la porte) et un retour arrière écrit mais seulement essayé le 2026-11-13 ; (2) l'atelier de formation de la gestionnaire clients, prévu le 2026-11-12 (rubrique 7 de `70-plan.md`), a eu lieu le 2026-11-13 avec l'étape 17 ; (3) le pré-mortem a été rejoué le 2026-12-08 et la rubrique 8 de `70-plan.md` mise à jour (version 1.2) ; (4) les dates du pilote et de la bascule sont tenues | `70-plan.md` · version 1.2 | échéances redatées avec l'ancienne date ; aucune correction de valeur |

## 2. Registre des actions

Une ligne par action sur un outil réel. Une action sur l'espace d'essai relève de `80-construction.md` et de `85-recette.md` : elle n'est pas ici. Dix-sept des vingt-cinq actions sont réversibles ; les trois dont l'effet part chez un client (A-12, A-15, A-20) ne le sont pas et portent leur public, leur plafond et ce qui limite les dégâts. RF : responsable financier ; GC : gestionnaire clients. Une « mesure d'attente » contient un défaut bloquant ouvert sans modifier la solution ni ses règles : elle se propose et se valide comme les autres, et sa levée sera une `A-xx` de plus.

| ID | Action | Où (outil · environnement) | Effet externe | Réversible · retour arrière prêt | Valideur · exécutant (rôles) | Validée le · valable jusqu'au | État | Preuve |
|---|---|---|---|---|---|---|---|---|
| A-01 | Ouvrir la plateforme P (palier d'entrée) et créer le compte de service « flux-relances » | plateforme P · réel | non | oui · désactiver puis supprimer le compte, 4 min `[F]`, essayé le 2026-11-13 sur le compte de test de l'espace d'essai · prêt | RF · RF | 2026-10-27 (porte) · sans date limite | faite le 2026-10-28 | liste des comptes relue le 2026-11-13 : un compte de service nommé, aucun compte personnel |
| A-02 | Poser les trois secrets (accès-listes, accès-messagerie, accès-alerte) dans le coffre de la plateforme | plateforme P · réel | non | oui · révoquer chaque secret et en poser un neuf, 9 min `[F]`, essayé le 2026-11-13 · prêt | RF · RF | 2026-10-27 · sans date limite | faite le 2026-10-28 | les trois noms présents au coffre, relus le 2026-11-13 (noms seulement) |
| A-03 | Sauvegarde datée du 2026-11-13 : copie des classeurs de pilotage et du dispositif, liste des dossiers de la boîte partagée | S2, S3 · réel | non | sans objet (lecture) · restauration d'une copie essayée le 2026-11-13, 3 min `[F]` · prêt | RF · GC | 2026-11-13 · 2026-11-13 | faite le 2026-11-13 | copies datées déposées dans le dossier de sauvegarde |
| A-04 | Accorder au compte de service les droits de `60-specification.md` §6 sur le dépôt et S2 : lecture du dépôt et du pilotage, lecture et écriture limitée aux onglets du dispositif | S2 · réel | non | oui · retirer les droits, 2 min `[F]`, essayé le 2026-11-13 · prêt | RF · RF | 2026-11-13 · 2026-11-20 | faite le 2026-11-13 | liste des droits relue |
| A-05 | Accorder au compte de service les droits de §6 sur la boîte partagée : brouillons dans deux dossiers, lecture de « Envoyés », suppression de ses brouillons, aucun droit d'envoi | S3 · réel | non | oui · retirer les droits, 2 min `[F]`, essayé le 2026-11-13 · prêt | RF · RF | 2026-11-13 · 2026-11-20 | faite le 2026-11-13 | liste des droits relue |
| A-06 | Importer la version 1.1 du flux, inactive, dans l'espace « production » | plateforme P · réel | non | oui · supprimer la version importée, 1 min `[F]`, ou réimporter la 1.0, 22 min `[F]` (T-34 de la passe 3) · prêt | RF · RF (l'indépendant guide, sans accès) | 2026-11-13 · 2026-11-20 | faite le 2026-11-13 | version 1.1 présente et inactive, empreinte de l'export celle de la passe 3 |
| A-07 | Charger la version R1 des règles et des trois modèles dans le classeur de pilotage, et noter son approbation (version, date, empreintes) | S2 · réel | non | oui · restaurer la copie datée de A-03 et supprimer la ligne d'approbation : le flux refuse alors de s'exécuter, ce qui est l'état sûr, 3 min `[F]` · prêt | RF · RF | 2026-11-13 · 2026-11-20 | faite le 2026-11-13 | onglet « approbation » : R1, 2026-11-13, empreintes celles de `donnees-essai/` |
| A-08 | Armer les alertes : destinataires et suppléants, canal messagerie, et le second scénario d'alerte de silence avec son propre déclencheur (Q-13) | plateforme P · réel | non (messages internes) | oui · désactiver le second scénario, remettre les destinataires, 3 min `[F]` · prêt | RF · RF | 2026-11-13 · 2026-11-20 | faite le 2026-11-13 | message d'essai reçu par les quatre rôles, 2 min après l'envoi |
| A-09 | Activer le déclencheur de la veille (étapes 8 et 9), étape 8 désactivée | plateforme P · réel | non | oui · désactiver le déclencheur, 1 min `[F]` · prêt | RF · RF | 2026-11-13 · 2026-11-16 | faite le 2026-11-16 à 07 h 50 | déclencheur lu actif ; aucune ligne d'historique écrite le 2026-11-16 (T-19) |
| A-10 | Essayer le refus d'envoi du compte de service sur la vraie boîte : un brouillon de test vers l'adresse interne de la finance | S3 · réel | non : adresse interne ; si l'envoi aboutissait, un message interne | sans objet · brouillon de test supprimé | RF · RF | 2026-11-13 · 2026-11-16 | faite le 2026-11-16 à 08 h 40 | envoi refusé, tentative au journal de la boîte |
| A-11 | Essayer l'interrupteur « Suspendre » en conditions réelles | S2 · réel | non | oui · décocher la case, 10 s `[F]` · prêt | RF · GC | 2026-11-13 · 2026-11-16 | faite le 2026-11-16 (coché à 11 h 30, décoché à 11 h 45) | brouillons supprimés au passage de 11 h 40 |
| A-12 | Premier lot réel : envoyer, depuis les brouillons du flux, les relances du lundi 2 hors comptes clés | S3 · réel | oui · clients dont une facture a atteint un niveau, hors comptes clés, 40 au plus, un seul jour (2026-11-23) · RF | non · aucun ; limite : comptes clés exclus, 40 au plus, simulation lue le 2026-11-17 (tableau d'écarts du lundi 1), chaque relance relue et envoyée par la GC, message rectificatif prêt | RF · GC | 2026-11-20 · 2026-11-23 | faite le 2026-11-23 | 28 courriels envoyés, 28 lignes d'historique, `sources/releve-pilote-2026-11-23.md` |
| A-13 | Règle de classement de la boîte : tout courriel envoyé dont l'objet ne commence pas par « Facture » va dans « Envoyés – autres » (réponse à Q-17) | S3 · réel | non | oui · supprimer la règle, 1 min `[F]`, essayé sur la boîte de test le 2026-11-19 · prêt | RF · RF | 2026-11-20 · 2026-11-23 | faite le 2026-11-20 | règle active ; trois courriels de test rangés |
| A-14 | Remettre en route l'étape 8 (écriture de l'historique à l'envoi) | plateforme P · réel | non | oui · désactiver l'étape, 1 min `[F]` (T-19) · prêt | RF · RF | 2026-11-20 · 2026-11-23 | faite le 2026-11-20 après A-13 | un courriel de test envoyé depuis un brouillon : sa proposition passe à « envoyée » |
| A-15 | Lot suivant : envoyer les comptes clés du lundi 2 (RF), puis les relances des lundis 3 et 4 | S3 · réel | oui · clients dont une facture a atteint un niveau, 60 relances au plus par lundi, comptes clés compris, du 2026-11-24 au 2026-12-08 · RF | non · aucun ; limite : plafond de 60, relecture de chaque brouillon, premier lot lu le 2026-11-24 (28 courriels, 0 réclamation à 24 h), arrêt au premier signal de `60-specification.md` §13, message rectificatif prêt | RF · GC, comptable, RF | 2026-11-24 · 2026-12-08 | faite les 2026-11-24, 11-30 et 12-07 | comptes clés 5, 6 et 5 ; relances 37 et 30 ; `sources/releve-pilote-2026-11-30.md`, `-12-07.md` |
| A-16 | Ajouter un seuil de montant de 15 € aux règles (version R2), à la demande de la GC | S2 · réel | non | oui · restaurer R1, 3 min `[F]` · prêt | RF · RF | refusée le 2026-11-27 | annulée | message du RF du 2026-11-27 ; onglet « approbation » : R1 inchangée jusqu'au 2026-12-14 |
| A-17 | Corriger l'accent de « échéance » dans le modèle du niveau 2 (R1 devient R1.1), remarque de la comptable du 2026-12-07 | S2 · réel | non | oui · restaurer le modèle R1 depuis la copie de A-03, 2 min `[F]` · prêt | RF · RF | proposée le 2026-12-08, jamais validée | annulée : le changement a été fait hors registre le 2026-12-11 (incident ci-dessous), la suite est A-18 | garde-fou T-22 : flux refusé à 09 h 32 le 2026-12-14 ; journal du 2027-01-13 |
| A-18 | Garder le texte corrigé du modèle du niveau 2 (R1.1) et noter son approbation (version, date, empreintes), suite de l'incident du 2026-12-11 | S2 · réel | non | oui · supprimer la ligne : le flux refuse alors de s'exécuter, 1 min `[F]` ; ou restaurer le modèle R1 depuis la copie de A-03, 2 min `[F]` · prêt | RF · RF | 2026-12-14 à 10 h 09, après la relecture du changement et T-08 et T-22 rejoués à 10 h 08 · 2026-12-14 | faite le 2026-12-14 à 10 h 12 | onglet « approbation » : R1.1 ; flux relancé à 10 h 14 |
| A-19 | Sauvegarde datée du vendredi 2026-12-11 : classeurs et export du flux | S2, plateforme P · réel | non | sans objet (lecture) · restauration essayée à A-03 · prêt | RF · GC | 2026-12-10 · 2026-12-11 | faite le 2026-12-11 à 12 h 05 | copies datées déposées |
| A-20 | Bascule : séance du lundi 2026-12-14 avec le flux seul, case « Suspendre » décochée, ancienne méthode conservée en repli ; puis chaque lundi | plateforme P, S3 · réel | oui · clients dont une facture a atteint un niveau, 100 propositions au plus par lundi (plafond du flux, `60-specification.md` §7), comptes clés compris, chaque relance relue et envoyée par une personne · RF | non · aucun ; limite : plafond du flux, relecture, interrupteur, seuils d'arrêt de §14, ancienne méthode disponible jusqu'à la sortie de la surveillance renforcée, message rectificatif prêt | RF · GC (suppléante : comptable) | 2026-12-10 · tant qu'aucun seuil d'arrêt n'est franchi | faite le 2026-12-14 | séance de 62 min, 29 courriels et 5 comptes clés ; `sources/releve-mensuel-2027-01-11.md` |
| A-21 | Envoyer la note de mise en production (une page) à l'équipe finance, au support et à la direction générale | messagerie · réel | non (messages internes) | non · aucun ; limite : message rectificatif prêt | RF · RF | 2026-12-10 · 2026-12-11 | faite le 2026-12-11 | note envoyée |
| A-22 | Passer la veille à 30 min le lundi et supprimer le passage de 17 h (déclencheur de la veille) | plateforme P · réel | non | oui · remettre les valeurs de A-09, 1 min `[H]` · à essayer avant la validation | RF · RF | validation attendue ; prérequis : `60-specification.md` version 1.5 (T-06 en 30 min, D-07), version 1.2 du flux, passe 5 de `85-recette.md` (T-06, T-12, T-19 et T-42) | proposée le 2027-01-12 | — |
| A-23 | Faire pointer l'adresse de notification du compte de la plateforme vers un alias lu par le RF et la GC (avis de maintenance de l'éditeur) | plateforme P · réel | non | oui · remettre l'adresse précédente, 1 min `[H]` · à essayer | RF · RF | validation attendue | proposée le 2027-01-12 | — |
| A-24 | Mesure d'attente : message de consigne temporaire à la GC et à la comptable : avant d'envoyer, retirer ou corriger les brouillons des factures de l'onglet « règlements partiels » (D-07) | messagerie · réel | non (messages internes) | non · aucun ; limite : message rectificatif prêt | RF · RF | validation attendue ; prérequis : A-25 faite | proposée le 2027-01-12 | — |
| A-25 | Mesure d'attente (D-07) : créer l'onglet « règlements partiels » dans le classeur de pilotage (numéro de facture, solde dû), tenu par la comptable à chaque lettrage | S2 · réel | non | oui · supprimer l'onglet, 1 min `[H]` · à essayer | RF · comptable | validation attendue | proposée le 2027-01-12 | — |

États : proposée · validée · faite · annulée (A-16, A-17) · revenue en arrière (aucune à ce jour : le repli à la main du 2026-12-28, un lundi de panne de la plateforme, applique la fiche d'exploitation, il ne défait aucune action). Règles vérifiées sur ce tableau : la validation précède l'exécution, sans exception (A-17, faite hors registre, n'est pas validée après coup : elle est annulée, voir l'incident ci-dessous) ; aucune action réversible n'est validée sans retour arrière prêt, sauf A-01 et A-02 (écart de la rubrique 1) ; chaque effet externe nomme son public et son plafond.

**Incident du 2026-12-11 : modèle du niveau 2 corrigé hors registre (A-17 annulée).** Le vendredi 2026-12-11, après la sauvegarde A-19, le responsable financier a corrigé l'accent dans le modèle du niveau 2 sans que A-17, proposée le 2026-12-08, soit validée, et sans noter d'approbation. Le lundi 2026-12-14 à 09 h 32 le garde-fou « changement non approuvé » (T-22) a refusé l'exécution ; aucune relance n'est partie avec le texte non approuvé et aucune exécution n'a eu lieu entre le 2026-12-11 et le 2026-12-14 : la mesure reste comparable. Rien ne se régularise après coup : A-17 n'est pas validée, elle est annulée, et la suite est proposée en A-18 (garder le texte corrigé et noter son approbation). Le propriétaire a relu le changement (un accent), l'indépendant a rejoué T-08 et T-22 dans l'espace d'essai à 10 h 08 (conformes, consignés en `85-recette.md`, version 1.2), puis le propriétaire a validé A-18 à 10 h 09 et l'a faite à 10 h 12. Son message du 2026-12-14, conservé tel que reçu, parle d'une validation de A-17 « après coup » : elle ne compte pas, seule la validation de A-18 en est une. Les versions 1.0 et 1.1 de ce document écrivaient A-17 « régularisée » : corrigé en version 1.2 (journal du 2027-01-13).

### Fiches d'action

Quatre actions ne sont pas triviales : l'import, le chargement des règles, le premier lot réel et la bascule. Les autres se font en un geste vérifiable, leur retour arrière tient dans la colonne du registre.

#### A-06 — Importer la version 1.1 du flux, inactive
Prérequis : passe 3 réussie ; A-01, A-02 et A-03 faites · Exécutée par : responsable financier, l'indépendant guide par visioconférence sans accès à l'espace · Durée prévue `[H]` : 20 min
Pas à pas : 1. L'indépendant dépose l'export de la version 1.1 (fichier sans secrets) dans le dossier de dépôt. 2. Le responsable financier ouvre l'espace « production » et importe le fichier ; l'import ne crée aucun déclencheur. 3. Il relie les trois connexions aux trois secrets du coffre. 4. Il vérifie que le scénario est inactif et que l'empreinte de l'export est celle que l'indépendant a notée à la passe 3. 5. Il note la version 1.1 dans l'onglet « approbation » du classeur du dispositif.
Effet attendu : le flux 1.1 existe dans l'espace production, inactif ; aucune exécution n'a eu lieu.
Si ça se passe mal — signal : le scénario se déclenche à l'import, ou l'empreinte diffère · retour arrière pas à pas : 1. désactiver le scénario ; 2. le supprimer ; 3. au besoin importer l'export de la version 1.0 ; 4. relire l'empreinte · temps mesuré à l'essai `[F]` : 1 min pour supprimer, 22 min pour réimporter la 1.0 · comment on vérifie que l'état d'avant est revenu : la liste des scénarios de l'espace production est vide, ou ne porte que la 1.0 inactive.
Secrets : accès-listes, accès-messagerie, accès-alerte, dans le coffre de la plateforme, propriétaire responsable financier ; jamais la valeur.

#### A-07 — Charger R1 et noter son approbation
Prérequis : A-03 et A-04 faites · Exécutée par : responsable financier · Durée prévue `[H]` : 15 min
Pas à pas : 1. Ouvrir le classeur de pilotage (la copie de A-03 est gardée). 2. Écrire dans l'onglet « règles » la version R1 : délais de 7, 21 et 35 jours, limite de 60 jours, plafond de 100 propositions, fraîcheur d'un jour ouvré, jours fériés, reprises à 1, 5 et 15 min, heure du silence à 10 h, puis les trois modèles. 3. Relire les trois modèles. 4. Lancer le module « empreintes » du flux, qui affiche l'empreinte des règles et celle des modèles. 5. Noter dans l'onglet « approbation » : version R1, date, les deux empreintes, rôle de l'approbateur.
Effet attendu : le flux accepte de s'exécuter ; un modèle modifié ensuite sans nouvelle approbation le fait refuser (T-22).
Si ça se passe mal — signal : le flux refuse de s'exécuter au premier lancement · retour arrière : restaurer la copie datée de A-03, supprimer la ligne d'approbation · temps mesuré `[F]` : 3 min · état d'avant revenu : l'onglet « règles » est identique à la copie, le flux refuse de s'exécuter.
Secrets : sans objet.

#### A-12 — Premier lot réel (lundi 2)
Prérequis : A-03 à A-11 faites ; Q-16 et Q-17 levées ; simulation lue (tableau d'écarts du lundi 1, le 2026-11-17) ; A-13 et A-14 faites ; message rectificatif relu · Exécutée par : gestionnaire clients ; le responsable financier relit le lot le lendemain · Durée prévue `[H]` : la séance du lundi
Pas à pas : 1. Le lundi 2026-11-23 la gestionnaire clients dépose l'extraction et lance le flux. 2. Elle relit chaque brouillon hors comptes clés, le corrige ou le supprime, puis l'envoie : 40 au plus. 3. Les comptes clés restent dans « Comptes clés à valider » ; ils ne partent pas ce jour. 4. Au-delà de 40 envois elle s'arrête : les brouillons restants sont supprimés, les factures reviennent à la liste suivante (EF-01). 5. Le mardi 2026-11-24 le responsable financier relit les copies envoyées avant de valider A-15.
Effet attendu : jusqu'à 40 courriels partis du compte de la gestionnaire clients, une ligne d'historique chacun, aucune alerte.
Aucun retour arrière (envoi) : ce qui limite les dégâts : plafond de 40 clients, comptes clés exclus, simulation du lundi 1 lue, relecture de chaque brouillon par une personne. Message rectificatif prêt : « Nous vous prions de ne pas tenir compte de notre message du <date> relatif à la facture <numéro> : il a été envoyé par erreur. » ; envoyé par la gestionnaire clients, après accord du responsable financier, au seul client concerné.
Secrets : sans objet.

#### A-20 — Bascule
Prérequis : fin du pilote décidée « continuer » (2026-12-08) ; A-19 faite ; étape 8 vérifiée active le vendredi ; interrupteur essayé (A-11) ; la comptable joignable le lundi · Exécutée par : gestionnaire clients, avec le responsable financier · Durée prévue `[H]` : une séance
Pas à pas : 1. Le vendredi 2026-12-11 : A-19, puis le responsable financier vérifie que l'étape 8 est active. 2. Le lundi 2026-12-14 vers 09 h 30 : la gestionnaire clients dépose l'extraction et lance le flux. 3. Elle relit, corrige et envoie. 4. À midi, le responsable financier lit les compteurs et les alertes (6 min). 5. Le soir, il compare le nombre de courriels du dossier « Envoyés » au nombre de lignes de l'historique.
Effet attendu : une exécution au journal avant 10 h, des lignes d'historique écrites par le flux, aucun écart le soir.
Si ça se passe mal — signal : un seuil d'arrêt de `60-specification.md` §13 ou §14, ou une alerte non traitée à 12 h le lundi · retour arrière pas à pas : 1. cocher « Suspendre » (responsable financier ou gestionnaire clients) ; 2. la gestionnaire clients reprend la séance à la main le même lundi, procédure unique de `20-diagnostic.md` §7 ; 3. le soir, comparer « Envoyés » et historique ; 4. supprimer les brouillons non envoyés · temps mesuré `[F]` : 10 s pour la case (A-11) ; les relances déjà envoyées ne se défont pas (message rectificatif) · comment on vérifie que l'ancienne méthode a repris : la séance du lundi est tenue à la main, la comparaison du soir est sans écart.
Aucun retour arrière pour les envois : plafond de 100 propositions, relecture, ancienne méthode disponible.

## 3. Feu vert du pilote

Décideur : le responsable financier (`60-specification.md` §13). Critères : ceux de §13, signés sans changement le 2026-11-13 (la version 1.4 de la spécification ne modifie que les cas de refus, le verrou et les questions Q-16 et Q-17).

| Condition | Pièce | Remplie ? |
|---|---|---|
| Recette prononcée : « prêt avec réserves », réserves acceptées en rubrique 1 | `85-recette.md` version 1.1 ; journal du 2026-11-13 | oui |
| Aucun défaut bloquant ouvert | D-01 à D-06 corrigés, aucun bloquant | oui |
| Porte constatée | journal du 2026-10-27 | oui |
| Fiche des critères du pilote signée, sans changement depuis | fiche du 2026-11-13 (`60-specification.md` §13) | oui |
| Actions de préparation faites, chacune avec sa preuve | A-01 à A-08 faites ; A-09 à faire le 2026-11-16 à 07 h 50 | oui, A-09 en condition |
| Interrupteur essayé en conditions réelles, retour à l'ancienne méthode décrit | T-18 en recette et sur la plateforme (passe 3) ; en réel : A-11 au lundi 1 | en condition : A-11 au lundi 1 |
| Alertes essayées de bout en bout, destinataires et suppléants joignables | message d'essai reçu par les quatre rôles (A-08) ; alerte de silence de 10 h au lundi 1 | en condition : alerte de 10 h reçue au lundi 1 |
| Mode opératoire déroulé par quelqu'un qui ne l'a pas écrit | la comptable, le 2026-11-13, fiche révision 2 : trois lacunes, corrigées dans la révision 3 (rubrique 8) | oui |
| Surveillance renforcée organisée | rubrique 4 | oui |
| Utilisateurs du pilote prévenus et formés au niveau requis | rubrique 7 : la GC formée le 2026-11-13, la comptable a essayé la fiche, le support prévenu le 2026-11-09 | oui |
| Sauvegarde datée de ce que le pilote modifie ; plafonds des effets externes en place | A-03 ; plafonds de A-12 et A-15 | oui |
| Pour tout effet externe : simulation lue par le valideur, premier lot réduit choisi, message rectificatif prêt | le lundi 1, en parallèle, n'a aucun effet externe : c'est la simulation ; A-12 (lot réduit) est validée après sa lecture ; message rectificatif relu | en condition : A-12 validée après la lecture du 2026-11-17 |

Décision : **feu vert avec conditions** — responsable financier, 2026-11-13 (simulée). Conditions : A-09 faite avant le lundi 1 ; A-10 et A-11 réussies et alerte de 10 h reçue au lundi 1, sans quoi le lundi 2 n'a pas lieu (responsable financier, 2026-11-16) ; Q-16 levée au lundi 1 (responsable financier avec l'indépendant, 2026-11-16) ; liste d'accès aux comptes clés relue avant le lundi 2 (responsable financier, 2026-11-18) ; A-13 et A-14 validées après la réponse à Q-17, A-12 validée après la lecture de la simulation (responsable financier, 2026-11-20). Le lundi 1 se tient en parallèle. Q-14 : cadence de 10 min conservée, palier à 35 € accepté pour novembre et décembre au plus, direction générale informée (retour de l'apport projeté à 20,8 mois `[E]` à ce palier) ; la facture de décembre se lit au relevé du 2027-01-11.

## 4. Pilote

Périmètre, dates et mode : `70-plan.md` §3 (version 1.2) et `60-specification.md` §13. Les relevés sont ceux de `mission/sources/` ; chaque valeur `[F]` y renvoie.

| Date | Séance ou jour | Mode | Relevés (`IND-xx` · valeur · source) | Écarts expliqués un à un | Incidents · `D-xx` | Décision du jour |
|---|---|---|---|---|---|---|
| 2026-11-16 | lundi 1 | parallèle, étape 8 désactivée (T-19) | IND-02 : 0 · IND-04 : 0 · IND-03 et IND-08 non comptés · séance à la main 121 min `[F]` · `releve-pilote-2026-11-16.md` | 8 lignes : 5 factures sous 15 €, 1 facture payée lundi matin, 2 « à traiter à la main » relancées après correction | aucun incident ; A-09 à A-11 réussies ; alerte de 10 h reçue à 10 h 01 ; Q-16 levée (63 lignes sur 63) | lundi 2 autorisé sous A-12 après lecture du tableau (2026-11-17) |
| 2026-11-23 | lundi 2 | préparation avec validation, premier lot sous A-12 | IND-03 : 57 min · IND-05 : 25,6 % · IND-02 : 0 · IND-04 : 0 · IND-08 : 1 sur 1 · `releve-pilote-2026-11-23.md` | sans objet (rien à comparer à la main) | aucun | A-15 validée le 2026-11-24 après lecture du lot |
| 2026-11-30 | lundi 3, fin de mois | préparation avec validation, A-15 | 81 factures contre 61 le 2026-09-07 · IND-03 : 64 min · IND-05 : 26,9 % · IND-02 : 0 · IND-04 : 0 · `releve-pilote-2026-11-30.md` | sans objet | double lancement refusé (T-12, T-30) ; redémarrage de la plateforme à 09 h 47, 17 brouillons déjà créés adoptés, aucun doublon (T-15b, T-29) ; aucun `D-xx` | on continue ; A-16 refusée le 2026-11-27 (demande de seuil) |
| 2026-12-07 | lundi 4, tenu par la comptable | préparation avec validation, A-15 | IND-03 : 58 min · IND-05 : 25,6 % · IND-02 : 0 · IND-04 : 0 · IND-08 : 1 sur 1 · `releve-pilote-2026-12-07.md` | sans objet | deux alertes « identifiant introuvable » (objet modifié, T-23), traitées seule ; litige signalé en séance, brouillon retiré en 7 min (T-06) ; remarque sur l'accent → A-17 proposée | fin du pilote décidée le 2026-12-08 |
| 2026-12-14 | lundi de bascule | réel | IND-03 : 62 min · IND-05 : 24,4 % · 29 relances et 5 comptes clés · `releve-mensuel-2027-01-11.md` | sans objet | flux refusé à 09 h 32 (modèle modifié hors version approuvée : incident du 2026-12-11, A-17 annulée) ; A-18 validée à 10 h 09 puis faite à 10 h 12 ; relancé à 10 h 14 ; aucun `D-xx` | bascule maintenue |
| 2026-12-21 | surveillance renforcée | réel | IND-03 : 55 min · IND-05 : 27,5 % · 29 relances et 4 comptes clés | sans objet | aucun | — |
| 2026-12-28 | surveillance renforcée | réel, repli à la main | séance à la main de 118 min par la comptable (GC en congé) · aucune opération du flux | sans objet | plateforme indisponible de 08 h à 14 h 30 (maintenance de l'éditeur annoncée sur une adresse non lue) ; absence de brouillons constatée à 10 h, décision de passer à la main à 10 h 20 ; changement subi | repli à la main (fiche d'exploitation) ; A-23 proposée le 2027-01-12 |
| 2027-01-04 | surveillance renforcée | réel | IND-03 : 58 min · IND-05 : 27,7 % · 32 relances et 6 comptes clés | sans objet | une alerte « identifiant introuvable » (courriel envoyé avec l'objet modifié), ligne complétée à la main | — |

**Surveillance renforcée** — du premier jour du pilote jusqu'à un critère de sortie écrit, après la bascule.

| Ce qu'on lit | Qui (rôle) | Rythme | Seuil qui déclenche | Action |
|---|---|---|---|---|
| Brouillons créés, journal et compteurs de l'exécution | GC (comptable en suppléance) | chaque lundi à 10 h, puis en fin de séance | aucun brouillon à 10 h ; file des échecs non vide | séance à la main décidée à 10 h 30 au plus tard ; rejouer la file |
| Alertes reçues | RF (suppléant : GC) | au fil de l'eau le lundi, relevé à midi | alerte non traitée à 12 h | cocher « Suspendre », séance à la main |
| Courriels du dossier « Envoyés » et historique | RF | chaque lundi soir pendant deux mois, puis chaque mois | écart entre les deux | alerte « double envoi » ou « envoi hors validation » : suspendre |
| Durée de la séance et relances retirées ou corrigées (IND-03, IND-05) | GC | chaque lundi | IND-03 au-dessus de 60 min ; IND-05 au-dessus de 20 % | lecture par phase ; motifs de retrait listés |
| Réclamations après relance (IND-01, IND-02) | responsable du support | chaque semaine | un cas de relance à tort | suspendre, chercher la cause avant le lundi suivant |
| Opérations facturées de la plateforme (IND-09) | RF | chaque semaine, facture chaque mois | quota de 1 000 atteint | noter la date, appliquer la décision de Q-14 |

Durée et critère de sortie `[H]` : trois lundis de suite menés avec le flux, sans alerte non traitée à 12 h, avec IND-03 au plus à 60 min et IND-08 d'au moins 87 % sur les quatre derniers lundis. Constructeur joignable jusqu'au 2027-01-13 (garantie de 30 jours après la bascule). Retour au rythme de revue de `70-plan.md` §6 à la sortie. **État au 2027-01-12 : non sortie.** Le lundi 2026-12-28 est mené à la main ; la série repart au 2027-01-04 ; les lundis 2027-01-11, 2027-01-18 et 2027-01-25 menés avec le flux sans alerte non traitée donneraient une sortie au plus tôt le 2027-01-25. L'ancienne méthode reste disponible jusqu'à cette sortie.

## 5. Fin du pilote

Décideur : le responsable financier (`60-specification.md` §13) ; décision du 2026-12-08 (simulée), direction générale informée. Le pré-mortem a été rejoué le même jour, avant la décision.

**Pré-mortem rejoué (`70-plan.md` étape 22, version 1.2).** Deux feuilles individuelles, écrites seules par la gestionnaire clients et la comptable le 2026-12-08 (`sources/messages-du-client-2026-11-11-au-2027-01-12.md`). Gestionnaire clients : les petits montants à supprimer chaque lundi (nouvelle histoire n° 10), le risque d'envoyer à un client qui vient de payer (histoire n° 2, T-13 le couvre), le lundi de fin de mois (pointe mesurée le 2026-11-30 : 64 min). Comptable : décider trop tard de passer à la main le jour d'une indisponibilité de la plateforme (nouvelle histoire n° 11), le fichier du rapprochement à mettre à jour (révision 3 de la fiche), les alertes « identifiant introuvable » (T-23, fiche). Les histoires n° 10 et n° 11 sont classées « à mitiger » ; aucune objection n'est bloquante.

| Critère (cité) | Seuil (cité) | Mesuré (période · source · statut) | Atteint ? |
|---|---|---|---|
| Généralisation : IND-03, moyenne des lundis 2 à 4 | 60 min au plus `[F]` (§13) | 59,7 min `[F]` : 57, 64 et 58 min (n = 3, minimum 57, maximum 64) ; lundis des 2026-11-23, 11-30, 12-07 · relevés du pilote | oui, de peu |
| IND-04 : relances envoyées sans validation | aucune | 0 sur 95 relances et 16 comptes clés `[F]` | oui |
| IND-02 : relances à tort imputables au flux | aucune | 0 `[F]` | oui |
| Maintenance | 1,1 h par mois au plus `[E]` | 0,9 h sur les quatre semaines `[F]` (GC 0,5 h ; RF 0,4 h) | oui |
| Condition du plan (`70-plan.md` étape 23) | la comptable a tenu une séance de pilote | lundi 4 : 58 min, sans appel `[F]` | oui |
| Arrêt du pilote | une relance sans validation ; deux relances à tort dans la semaine ; plus de 115 min `[E]` deux lundis de suite | aucun seuil franchi `[F]` | oui |
| Prolongation | séance entre 60 et 115 min en moyenne | sans objet (59,7 min) | — |

Hypothèses `[H]` de `50-rentabilite.md` levées par le pilote : aucune. Un pilote d'un mois ne déclare aucun gain ; il lit la montée en charge d'une équipe. Non levées, elles passent à `mesurer-gains` : temps résiduel de 32 min `[H]` (la séance entière dure 59,7 min en moyenne au pilote, à lire par relance), part du temps libéré réemployée (les appels commencent le 2026-12-21), adoption, maintenance sur le régime établi, erreurs évitées.
Décision : **continuer** — responsable financier, 2026-12-08, direction générale informée. Motif : les critères signés sont atteints, de peu pour la durée. Seconde phase (EF-05, EF-09, EF-13, EF-14, EF-15) : pas de décision avant le premier relevé de production, parce que le gain observé du pilote ne justifie pas encore 450 € `[H]`.

## 6. Bascule

| Élément | Contenu |
|---|---|
| Jour et heure `[H]` | lundi 2026-12-14, lancement vers 09 h 30 ; réel : 10 h 14, après le refus du garde-fou à 09 h 32 |
| Ordre des étapes | vendredi 2026-12-11 : A-19, étape 8 vérifiée active, A-21 ; lundi 2026-12-14 : lancement par la gestionnaire clients, comptable joignable ; midi : le responsable financier lit les compteurs ; soir : comparaison « Envoyés » et historique |
| Actions du jour | A-19 (sauvegarde du vendredi), A-20, A-21 ; A-18 (suite de l'incident, A-17 annulée) |
| Version mise en service | flux 1.1 ; règles R1.1 (approbation du 2026-12-14 à 10 h 12) |
| Retour arrière | signal : un seuil d'arrêt de `60-specification.md` §13 ou §14, ou une alerte non traitée à 12 h le lundi · déclenché par le RF ou la GC · comment : case « Suspendre », séance à la main le même lundi · vérification : séance tenue à la main, comparaison du soir sans écart (fiche A-20) |
| Lectures du premier jour | GC à 10 h (les brouillons existent) · RF à midi (compteurs, alertes) · RF le soir (« Envoyés » contre historique) |
| Seuils d'arrêt en vigueur | ceux de `60-specification.md` §14 : IND-04 un cas ; IND-02 deux cas dans la semaine ; IND-03 plus de 156 min deux lundis de suite ; IND-01 plus de 13 par mois deux mois de suite ; IND-05 plus de 30 % deux lundis de suite ; IND-08 moins de 60 % deux mois de suite ; IND-09 plus de 24 € deux mois de suite ; IND-10 plus de 2 h par mois deux mois de suite |
| Ancienne méthode | conservée jusqu'à la sortie de la surveillance renforcée (rubrique 4) : pas sortie au 2027-01-12 |
| Communication | A-21, note du 2026-12-11 |

Décision : **bascule** — responsable financier, 2026-12-10 (simulée) ; faite le 2026-12-14. Premier jour : séance de 62 min, 29 relances et 5 comptes clés ; le flux a commencé à 10 h 14 ; à midi une seule alerte, celle du matin ; le soir 29 courriels dans « Envoyés » pour 29 lignes d'historique, sans écart ; les comptes clés ont été envoyés le lendemain.

## 7. Adoption

Les six questions viennent de `70-plan.md` §4 (version 1.2) ; on y ajoute ce qui est fait.

**Impact par rôle**

| Rôle | Ce qui change | Ce qui disparaît | Ce qui reste | Formation ou guide (forme · quand) | Qui approuve ce changement | Vérifié par un essai sans le consultant |
|---|---|---|---|---|---|---|
| Gestionnaire clients | la liste, les motifs et les brouillons sont prêts ; elle relit, corrige et envoie ; la séance passe de 114,3 min à 58,3 min en moyenne `[F]` | la recherche dans « suivi », la copie des modèles, la note de fin de séance | l'extraction, la relecture, l'envoi, la décision par facture | atelier d'une demi-journée et fiche · 2026-11-13 | responsable financier | oui, le 2026-11-13 : lancer le flux, corriger un brouillon, rejouer la file, cocher « Suspendre » (feuille d'essai du responsable financier) |
| Comptable | tient le lundi en suppléance avec la même procédure ; met à jour le fichier du rapprochement à chaque lettrage | sa façon propre de relancer | le lettrage du vendredi | fiche d'exploitation et lundi 4 · 2026-11-13 et 2026-12-07 | responsable financier | oui : essai de la fiche sur 61 factures fictives, trois erreurs courantes corrigées seule (2026-11-13) ; lundi 4 sans appel ; repli à la main du 2026-12-28 |
| Responsable financier | lit compteurs, journal et alertes (6 min par lundi `[F]`) ; approuve les règles dans l'onglet « approbation » ; décide | — | la validation des comptes clés, les décisions de règles | fiche et lecture du journal · 2026-11-13 | direction générale (informée) | oui : A-07, puis A-18 |
| Responsable du support et agents | alimentent la colonne « litige » chaque jour ; un litige signalé retire la relance, même un lundi pendant la séance | les questions de la finance aux commerciaux | le traitement des réclamations | demi-page et 10 min en réunion d'équipe · 2026-11-09 | responsable du support | oui : T-06 en réel, brouillon retiré 7 min après le signalement (2026-12-07) |
| Commerciaux | ne sont plus interrogés par la finance | le message du lundi matin | la réponse pour un litige absent de la colonne | message de la direction générale · 2026-10-12 | direction générale | sans objet : aucun geste nouveau |
| Direction générale | décide la porte, la fin du pilote et chaque lecture de `95-mesure.md` | — | le critère d'investissement | note d'une page et points de 20 min · 2026-10-12, 10-27, 12-08 | — | sans objet |

Approbations. Le responsable financier approuve la façon de travailler de la finance, le responsable du support celle du support, la direction générale celle des commerciaux. Questions posées au rôle compétent : la mesure des durées de séance par rôle demande-t-elle une information du personnel ? posée à la direction générale le 2026-11-09, réponse du 2026-11-11 (« durées et compteurs par rôle, jamais par personne ; l'équipe finance a été informée le 12 octobre et n'a pas d'objection ») ; base légale et durée de conservation de l'historique (Q-05) : fiche de traitement de la personne désignée pour la conformité, reçue le 2026-11-12 (3 ans après la dernière relance, propositions 90 jours, journal 12 mois). Le pack écrit les questions et les réponses reçues ; il ne conclut ni sur la conformité ni sur le droit du travail.

**Les six questions d'adoption**

| # | Réponse du plan (renvoi) | Fait le | Pièce | Reste |
|---|---|---|---|---|
| 1 | Qui reprend, avec quelle autonomie (70 §4, 1) | 2026-11-13 : propriétaire le responsable financier, maintenance la gestionnaire clients, suppléante la comptable ; acceptés par écrit le 2026-12-15 | messages du 2026-11-13 et du 2026-12-15 | — |
| 2 | Gestes à savoir faire sans le consultant (70 §4, 2) | 2026-11-13 (gestionnaire clients), 2026-12-07 (comptable) | feuille d'essai ; relevé du lundi 4 | — |
| 3 | Formation, guide, documentation par rôle (70 §4, 3) | 2026-11-09 (support), 2026-11-13 (gestionnaire clients, comptable) ; fiche révision 5 | rubrique 8 | une séance de plus à la comptable en suppléance (voir `95-mesure.md`) |
| 4 | Accès, propriétaires de comptes, procédures de secours (70 §4, 4) | 2026-11-13 et 2026-12-15 | liste des accès relue, trois comptes de service, aucun compte personnel, aucun accès de l'indépendant | revue des accès le 2027-06-14 |
| 5 | Comment on a vérifié que l'équipe sait corriger une erreur courante (70 §4, 5) | 2026-11-13 ; 2026-12-07 ; 2026-12-28 | trois erreurs corrigées seule ; deux alertes « identifiant introuvable » traitées seule ; repli à la main décidé à 10 h 20 | — |
| 6 | Support après la transmission et nouvelle mission (70 §4, 6) | 2026-12-15 | acceptation des trois rôles ; devis du 2026-10-20 | garantie jusqu'au 2027-01-13 ; D-07 notifié le 2027-01-12 : le responsable financier tranche avec l'indépendant avant cette date s'il le prend en charge sans frais (défaut de la version livrée) ou comme demande de modification (`60-specification.md` §17) |

**Formation et communication**

| Public | Message ou formation | Canal | Moment `[H]` | `A-xx` | Fait le · pièce |
|---|---|---|---|---|---|
| Direction générale | note d'une page et point de 20 min | note, réunion | 2026-10-12, 2026-10-27, 2026-12-08 | sans objet (antérieur au registre ou sans effet sur un outil) | faits aux trois dates (journal) |
| Gestionnaire clients | atelier et fiche d'exploitation | atelier | 2026-11-12 (plan), faite le 2026-11-13 | sans objet | 2026-11-13 · feuille d'essai |
| Comptable | réunion de 20 min et fiche | réunion | 2026-10-12, 2026-11-13 | sans objet | faits |
| Responsable du support et agents | message du responsable du support, puis 10 min en réunion | message, réunion | 2026-10-12, 2026-11-09 | sans objet | faits |
| Commerciaux | message de la direction générale | message | 2026-10-12 | sans objet | fait |
| Finance, support, direction générale | note de mise en production d'une page | messagerie | 2026-12-11 | A-21 | faite le 2026-12-11 |
| Clients | aucune annonce : les modèles de courriel restent ceux de la finance | — | — | — | — |

Support de transition : l'indépendant répond des défauts de la version livrée jusqu'au 2027-01-13, sans frais, d'après son devis (suppléante : sa consœur désignée au devis). Relèvent d'une nouvelle mission : la seconde phase, un changement de S1, S2 ou S3, un niveau de relance de plus, tout envoi par le flux.

## 8. Exploitation et transfert

Le mode opératoire est la fiche d'exploitation de `80-construction.md` (`80-construction/fiche-exploitation.md`, **révision 5**, 2027-01-12) : il n'existe qu'à cet endroit.

| Question du mode opératoire | Réponse (fiche d'exploitation, rubriques 1 à 4) | Déroulé par (rôle, autre que l'auteur) le | Lacune → révision de la fiche |
|---|---|---|---|
| Comment vérifier que ça marche ? | quatre signaux : une exécution a eu lieu, file des échecs, alertes, version qui tourne | la comptable, le 2026-11-13 (révision 2) et le 2026-12-07 | où lancer le flux, comment mettre à jour le fichier du rapprochement, sens de « ouvert » et de « rejoué » → **révision 3, 2026-11-13** |
| Que faire en cas d'incident ? | tableau par symptôme : première action, qui prévenir, quand suspendre | la comptable le 2026-11-13 ; le 2026-12-07 (deux alertes « identifiant introuvable ») ; le 2026-12-28 (plateforme indisponible, décision à 10 h 20) | heure limite de la séance à la main (10 h 30, non 12 h) et ligne « plateforme indisponible » → **révision 4, 2026-12-09** (pré-mortem du 2026-12-08) |
| Qui joindre ? | propriétaire, suppléants, support de la plateforme, indépendant | la comptable, le 2026-12-28 (a joint le responsable financier à 10 h 12) | l'avis de maintenance est parti vers une adresse non lue → **révision 5, 2027-01-12** (dépendances, A-23) |
| Comment revenir en arrière ? | case « Suspendre », méthode à la main, version précédente du flux, rejeu de la file | la gestionnaire clients (interrupteur, A-11, 2026-11-16) ; la comptable (repli à la main, 2026-12-28) | aucune |

Accès et comptes : liste relue le 2026-11-13 et le 2026-12-15, comptes de l'entreprise, aucun compte personnel, aucun accès de l'indépendant. Secrets : accès-listes, accès-messagerie, accès-alerte, dans le coffre de la plateforme ; noms et endroits seulement (`60-specification.md` §9), jamais leur valeur. Version en service : flux 1.1 (import du 2026-11-13) ; règles R1.1 (approbation du 2026-12-14 à 10 h 12).

| Rôle | Tenu par (rôle) | Suppléant (rôle) | Accepté par écrit le |
|---|---|---|---|
| Propriétaire (décide des règles, détient les comptes) | responsable financier | gestionnaire clients | 2026-12-15 |
| Exploitant (maintenance courante, `60-specification.md` §17) | gestionnaire clients | comptable | 2026-12-15 |

Revues datées : accès tous les 6 mois, la première le 2027-06-14 ; coût de fonctionnement chaque mois (relevés des 2027-01-11, 2027-02-08) ; plan avant la décision de renouvellement du logiciel de facturation de mars 2027, le 2027-02-08. La mise en service ne clôt pas le cas : la clôture vient après la mesure.

## 9. Ce que reçoit la mesure

| Élément | Contenu |
|---|---|
| Début de la période de mesure | 2026-12-14, date de la bascule ; première période mesurée : du 2026-12-14 au 2027-01-10 |
| Versions en service | flux 1.1 depuis le 2026-11-13 ; règles R1 jusqu'au 2026-12-14 à 10 h 09, R1.1 ensuite ; aucune autre version |
| Changements depuis le feu vert | A-16 annulée (aucun effet) ; A-17 annulée et A-18 (R1.1) : incident du 2026-12-11 (modèle corrigé hors registre), bloqué par le garde-fou, sans exécution entre-temps, mesure comparable ; changement subi : maintenance de l'éditeur le 2026-12-28 (indisponibilité de 6 h 30, aucun écart de comportement aux lundis suivants) ; A-22 à A-25 proposées, non faites (A-24 et A-25 sont des mesures d'attente) |
| Hypothèses de `50-rentabilite.md` restées ouvertes | temps résiduel `[H]` de 32 min, part du temps libéré réemployée, taux d'adoption, maintenance, erreurs évitées, fonctionnement, coût d'une erreur ; levées : aucune |
| Relevés à fournir | tous les `IND-xx` de `60-specification.md` §14 : relevé mensuel des séances et compteurs (gestionnaire clients), facture et opérations de la plateforme (responsable financier), réclamations par motif (responsable du support), appels et stock des retards (responsable financier), heures de maintenance et de supervision (notes du classeur) ; chaque mois, dépôt dans `mission/sources/` (`70-plan.md` §6) |

## Décision attendue

Valider les mesures d'attente A-25 puis A-24, et l'action A-23 — ou les refuser une à une — et, quand la passe 5 de `85-recette.md` aura rejoué T-06, T-12, T-19 et T-42 sur la version 1.2 du flux, A-22 (responsable financier). Décider si le flux reste en service sous D-07, avec la consigne de A-24 et l'onglet de A-25, ou si la séance revient à la main jusqu'à la passe 5 : le verdict de la version en service est relu « pas prêt pour la version en service » tant que D-07 est ouvert (`85-recette.md` §10, journal du 2027-01-12). Décider la sortie de la surveillance renforcée, au plus tôt le 2027-01-25. Trancher avec l'indépendant, avant le 2027-01-13, la prise en charge de D-07 : défaut de la version livrée ou demande de modification (`60-specification.md` §17). Aucune de ces décisions ne change une décision déjà inscrite.
