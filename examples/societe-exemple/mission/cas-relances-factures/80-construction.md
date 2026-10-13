# Construction — Relances de factures échues

2026-11-10, révisé le 2026-11-12 (version 1.1) · Option construite : 4, flux sur plateforme sans code (`40-solutions.md`, décision du 2026-10-06) · Construit par : consultant IA (maquette exécutable) ; l'indépendant monte ensuite la plateforme · Valideur : responsable financier · Décideur : responsable financier · Rédigé par : consultant IA · Version de la construction : 1.1 (maquette ; la 1.0 du 2026-11-10 reste archivée) · Spécification lue : `60-specification.md`, version 1.4 du 2026-11-12 (la 1.3 du 2026-11-06 pour la version 1.0)
Mode : le pack construit seul la maquette exécutable de la logique ; un tiers (l'indépendant) monte ensuite la plateforme sur la fiche de montage, le pack contrôle les pièces qu'il rend · Porte : constatée le 2026-10-27, pièce : `sources/fiche-de-porte-2026-10-27.md`
Pour l'équipe qui teste et qui exploite. Écrit pour être suivi sans avoir assisté à la construction.

**Version 1.1, précisée le 2026-11-12, après la passe 1 de la recette.** La recette (`85-recette.md`) a joué 43 tests sur la version 1.0 gelée : 39 réussis, 4 échoués (T-26, T-27, T-28, T-39). Les quatre échecs étaient des défauts de la logique (D-03 à D-06, `85-recette.md` rubrique 7), corrigés dans la version 1.1 ; deux autres défauts touchaient des documents, pas le programme (D-01 : `60-specification.md` version 1.4 et `30-exigences.md` version 1.2 ; D-02 : `80-construction/fiche-exploitation.md` révision 2). Seul `flux_relances.py` change dans la livraison ; les règles R1 et les trois modèles sont identiques octet pour octet, donc l'approbation du responsable financier reste valable. La passe 2 teste la version 1.1 : 43 tests sur 43. Les contrôles de tranche ont été rejoués à l'identique sur la 1.1 (28 sur 28). La différence relue avant le gel est dans `80-construction/journal-versions.md`. Les rubriques ci-dessous disent la version 1.1 ; les pièces de la 1.0 restent rangées à côté de celles de la 1.1.

**Ce que ce livrable est, et n'est pas.** La plateforme P n'est pas atteignable depuis cette session : aucune instance d'essai n'existe à la date de ce document. Le pack applique donc la méthode de repli de `construire-solution` (`references/garde-fous.md` partie 5) pour un flux sans code : une **fiche de montage** (`80-construction/fiche-de-montage.md`) que l'indépendant assemble, et, en plus, une **maquette exécutable** de la logique de `60-specification.md` : un petit programme Python à bibliothèque standard seule (`80-construction/livraison/flux_relances.py`), qui lit un extrait de facturation sur fichiers, écrit des brouillons dans une boîte de messagerie simulée et ne peut rien envoyer. La maquette est la logique de la plateforme écrite autrement, pas la plateforme : sa latence, ses connecteurs et ses limites ne sont pas mesurés. La version « 1.0 » de ce document est la maquette. **La version de la plateforme n'existe pas** : elle ne peut pas être déclarée prête, tous les contrôles qui la touchent sont « prévus ».

**Deux horloges.** Les dates de la mission (ce document, les journaux, les versions) suivent le calendrier fictif de `70-plan.md`. Les commandes citées ont été réellement exécutées le 2026-10-13 sur la machine de l'auteur du pack, avec Python 3.14.6 ; leur sortie, datée de l'heure réelle, est rangée dans `80-construction/sorties-simulees/`. L'ordre des dates n'est donc pas celui de la mission.

**Qui construit, qui teste.** Le consultant IA a construit la maquette ; il en exécute aussi les tests en `85-recette.md`, ce qu'il y dit en tête. Le constructeur ne déclare aucun critère d'acceptation « réussi » : un contrôle de tranche passé n'est pas une recette.

## 1. Point de départ

Livrables lus : `60-specification.md` version 1.3 (2026-11-06), puis version 1.4 (2026-11-12) pour la version 1.1 de la maquette, `40-solutions.md` version 1.1 (2026-10-15), `70-plan.md` version 1.1 (2026-10-16), `30-exigences.md` version 1.1 (2026-10-09), puis version 1.2 (2026-11-12), `50-rentabilite.md` version 1.1 (2026-10-16). Journal de mission lu : porte constatée le 2026-10-27, plateforme P confirmée le 2026-10-23, devis signé le 2026-10-28.

Phase construite : première phase (EF-01 à EF-04, EF-06 à EF-08, EF-10, EF-11), avec les exigences non fonctionnelles ENF-01, ENF-04 à ENF-10 qui la bordent. Hors phase : EF-05, EF-09, EF-12 (la messagerie permet déjà de corriger ou de supprimer un brouillon), EF-13, EF-14, EF-15.

Limites de la construction, reprises mot pour mot de `70-plan.md` (lot 3, « Ce qu'on ne fait pas dans ce lot ») : aucune relance réelle envoyée par le flux ; aucune connexion à S1 ; aucun changement des critères du pilote une fois signés.

S1 à S4 (`30-exigences.md` §6) : S1 logiciel de facturation, S2 tableur partagé, S3 messagerie, S4 outil de tickets. Les doubles de l'essai remplacent S2 et S3 ; S1 est une extraction déposée en fichier, S4 n'est lu que par l'intermédiaire de la colonne « litige » de S2.

## 2. Ce qui existait déjà

Recherche annoncée avant d'être faite : au plus 30 min, par l'indépendant avant son devis ; le pack n'a pas pu relire les pages (aucun accès réseau dans cette session).

| Candidat (adresse, lu le) | Auteur · dernière mise à jour · licence | Exigences couvertes | Autorisations demandées · coût à l'exécution | Fait en plus | Décision et raison |
|---|---|---|---|---|---|
| modèle « relance de factures » de la bibliothèque de l'éditeur de P, lu par l'indépendant (devis du 2026-10-20) | éditeur · date et licence non communiquées `[H]` | EF-07 seulement | écriture dans la messagerie · non lu `[H]` | écrit les courriels et les envoie directement, sans clé de dédoublonnage ni journal | inspiration seulement : l'envoi direct contredit EF-10 |
| flux publics de la communauté, flux internes de la finance | — | — | — | — | non vérifié `[H]` : pages non relues par le pack ; la finance n'a aucun flux interne connu `[H]` ; rôle qui peut le faire : indépendant, avant le montage |

## 3. Environnement d'essai

| Élément | Valeur | Preuve |
|---|---|---|
| Nom | `essai-relances` | repris tel quel en `85-recette.md` et `90-mise-en-service.md` |
| Lieu · détenteur | pour la maquette : un dossier temporaire neuf à chaque exécution, copié de `80-construction/donnees-essai/espace-modele/` · consultant IA ; pour la plateforme : un espace de travail « essai-relances » à créer par le responsable financier, séparé de la production (la page de l'éditeur le permet) | exécution des contrôles de tranche, 2026-10-13 ; espace de la plateforme : à créer `[H]` |
| Comptes de test | `service-messagerie` (créer et supprimer ses brouillons, lire, lister ; aucun droit d'envoi), `service-alerte` (poster des messages d'alerte), classeur : dépôt et pilotage en lecture seule, écriture limitée aux huit onglets du dispositif | tranche 0 : envoi refusé, écriture hors onglets refusée, tentative consignée |
| Absent de l'essai | envoi réel, écriture chez un tiers, secret de production, mode réel (le programme le refuse avec le code 2) | `sorties-simulees/controles-tranches-v1.0.txt` et `-v1.1.txt`, tranche 0 |
| Mode simulation | seul mode ; tout ce que la maquette écrit tient dans l'espace d'essai ; copie du rejeu rangée dans `sorties-simulees/rejeu-2026-09-07/` | tranches 0 et 3 |
| Données | 61 factures fictives qui reproduisent le décompte de la séance du 2026-09-07, motifs compris `[F]` ; adresses en `.invalid` ; attendu écrit à part et indépendant du flux | `donnees-essai/LISEZ-MOI.md` : comment produites ; empreintes ; balayage du 2026-10-13, rien à relire |
| Mis à disposition par le client | instance d'essai de la plateforme, comptes de test, trois connexions de test (`connexion-listes-essai`, `connexion-messagerie-essai`, `connexion-alerte-essai`, noms seulement) | responsable financier · date prévue 2026-11-11 `[H]` ; non mis à disposition à la date de ce document |

## 4. Plateforme et compagnon

Plateforme décidée en `40-solutions.md` : flux sans code, plateforme P (confirmée au journal le 2026-10-23). Ligne de `COMPAGNONS.md` lue : les compagnons de construction listés visent n8n, Make et un agent écrit en Python ; aucun ne couvre la plateforme P, aucun n'a été appelé. **Méthode de repli maison**, dite telle : fiche de montage par tranche pour la plateforme (ligne « flux sans code »), et, à titre de maquette de la logique, la méthode « script ou petit service » (un test automatisé par test de `60-specification.md` §12 que la tranche rend exécutable, doubles de S2 et S3, mode simulation par défaut, une commande reproductible, journal dans un fichier).

| Composant | Version ou identifiant fixé | Lu le · dans quoi |
|---|---|---|
| Plateforme P (instance d'essai) | non lue : aucune instance n'existe `[H]` | à lire par l'indépendant avant le montage, page d'administration |
| Connecteurs (classeur, messagerie, alerte) | non lus `[H]` | idem |
| Python (maquette) | 3.14.6, bibliothèque standard seule | 2026-10-13 · `python --version` sur la machine d'exécution |
| Maquette | `flux_relances` 1.1 (la 1.0 reste archivée) | 2026-10-13 · `python flux_relances.py version` |
| Modèle d'IA | sans objet : aucun modèle n'intervient (`60-specification.md` §4) | — |

## 5. Tranches

Commande des contrôles : `python -X utf8 donnees-essai/controles_tranches.py`, depuis `80-construction/`. Sortie intégrale et date réelle d'exécution : `sorties-simulees/controles-tranches-v1.0.txt` pour la version 1.0 et `sorties-simulees/controles-tranches-v1.1.txt` pour la version 1.1 (2026-10-13). Les mêmes 28 contrôles ont été joués sur chacune des deux versions gelées.

| Tranche | Étapes de 60 §4 · exigences servies | Ce qu'elle livre (entrée → sortie lisible) | Garde-fous posés | Tests de 60 §12 rendus exécutables | Contrôle de tranche | Versions contrôlées |
|---|---|---|---|---|---|---|
| 0 Socle | — · ENF-01, ENF-06, ENF-10 | espace d'essai nommé ; mode simulation seul ; journal d'exécution ; case « Suspendre » lue avant les étapes 1, 5 et 6 ; verrou d'exécution unique ; refus des règles et modèles non approuvés | simulation, absence de droit d'envoi, journal, interrupteur, verrou, empreinte de la version approuvée | T-10, T-18, T-22 | exécuté : 6 contrôles passés, aucun écart (lancement à vide, case cochée, verrou, isolement, tentative d'envoi consignée) · 2026-10-13 | 1.0 et 1.1 |
| 1 Lire et contrôler | 1, 2, 3 · EF-01, ENF-09 | extraction du jour → liste candidate avec niveau ; ou refus « rapprochement trop ancien » | erreurs définitives vers la file des échecs ; extraction du jour seulement | T-01, T-02, T-13, T-16, T-21, T-25 | exécuté : 6 contrôles passés, aucun écart (61 factures lues, niveaux 1 à 3, rapprochement du jeudi refusé, du vendredi accepté, colonne absente) · 2026-10-13 | 1.0 et 1.1 |
| 2 Écarter | 4 · EF-02, EF-03, EF-04, EF-06 | liste candidate → propositions, écarts avec motif, comptes clés à part | motif de chaque écart au journal | T-03, T-04, T-05, T-07, T-14, T-24 | exécuté : 3 contrôles passés, aucun écart (9 payées, 4 déjà relancées, 6 en litige ; 5 comptes clés ; 19 motifs au journal) · 2026-10-13 | 1.0 et 1.1 |
| 3 Brouillons simulés | 5 · EF-07, EF-08, EF-10 | propositions → brouillons dans la boîte simulée (37 + 5) | clé de dédoublonnage ; aucun droit d'envoi ; brouillon relu après écriture ; réconciliation d'un brouillon sans proposition | T-08, T-09, T-12, T-15 | exécuté : 5 contrôles passés, aucun écart (lancé deux fois : 42 brouillons ; processus arrêté net après 10 brouillons : reprise à 42 clés distinctes) · 2026-10-13 | 1.0 et 1.1 |
| 4 Historique et litiges | 8, 9 · EF-11, EF-04 | courriel envoyé → ligne d'historique ; litige saisi → brouillon retiré au passage suivant | clé de l'historique ; identifiant du courriel noté ; réglage du pilote (étape 8 activable) ; verrou partagé | T-06, T-11, T-19, T-23 | exécuté : 3 contrôles passés, aucun écart (4 envois → 4 lignes ; litige → brouillon retiré ; étape 8 désactivée) · 2026-10-13 | 1.0 et 1.1 |
| 5 Erreurs et alertes | §7, §10 · ENF-04, ENF-05, ENF-08 | file des échecs, reprises, alertes, plafond, alerte sur silence | reprises 1, 5, 15 min avec variation ; plafond de 100 ; alerte indépendante de la boîte partagée | T-16, T-17, T-20, T-21 | exécuté : 5 contrôles passés, aucun écart (S3 coupé 10 min : reprises puis 42 brouillons ; coupé 4 h : 42 lignes dans la file ; 150 propositions : arrêt ; silence à 10 h) · 2026-10-13 | 1.0 et 1.1 |

Résultat d'ensemble : 28 contrôles passés sur 28, sur la version 1.0 puis sur la version 1.1. Ce que ces contrôles ne couvrent pas, la recette l'a cherché (`85-recette.md`, 43 tests) : panne de S2 en cours d'exécution, brouillon relu différent, règle modifiée pendant une exécution, double envoi, liste vide suspecte, litiges sans mise à jour. Elle a trouvé quatre défauts de la logique, corrigés dans la 1.1 ; l'historique reconstitué à partir du seul journal n'a pas de test dédié (`85-recette.md`, rubrique 9).

| Exigence de la phase | Tranche | Remarque |
|---|---|---|
| EF-01 | 1 | report d'une facture écartée : la liste couvre toute facture sans relance consignée à son niveau |
| EF-02, EF-03, EF-04 | 2 | EF-04 : retrait en cours de séance en tranche 4 (étape 9) |
| EF-06 | 2 | dossier à part en tranche 3 ; contrôle des copies envoyées en tranche 4 |
| EF-07, EF-08, EF-10 | 3 | EF-10 posée dès la tranche 0 (aucun droit d'envoi) |
| EF-11 | 4 | |
| ENF-01, ENF-06, ENF-10 | 0 | droits minimaux, journal, interrupteur |
| ENF-09 | 1 | |
| ENF-04, ENF-05, ENF-08 | 5 | ENF-08 aussi en tranche 2 ; ENF-04 se teste en recette (T-20) |
| ENF-02, ENF-03, ENF-07 | — | ENF-02 : lieu d'hébergement lu sur la page de l'éditeur (porte c) ; ENF-03 : Q-05 ouverte ; ENF-07 : validation par la personne, dossier à part pour les comptes clés |

## 6. Garde-fous

| Garde-fou (60 §) | Exigence | Comment il est construit | Tranche | Contrôle |
|---|---|---|---|---|
| Simulation et absence de droit d'envoi (§4, §6) | EF-10 | le compte `service-messagerie` n'a pas le droit d'envoyer ; le mode réel n'existe pas dans le programme | 0, 3 | exécuté : envoi refusé, « Envoyés » vide, tentative consignée, mode réel : code 2 (2026-10-13) ; plateforme : prévu (droits relevés par l'indépendant) |
| Dédoublonnage (§8) | EF-03, EF-11 | clé = numéro de facture et niveau, cherchée dans les propositions et dans la boîte avant création, notée après la réussite ; à la reprise, le brouillon existant est adopté | 3, 4 | exécuté : flux lancé deux fois ; processus arrêté net juste après l'écriture d'un brouillon, puis relancé : 42 clés distinctes (2026-10-13) |
| Journal d'exécution (§10) | ENF-06 | une ligne par élément et par étape : clé, étape, résultat, heure, version du flux et des règles ; ni nom ni adresse | 0 | exécuté : motif de chaque écart relu (19 lignes) ; en recette, T-01 relit dans le journal seul la décision de chacune des 61 factures et T-22 la version des règles inscrite à chaque ligne ; le parcours complet d'une facture (décision, brouillon, envoi) n'est pas relu d'un seul bloc : pas de test dédié (`85-recette.md`, rubrique 9) |
| Erreurs, file des échecs, alerte (§7) | ENF-08 | reprises à 1, 5, 15 min avec variation de 10 % puis file des échecs (passagère) ; aucune reprise puis alerte (définitive) | 5 | exécuté : S3 coupé 10 min, coupé 4 h ; colonne absente ; S2 coupé en cours d'exécution : essayé en recette, T-28, échoué en passe 1 (D-05) puis réussi en passe 2 sur la 1.1 |
| Interrupteur, verrou, plafonds (§7) | ENF-10 | case lue avant les étapes 1, 5, 6 et à chaque passage de la veille ; verrou périmé après 30 min ; 100 propositions au plus `[H]` | 0, 5 | exécuté : case cochée avant l'exécution ; verrou ; 150 propositions → arrêt ; case cochée en cours de séance : essayée en recette, T-18, réussi |
| Secrets (§9) | — | trois noms de secrets, jamais de valeur ; aucun secret dans le code | 0 | exécuté : balayage du 2026-10-13, rien à relire (83 fichiers) |
| Moindre privilège (§6) | ENF-01 | droits des doubles comparés au tableau de §6 | 0 | exécuté : envoi et écriture hors onglets refusés ; droits relevés sur la plateforme : prévu |
| Sauvegarde, versions, retour arrière (§11) | — | manifeste d'empreintes et archive exportée à chaque version ; version restaurée dans un dossier neuf | toutes | exécuté : restauration de l'archive 1.0, manifeste conforme, séance rejouée : 0,48 s `[F]` pour l'essai (2026-10-13) ; sauvegarde datée des classeurs : prévue (action de 90) |
| Alerte sur silence (§10) | — | scénario « Silence » : aucune ligne « début » du jour à l'heure de `silence_heure` | 5 | exécuté : à 10 h sans exécution, alerte au responsable financier ; avec exécution, aucune (2026-10-13) ; déclencheur distinct de la plateforme : Q-13 ouverte |
| Réglage du pilote (§4, §13) | — | paramètre `etape8_active` de l'onglet « commande » | 4 | exécuté : étape 8 désactivée, aucune alerte, aucune ligne d'historique (2026-10-13) ; T-19 complet (remise en route comprise) : réussi en recette |
| Règles qui changent (garde-fous partie 2) | — | règles et modèles lus au début de chaque exécution, version notée au journal | 0 | exécuté en recette : T-22 (règle modifiée pendant une exécution : sans effet sur l'exécution en cours), réussi |
| Changement non approuvé (garde-fous partie 2, `60` §17) | — | empreinte des règles et des modèles comparée à l'approbation avant toute exécution | 0 | exécuté en tranche 0 : jeu approuvé accepté ; modèle modifié hors procédure : essayé en recette, T-22, réussi |
| Lecture après écriture (garde-fous partie 1) | — | le brouillon créé est relu dans la boîte et comparé à l'intention avant la proposition | 3 | exécuté : brouillons relus lors du rejeu ; brouillon relu différent : essayé en recette, T-27, échoué en passe 1 (D-04) puis réussi en passe 2 |

## 7. Livré

| Fichier (dans `80-construction/livraison/`) | Version | Empreinte (SHA-256) | Contenu | Balayé le · résultat |
|---|---|---|---|---|
| `flux_relances.py` | 1.1 (la 1.0, `e6564afc43b75882d6669e8d63b8b903b0f7f44ac1bd050d9f96e983f3d4888d`, est dans l'archive 1.0) | `83f1698c3ed46221a4796fdeee6d45acc6d241ba9bd9269ebed45bf76e404030` | la maquette : étapes 1 à 6, 8 et 9, garde-fous, ligne de commande | 2026-10-13 · rien à relire |
| `essai_s2_s3.py` | 1.0 (inchangé en 1.1) | `af697cc0437b8dd8afbc9ed49da4d70a6831b090402122f107191d2b5e0788bf` | doubles de S2 et de S3 : droits, pannes, arrêt net | 2026-10-13 · rien à relire |
| `regles-v1.0.csv` | R1 (fichier inchangé) | `677eb04fe39937bbf133595f67966f6278b8b7a4f680c6fea16c9b70c32613e5` | délais 7, 21, 35 jours ; limite 60 jours ; plafond 100 ; reprises ; heure du silence ; libellés des niveaux | 2026-10-13 · rien à relire |
| `modeles/niveau-1.txt` | R1 (inchangé) | `e1fad54fa909e3862f0e57ab25c62b863885ac38de9e9d5716bde8f4a856f4ab` | modèle de courriel du niveau 1 | 2026-10-13 · rien à relire |
| `modeles/niveau-2.txt` | R1 (inchangé) | `6e0c4847f31d30c6397e44eb45cc7ec3a9d6786b8f9cb5b112b2bbb3464eef1c` | modèle du niveau 2 | 2026-10-13 · rien à relire |
| `modeles/niveau-3.txt` | R1 (inchangé) | `b9f87adf9313fc55169b7f3d5c17defc1e89bb3fa40f0060833de23b8e132694` | modèle du niveau 3 | 2026-10-13 · rien à relire |
| `MANIFESTE.sha256` | 1.1 (celui de la 1.0, `782e7da35dcab25163266e12edb6c862b77b59578bb9fa5a4002945a5165dec5`, est dans l'archive 1.0) | `829258c36d5ad24fffd7402c1e78cb29bf9bf49aea1cea7ed717ef22ad111181` | empreinte de chaque fichier ci-dessus ; `python livraison/flux_relances.py verifier-livraison` le compare à ce qui est livré | 2026-10-13 · conforme |
| `archives/flux-relances-v1.0.zip` | 1.0 | `dbaa825a79ee8413b0e645c509e96db03ebb75ac20c45ef51967c935fb01ada8` | export de la version 1.0, fabriqué de façon reproductible ; sert au retour arrière de la 1.1 | 2026-10-13 · rien à relire |
| `archives/flux-relances-v1.1.zip` | 1.1 | `8408d8b7321f3c12bc1f9222e30637aa9898b3844bc8d21586ed8f6a6b2d1c9c` | export de la version 1.1, fabriqué de façon reproductible | 2026-10-13 · rien à relire |

Journal des versions : `80-construction/journal-versions.md`. Balayage (commande, date, résultat) : `sorties-simulees/balayage-v1.0.txt` pour la 1.0 et `sorties-simulees/balayage-v1.1.txt` pour la 1.1 ; méthode : `donnees-essai/balayer.py` (mot de secret suivi d'une valeur, chaîne longue mélangeant lettres et chiffres, fichier d'environnement ou clé privée, adresse de courriel hors `.invalid`, numéro de téléphone, adresse postale). Le balayage réduit le risque, il ne prouve pas l'absence ; il se refait à chaque version.

Non livré : l'export du flux de la plateforme P (aucune instance), la seconde phase (EF-05, EF-09, EF-13, EF-14, EF-15), tout accès à S1.

**Liste « prêt pour la recette »** (`construire-solution`, `references/modeles.md` partie D), passée sur la maquette 1.0, puis repassée sur la 1.1 (les pièces ci-dessous sont celles de la 1.1) :

| # | Point | Oui ou non · pièce |
|---|---|---|
| 1 | chaque tranche a son contrôle exécuté ou prévu | oui · rubrique 5, `sorties-simulees/controles-tranches-v1.1.txt` (28 sur 28) |
| 2 | table exigence → tranche sans orpheline | oui · rubrique 5 |
| 3 | chaque garde-fou de 60 §7 à §11 construit ou écarté par un écart | oui pour la maquette · rubrique 6 ; sur la plateforme : non, la plateforme n'existe pas |
| 4 | isolement et simulation prouvés par un essai | oui pour la maquette · tranche 0 ; sur la plateforme : non |
| 5 | retour arrière essayé, durée relevée | oui pour la maquette · `sorties-simulees/retour-arriere-v1.1-vers-v1.0.txt` (0,49 s) ; sur la plateforme : non |
| 6 | livraison balayée | oui · `sorties-simulees/balayage-v1.1.txt` |
| 7 | version numérotée, exportée, empreinte, rien modifié depuis | oui · rubrique 7 ; `verifier-livraison` : conforme |
| 8 | écarts traités | oui · rubrique 8 (60 v1.4 ; Q-14, Q-15, Q-16 et Q-17 ouvertes, non bloquantes pour la recette) |
| 9 | réglages du pilote construits et contrôlés | oui pour la maquette · tranche 4 ; sur la plateforme : non |
| 10 | fiche d'exploitation à quatre réponses, essai par un tiers prévu | oui · `fiche-exploitation.md`, révision 2 ; essai par la comptable prévu au 2026-11-13 |
| 11 | chiffres relevés comparés aux seuils de 50, dépassement dit | oui · rubrique 9 |
| 12 | étape d'IA : consignes, modèle, jeux séparés | sans objet : aucun modèle n'intervient |

La maquette 1.1 passe la liste ; la 1.0 la passait aussi, et la recette a pourtant trouvé quatre défauts de la logique que cette liste ne cherche pas : « prêt pour la recette » n'est pas « sans défaut ». La version de la plateforme ne peut pas la passer (points 3, 4, 5 et 9) : elle ne sera « prête » que lorsque l'indépendant aura rendu l'export et les sorties d'exécution de la fiche de montage.

## 8. Écarts avec la spécification

Traitement : une précision qui change un comportement, un seuil ou un nombre a donné la version 1.3 de `60-specification.md` (2026-11-06, ligne « correction » au journal de mission) ; un trou à trancher devient une question.

| Rubrique de 60 | Constat | Traitement | État |
|---|---|---|---|
| §5 contrat de l'extraction (Q-10) | la version 1.2 supposait une extraction à neuf colonnes dont la date du rapprochement ; l'extraction de S1 ne la porte pas (fiche de porte, ligne g) | extraction à sept colonnes, date de l'extraction portée par le nom du fichier, date du rapprochement dans un fichier d'une ligne : 60 v1.3 rubriques 4 et 5 | corrigé |
| §4 étape 8 et §5 copie envoyée (Q-11) | l'identifiant de relance n'est pas conservé sur la copie envoyée ; la messagerie ne limite pas l'envoi d'un dossier à un compte (fiche de porte, ligne d) | la proposition est retrouvée par l'objet « Facture <numéro> — <libellé du niveau> » ; contrôle a posteriori des copies envoyées pour les comptes clés : 60 v1.3 | corrigé |
| §4 étape 8 | le déclencheur de l'étape 8 n'était pas écrit | l'étape 8 s'exécute à chaque passage de la veille (toutes les 10 min le lundi de 8 h à 12 h, puis à 17 h les autres jours ouvrés) : 60 v1.3 | corrigé |
| §4 cas de refus | le garde-fou « changement non approuvé » n'avait ni cas de refus ni test | refus d'une exécution dont les règles ou les modèles ne sont pas ceux que le responsable financier a approuvés ; T-22 : 60 v1.3 | corrigé |
| §4 cas de refus, ENF-08 | une relance notée à un niveau que l'âge de la facture ne justifie pas, ou une échéance dans le futur, n'étaient pas prévues | « à traiter à la main » ; T-24 : 60 v1.3 | corrigé |
| §4 cas de refus, ENF-09 | l'extraction du jour absente alors qu'une plus ancienne existe n'était pas un cas écrit | jamais traitée ; reprises puis alerte ; T-25 : 60 v1.3 | corrigé |
| §7 interrupteur | « lue avant chaque étape » : une facture ne coûte pas une lecture ; la suppression des brouillons se fait au passage suivant de la veille | lue avant les étapes 1, 5 et 6 et à chaque passage ; retard maximal 10 min `[H]` : 60 v1.3 | corrigé |
| §5 propositions, §8 | une reprise après un arrêt entre les écritures groupées de l'étape 8 doublait une alerte ou une ligne | l'identifiant du courriel envoyé est noté dans la proposition : 60 v1.3 | corrigé |
| §7 alerte et cas de panne de S3 | « canal : message dans la messagerie » : si l'alerte passait par la boîte partagée, elle ne partirait pas pendant une panne de S3, alors que la ligne S3 du tableau des pannes dit qu'elle part | la maquette envoie les alertes par un compte distinct de la boîte partagée ; à confirmer sur la plateforme | question Q-15 |
| §14 IND-09, `40-solutions.md` §8 | la consommation dépasse l'estimation de 600 actions par mois (rubrique 9) | dit au décideur ; recalcul à demander à `chiffrer-rentabilite` s'il choisit le palier supérieur | question Q-14 |
| §4 cas de refus ; `30-exigences.md` CA-08, ENF-07 | trouvé en écrivant les tests T-07 et T-10 de la recette : la spécification disait deux choses (envoi « impossible ou alerte » à la rubrique 12, refus d'un compte clé envoyé par un autre rôle à la rubrique 4) alors que la messagerie ne sait pas limiter l'envoi d'un dossier à un compte (Q-11, levée le 2026-10-22) ; CA-08 en héritait, avec un cas « relance modifiée après validation » que le dispositif ne voit pas, la validation étant l'envoi par la personne | 60 v1.4 et 30 v1.2 (2026-11-12), `85-recette.md` D-01 | corrigé |
| §4 états d'une proposition | rien ne disait ce que devient une proposition dont le brouillon a été supprimé à la main | 60 v1.4 ; la logique est corrigée en 1.1 (`85-recette.md` D-03) | corrigé |
| §5 contrat de l'extraction | le contrat fixe les colonnes, la date et le montant, pas le séparateur, l'encodage ni l'écriture décimale | question Q-16 | ouverte : levée au lundi 1 du pilote, en parallèle |
| §4 étape 8 | si « Envoyés » contient d'autres courriels que des relances, chacun lève l'alerte « identifiant introuvable » (T-23) | question Q-17 | ouverte : avant la remise en route de l'étape 8 |

## 9. Chiffres relevés

Une durée ou une consommation mesurée dans l'essai est `[F]` pour l'essai et `[H]` comme valeur de production. Commandes et sorties : `sorties-simulees/mesure-operations-v1.0.txt` et `-v1.1.txt` (2026-10-13) ; les chiffres de consommation sont identiques dans les deux versions (153, 342, 267 et 236 opérations).

| Grandeur | Estimation (source) | Relevé dans l'essai | Seuil de 50 (point mort) | Lecture |
|---|---|---|---|---|
| Effort de construction, première phase | 2 jours payés `[H]` (`50-rentabilite.md` §2) ; devis 900 € HT | maquette : non relevé `[H]` (le consultant IA ne tient pas de feuille de temps) ; plateforme : à relever dans la feuille de temps de l'indépendant | devis au plus 975 € payés `[E]` (50 §4) | devis de 900 € `[F]`, sous le seuil ; effort réel à relever |
| Consommation d'un lundi (étapes 1 à 6, rejeu de 61 factures, 42 propositions) | 150 actions par séance `[E]` (`40-solutions.md` §8) | 153 opérations `[F]` pour l'essai | — | conforme à l'estimation, pour la seule exécution du lundi |
| Consommation d'une semaine type (le lundi, la veille toutes les 10 min jusqu'à 12 h, un passage à 17 h les autres jours) | 600 actions par mois, soit 150 par semaine `[E]` (40 §8) | 342 opérations par semaine `[F]`, soit 1 482 par mois (× 52/12) `[H]` pour la production ; à 20 min : 267 par semaine, 1 157 par mois ; à 30 min : 236 par semaine, 1 023 par mois | fonctionnement au plus 24 € par mois `[E]` (`70-plan.md` §5) ; le palier d'entrée (20 €) inclut 1 000 opérations (page de l'éditeur, 2026-10-21) | **dépassement** : 148 % du quota à 10 min ; la veille consomme plus que l'exécution elle-même (189 opérations de plus par semaine) ; un mois de cinq lundis dépasse même à 30 min |
| Conséquence chiffrée si la production confirme | gain brut 135,68 €, net 84,68 €, retour 17,1 mois `[E]` (50 §3) | au palier à 35 € : net 69,68 €, retour (1 348 + 135,68 × 0,75) ÷ 69,68 = 20,8 mois `[E]`, recalculé pour information, `50-rentabilite.md` n'est pas modifié | retour au plus 18 mois `[F]` (`30-exigences.md` §8) | au-dessus du critère de 18 mois si le palier à 35 € s'applique tous les mois : dit au décideur (Q-14) |
| Durée du rejeu (ENF-05) | moins de 5 min `[H]` (30 §7) | 0,2 s pour la maquette `[F]` (trois mesures de 0,19 à 0,27 s) | — | sans valeur pour la plateforme : à chronométrer en recette sur l'instance, 42 brouillons créés un par un `[H]` |
| Durée du retour arrière | environ 1 h `[H]` (60 §11) | 0,48 s `[F]` (restauration de l'archive, manifeste conforme, séance rejouée) | — | valeur de l'essai ; sur la plateforme, à mesurer lors du montage |
| Maintenance pressentie | 1 h par mois `[H]` (50 §2) | non relevable dans l'essai | au plus 1,1 h par mois `[E]` | à relever au pilote (IND-10) |
| Limites de la plateforme rencontrées | — | aucune : la plateforme n'a pas été utilisée | — | à relever par l'indépendant au montage |

Dit au décideur (rubrique « Décision attendue ») : la consommation de la veille, pas celle du lundi, est ce qui pousse le fonctionnement au-delà du palier d'entrée. Trois leviers existent et aucun n'est appliqué par la construction : passer la veille à 30 min (retrait d'un brouillon de litige en 30 min au lieu de 10, T-06 à réécrire), accepter le palier à 35 €, ou retirer d'autres opérations (lecture de la case par étape plutôt que par facture : déjà fait ; relecture des brouillons : exigée par le contrat commun).

## 10. Fiche d'exploitation et ce qui reste au client

Fiche : `80-construction/fiche-exploitation.md`, **révision 5** (2027-01-12), décrit la version 1.1. Historique : la révision 1 décrivait la 1.0 ; la révision 2 (2026-11-12) ajoutait la conduite à tenir après un arrêt net, message « une exécution est déjà en cours » (`85-recette.md` D-02) ; la révision 3 (2026-11-13) corrigeait trois lacunes trouvées par la comptable à son essai (où lancer le flux, le fichier du rapprochement, « ouvert » et « rejoué ») ; la révision 4 (2026-12-09) fixe l'heure limite de la séance à la main et ajoute la ligne « plateforme indisponible » ; la révision 5 (2027-01-12) ajoute la dépendance aux avis de l'éditeur et la limite connue D-07 (`90-mise-en-service.md` §8). Ses quatre réponses : comment vérifier que ça marche (rubrique 1), que faire en cas d'incident (2), qui joindre (3), comment revenir en arrière (4). Essayée par un tiers : oui, par la comptable, qui ne l'a pas écrite (2026-11-13, 2026-12-07, 2026-12-28). La fiche de montage de la plateforme est à part : `80-construction/fiche-de-montage.md`.

Ce que le client fera dans ses propres outils (le pack ne fait rien de cela). Les lignes qui touchent l'outil de production deviendront une action `A-xx` de `90-mise-en-service.md` avec son retour arrière ; les trois premières agissent sur l'espace d'essai et relèvent de 80 et de 85, pas du registre de 90 :

| Action pressentie | Où | Réversible ? | Retour arrière prévu | Rôle qui décidera |
|---|---|---|---|---|
| créer l'espace « essai-relances » et ses trois connexions de test | plateforme P | oui | supprimer l'espace et révoquer les connexions | responsable financier |
| monter le flux dans l'espace d'essai selon la fiche de montage et rendre l'export balayé | plateforme P | oui | supprimer le flux monté | responsable financier (exécute : indépendant) |
| rejouer la recette (les 43 tests de `85-recette.md`, dans la mesure où ils se jouent sur la plateforme) sur l'espace d'essai | plateforme P | oui | sans objet : lecture et brouillons de test | gestionnaire clients et responsable financier |
| créer les trois comptes de service et poser les trois secrets de production dans le coffre | plateforme P, coffre | oui | révoquer et recréer | responsable financier |
| noter l'approbation de la version des règles et des modèles (onglet « approbation ») | classeur de pilotage | oui | effacer la ligne : le flux refuse de s'exécuter | responsable financier |
| importer la version dans l'espace de production, désactivée, avec une sauvegarde datée des classeurs | plateforme P, S2 | oui | supprimer le flux importé ; restaurer la sauvegarde | responsable financier |
| armer la veille (10 min le lundi, 17 h les autres jours), le scénario « Silence » et le rappel de calendrier de 10 h | plateforme P, S3 | oui | désactiver les déclencheurs | responsable financier |
| passer le mode simulation à réel (création de brouillons dans la boîte partagée) | réglage du flux | oui | remettre en simulation, supprimer les brouillons créés | responsable financier |
| désactiver l'étape 8 pour le premier lundi du pilote, puis la remettre en route | onglet « commande » | oui | remettre le réglage | indépendant, pour le responsable financier |

## 11. Questions ouvertes

À la suite de la série de `60-specification.md` §16.

| ? | Question | Rôle qui répond | Bloquante pour la recette ? |
|---|---|---|---|
| Q-14 | Que choisir face à la consommation : la cadence de 10 min avec le palier à 35 € (retour de 20,8 mois `[E]`), la veille à 30 min, ou une autre économie ? (`60-specification.md` §16, rubrique 9) | responsable financier ; direction générale informée | non ; oui avant le feu vert du pilote |
| Q-15 | Le connecteur d'alerte de la plateforme est-il indépendant de la boîte partagée de la finance ? S'il ne l'est pas, l'alerte d'une panne de S3 ne part pas | indépendant | non pour la recette de la maquette ; oui avant le montage sur la plateforme |

| Q-16 | Quel est le fichier exact de l'export de S1 : séparateur, encodage, marque d'ordre des octets, écriture décimale ? (`60-specification.md` §16, version 1.4) | indépendant, avec le responsable financier | non ; à lever au plus tard au lundi 1 du pilote |
| Q-17 | Le dossier « Envoyés » de la boîte partagée ne contient-il que des relances ? (`60-specification.md` §16, version 1.4) | responsable financier, indépendant | non ; oui avant la remise en route de l'étape 8 |

Restent ouvertes de la série précédente : Q-05 (bloquante avant la production), Q-13 (avant le pilote), Q-08 et Q-02 (non bloquantes).

## Décision attendue

Version 1.1 (2026-11-12) : prendre acte des quatre corrections de la logique et de la version 1.1 comme version testée par la passe 2 ; la décision sur la suite est celle de `85-recette.md`. Fiche d'exploitation, révision 5 (2027-01-12) : à confirmer par le responsable financier en même temps que les actions A-23 à A-25 de `90-mise-en-service.md`, qu'elle suppose.

Version 1.0 (2026-11-10), décidée le même jour : déclarer la maquette 1.0 prête pour la recette — ou trancher les écarts de la rubrique 8. Trois confirmations avec elle : que la recette de la logique s'exécute sur la maquette (exécutée par le consultant IA, qui l'a construite, ce que `85-recette.md` dit en tête) et se prononce par la gestionnaire clients et le responsable financier ; que la version de la plateforme n'est pas prête et que la recette se rejoue dessus avant le premier lundi du pilote ; que Q-14 se tranche avant le feu vert du pilote.
