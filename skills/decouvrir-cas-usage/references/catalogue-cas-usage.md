# Catalogue de pistes par fonction

> **Pistes à vérifier sur le terrain, pas des recommandations.** Ce catalogue aide à poser de bonnes
> questions et à relire une cartographie ; il ne dit rien de l'entreprise étudiée. Aucun gain n'y est
> chiffré : le chiffrage vient des mesures de l'entreprise (`chiffrer-rentabilite`).

À ouvrir à l'étape « Formuler les cas d'usage » de `decouvrir-cas-usage`.

## Comment s'en servir

1. Parcourir les fonctions présentes dans l'entreprise et chercher, dans les sources ou en entretien, le
   signal de chaque piste.
2. Une piste entre dans le portefeuille seulement si une tâche de `01-cartographie-taches.md` la fonde
   (preuve « observé » ou « déclaré »). Sinon elle reste une hypothèse `[H]`, classée « À creuser », avec
   la question à poser.
3. Écrire chaque piste comme un résultat métier, pas comme un outil. Si l'entreprise répond « on a déjà
   un outil pour ça », c'est la réponse la moins chère : la noter dans « Déjà disponible ».
4. Adapter : le secteur, la taille et les outils changent les données, la validation et les contraintes.
   Dédoublonner avec les cas déjà trouvés (même déclencheur, même transformation, même résultat, même
   responsable = un seul cas).
5. Avant de retenir une piste, se demander si la tâche ne devrait pas plutôt disparaître (dernière
   section).

## Vente

| Piste (résultat visé) | Signal à chercher | À vérifier avant de retenir |
|---|---|---|
| Comptes rendus de rendez-vous rédigés et saisis dans le CRM sans ressaisie | notes prises à la main puis recopiées ; champs du CRM vides ou remplis tard | qualité de la source (notes, enregistrement) ; accord des interlocuteurs pour enregistrer ; relecture par le commercial |
| Demandes entrantes qualifiées et routées vers le bon commercial | formulaires et courriels triés à la main ; délais de première réponse très variables | critères de qualification écrits ; sort des cas ambigus |
| Devis et propositions préparés à partir d'un brief et d'un catalogue | documents recomposés depuis d'anciennes propositions ; remises décidées au cas par cas | règles de prix et de remise ; validation avant tout envoi à un client |
| Relances de devis et d'opportunités dormantes au bon moment | opportunités sans date de prochaine action ; relances faites de mémoire | qui choisit le ton et le moment ; fréquence acceptable pour le client |
| Préparation d'un rendez-vous : synthèse du compte, de l'historique et des actualités | plusieurs onglets ouverts avant chaque rendez-vous | accès aux données du CRM ; fraîcheur des informations |
| Qualité des données du CRM : doublons, champs vides, fiches périmées | rapports de pipeline auxquels personne ne se fie ; nettoyages manuels périodiques | règles de fusion ; qui valide les fusions |
| Réponses aux appels d'offres ou questionnaires de conformité depuis une base de réponses validées | mêmes questions reposées d'un client à l'autre ; réponses copiées de documents anciens | existence de la base ; validation juridique ou sécurité |

## Marketing

| Piste (résultat visé) | Signal à chercher | À vérifier avant de retenir |
|---|---|---|
| Déclinaison d'un contenu validé en plusieurs formats (article, publications, lettre d'information) | contenus réécrits à la main pour chaque canal | ligne éditoriale ; relecture humaine avant publication |
| Premiers jets de contenus à partir de sources internes (études de cas, notes produit) | contenus attendus mais repoussés faute de temps ; sources dispersées | exactitude des faits ; droit de citer un client ; validation |
| Rapport de performance assemblé à partir de plusieurs sources | rapport mensuel construit par copier-coller entre outils | définitions de métriques partagées ; qualité des données d'origine |
| Veille concurrentielle ou sectorielle synthétisée | veille faite « quand on a le temps » ; alertes lues par une seule personne | sources autorisées ; ce que l'équipe fait réellement de la veille |
| Contacts issus d'événements ou de formulaires nettoyés et qualifiés | fichiers importés à la main ; doublons ; enrichissement manuel | base légale d'utilisation des contacts ; règles de protection des données |
| Variantes de textes pour des tests (objets de courriel, annonces) | tests limités par le temps de rédaction | cadre de marque ; mesure du test |
| Brouillons de réponses aux avis et commentaires | avis sans réponse ; réponses écrites une à une | ton de marque ; les cas sensibles (litige, santé) restent traités par un humain |

## Service client

| Piste (résultat visé) | Signal à chercher | À vérifier avant de retenir |
|---|---|---|
| Demandes entrantes triées et routées (catégorie, urgence, langue) | tickets triés à la main ; réaffectations fréquentes | catégories stables ; taux actuel de mauvaise affectation |
| Brouillons de réponses depuis la base de connaissances, validés par l'agent | agents qui cherchent la même réponse dans plusieurs documents | base à jour ; validation avant envoi |
| Questions fréquentes traitées, avec passage à un humain quand il le faut | mêmes questions reçues chaque semaine ; demandes de statut | seuils de transfert ; ce qui ne doit jamais être répondu seul |
| Résumé d'un échange pour un transfert entre niveaux ou entre équipes | clients qui doivent répéter leur problème | données personnelles contenues dans le résumé |
| Repérage des demandes à risque (résiliation, réclamation, urgence) | escalades tardives ; réclamations découvertes après coup | définition du risque ; qui est alerté, et quand |
| Base de connaissances mise à jour depuis les tickets résolus | savoir-faire dans la tête des agents ; articles périmés | propriétaire de la base ; validation du contenu |
| Analyse des motifs de contact pour agir sur leur cause | mêmes motifs chaque mois ; demandes provoquées par un défaut d'information ou de produit | qualité des catégories ; supprimer la cause vaut mieux que mieux traiter le ticket (issue « Éliminer ») |

## Finance et comptabilité

| Piste (résultat visé) | Signal à chercher | À vérifier avant de retenir |
|---|---|---|
| Données des factures fournisseurs extraites et pré-saisies | saisie manuelle de factures aux formats variés | validation avant comptabilisation ; séparation des tâches |
| Rapprochement bancaire assisté | lignes non rapprochées traitées à la main chaque mois | règles de rapprochement ; exceptions |
| Relances des factures clients échues | liste des échus tenue dans un tableur ; relances à des rythmes différents | politique de relance écrite ; clients sensibles traités par un humain |
| Notes de frais contrôlées face à la politique | contrôles manuels ; justificatifs manquants | politique écrite ; le rejet reste une décision humaine |
| Clôture préparée : contrôles et écarts à expliquer | clôture lente ; listes de contrôles dans un tableur | périmètre ; responsabilité comptable : les écritures restent validées par un humain |
| Écarts budgétaires commentés pour le reporting | analyses rédigées à la main ; mêmes explications reprises | accès aux données ; validation par le contrôle de gestion |
| Réponses aux fournisseurs sur le statut des paiements | « où en est ma facture ? » reçu régulièrement | accès en lecture au statut ; informations qu'on peut donner |

## Ressources humaines

| Piste (résultat visé) | Signal à chercher | À vérifier avant de retenir |
|---|---|---|
| Fiches de poste et offres rédigées ou relues à partir d'un modèle | offres recopiées puis retouchées à la main | validation RH et du manager ; formulations à vérifier |
| Créneaux d'entretien proposés et confirmés | échanges de courriels pour fixer une date | calendriers accessibles ; accord des personnes |
| Questions RH fréquentes traitées depuis les documents internes | mêmes questions (congés, politique, paie) posées à l'équipe RH ; règles dispersées | exactitude et mise à jour ; les cas individuels restent humains |
| Parcours d'arrivée suivi : documents, accès, rappels aux managers | liste d'arrivée dans un tableur ; accès oubliés | outils concernés ; confidentialité |
| Synthèse anonymisée de retours d'enquêtes ou d'entretiens | commentaires libres peu exploités | anonymisation ; risque de réidentification |
| Documents standards préparés (promesses, avenants types) | documents recomposés par copier-coller de modèles | validation juridique ; données personnelles |
| Présélection structurée de candidatures sur critères explicites | volumes de candidatures traités à la main | **usage sensible** (décisions sur des personnes) : critères écrits, décision et validation humaines, conformité à faire vérifier avant tout essai |

## Opérations et logistique

| Piste (résultat visé) | Signal à chercher | À vérifier avant de retenir |
|---|---|---|
| Commandes suivies, retards signalés | statuts recoupés à la main entre plusieurs outils | qualité des statuts ; qui agit sur l'alerte |
| Données extraites des documents de transport, bons de livraison et bons de commande | saisie depuis des PDF ou des papiers | formats variés ; contrôle avant intégration |
| Propositions de réapprovisionnement validées par un humain | commandes passées « au jugé » ou depuis un tableur | historique disponible ; règles de stock ; la décision d'achat reste humaine |
| Clients informés des retards avant qu'ils ne demandent | clients qui appellent pour savoir où en est leur commande | message validé ; seuils de retard |
| Rapports quotidiens consolidés depuis plusieurs systèmes | rapport assemblé chaque matin par copier-coller | sources accessibles ; définitions communes |
| Demandes d'intervention (maintenance, incidents) triées et priorisées | demandes reçues par plusieurs canaux ; priorités décidées au cas par cas | critères de priorité ; les urgences de sécurité restent humaines |
| Procédures et consignes rédigées à partir d'enregistrements du travail | savoir-faire dans la tête des anciens ; procédures absentes ou périmées | accord des personnes ; validation par un responsable, sécurité comprise |

## Direction

| Piste (résultat visé) | Signal à chercher | À vérifier avant de retenir |
|---|---|---|
| Tableau de bord hebdomadaire consolidé, avec commentaire des écarts | chiffres demandés à plusieurs équipes avant chaque comité | sources fiables ; définitions communes |
| Réunions préparées, comptes rendus rédigés, actions suivies | décisions prises puis oubliées ; comptes rendus tardifs | accord pour enregistrer ; confidentialité |
| Synthèse de veille (marché, concurrents, réglementation) | informations lues au hasard des alertes | fiabilité des sources ; données confidentielles |
| Boîte de réception de direction triée, avec brouillons de réponse | direction submergée de demandes simples | accès à une messagerie sensible ; aucun envoi automatique |
| Dossiers de décision : synthèse de documents et comparatif d'options | dossiers volumineux résumés à la main | fidélité de la synthèse ; relecture |
| Engagements pris en comité suivis | engagements retrouvés par hasard | propriétaire du suivi ; rappels acceptables |
| Rapports aux financeurs ou aux actionnaires assemblés depuis les sources internes | reporting périodique recomposé à chaque fois | confidentialité ; validation avant diffusion |

## À éliminer ou à simplifier avant d'automatiser

Ces tâches reviennent souvent dans les cartographies et appellent d'abord une suppression :

- des rapports que personne ne lit ni n'utilise pour décider ;
- des validations systématiques qui n'ont jamais rien refusé ;
- une même information saisie dans deux outils ;
- des relances ou des contrôles faits « au cas où », sans règle ni effet constaté ;
- des réunions de suivi qui répètent un tableau déjà lisible ;
- des demandes récurrentes provoquées par un défaut d'information : supprimer la cause plutôt que traiter
  les demandes.
