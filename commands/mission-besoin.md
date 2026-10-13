---
description: Démarrer ou reprendre une mission IA à partir d'un besoin déjà nommé (porte « besoin connu » du pack consultant-ia).
argument-hint: "<le besoin, en une phrase>"
---

# Mission IA — porte « besoin connu »

Utilise la compétence `router-mission-ia` :

1. Affiche d'abord l'état du dossier `mission/` du répertoire de travail.
2. Ouvre la porte « besoin connu » pour ce besoin : $ARGUMENTS
3. Si un dossier `mission/cas-<slug>/` existe déjà pour ce besoin, reprends à l'étape suivante ;
   sinon commence par `cadrer-besoin`, qui fixe le nom du dossier (deux à quatre mots) et que les
   autres étapes reprennent tel quel. Les étapes vont du cadrage (10) à la mesure du gain (95) ; chacune
   finit par une décision du client.

Rien ne touche un outil réel sans la validation de l'action précise (règle 7 d'`ARCHITECTURE.md`) : on
construit et on teste dans un environnement d'essai, et toute action sur un outil de l'entreprise est
proposée dans 90-mise-en-service avec son retour arrière.
