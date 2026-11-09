# Actions types, retour arrière et effets externes

À ouvrir pour dresser le registre des actions (étape 2 de `SKILL.md`) et pour écrire la fiche de chacune. Les lignes du catalogue sont des
points de départ à vérifier sur l'outil réel, jamais des garanties : la capacité d'un outil à défaire une action se lit dans sa documentation,
se date, et surtout s'essaie. Aucune durée n'est donnée ici : elle se mesure à l'essai.

## 1. Ce que « retour arrière prêt » veut dire

Quatre conditions, toutes vérifiables :

1. **Écrit pas à pas**, de façon qu'un tiers puisse le faire sans l'auteur (fiche d'action, `modeles.md` partie B).
2. **Essayé** sur copie ou en environnement d'essai, avec le temps mesuré `[F]` et la vérification que l'état d'avant est revenu.
3. **Ses prérequis sont en place** : sauvegarde datée et restaurable (une sauvegarde jamais restaurée n'en est pas une), ancienne version
   conservée, accès de la personne qui défait.
4. **Son signal et son rôle sont écrits** (70 §3, 60 §14), pour qu'il ne dépende pas d'une discussion le jour de l'incident. La validation d'une
   action vaut validation de son retour arrière, déclenché par ce signal et par ce rôle.

Un retour arrière a des limites, qu'on écrit : ce qu'il ne défait pas (messages partis, données déjà lues par un tiers, écritures chez un tiers).
Une fois exécuté, il se note sur la ligne de l'action (état « revenue en arrière », avec les deux dates : faite, puis défaite) et au journal.

## 2. Le catalogue

| Action type | Réversible ? | Retour arrière usuel | Piège |
|---|---|---|---|
| Créer un compte de service, accorder des droits | oui | retirer le droit, désactiver ou supprimer le compte | droits trop larges « pour aller plus vite » ; compte personnel |
| Poser un secret dans le coffre de l'outil | oui | révoquer le secret et en poser un neuf | la valeur transite par un message, un document ou le dossier de mission : le pack ne la voit jamais |
| Sauvegarder avant modification | sans objet (lecture) | — | sauvegarde jamais restaurée en essai ; sauvegarde non datée |
| Importer la version construite, inactive | oui | supprimer la version importée, ou réimporter la précédente | l'import active le flux sans que personne l'ait demandé |
| Activer un déclencheur ou une exécution planifiée | oui s'il n'y a pas d'effet externe | désactiver (interrupteur) | l'activation lance aussitôt une exécution sur le stock accumulé |
| Charger des règles ou une table de paramètres | oui avec une copie datée | restaurer la copie | règle modifiée sans date ni propriétaire |
| Migrer des données existantes | en partie | restaurer la sauvegarde ; ancien support passé en lecture seule | source écrasée ; migration sans contrôle d'un échantillon |
| Écrire dans un logiciel de l'entreprise (créer, modifier des enregistrements) | souvent non | correction par lot, grâce à la clé de dédoublonnage et au journal des écritures | écriture sans clé stable ; aucune liste de ce qui a été écrit |
| Envoyer vers l'extérieur (message, document, notification) | non | message rectificatif ; aucun retour pour l'envoi lui-même | envoi en masse, doublon, mauvais destinataire |
| Publier (page, annonce, contenu public) | en partie | dépublier ; la copie extérieure reste | contenu déjà copié ou indexé |
| Payer, émettre un document comptable | non | contre-passation ou avoir, par le rôle compétent | action hors du périmètre validé |
| Envoyer des données à un service tiers ou à un modèle d'IA | non | arrêter l'envoi ; demander l'effacement selon les conditions du tiers | région d'hébergement et conservation chez le tiers non lues |
| Supprimer ou archiver des données | suppression non, archivage oui | restaurer l'archive | suppression avant la fin de la durée de conservation |
| Activer les alertes et leurs destinataires | oui | désactiver, changer de destinataire | alerte envoyée à un absent, sans suppléant |
| Désactiver l'ancienne méthode | oui si le repli est conservé | réactiver | retirer l'ancienne voie le jour de la bascule |
| Annoncer ou former (message à une équipe) | l'envoi non | message rectificatif | annonce faite avant la décision |
| Retirer le dispositif (arrêt) | selon l'action | — | oublier les accès à révoquer, l'abonnement, les données, le journal à conserver |

## 3. Effets externes

- **Définition.** Tout ce qui quitte l'entreprise ou touche une personne qui n'en fait pas partie : message, document, notification, publication,
  écriture chez un tiers, paiement, envoi de données à un service extérieur ou à un modèle d'IA.
- **Ce que la validation nomme.** Le public touché, le plafond (nombre au plus, période), le rôle qui répond de la relation, et ce qui part (le modèle de
  message, lu par le valideur). Sans plafond, l'effet n'est pas validé.
- **Avant le premier effet réel.** Une simulation (le dispositif calcule ce qu'il ferait, rien ne part) lue par le valideur, puis un premier lot réduit qu'il
  choisit. La suite attend la lecture de ce lot : erreurs, réactions, plaintes. Chaque lot suivant et chaque relèvement de plafond est une action nouvelle.
- **Qui le fait.** Un rôle du client. Le pack prépare le texte, le lot et la fiche.
- **Pendant un pilote en parallèle.** L'étape qui enverrait est désactivée ou seulement observée : le dire étape par étape (60 §4).
- **Le message rectificatif** se prépare avant d'en avoir besoin : qui l'envoie, à qui, avec quel texte.

## 4. Secrets, comptes, données

- **Secrets.** Le document dit le nom, l'endroit (le coffre de l'outil), le propriétaire et l'échéance de rotation ; il ne contient jamais la valeur, même
  masquée. Le pack ne lit ni n'écrit aucun secret : le propriétaire le pose et confirme sa présence (le nom apparaît dans le coffre), il n'envoie pas la valeur.
- **Comptes.** Comptes de service nommés, droits minimaux, propriétaire désigné ; jamais un compte personnel. Pas d'accès permanent pour le constructeur : un
  accès ouvert pour la durée d'une action est lui-même une action, avec sa fermeture.
- **Données.** Pendant le pilote, les données réelles restent dans les outils du client. Le pack reçoit des compteurs, des durées et des constats ; tout export
  déposé dans `mission/sources/` est agrégé ou anonymisé avant le dépôt.

## 5. Après le feu vert : les changements

- **Ce qui compte comme changement.** Version du flux ou du code ; règle ou paramètre ; consigne ou modèle d'IA ; droit ou compte ; périmètre (équipe, volume,
  public) ; destinataire d'une alerte ; palier ou tarif de la plateforme.
- **Conduite.** Une `A-xx` nouvelle, validée avant ; tests concernés rejoués (`tester-solution`, et le jeu d'évaluation pour un composant d'IA) ; numéro de version
  noté au registre.
- **Changement subi.** L'éditeur modifie l'outil, le fournisseur remplace un modèle : ce n'est pas une faute du client. On l'écrit au registre à la date où on le
  constate, avec la décision (rejouer les tests, accepter, revenir), et on le signale à `mesurer-gains`.
- **Changement fait hors registre.** Il ne se régularise pas après coup : le journal l'écrit comme un incident daté (qui, quoi, quand, effet constaté), le registre
  propose la suite en `A-xx` nouvelles (garder, défaire, corriger), validées avant d'être faites, et la période concernée est marquée « version non validée » pour la mesure.
- **Défaut bloquant ouvert en exploitation.** Suspendre, retirer, prévenir : chaque mesure de confinement est une `A-xx` marquée « mesure d'attente » (elle ne modifie
  ni la solution ni ses règles), proposée et validée comme les autres. La correction repasse par `construire-solution` puis `tester-solution` ; la levée des mesures est une
  `A-xx` de plus.
