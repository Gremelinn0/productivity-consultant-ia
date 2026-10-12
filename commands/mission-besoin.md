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
   autres étapes reprennent tel quel.

Rien ne sort du dossier de mission : pas d'envoi, pas de publication, pas de modification des outils
de l'entreprise.
