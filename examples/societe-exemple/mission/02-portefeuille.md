# Portefeuille de cas d'usage — Société Exemple, cinq équipes

2026-09-16 · Demandeur et valideur : direction générale · Rédigé par : consultant IA

## 1. Vue d'ensemble

Valeur = gain mensuel `[E]`, calculé comme durée × volume de `01-cartographie-taches.md` : c'est un plafond (100 % du temps actuel), que `03-chiffrage.md` réduira. Les durées et volumes en `[H]` viennent de la direction seule pour les ventes et la logistique. Facilité et risque : haut, moyen ou bas, avec une raison d'une ligne ; « à classer » quand une donnée manque, avec la donnée et la personne qui la fournit. Pour un cas trié « Simplifier d'abord », ils se notent après simplification.

| Cas | Équipe(s) | Valeur (gain mensuel `[E]`) | Facilité | Risque | Classe (raison si « À écarter ») |
|---|---|---|---|---|---|
| Tri des tickets entrants | Support | 20,5 h (1 min × 1 230 tickets) | haute : huit catégories écrites, volumes mesurés, règles de classement peut-être déjà dans l'outil `[H]` | bas : un ticket mal classé est repris par la permanence | Gains rapides |
| Relances de factures échues | Finance (avec le support et les ventes) | 10,4 h (6,5 min × 96 relances) | moyenne après simplification : données accessibles ; les trois règles à écrire et les litiges que la finance ne voit pas sont les simplifications à faire d'abord | haut : un message part chez un client, essai raté en 2024 ; validation humaine avant tout envoi | Projets |
| Statut de commande | Support (avec la logistique) | 24 h (3 min × 480 tickets) | moyenne : suivi du transporteur saisi à la main, parfois périmé `[H]` | moyen : un statut faux se voit chez le client ; validation par échantillon | Projets |
| Rapprochement des paiements | Finance | 8 h `[H]` (120 min × 4 séances) | à classer : le logiciel sait-il importer un fichier bancaire ? `[H]` | moyen : écriture comptable, validée par la comptable | À creuser : manque les capacités du logiciel, que fournit le responsable financier |
| Demandes de devis | Ventes | 33,3 h `[H]` (10 min × 200 demandes) | à classer : volume et durée jamais mesurés `[H]` | moyen : un prix faux engage l'entreprise | À creuser : manque une mesure, que fournit le responsable des ventes |
| Réapprovisionnement | Logistique | 16 h `[H]` (240 min × 4 mises à jour) | à classer : seuils non vérifiés `[H]` | moyen : rupture ou surstock ; la décision d'achat reste humaine | À creuser : manquent les seuils et une mesure, que fournit le responsable logistique |
| Aide à la réponse aux réclamations de facture | Support | 3,0 h (14 min × 13 tickets) | moyenne : données dans trois outils | haut : un geste commercial mal décidé | À écarter : valeur faible, et la cause se traite à la source par le cas des relances |

## 2. Fiches

### Tri des tickets entrants — Gains rapides
- **Résultat** : chaque ticket entrant arrive classé dans l'une des huit catégories et affecté à la bonne personne.
- **Pour qui** : la permanence du support (responsable du support et agents, en rotation).
- **Problème** : la permanence lit et classe chaque ticket à la main ; 67 tickets par mois restent non classés `[F]`.
- **Déclencheur** : l'arrivée d'un ticket dans la boîte partagée du support.
- **Entrées** : l'objet et le texte du ticket ; la liste des huit catégories ; les règles d'affectation par catégorie, à écrire ; l'historique du client, facultatif.
- **Ce que fait le système** : 1. lit l'objet et le texte ; 2. propose une catégorie ; 3. propose une affectation ; 4. marque « à vérifier » quand le doute est fort ; 5. la permanence confirme ou corrige.
- **Sorties** : la catégorie et l'affectation, écrites dans l'outil de tickets ; la liste des tickets « à vérifier ».
- **Valeur** : temps. 1 min × 1 230 tickets = 1 230 min = 20,5 h par mois `[E]` (plafond). Qualité : moins de tickets non classés (67 par mois `[F]`).
- **Limites et validation humaine** : tickets ambigus ou à plusieurs sujets ; la permanence valide les cas douteux ; l'étiquette « litige » reste posée par un humain ; le contenu des tickets (noms, adresses) reste dans l'outil, dans l'Union européenne.
- **Preuve** : observé — export des tickets (1 230 tickets par mois, 5,4 % non classés `[F]`) ; déclaré — entretien support (1 min par ticket `[H]`, le responsable du support peut le confirmer).
- **Déjà disponible** : l'outil de tickets propose peut-être des règles de classement automatiques, jamais activées `[H]` (le responsable du support peut le confirmer).

### Relances de factures échues — Projets
- **Résultat** : les relances de factures échues partent au bon moment, au bon client et seulement quand elles sont justifiées, après validation d'un humain.
- **Pour qui** : la gestionnaire clients, qui prépare et envoie ; le responsable financier, qui valide les comptes clés et reçoit le troisième niveau en copie.
- **Problème** : la séance du lundi dure 156 min `[F]`, dont 76 min de contrôles à la main `[E]` ; des relances partent encore à des clients qui ont payé ou qui sont en litige (13 réclamations par mois `[F]`).
- **Déclencheur** : chaque lundi, les factures qui atteignent J+7, J+21 ou J+35 après l'échéance.
- **Entrées** : l'export des factures échues ; l'historique des relances (onglet « suivi ») ; les paiements rapprochés ; les litiges connus du support ; la liste des comptes clés ; les modèles de courriel.
- **Ce que fait le système** : d'abord, sans système, on simplifie (procédure unique avec les trois règles écrites, lettrage avant la séance, colonne « litige » alimentée chaque jour, liste des comptes clés) et on re-mesure la séance. Ensuite : 1. calcule le niveau de chaque facture ; 2. écarte les factures déjà relancées à ce niveau, payées, en litige ou sous le seuil ; 3. met à part les comptes clés pour validation ; 4. prépare un courriel par facture à partir du modèle du niveau ; 5. présente la liste et les motifs d'exclusion ; 6. note chaque envoi dans le suivi.
- **Sorties** : la liste des relances proposées, avec le motif de chaque exclusion ; les brouillons de courriel ; le suivi à jour.
- **Valeur** : temps. 6,5 min × 96 relances = 624 min = 10,4 h par mois `[E]` (plafond, avant simplification : la re-mesure le précisera). Trésorerie et relation client : non chiffrées.
- **Limites et validation humaine** : aucun envoi sans validation humaine (décision de la direction après l'essai de 2024) ; comptes clés validés par le responsable financier ; litiges à signaler par le support ; trois règles non écrites à fixer d'abord (seuil de 15 €, comptes clés, litiges).
- **Preuve** : observé — séance du 2026-09-07 (61 factures, 24 relances, 37 non relancées avec leur motif `[F]`) et export de facturation (96 relances par mois `[F]`) ; déclaré — entretien finance ; hypothèse `[H]` — environ trois plaintes en 2024 (le responsable financier peut confirmer).
- **Déjà disponible** : le module de relances automatiques du logiciel de facturation est présent et désactivé `[F]` (export de facturation) ; ses capacités d'exclusion ne sont pas vérifiées `[H]` (le responsable financier peut les confirmer).

### Statut de commande — Projets
- **Résultat** : le client connaît l'état de sa commande sans avoir à le demander, ou reçoit la réponse sans attendre un agent.
- **Pour qui** : les agents du support ; les clients.
- **Problème** : 480 tickets par mois `[F]` posent la même question ; chaque réponse demande 3 min `[H]` de recherche dans trois outils.
- **Déclencheur** : un ticket de statut ; en amont, l'expédition d'une commande.
- **Entrées** : le numéro de commande ; son statut dans le logiciel de facturation ; le numéro de suivi du transporteur (tableur des expéditions, saisi à la main) ; le modèle de réponse.
- **Ce que fait le système** : 1. reconnaît un ticket de statut ; 2. retrouve la commande ; 3. lit le statut et le suivi ; 4. prépare la réponse type ; 5. un agent valide, par échantillon au début.
- **Sorties** : une réponse prête à envoyer ; le ticket clos ou signalé.
- **Valeur** : temps. 3 min × 480 tickets = 1 440 min = 24 h par mois `[E]` (plafond).
- **Limites et validation humaine** : le suivi est périmé 2 à 3 fois par semaine `[H]`, donc une réponse peut être fausse ; tout cas inhabituel (retard, colis perdu) reste à un agent ; validation par échantillon.
- **Preuve** : observé — export des tickets (480 tickets de statut sur 1 230 `[F]`) ; déclaré — entretien support (3 min par ticket `[H]` ; suivi parfois périmé `[H]`).
- **Déjà disponible** : rien de vérifié. À vérifier d'abord : un avis d'expédition envoyé automatiquement au client par le logiciel de facturation `[H]` (le responsable financier peut le confirmer), qui supprimerait une partie de ces tickets.

### Rapprochement des paiements — À creuser
- **Résultat** : les paiements reçus sont rapprochés des factures dès leur arrivée, avant la séance des relances.
- **Pour qui** : la comptable.
- **Problème** : le lettrage a lieu une fois par semaine, le jeudi, en 2 h `[H]` ; le lundi, des paiements du vendredi ne sont pas rapprochés (9 factures sur 61 `[F]`).
- **Déclencheur** : la réception du fichier bancaire.
- **Entrées** : le relevé bancaire ; les factures ouvertes ; les règles de rapprochement (montant, référence).
- **Ce que fait le système** : 1. lit le fichier bancaire ; 2. propose les rapprochements évidents ; 3. liste les lignes non reconnues ; 4. la comptable valide.
- **Sorties** : les paiements lettrés ; la liste des écarts.
- **Valeur** : temps. 120 min × 4 séances = 480 min = 8 h par mois `[E]` (plafond).
- **Limites et validation humaine** : écritures comptables, validées par la comptable ; paiements groupés et exceptions.
- **Preuve** : déclaré — entretien finance (2 h par séance `[H]`, la comptable peut le confirmer) ; observé — export de facturation (dernier lettrage le jeudi 2026-08-27) et séance (9 factures payées non rapprochées `[F]`).
- **Déjà disponible** : le logiciel sait peut-être importer un fichier bancaire et proposer les rapprochements `[H]` (le responsable financier peut le confirmer).

### Demandes de devis — À creuser
- **Résultat** : une demande de devis reçue par courriel devient un brouillon de devis prêt à relire.
- **Pour qui** : les commerciaux.
- **Problème** : la demande est ressaisie à la main dans le logiciel, 10 min `[H]` par demande, 200 demandes par mois `[H]`.
- **Déclencheur** : le courriel d'un client qui demande un devis.
- **Entrées** : le texte libre du courriel ; le catalogue ; la grille tarifaire et les règles de remise ; l'historique du client.
- **Ce que fait le système** : 1. extrait produits et quantités ; 2. les rapproche du catalogue ; 3. applique la grille ; 4. prépare le brouillon dans le logiciel ; 5. signale ce qui manque ; 6. le commercial relit et envoie.
- **Sorties** : un brouillon de devis ; la liste des questions à poser au client.
- **Valeur** : temps. 10 min × 200 demandes = 2 000 min = 33,3 h par mois `[E]` (plafond, sur deux `[H]`).
- **Limites et validation humaine** : un prix faux engage l'entreprise ; les remises exceptionnelles vont à la direction ; validation avant tout envoi.
- **Preuve** : déclaré par la direction seule `[H]` (le responsable des ventes peut le confirmer) ; non observé.
- **Déjà disponible** : rien de vérifié.

### Réapprovisionnement — À creuser
- **Résultat** : des propositions de réapprovisionnement prêtes, que le responsable logistique valide.
- **Pour qui** : le responsable logistique.
- **Problème** : le tableau de réapprovisionnement est remis à jour à la main chaque semaine, 240 min `[H]`, par ressaisie entre le logiciel et le tableur.
- **Déclencheur** : le début de la semaine.
- **Entrées** : les stocks ; les ventes récentes ; les seuils de réassort ; les délais des fournisseurs.
- **Ce que fait le système** : 1. lit les stocks et les ventes ; 2. les compare aux seuils ; 3. propose les quantités ; 4. le responsable logistique valide.
- **Sorties** : un tableau de propositions de commande.
- **Valeur** : temps. 240 min × 4 mises à jour = 960 min = 16 h par mois `[E]` (plafond, sur deux `[H]`).
- **Limites et validation humaine** : la décision d'achat reste humaine ; seuils non vérifiés.
- **Preuve** : déclaré par la direction seule `[H]` (le responsable logistique peut le confirmer) ; non observé.
- **Déjà disponible** : le logiciel calcule peut-être des seuils de réassort `[H]` (le responsable logistique peut le confirmer).

### Aide à la réponse aux réclamations de facture — À écarter
- **Résultat** : pour une réclamation après relance, l'agent a sous les yeux le résumé du dossier (facture, paiement, relances reçues).
- **Pour qui** : les agents du support. Qui décide : l'agent pour la réponse, la finance pour l'avoir.
- **Problème** : chaque réclamation demande 14 min `[H]` pour rassembler les informations et appeler la finance.
- **Déclencheur** : un ticket de réclamation après relance.
- **Entrées** : la facture ; le paiement ; l'historique de relance ; les échanges du ticket.
- **Ce que fait le système** : 1. rassemble les pièces ; 2. résume le dossier ; 3. signale les incohérences ; 4. l'agent décide.
- **Sorties** : un résumé de dossier dans le ticket.
- **Valeur** : temps. 14 min × 13 tickets = 182 min = 3,0 h par mois `[E]` (plafond). Valeur faible : c'est la raison de la classe « À écarter » ; la cause se traite à la source, par le cas des relances (moins de relances à tort, moins de réclamations).
- **Limites et validation humaine** : l'avoir et le geste commercial sont des décisions humaines ; le résumé contient des données personnelles.
- **Preuve** : observé — export des tickets (13 réclamations par mois `[F]`) ; déclaré — entretien support (14 min par ticket `[H]`).
- **Déjà disponible** : rien.

## 3. Recommandation

**À éliminer d'abord, sans IA.**
- Le rapport hebdomadaire des ventes : 3 h et 165 € par mois `[E]`, que la direction ne lit pas `[H]`. Test de suppression de quatre semaines, réversible. Décident : la direction générale et le responsable des ventes.
- Le rapport mensuel de pilotage : le réduire aux trois chiffres que la direction lit (ventes, encaissements, valeur du stock) avant de songer à l'automatiser ; gain non chiffré tant que la version courte n'existe pas. Décident : la direction générale et le responsable financier.
- La cause des demandes de statut : si le logiciel peut envoyer un avis d'expédition au client `[H]`, une partie des 480 tickets par mois `[F]` disparaît. Décide : le responsable financier, qui administre l'outil.

**Trois cas à faible effort et forte valeur, un par équipe quand c'est possible.** Il n'y a qu'un gain rapide, le tri des tickets. Les relances et le statut de commande sont des projets, recommandés pour leur valeur (10,4 h et 24 h par mois `[E]`) et parce que la trésorerie est la priorité de la direction. Le support compte deux cas, la finance un. La direction et les ventes sont servies par la suppression des rapports ; la logistique attend son entretien.

**Ce qui ferait changer cette recommandation.**
- Le module de relances du logiciel sait exclure litiges, comptes clés et petits montants `[H]` : les relances deviennent un réglage, plus un projet.
- Un avis d'expédition automatique existe : le statut de commande perd l'essentiel de sa valeur et sort de la liste.
- Les ventes mesurent plus de 30 h par mois de ressaisie de devis : le cas des devis passe devant le statut de commande.
- La direction veut toutes les équipes couvertes avant de lancer : on ajoute le rapprochement des paiements et le réapprovisionnement après leurs entretiens courts.

## Décision attendue

Quels cas creuser : pour chacun, creuser, mettre en attente ou écarter.
- Creuser : tri des tickets, relances de factures échues, statut de commande.
- Mettre en attente : rapprochement des paiements (le responsable financier lit la documentation de l'éditeur), demandes de devis (entretien court avec le responsable des ventes), réapprovisionnement (entretien court avec le responsable logistique).
- Écarter : aide à la réponse aux réclamations de facture.
