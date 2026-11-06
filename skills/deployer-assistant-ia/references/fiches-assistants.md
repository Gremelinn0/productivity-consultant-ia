# Les fiches assistants : où lire, quoi relever

Cette page sert à deux moments : comparer les options (étape 4) et préparer la formation (étape 9). Ses valeurs sont un
repère daté, jamais une source du livrable : plans, prix et options changent en quelques mois. Le livrable ne reprend
que ce qui a été relu sur la page officielle, le jour de la mission, avec le lien et la date.

Relevé du 06/11/2026. **[lu]** : page officielle ouverte et lue ce jour-là. **[relevé]** : repéré sur la page citée sans
seconde lecture, à vérifier en priorité. Ces deux mots valent pour cette page : dans le livrable, un fait relu le jour même
est `[F]`, un repère non relu reste `[H]`. Une fiche trouvée fausse se corrige ici, avec sa nouvelle date.

## Partie 1. Comparer

### La grille à relever pour chaque candidat

Une ligne par fait, avec sa page officielle et sa date de lecture. Une page inaccessible s'écrit « non vérifié ».

| Ce qu'on relève | La question qu'il tranche |
|---|---|
| Plan, prix par siège, engagement, minimum et maximum de sièges | Le plan tient-il le nombre de personnes et le budget ? |
| Ce que le plan ouvre : connexion unique, création automatique des comptes, journaux d'audit, durée de conservation réglable | Tient-il les contraintes écrites à l'étape 3 ? |
| Entraînement sur les données : par défaut, exceptions, qui peut le couper | Que dire aux salariés et au rôle compétent ? |
| Lieu de stockage et de traitement, options régionales et leurs conditions | Tient-il une clause de lieu ? |
| Conservation, suppression, fichiers et mémoire compris | Que répondre sur la durée ? |
| Accord de sous-traitance (DPA), liste des sous-traitants, certifications | Quelles pièces joindre au dossier ? |
| Statistiques : ce que voit l'administrateur, par personne ou par équipe, ce qui se masque | Que décider et annoncer à l'équipe ? |
| Connecteurs et extension du navigateur : qui les ouvre, listes autorisées, ce qui reste hors des journaux | Quels réglages proposer ? |
| Mémoire et instructions : à quels niveaux, activées comment | Que cadrer dans la charte et la formation ? |

Un assistant absent des fiches se relève avec la même grille : la méthode vaut pour tout éditeur.

### Claude (Anthropic)

| Fait | Valeur au 06/11/2026 | Page | Statut |
|---|---|---|---|
| Team | 2 à 150 sièges ; Standard 20 USD par siège et par mois à l'année, 25 au mois ; Premium 100 ou 125 | https://claude.com/pricing | [relevé] |
| Enterprise | 20 USD par siège et par mois à l'année plus l'usage au tarif API ; minimum 20 sièges en libre-service, 50 en commercial | https://support.claude.com/en/articles/9797531 | [relevé] |
| Ce qu'ajoute Enterprise | SCIM, journaux d'audit, conservation réglable, accès par rôles | https://claude.com/pricing | [lu] |
| Entraînement, offres commerciales | Non par défaut ; exceptions : le pouce levé ou baissé envoie la conversation, gardée jusqu'à 5 ans, sauf si un Owner coupe ce réglage | https://privacy.claude.com/en/articles/7996868 | [lu] |
| Lieu | Stockage aux États-Unis ; routage États-Unis, Europe, Asie, Australie ; choix de routage réservé à Enterprise à l'usage | https://privacy.claude.com/en/articles/7996890 | [lu] |
| Conservation | Suppression côté serveur sous 30 jours ; réglable sur Enterprise ; les projets ont leurs règles | https://privacy.claude.com/en/articles/7996866 | [relevé] |
| Accord de sous-traitance | Intégré aux conditions commerciales | https://www.anthropic.com/legal/data-processing-addendum | [relevé] |
| Statistiques | Les Owners voient l'usage par personne, classement et export compris. Le réglage « Member analytics » ne vise que la vue d'un membre sur son propre usage, sur Enterprise à l'usage. Aucun réglage trouvé pour couper la vue de l'administrateur par personne | https://support.claude.com/en/articles/12883420 | [lu] |
| Extension Chrome | Activée par défaut sur Team ; listes de sites autorisés et bloqués, valables aussi pour le navigateur de Cowork ; non prise en charge en conservation zéro | https://support.claude.com/en/articles/13065128 | [lu] |
| Cowork | S'exécute dans le cloud par défaut, sur les serveurs d'Anthropic ; le local reste pour les déploiements déjà en place | https://support.claude.com/en/articles/14479288 | [lu] |
| Mémoire | Activée pour les organisations créées depuis le 31/10/2026, désactivée pour les plus anciennes ; supprimer une conversation n'efface pas forcément la mémoire | https://support.claude.com/en/articles/11817273 | [relevé] |

### ChatGPT (OpenAI)

| Fait | Valeur au 06/11/2026 | Page | Statut |
|---|---|---|---|
| Business | 2 à 200 sièges ; Standard 20 USD à l'année, 25 au mois ; Premium 100 ou 125 | https://openai.com/fr-FR/business/pricing | [relevé] |
| Enterprise | Sur devis ; création automatique des comptes et API de conformité | https://help.openai.com/en/articles/10011769 | [relevé] |
| Entraînement | Non par défaut sur Business et Enterprise ; activé par défaut sur les comptes individuels | https://help.openai.com/en/articles/7730893 | [relevé] |
| Lieu | Business : stockage régional en cours de déploiement, sans traitement régional. Enterprise : Europe et Suisse, traitement sous conditions | https://help.openai.com/en/articles/20001418 | [relevé] |
| Conservation | 30 jours après suppression ; les fichiers suivent leurs propres règles | https://help.openai.com/en/articles/8983778 | [relevé] |
| Accord de sous-traitance | Page dédiée, liste des sous-traitants à part | https://openai.com/policies/data-processing-addendum | [relevé] |
| Statistiques | Des métriques d'usage ; masquage des noms non trouvé | https://help.openai.com/en/articles/8798634 | [relevé] |

### Copilot (Microsoft)

| Fait | Valeur au 06/11/2026 | Page | Statut |
|---|---|---|---|
| Copilot Chat | Inclus avec un abonnement Microsoft 365 éligible, liste à relire pour le plan du client : l'option « ne rien ajouter » à regarder d'abord | https://www.microsoft.com/fr-fr/copilot/features/chat | [relevé] |
| Copilot pour les PME | Offre à 15,60 € HT par utilisateur et par mois en paiement annuel, 18,20 € hors offre, limité à 300 utilisateurs ; lire la durée de l'offre | https://www.microsoft.com/fr-fr/copilot/pricing/business | [lu] pour le prix |
| Entraînement | Les demandes, réponses et données lues par Microsoft Graph n'entraînent pas les modèles de fondation | https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy | [lu] |
| Lieu | EU Data Boundary, avec un routage hors UE à vérifier sur chaque abonnement récent ; le sous-traitant Anthropic est à vérifier en UE | https://learn.microsoft.com/en-us/copilot/microsoft-365/ | [relevé], page citée au relevé introuvable : la rechercher |
| Statistiques | Rapports d'administration : noms masqués selon un réglage de l'organisation, qu'un administrateur global peut changer | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports | [lu] |
| Audit, conservation | Par Microsoft Purview | https://learn.microsoft.com/en-us/purview/audit-copilot | [relevé] |

## Partie 2. Former

### Où poser quoi : trois questions, dans l'ordre

Elles valent pour tout assistant ; les noms changent, pas la logique.

1. **Faut-il un fichier en sortie, ou un travail sur plusieurs fichiers ?** Non : la conversation suffit. C'est le cas le
   plus fréquent, et le moins coûteux.
2. **La tâche touche-t-elle du code, un dépôt, un terminal ?** Oui : l'outil de code, avec une personne qui sait relire
   le résultat.
3. **Se répète-t-elle ?** Oui : un projet avec ses instructions, ou une tâche planifiée que l'exploitant inscrit à la
   revue de chaque trimestre. Non : une conversation ou une tâche ponctuelle dans l'espace de travail.

Sur Claude, cela donne Chat, Code et Cowork. Une tâche dans Cowork consomme plus qu'une conversation : on ne s'en sert
pas quand une conversation suffit.

### Les trois niveaux d'instructions

Une consigne se pose au niveau le plus large où elle reste vraie.

| Niveau | Ce qu'on y met | Qui l'écrit | Où |
|---|---|---|---|
| L'organisation | Le ton, ce qu'on ne fait jamais, les règles de la charte | L'exploitant, relu par le décideur | Réglages de l'organisation, là où le plan l'ouvre |
| Le projet ou l'équipe | Le contexte d'un métier, ses modèles, ses documents | Le référent de l'équipe | Le projet partagé |
| La personne | Ses préférences : format, longueur, langue | Chacun | Ses préférences personnelles |

Une règle de confidentialité ne dépend jamais des préférences d'une personne. Les instructions se relisent à la revue du
trimestre ; un projet sans responsable nommé se ferme.
