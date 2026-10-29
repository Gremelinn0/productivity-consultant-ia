# Trame du cahier des charges CRM

Un cahier des charges CRM reste un cahier d'exigences du pack : les douze rubriques du modèle de
`rediger-cahier-des-charges/references/modeles.md`, mode exigences. Cette trame dit, rubrique par rubrique, ce
qu'un CRM doit y trancher, puis donne la méthode pour constituer les besoins et le gabarit des annexes. Les questions
qui obtiennent chaque réponse sont dans la base : `crm-parametrage` (le paramétrage, avec le consultant) et `crm`
(l'existant).

## 1. Ce que chaque rubrique tranche pour un CRM

| Rubrique du modèle | Ce qu'elle doit trancher pour un CRM |
|---|---|
| 1. Contexte et objectifs | l'entreprise (taille, structure, clientèle entreprises ou particuliers, canaux de vente) ; les objectifs d'affaires, traduits en objectifs opérationnels puis en indicateurs ; les facteurs de succès posés au lancement |
| 2. Utilisateurs et rôles | la liste des utilisateurs actuels et futurs, par équipe ; qui mène le projet, qui le sponsorise, qui arbitre ; qui écrit les besoins, qui valide la recette des données ; administrateurs, utilisateurs, lecture seule |
| 3. Processus cible | le parcours d'un contact jusqu'au client puis après la vente ; un pipeline par offre dont les étapes diffèrent ; pour chaque étape, l'action qui la fait franchir (annexe A) |
| 4. Exigences fonctionnelles | une exigence par cas d'usage retenu, par lot pour un grand projet (par exemple un lot « référentiel client unique », un lot « campagnes ») ; visibilité et droits ; activités ; raisons de perte ; attribution des leads ; rendez-vous ; messagerie ; téléphonie ; devis et facturation ; suivi après la vente |
| 5. Données | les objets portés (contacts, entreprises, affaires, et ceux du métier : commandes, points de vente, produits) ; la clé qui identifie un contact, source par source, et la règle de dédoublonnage ; les champs obligatoires et leur coût pour la collecte ; les calculs stockés (premier, dernier, nombre, total, écart de temps) ; les segmentations attendues ; la volumétrie ; le catalogue (annexe C) |
| 6. Intégrations | chaque outil qui écrit dans le CRM ou en lit (site, boutique, caisse, gestion, emailing, SMS, rendez-vous, téléphonie, facturation, gestion de projet) ; le sens et le déclencheur de chaque flux ; ce qui ne doit jamais créer de doublon |
| 7. Exigences non fonctionnelles | hébergement en ligne ou chez soi ; lieu de stockage et conformité (protection des données, normes de sécurité) ; authentification, connexion unique, déconnexion automatique ; disponibilité, support, correction des défauts ; formation (qui, sous quelle forme, formateurs internes) ; maintenance et engagement de l'éditeur à ne pas retirer une fonctionnalité indispensable |
| 8. Contraintes | budget des licences et budget de mise en place, séparés ; modèle d'abonnement (par utilisateur, par contact, par volume d'e-mails) ; date ; outils imposés ; reprise des données (complète, différentielle, au fil de l'eau) ; quotas d'API |
| 9. Critères d'acceptation | testables : un contact importé deux fois n'existe qu'une fois ; un rendez-vous pris en ligne s'attache à la bonne affaire ; un utilisateur en lecture seule ne modifie rien |
| 10. Indicateurs | adoption (utilisateurs actifs, affaires avec une activité prévue), nombre de contacts en base, taux de remplissage et de joignabilité, conversion par étape, durée du cycle ; chacun avec sa mesure de départ |
| 11. Hors périmètre | ce qui reste dans un autre outil (facturation, gestion de projet), ce qui attend un second lot |
| 12. Questions ouvertes | les questions de `crm-parametrage` sans réponse, en `Q-xx` |

Organisation du projet (équipe, comités, méthode, outils, calendrier, risques) : elle relève du plan, écrit par
`planifier-deploiement`. Une grille des tâches et des rôles (qui réalise, qui approuve, qui est consulté, qui est
informé) et trois instances (un point hebdomadaire des opérationnels, un comité de pilotage pour les arbitrages, un
comité de direction pour le budget et les risques) suffisent à la plupart des projets.

## 2. Constituer les besoins, cas d'usage par cas d'usage

1. **Cartographier les utilisateurs** : tous, qualifiés par équipe et par usage. Couvrir tous les cas d'usage, même
   rares. Pour l'échantillon, préférer les extrêmes : un ou deux utilisateurs très à l'aise, un ou deux nouveaux
   venus, et celui qui préfère ses outils à lui.
2. **Observer** : une séance par personne, notée sur cinq entrées (activités, environnement, interactions, objets,
   utilisateurs). Au-delà d'une dizaine de séances, une de plus n'apporte presque rien.
3. **Interroger**, cas d'usage par cas d'usage, avec les trois questions de la partie 8 de `crm-parametrage` : ce
   que la personne cherche à faire et pourquoi, comment elle le fait, ce qui pourrait être mieux fait. Pour un grand
   projet, ajouter par cas d'usage un questionnaire court, sur une échelle d'accord en cinq points : la tâche a-t-elle
   abouti, a-t-elle paru facile, a-t-elle pris plus ou moins de temps que prévu ?
4. **Regrouper** dans une grille cas d'usage × difficultés : compter combien de fois chaque difficulté revient, pour
   repérer les plus fréquentes et creuser les rares, sans transformer le qualitatif en score.
5. **Écrire les cas d'usage définitifs**, puis la grille des besoins fonctionnels, et découper par lots quand le
   projet est grand.

## 3. Annexes : gabarit de `30-exigences/annexes-crm.md`

### A. Pipelines et étapes

Un tableau par pipeline, une colonne par étape :

| | Étape 1 | Étape 2 | … | Signé |
|---|---|---|---|---|
| Ce qui fait franchir l'étape | | | | |
| Actions et activités créées | | | | |
| Délai avant alerte | `[H]` | | | |
| Probabilité de signature | `[H]` | | | 100 % |

Étapes types d'un cycle de vente entre entreprises : intégration du lead, premier rendez-vous, découverte faite,
proposition envoyée, propositions suivantes, négociation, décision, signé, puis début du premier projet. Les délais
et les probabilités sont des hypothèses à faire valider, jamais reprises d'un autre client.

### B. Droits et visibilité

| Utilisateur ou rôle | Équipe | Pipelines accessibles | Visibilité par défaut | Administrateur de | Lecture seule |
|---|---|---|---|---|---|

### C. Catalogue

Le fichier du client si le catalogue est long (option recommandée), sinon le tableau : catégorie, description,
unité, prix par devise, taxe, image, fichiers, code, visibilité, et les variantes par modalité de paiement
(paiement unique, abonnement mensuel, trimestriel ou annuel, paiement en plusieurs fois avec le montant de chaque
échéance). Les variantes se créent dans le CRM après l'import.

### D. Raisons de perte

Une liste fermée, à adapter : information manquante ou fausse, pas de produit adapté, non éligible, trop cher, absent
au rendez-vous, n'a pas compris l'offre, besoin différent découvert en rendez-vous, pas décideur, tarification,
concurrence, projet reporté, autre. Préciser si une raison libre est permise : elle enrichit, mais ne s'analyse pas.

### E. Automatisations souhaitées

| Déclencheur | Condition | Action | Objet | Qui est prévenu | Priorité |
|---|---|---|---|---|---|

### F. Messagerie et rendez-vous

Les boîtes et les domaines à connecter ; les modèles d'e-mails à reprendre ; la règle d'un rendez-vous pris en ligne
(créer ou rattacher la personne et l'affaire, ne jamais créer de doublon) ; les liens de rendez-vous dans les relances.

## Provenance

Reprise et dépersonnalisée, le 29/10/2026, d'une trame de cahier des charges CRM écrite pour un éditeur, de son
modèle de cadrage commenté, d'un fichier de réponses d'un projet client (cas anonymisé :
`cas-reseau-immobilier.md`) et d'un assistant conversationnel qui posait ces questions. Les exemples chiffrés
d'origine (délais, probabilités, budget) ne sont pas repris : ils étaient propres à un client.
