---
description: Démarrer ou reprendre une mission IA sans besoin défini — brancher le pack sur le contexte de l'entreprise et faire ressortir les cas d'usage (porte « découverte » du pack consultant-ia).
argument-hint: "[entreprise, équipe ou périmètre]"
---

# Mission IA — porte « découverte »

Utilise la compétence `router-mission-ia` :

1. Affiche d'abord l'état du dossier `mission/` du répertoire de travail.
2. Ouvre la porte « découverte » pour : $ARGUMENTS
3. Commence par `decouvrir-cas-usage` : inventorie les sources disponibles (fichiers déposés dans
   `mission/sources/`, outils déjà connectés à la session, entretiens à mener) et demande
   l'autorisation de lire chacune avant de l'ouvrir.

Rien ne sort du dossier de mission : pas d'envoi, pas de publication, pas de modification des outils
de l'entreprise.
