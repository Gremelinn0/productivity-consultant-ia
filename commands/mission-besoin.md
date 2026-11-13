---
description: Démarrer ou reprendre une mission IA à partir d'un besoin déjà nommé (porte « besoin connu » du pack consultant-ia).
argument-hint: "<le besoin, en une phrase>"
---

# Mission IA — porte « besoin connu »

Utilise la compétence `router-conseiller-une-mission-ia` :

1. Affiche d'abord l'état du dossier `mission/` du répertoire de travail.
2. Ouvre la porte « besoin connu » pour ce besoin : $ARGUMENTS
3. Si un dossier `mission/cas-<slug>/` existe déjà pour ce besoin, reprends à l'étape suivante ;
   sinon commence par `cadrer-besoin`, qui fixe le nom du dossier (deux à quatre mots) et que les
   autres étapes reprennent tel quel. Les étapes ici vont du cadrage (10) au plan (70), puis à la mesure du gain
   (95) ; chacune finit par une décision du client. Après 70, la mission passe au pack Créer un agent IA, qui
   construit, teste et met en service (80, 85, 90) dans le même dossier : la porte affiche ces étapes « au pack
   Créer un agent IA » et dit comment l'appeler.

Rien ne touche un outil réel sans la validation de l'action précise (règle 7 d'`ARCHITECTURE.md`) : toute
action sur un outil de l'entreprise est proposée dans 90-mise-en-service, au pack Créer un agent IA, avec son
retour arrière.
