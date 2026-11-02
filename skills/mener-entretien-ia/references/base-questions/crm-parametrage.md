# Base de questions : le cahier des charges et le paramétrage d'un CRM

<!-- hors-ligne -->

Le détail qu'un cahier des charges CRM doit trancher avant tout paramétrage : les acteurs du projet, les droits, les objets et leurs identifiants, les pipelines, les produits, la messagerie, les exigences non fonctionnelles. Réservé aux questionnaires préparés avec le consultant (`auditer-crm`) : ces questions supposent une mission engagée, l'agent en ligne ne les pose pas. Le diagnostic d'un CRM en place part de `crm`. Un questionnaire préparé part d'ici et du cadrage (`cadrage`), garde les questions utiles, et n'adapte que ce qui change pour l'entreprise.

## 1. Le projet et ses acteurs

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| CP01 | Qui mène le projet CRM en interne, qui le sponsorise, et qui tranche en cas de désaccord ? | Le responsable du projet et l'instance qui arbitre | la personne |
| CP02 | Qui écrit les besoins de chaque équipe, et qui valide la recette des données ? | Les rôles du cahier des charges et de la recette | la personne |
| CP03 | Quels prestataires interviennent (éditeur, intégrateur, assistance à maîtrise d'ouvrage), et qui chez eux reçoit les documents ? | Le périmètre de chacun et les interlocuteurs | un document |

## 2. Les utilisateurs, les équipes et les droits

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| CP04 | Quelles équipes et quels sous-groupes faut-il créer, et à quels pipelines chacun doit-il accéder ? | Les groupes de visibilité et les accès par pipeline | la personne |
| CP05 | Un nouvel élément doit-il être visible par tous, ou seulement par son propriétaire et les administrateurs ? | La visibilité par défaut des contacts, entreprises et affaires | la personne |
| CP06 | Qui est administrateur, et qui doit rester en lecture seule ? | Les ensembles de droits par rôle | la personne |
| CP07 | Faut-il une connexion unique d'entreprise, une limite à un poste ou une déconnexion automatique ? | Les exigences de sécurité des accès | un document |

## 3. Les objets, les champs et les identifiants

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| CP08 | Quelle clé identifie un contact de façon unique, source par source (e-mail, téléphone, autre) ? | La règle de dédoublonnage et l'identifiant maître | l'outil |
| CP09 | Quels objets le CRM doit-il porter en plus des contacts, entreprises et affaires (commandes, points de vente, produits) ? | Le modèle de données cible | la personne |
| CP10 | Quels champs doivent être obligatoires, sans freiner la saisie ni les formulaires de collecte ? | Les champs obligatoires et leur coût pour la collecte | la personne |
| CP11 | Quels calculs (premier achat, dernier achat, nombre, total) doivent être stockés dans des champs ? | Les agrégats et les segmentations possibles | la personne |

## 4. Les pipelines et les activités

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| CP12 | Combien de pipelines faut-il, et leurs étapes diffèrent-elles vraiment ? | Le nombre de pipelines ; ceux aux étapes identiques se fusionnent | la personne |
| CP13 | Pour chaque étape, quelle action fait passer l'affaire à la suivante, et quelle probabilité de signature lui donner ? | La définition des étapes et la prévision | la personne |
| CP14 | Quels types d'activité faut-il garder, créer ou retirer, et chaque affaire doit-elle toujours avoir une activité prévue ? | Les réglages d'activités | la personne |
| CP15 | Les raisons de perte se choisissent-elles dans une liste fermée, ou peut-on en écrire une libre ? | Le format des raisons de perte, et ce qu'on pourra en analyser | la personne |

## 5. Les produits, les devis et les paiements

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| CP16 | Quels produits et services faut-il importer, avec quels prix, devises, taxes et modalités de paiement ? | Le catalogue et ses variantes | un document |
| CP17 | Les devis, les factures et les paiements doivent-ils se faire dans le CRM, ou rester dans leur outil actuel et s'y synchroniser ? | L'outil de devis et de facturation, et l'intégration | la personne |

## 6. La messagerie, les rendez-vous et la téléphonie

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| CP18 | Quelles boîtes mail et quels domaines faut-il connecter et synchroniser avec le CRM ? | Les connexions de messagerie | l'outil |
| CP19 | Un rendez-vous pris en ligne doit-il créer ou mettre à jour le contact et l'affaire, sans jamais créer de doublon ? | L'intégration de l'outil de rendez-vous | la personne |
| CP20 | Les appels doivent-ils partir du CRM et s'y enregistrer ? | L'intégration de la téléphonie | la personne |

## 7. Les exigences non fonctionnelles

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| CP21 | Où les données doivent-elles être hébergées, et quelles règles (protection des données, normes de sécurité) le CRM doit-il respecter ? | Les exigences d'hébergement et de conformité | un document |
| CP22 | Comment les données existantes seront-elles reprises : import complet, différentiel ou au fil de l'eau ? | La méthode de reprise des données | la personne |
| CP23 | Quels délais de disponibilité, de support et de correction attendez-vous de l'éditeur et de l'intégrateur ? | Le niveau de service à contractualiser | la personne |
| CP24 | Qui faut-il former, sous quelle forme, et faut-il des formateurs internes ? | Le plan de formation | la personne |
| CP25 | Quel budget est prévu pour les licences, et lequel pour la mise en place et les intégrations ? | Le modèle d'abonnement et l'enveloppe de mise en place | la personne |

## 8. Les besoins, cas d'usage par cas d'usage

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| CP26 | Que cherchez-vous à faire dans le CRM pour ce cas d'usage, et pourquoi ? | Le besoin réel derrière la demande | la personne |
| CP27 | Comment le faites-vous aujourd'hui, et avec quel outil ? | L'existant à reprendre ou à remplacer | la personne |
| CP28 | Qu'est-ce qui pourrait être mieux fait, selon vous ? | Les difficultés à compter dans la grille des cas d'usage | la personne |
