# Spécification — Relances de factures échues

2026-10-09 · Option retenue : 4, workflow sans code (`40-solutions.md`, décision du 2026-10-06) · Demandeur : direction générale · Valideur et décideur : responsable financier · Rédigé par : consultant IA · Version 1.1, précisée le 2026-10-12 : mode parallèle du pilote et règle de création des brouillons (rubriques 4, 8, 12 et 13) · Exigences lues : `30-exigences.md`, version 1.1 du 2026-10-09
Pour l'équipe qui construit. Écrit pour être suivi sans avoir assisté à la mission. Les renvois à `30-exigences.md` visent sa version 1.1.
Mode spécification : le journal porte, pour ce cas, la validation de `40-solutions.md` (2026-10-06) et celle de `50-rentabilite.md` avec la décision « y aller » (2026-10-08), prise contre la recommandation de mesurer d'abord. La porte de `40-solutions.md` §10 reste : aucune dépense de construction avant le 2026-10-27. S1 à S4 : logiciel de facturation, tableur partagé, messagerie, outil de tickets (`30-exigences.md` §6). Première phase décrite ici : EF-01 à EF-04, EF-06 à EF-08, EF-10 et EF-11.

## 1. Problème et objectif

Problème (`10-besoin.md`). Des relances de factures échues partent chez des clients qui ont déjà payé ou qui sont en litige, et la séance du lundi prend 156 min `[F]`. La direction veut des relances au bon moment, vers les bons clients, avec un humain qui valide chaque envoi.

Option retenue (`40-solutions.md`). Un flux sur plateforme sans code, construit par un indépendant spécialisé. Il lit un fichier d'extraction et des listes de S2, écrit des brouillons dans S3 et ne peut rien envoyer : la personne envoie. Raisons : il couvre les neuf exigences indispensables, il coûte moins que l'option 3, il lit des fichiers et reste portable. Il suit l'option 0 (les cinq standardisations de `20-diagnostic.md`), qui s'applique déjà.

Gain estimé (`50-rentabilite.md`). Apport de l'option 4 : 136 € de gain brut et 85 € de gain net par mois, retour en 17,1 mois au central `[E]`. Quatre hypothèses `[H]` sont proches de leur seuil `[E]` : 83 min gagnées contre 80, 80 % de temps réemployé contre 77 %, 90 % d'adoption contre 87 %, 1 h de maintenance contre 1,1 h.

Objectif, en résultats observables (cibles de `10-besoin.md` §8, acceptées le 2026-09-24 `[F]`) : séance du lundi sous 60 min (156 min au départ `[F]`, 115 min après l'option 0 `[E]`) ; au plus 7 réclamations après relance par mois (13 au départ `[F]`) ; aucune relance envoyée sans validation humaine.

Porte (`40-solutions.md` §10, reprise sans changement). La construction ne démarre pas avant le 2026-10-27, et seulement si les quatre conditions de la porte sont constatées : (1) la moyenne des trois lundis (2026-10-12, 2026-10-19, 2026-10-26), tenus selon la procédure unique, laisse au moins 112 min aux phases É1, É2, É5 et É6 de la séance `[E]` (seuil du point mort, `50-rentabilite.md` §4) ; (2) le devis est d'au plus 975 € payé et la maintenance estimée d'au plus 1,1 h par mois `[E]` ; (3) la direction générale a nommé l'usage du temps libéré ; (4) la colonne « litige » a reçu une mise à jour datée cinq jours ouvrés de suite `[H]`. Aucune dépense avant elle.

## 2. Non-objectifs

- Téléphone et courrier recommandé au-delà de J+60 (J+60 : soixante jours après l'échéance) : jugement et relation, tenus par le responsable financier.
- Contentieux, avoirs et gestes commerciaux : décisions de la finance.
- Envoi par le flux : interdit. Le flux écrit des brouillons ; la personne envoie.
- Lien direct avec S1 : le flux lit un fichier déposé, jamais S1, pour rester portable en mars 2027.
- Modèle d'IA : aucun. La préparation est déterministe (option 5 écartée dans `40-solutions.md`).
- Rapprochement des paiements : reste humain, fait avant la séance.
- Seconde phase (1 jour `[H]`, décidée après le pilote) : seuil de montant (EF-05 : en première phase, la gestionnaire clients supprime à la main les brouillons des petites factures), présentation des factures écartées avec motif (EF-09), report par le flux (EF-13), compte rendu (EF-14), liste des retards de plus de 35 jours (EF-15). En première phase : une facture non relancée revient d'elle-même sur la liste suivante (EF-01, version 1.1) ; la gestionnaire clients relève à la main la durée de la séance et trois chiffres ; elle corrige les brouillons dans la messagerie (EF-12).

## 3. Utilisateurs et scénarios

1. En tant que gestionnaire clients, je veux ouvrir le lundi la liste des relances proposées, chacune avec son brouillon, afin de ne plus chercher ni vérifier à la main (EF-01 à EF-04, EF-07, EF-08).
2. En tant que gestionnaire clients, je veux lire, corriger puis envoyer moi-même chaque brouillon, afin qu'aucun client ne reçoive une relance que je n'ai pas vue (EF-10).
3. En tant que gestionnaire clients, je veux un avertissement clair quand l'extraction manque ou que le rapprochement des paiements est trop ancien, afin de savoir quoi faire (ENF-09).
4. En tant que gestionnaire clients, je veux voir à part les factures que le flux ne sait pas traiter, afin de les traiter à la main (ENF-08).
5. En tant que responsable financier, je veux relire et envoyer moi-même les relances des comptes clés, afin de contrôler ce qui touche mes principaux clients (EF-06).
6. En tant que responsable financier, je veux lire l'historique, qui a envoyé quoi et quand, afin de contrôler sans refaire le travail (EF-11).
7. En tant que comptable en suppléance, je veux suivre la même procédure et obtenir le même résultat, afin que la séance ne dépende pas de la personne.
8. En tant que responsable du support, je veux qu'un litige que je signale retire la relance concernée, même pendant la séance, afin de ne plus recevoir de réclamation pour une relance à tort (EF-04).

Cas vides et limites : aucune facture n'a atteint de niveau (liste vide, dite telle) ; contact absent ; facture au-delà de J+60 (exclue) ; niveau manqué (jamais de saut de niveau) ; même brouillon envoyé deux fois.

## 4. Comportement étape par étape

| N° | Déclencheur ou entrée | Ce que fait le dispositif | Sortie | Validation humaine (rôle · délai maximal) | Si l'étape échoue |
|---|---|---|---|---|---|
| 1 | La gestionnaire clients lance le flux le lundi, après avoir déposé l'extraction du jour | Vérifie que l'extraction est du jour et porte la date du dernier rapprochement ; arrête tout si ce rapprochement date de plus d'un jour ouvré `[H]` (ENF-09) | poursuite, ou avertissement sans aucune proposition | aucune | extraction absente : passagère ; rapprochement trop ancien ou date absente : définitive (§7) |
| 2 | Extraction valide | Lit les onglets « litiges », « comptes clés », « historique » et « règles » de S2 | données chargées | aucune | S2 illisible : passagère |
| 3 | Données chargées | Calcule pour chaque facture le niveau à proposer (règle ci-dessous) ; écarte les factures de plus de J+60 | liste candidate | aucune | date d'échéance vide : la facture va dans « à traiter à la main » (définitive) |
| 4 | Liste candidate | Écarte les factures payées (EF-02), déjà relancées au même niveau (EF-03), en litige (EF-04). Met à part les factures des comptes clés (EF-06) | relances retenues ; comptes clés à valider ; motif de chaque écart dans le journal | aucune | donnée contradictoire : « à traiter à la main » |
| 5 | Relances retenues | Compose un courriel par relance (EF-07) : modèle du niveau, numéro, montant, échéance et nom du contact repris de l'extraction. Crée un brouillon dans le dossier « Relances du lundi », ou « Comptes clés à valider ». Écrit une ligne « brouillon créé » dans « propositions » | brouillons et propositions | aucune | contact absent : définitive ; S3 ou S2 indisponible : passagère |
| 6 | Brouillons prêts | Avertit la gestionnaire clients, et le responsable financier s'il y a des comptes clés : nombre de propositions, de comptes clés, de factures « à traiter à la main » | message | aucune | message non parti : l'alerte sur silence le voit |
| 7 | Brouillons lus | **[humain]** La personne lit chaque brouillon, le corrige ou le supprime, puis l'envoie (EF-08, EF-10). Les brouillons des comptes clés ne sont envoyés que par le responsable financier | courriel envoyé, ou brouillon supprimé | gestionnaire clients, pendant la séance ; responsable financier, 2 jours ouvrés `[H]` pour un compte clé | sans objet |
| 8 | Courriel envoyé depuis la boîte | Retrouve la proposition par l'identifiant de relance ; écrit la ligne d'historique (EF-11) si la clé n'existe pas ; passe la proposition à « envoyée » | historique à jour | aucune | identifiant introuvable : file des échecs et alerte |
| 9 | Toutes les 10 min `[H]` le lundi de 8 h à 12 h | Relit « litiges » ; supprime tout brouillon non envoyé dont la facture vient d'entrer en litige, et avertit la gestionnaire clients (EF-04) | brouillon retiré | aucune | S2 illisible : passagère |

États d'une proposition : brouillon créé, envoyée, supprimée, en échec. Transitions : brouillon créé → envoyée (courriel envoyé par une personne, étape 8) ; brouillon créé → supprimée (la personne le supprime, l'étape 9 le retire, ou l'interrupteur) ; toute étape → en échec (erreur définitive ou reprises épuisées) ; en échec → brouillon créé (rejeu depuis la file des échecs).

Réglage du pilote. Pour le premier lundi du pilote (rubrique 13), l'indépendant désactive l'étape 8 : elle ne cherche aucune proposition et n'alerte pas, parce que les courriels du jour sont écrits et envoyés à la main. Il la remet en route avant le deuxième lundi (T-19).

Règle de niveau. Le niveau proposé pour une facture est celui qui suit sa dernière relance consignée (niveau 1 s'il n'y en a pas), si son délai est atteint : 7, 21 ou 35 jours après l'échéance `[H]`. Une facture ne saute jamais de niveau et ne reçoit qu'une relance par séance. La liste couvre toute facture qui a atteint un niveau sans relance consignée à ce niveau, même si elle a été écartée ou reportée à une séance précédente (EF-01, `30-exigences.md` version 1.1) : elle assure ainsi le report en première phase.

Rôle d'un modèle d'IA : sans objet, aucun modèle n'intervient.

**Traçabilité**

| EF | Étape(s) | Test(s) |
|---|---|---|
| EF-01 | 1, 3 | T-01, T-02 |
| EF-02 | 4 | T-03 |
| EF-03 | 3, 4 | T-04 |
| EF-04 | 4, 9 | T-05, T-06 |
| EF-06 | 4, 5, 7 | T-07 |
| EF-07 | 5 | T-08 |
| EF-08 | 5, 7 | T-09 |
| EF-10 | 5, 7 | T-10 |
| EF-11 | 8 | T-11, T-12 |
| ENF-08 | 3, 4, 5 | T-14 |
| ENF-09 | 1 | T-13 |
| ENF-10 | toutes | T-18 |

## 5. Flux de données

| Donnée | Origine | Traitement | Stockage et durée | Qui y accède | Sort-elle de l'entreprise ? |
|---|---|---|---|---|---|
| Extraction du lundi (factures échues, contacts, date du dernier rapprochement) | S1, extraite par la gestionnaire clients | lue par le flux ; brute | dossier de dépôt, supprimée après 30 jours `[H]` par la gestionnaire clients | gestionnaire clients, comptable, responsable financier, compte de service en lecture | elle transite par la plateforme, hébergée dans l'Union européenne à vérifier `[H]` (ENF-02) |
| Litiges | S2, alimenté par le support depuis S4 | lue ; brute | S2 | support, finance, compte de service en lecture | non |
| Comptes clés, règles (délais, seuil, modèles, jours fériés) | S2 | lues ; validées | S2 | responsable financier (écriture), compte de service en lecture | non |
| Propositions (clé, identifiant du client, niveau, état) | calcul du flux ; enrichie | écrite à l'étape 5 | classeur du dispositif, 90 jours `[H]` | gestionnaire clients, responsable financier | non ; ni nom ni adresse |
| Brouillon (texte, nom et adresse du contact) | modèle et extraction ; enrichi | créé à l'étape 5 | boîte partagée de la finance (S3) jusqu'à envoi ou suppression | gestionnaire clients, comptable, responsable financier | oui, vers le client, à l'envoi par la personne |
| Historique (clé, niveau, date, expéditeur) | copie envoyée ; validée | écrit à l'étape 8 | S2 ; durée à fixer (Q-05) | finance | non |
| Journal d'exécution (clé, étape, résultat, heure) | flux | écrit à chaque étape | classeur du dispositif, 12 mois `[H]` | responsable financier, gestionnaire clients | non ; aucune donnée personnelle |

## 6. Intégrations et droits

| Système | Compte utilisé (de service) | Droits demandés | Droits strictement nécessaires | Propriétaire du compte |
|---|---|---|---|---|
| S1 | aucun | aucun | aucun : la gestionnaire clients dépose l'extraction | responsable financier (administre S1) |
| Dossier de dépôt | compte de service des listes | lecture | lecture seule | responsable financier |
| S2, classeur de pilotage (litiges, comptes clés, règles) | compte de service des listes | lecture | lecture seule | responsable financier |
| S2, classeur du dispositif (propositions, historique, échecs, commande) | compte de service des listes | lecture et écriture | écriture limitée à ces onglets | responsable financier |
| S3, boîte partagée de la finance | compte de service de la messagerie | création de brouillons dans deux dossiers ; lecture du dossier « Envoyés » ; suppression de ses propres brouillons | aucun droit d'envoi ; envoi des comptes clés limité au responsable financier `[H]` (Q-11) | responsable financier |
| Plateforme | compte de service nommé, jamais un compte personnel | administration du flux | idem | responsable financier ; suppléant : gestionnaire clients |

## 7. Gestion des erreurs

| Type | Exemples | Comportement exigé |
|---|---|---|
| Passagère | extraction pas encore déposée, S2 ou S3 indisponible, délai dépassé | 3 reprises espacées de 1, 5 puis 15 min, avec une légère variation `[H]`, durée totale 30 min `[H]` ; au-delà, file des échecs et alerte |
| Définitive | rapprochement trop ancien, date du rapprochement absente, date d'échéance vide, contact absent, droit refusé, modèle introuvable | aucune reprise, qui retarderait l'alerte ; file des échecs et alerte immédiate. Une facture en cause va dans « à traiter à la main », jamais dans les propositions |

**File des échecs.** Onglet « échecs » du classeur du dispositif : clé, étape, erreur, heure. Consultable, rejouable (la gestionnaire clients coche « rejouer » et relance le flux sur ces clés). Conservée 90 jours `[H]` ; elle ne contient ni nom ni adresse. Vidée par la gestionnaire clients à chaque séance.

**Alerte.** Destinataire : la gestionnaire clients, suppléante : la comptable, pour une séance ; le responsable financier, suppléant : la gestionnaire clients, pour un silence ou un incident sur un compte clé. Canal : message dans la messagerie. Contenu : étape, clé, erreur, heure. Délai maximal : 5 min `[H]`.

**Interrupteur d'arrêt.** Une case « Suspendre » dans l'onglet « commande » du classeur du dispositif, modifiable par la gestionnaire clients et le responsable financier. Le flux la lit avant chaque étape. Suspendu, il ne crée plus rien et supprime les brouillons non envoyés ; l'étape 8 continue, pour que l'historique reste juste. Repli : la méthode d'avant, liste à la main selon la procédure unique (option 0).

**Plafonds.** Une exécution à la fois, un verrou l'impose. 100 propositions au plus par exécution `[H]` : au-delà, arrêt et alerte « volume anormal » (le rejeu de la séance du 2026-09-07 en produit 42 en première phase, comptes clés compris `[E]` : 61 − 9 − 4 − 6). L'étape 8 ne déclenche aucun autre flux.

## 8. Dédoublonnage

| Écriture non répétable | Clé stable | Où la clé est vérifiée, où elle est enregistrée |
|---|---|---|
| Création d'un brouillon | numéro de facture + niveau | vérifiée dans « propositions » avant la création (une proposition supprimée ou en échec ne bloque pas une nouvelle création) ; enregistrée après la réussite |
| Ligne d'historique | numéro de facture + niveau | vérifiée dans « historique » avant l'écriture ; enregistrée à la réussite. Mise à jour par clé, jamais d'insertion aveugle |
| Envoi d'un courriel | numéro de facture + niveau | le flux n'envoie pas. Une seconde copie envoyée avec la même clé déclenche une alerte « double envoi » au responsable financier |

## 9. Secrets

| Secret (nom) | Ce qu'il permet | Où il est conservé | Propriétaire | Échéance ou rotation |
|---|---|---|---|---|
| accès-listes | lire S2 et le dossier de dépôt, écrire dans le classeur du dispositif | coffre de la plateforme | responsable financier | revue tous les 6 mois `[H]` |
| accès-messagerie | créer des brouillons, lire « Envoyés » | coffre de la plateforme | responsable financier | revue tous les 6 mois `[H]` |
| accès-alerte | envoyer les messages d'alerte | coffre de la plateforme | responsable financier | revue tous les 6 mois `[H]` |

Ce document nomme les secrets, jamais leur valeur.

## 10. Observabilité

**Journal.** Pour chaque élément : clé, étape, résultat, heure ; aucun nom ni adresse. Conservé 12 mois `[H]`. Lisible par le responsable financier et la gestionnaire clients.

**Compteurs.** Par exécution et par jour : propositions créées, écartées par motif (payée, déjà relancée, litige), mises à part (comptes clés), « à traiter à la main », envoyées, en échec.

**Alertes.** Sur échec (§7). Sur silence : si aucune exécution n'a eu lieu le lundi à 10 h `[H]`, alerte au responsable financier ; si le flux d'envoi n'a rien consigné alors que des courriels sont partis, alerte aussi. Sur liste vide suspecte : une extraction qui contient des factures de plus de 7 jours d'échéance `[H]` et aucune proposition ni motif d'écart. Sur litiges : aucune mise à jour de la liste depuis 3 jours ouvrés `[H]`.

**Revue.** La gestionnaire clients lit les compteurs chaque lundi ; le responsable financier relit le journal chaque mois `[H]`.

## 11. Environnements et versions

Un environnement de test séparé : un classeur et une boîte de messagerie de test, avec 61 factures fictives qui reproduisent le décompte de la séance du 2026-09-07, motifs compris `[F]`. Une sauvegarde datée des classeurs et du flux avant toute modification en production. Une version numérotée du flux à chaque changement (1.0, 1.1…), notée au journal. Retour arrière : réimporter la version précédente, environ 1 h `[H]`.

## 12. Plan de test et recette

| ID | Exigence ou étape couverte | Scénario | Données | Résultat attendu | Environnement |
|---|---|---|---|---|---|
| T-01 | EF-01 | séance du 2026-09-07 rejouée | 61 factures `[F]` | la liste contient les 61 factures, au bon niveau (CA-01) | test |
| T-02 | EF-01, règle de niveau | facture à J+6, J+7, J+8 ; facture à J+25 sans relance consignée ; facture dont le litige a été levé depuis la séance précédente | 5 factures fictives | J+6 absente ; J+7 et J+8 niveau 1 ; J+25 niveau 1, pas de saut ; la facture au litige levé figure sur la liste (CA-01, version 1.1) | test |
| T-03 | EF-02 | factures payées | 9 `[F]` | aucune proposée, motif « payée » (CA-02) | test |
| T-04 | EF-03 | factures déjà relancées au niveau | 4 `[F]` | aucune proposée, motif « déjà relancée » (CA-03) | test |
| T-05 | EF-04 | factures en litige | 6 `[F]` | aucune proposée, motif « litige » (CA-04) | test |
| T-06 | EF-04, étape 9 | litige saisi après la création des brouillons | 1 facture | brouillon supprimé en moins de 10 min `[H]`, gestionnaire avertie | test |
| T-07 | EF-06 | factures de comptes clés | 5 `[F]` | brouillons dans « Comptes clés à valider » seulement ; envoi par un autre rôle impossible ou alerte (CA-06) | test |
| T-08 | EF-07 | courriels des relances proposées | les 24 relances envoyées à la séance `[F]` (14, 7, 3), parmi les propositions | modèle du niveau, numéro, montant, échéance exacts, 0 écart `[H]` (CA-07) | test |
| T-09 | EF-08 | ouverture de la séance | les brouillons du rejeu | chacun lisible avec son niveau avant tout envoi (CA-11) | test |
| T-10 | EF-10 | tentative d'envoi par le compte de service | 1 brouillon | refusée, aucun courriel parti, tentative au journal (CA-08) | test |
| T-11 | EF-11 | 24 courriels envoyés par une personne | 24 | 24 lignes d'historique : facture, niveau, date, expéditeur (CA-09) | test |
| T-12 | dédoublonnage | flux 1 lancé deux fois ; courriel envoyé deux fois | 24 propositions | ni brouillon ni ligne en double ; alerte « double envoi » (CA-09) | test |
| T-13 | ENF-09, cas limite critique | client qui a payé vendredi, paiement non rapproché, rapprochement vieux de 4 jours `[H]` | 1 facture | aucune proposition, message « rapprochement trop ancien » (CA-10) | test |
| T-14 | ENF-08 | factures sans adresse | 3 `[H]` | aucune proposée, listées « à traiter à la main » | test |
| T-15 | erreur passagère, reprise après panne | S2 coupé 10 min `[H]` ; flux interrompu au milieu des brouillons | 61 factures | reprises puis succès ; reprise du flux sans doublon | test |
| T-16 | erreur définitive | extraction illisible | 1 fichier | aucune reprise, file des échecs, alerte en moins de 5 min `[H]` | test |
| T-17 | pointe de volume | extraction de 150 factures `[H]` ; extraction produisant plus de 100 propositions | 2 jeux | moins de 5 min `[H]` (ENF-05) ; au-delà du plafond, arrêt et alerte | test |
| T-18 | ENF-10, alerte sur silence | case « Suspendre » cochée en cours de séance ; flux non lancé à 10 h `[H]` | brouillons non envoyés | brouillons non envoyés supprimés, aucun nouveau ; alerte au responsable financier | test |
| T-19 | pilote en parallèle (rubrique 13), réglage de l'étape 8 | les 24 courriels de la séance écrits et envoyés à la main pendant que le flux crée ses brouillons ; puis étape 8 remise en route | les 24 relances envoyées à la séance `[F]` | étape 8 désactivée : aucune alerte « identifiant introuvable », aucune ligne d'historique écrite par le flux ; remise en route : un courriel envoyé depuis un brouillon met à jour sa proposition | test |

**Cas limite critique.** Un client a payé vendredi, le paiement n'est pas rapproché et la facture atteint un niveau le lundi : aucune relance ne doit partir. C'est la panne de 2024 `[H]`, identifiée avec le responsable financier à partir de `20-diagnostic.md` §8. Test nommé : T-13. La recette échoue sans lui.

**Recette.** Prononcée par la gestionnaire clients et le responsable financier, pas par l'indépendant. Sur le rejeu des 61 factures, avec les critères de `30-exigences.md` §9, version 1.1 : CA-01 à CA-04 et CA-06 à CA-11 pour la première phase.

## 13. Pilote

- **Périmètre.** La séance du lundi, les trois niveaux, comptes clés compris ; quatre lundis consécutifs après la recette `[H]`.
- **Mode.** Premier lundi en parallèle : la gestionnaire clients mène la séance à la main (option 0), envoie ses propres courriels et note l'historique à la main ; elle compare avec les propositions, les écarts sont expliqués un par un, et elle supprime les brouillons du flux en fin de séance. L'étape 8 est désactivée ce jour-là (rubrique 4, T-19). Lundis 2 à 4 : en préparation avec validation systématique, la méthode à la main restant disponible comme repli.
- **Mesures relevées.** Les sept indicateurs de la rubrique 14 (IND-01 à IND-07).
- **Seuils du pilote.** Ils sont propres au pilote et distincts des seuils de production de la rubrique 14 : un pilote s'arrête plus tôt, sur peu de mesures. Pour la durée de la séance, le pilote s'arrête à plus de 115 min deux lundis de suite, la production à plus de 156 min deux lundis de suite (IND-03).
- **Généralisation.** Sur les lundis 2 à 4 : séance de 60 min au plus en moyenne (IND-03, cible de `10-besoin.md` §8 `[F]`) ; aucune relance envoyée sans validation (IND-04) ; aucune relance à tort imputable au flux (IND-02) ; maintenance de 1,1 h par mois au plus `[E]`.
- **Prolongation.** Séance entre 60 min `[F]` et 115 min `[E]` en moyenne (IND-03) : quatre lundis de plus, avec ajustement des règles.
- **Arrêt.** Une relance envoyée sans validation (IND-04), ou deux relances à tort dans la semaine (IND-02), ou une séance au-dessus de 115 min `[E]` deux lundis de suite (IND-03) : on suspend (ENF-10) et on revient à l'option 0.
- **Qui décide.** Le responsable financier ; la direction générale est informée.

Le calendrier et l'accompagnement sont dans `70-plan.md`.

## 14. Indicateurs

Reprise des indicateurs de `30-exigences.md` §10 (IND-01 à IND-07) ; l'entreprise mesure, pas le pack. Cette rubrique est la seule maison des seuils de production : correction, alerte, arrêt. Les seuils du pilote sont ceux de la rubrique 13. Un gain reste estimé tant qu'il n'est pas observé : les 136 € par mois sont `[E]` jusqu'aux quatre lundis du pilote.

| Indicateur (IND-xx) | Source de la mesure | Méthode | Périodicité · qui mesure | Départ à relever avant le pilote | Seuils de production : correction · alerte · arrêt | Attribution |
|---|---|---|---|---|---|---|
| IND-01 Réclamations après relance | réclamations du support (S4) | compte par semaine, par motif | chaque semaine · responsable du support | 13 par mois `[F]` ; motifs à classer (Q-07) | correction : plus de 7 par mois (la cible `[F]`) ; alerte : plus de 13 par mois (le départ) ; arrêt : plus de 13 par mois deux mois de suite `[H]` | « a contribué à » : les réclamations varient avec l'activité ; même période de l'an passé si le relevé existe `[H]` |
| IND-02 Relances parties à tort | colonne « à tort » de l'historique | comptage des cas constatés par la finance ou le support | chaque jour du pilote, puis chaque lundi · gestionnaire clients | à relever `[H]` (Q-07) | alerte : un cas ; arrêt : deux cas dans la semaine ; pas de seuil de correction | sans objet : tout cas est un défaut |
| IND-03 Durée de la séance | heure de début et de fin notée par la gestionnaire clients | minutes, par phase | chaque lundi · gestionnaire clients | 156 min `[F]` ; trois lundis re-mesurés | correction : plus de 60 min (la cible `[F]`) ; alerte : plus de 115 min `[E]` (le niveau des seules simplifications, `20-diagnostic.md` §9) ; arrêt : plus de 156 min deux lundis de suite | « a contribué à » : une seule équipe, pas de groupe témoin |
| IND-04 Relances envoyées sans validation humaine | copies envoyées comparées aux propositions, et droits d'envoi | comptage | à chaque envoi · responsable financier | 0 `[F]` | alerte et arrêt : un cas ; pas de seuil de correction | sans objet : tout cas est un défaut |
| IND-05 Part des relances proposées retirées ou corrigées | propositions supprimées ou brouillons modifiés | pourcentage | chaque lundi · gestionnaire clients | aucun départ `[H]` | correction : plus de 10 % `[H]` ; alerte : plus de 20 % `[H]` ; arrêt : plus de 30 % deux lundis de suite `[H]` | sans objet : mesure d'usage |
| IND-06 Stock des retards de plus de 35 jours | extraction de S1 | nombre et montant | chaque mois · responsable financier | 33 factures, 30 900 € HT `[E]` | correction : plus de 33 factures deux relevés de suite `[H]` ; alerte : plus de 40 `[H]` ; arrêt : sans objet (indicateur de contexte) | « a contribué à » : la saison et quelques gros clients pèsent |
| IND-07 Appels aux clients en retard de plus de 35 jours | décompte tenu à la main | nombre | chaque mois · responsable financier | à mesurer avant le lancement `[H]` | correction : moins de la moitié de ces clients appelés dans le mois `[H]` ; alerte : aucun appel ; arrêt : sans objet (indicateur de contexte) | « a contribué à » |

## 15. Risques

| ID | Risque | Probabilité `[H]` | Impact | Parade | Signal d'alerte |
|---|---|---|---|---|---|
| R-01 | Une relance part chez un client qui a payé : rapprochement oublié | moyenne | haut | contrôle de fraîcheur (ENF-09), relecture humaine | rapprochement daté de plus d'un jour ouvré |
| R-02 | La plateforme héberge hors de l'Union européenne ou change ses conditions | basse | haut | page de l'éditeur lue et datée avant de signer ; revue tous les 6 mois `[H]` | avis de l'éditeur |
| R-03 | Un connecteur évolue et le flux s'arrête sans bruit | moyenne | moyen | alerte sur silence | aucune exécution le lundi à 10 h `[H]` |
| R-04 | Un compte clé est envoyé sans le responsable financier | basse | haut | envoi limité à son compte ; sinon contrôle des copies envoyées | alerte « envoi hors validation » |
| R-05 | La liste des litiges n'est plus alimentée | moyenne | haut | alerte après 3 jours ouvrés sans mise à jour `[H]` | colonne en retard (pré-mortem de `04-feuille-de-route.md` version 1.1, ligne 1) |
| R-06 | Le temps gagné reste sous environ 80 min par séance `[E]` | moyenne | moyen | porte avant la construction, pilote avec arrêt | séance au-dessus de 60 min `[F]` |
| R-07 | S1 est remplacé en mars 2027 | basse | haut | entrées en fichiers, règles écrites ici | décision de renouvellement à l'ordre du jour |
| R-08 | L'indépendant n'est plus disponible | moyenne | moyen | cette spécification, fiche d'une page, suppléant désigné | demande de modification sans réponse sous 5 jours ouvrés `[H]` |

## 16. Questions ouvertes

| ? | Question | Rôle qui répond | Bloquante avant construction ? |
|---|---|---|---|
| Q-03 | Qui tient la liste des comptes clés, où est-elle écrite ? | responsable financier | oui |
| Q-05 | Quelle base légale et quelle durée de conservation pour l'historique ? | personne désignée par la direction générale | oui, avant la production |
| Q-06 | Jour et heure du rapprochement avant la séance | comptable | oui |
| Q-09 | Quelle plateforme, quel éditeur, quelle région d'hébergement ? | indépendant, après lecture des pages des éditeurs | oui |
| Q-10 | L'extraction de S1 porte-t-elle la date du dernier rapprochement des paiements ? À défaut, la comptable la saisit dans un fichier d'une ligne | responsable financier | oui |
| Q-11 | La messagerie permet-elle de limiter l'envoi d'un dossier de brouillons à un compte, et un identifiant de relance non visible du client se retrouve-t-il sur la copie envoyée ? À défaut : contrôle des copies envoyées et correspondance par numéro de facture et destinataire | responsable financier, indépendant | oui |
| Q-07 | Quel est le motif des 13 réclamations d'un mois `[F]` : relance à tort ou autre cause ? (départ de l'indicateur de relances à tort) | responsable du support | non, mais avant le pilote |
| Q-08 | Quelle règle suit la comptable quand elle remplace la gestionnaire clients ? | comptable | non |
| Q-02 | Quel seuil de montant pour la seconde phase ? | responsable financier | non |

## 17. Propriétaire de la maintenance

Propriétaire : le responsable financier, qui décide des changements de règles et détient les comptes de service. Maintenance courante : la gestionnaire clients, 1 h par mois `[H]` à son coût horaire (31 €), comme dans `50-rentabilite.md` ; la part de l'option 0 (0,5 h par mois) est celle du responsable financier, à son propre coût horaire. Suppléante : la comptable. Fiche d'une page à livrer avec le flux : ce que fait le dispositif, ses dépendances (S2, S3, plateforme, comptes de service), comment le mettre en pause (case « Suspendre »), comment rejouer la file des échecs.

Rythme de revue : accès tous les 6 mois `[H]` ; après tout changement de S1, S2 ou S3. Un changement est demandé au responsable financier, testé dans l'environnement de test, puis déployé en version numérotée avec sauvegarde.

## Décision attendue

Valider la spécification comme entrée de l'équipe qui construit — ou la corriger ; lever les questions bloquantes ; nommer le propriétaire de la maintenance.
