# Cas anonymisé : un réseau immobilier, projet CRM planifié puis arrêté

Un projet réel, rendu anonyme : ni le nom du client, ni ceux de ses équipes, ni ses chiffres. Il sert d'exemple de
constitution des besoins d'un CRM sur plusieurs équipes, et de ce qui fait qu'un projet bien cadré s'arrête quand
même. Ce n'est pas une preuve de résultat : le projet n'a pas été mis en service.

## Le contexte

Un réseau de professionnels de l'immobilier, présent dans deux pays, qui vend à la fois à des entreprises (des
agences et des indépendants qui rejoignent le réseau) et à des particuliers (des vendeurs et des acheteurs de
biens). Le marketing tenait déjà sa propre chaîne d'outils (collecte des événements du site, plateforme d'e-mails
déclenchés par ces événements, publicité) ; les ventes et l'animation du réseau n'avaient pas de suivi commun ; une
application interne servait les partenaires.

## Comment les besoins ont été constitués

- **Trois ateliers, un par équipe** : marketing, ventes et animation du réseau, technique. Chacun a rempli le même
  fichier de réponses, organisé comme le cahier des charges : utilisateurs et équipes, outils et sources des leads,
  structure du CRM (droits, champs, intégrations, répartition des leads, correspondance des champs), pipelines,
  produits et étiquettes, tableaux de bord, puis marketing (cibles, données de comportement, notation des leads,
  e-mails).
- **Un prérequis posé d'entrée** : tous les accès administrateur donnés avant le lancement, sur une seule adresse
  d'invitation, faute de quoi le projet ne démarre pas.
- **Les pipelines ont été débattus avant d'être dessinés** : trois pipelines par public (entreprises, vendeurs,
  acheteurs) contre un seul pipeline de qualification puis de vente, avec la source et la cible en étiquettes. Le
  second l'a emporté pour analyser toutes les données au même endroit ; les ventes ont gardé les mêmes étapes pour
  tous les publics, un cycle plus court restant possible pour un seul d'entre eux.
- **Les leads entrent par une boîte de prospects**, avec une étiquette de pipeline et un indice de chaleur, la source
  dans le contact ; seuls les plus qualifiés vont directement dans un pipeline. Un lead de particulier va à l'agence
  la plus proche ; sans agence, un message demande à l'équipe à qui l'attribuer. Les leads d'entreprises se
  répartissent par secteur et par initiative.
- **La notation des leads marketing restait dans l'outil d'e-mails**, la notation commerciale dans le CRM : deux
  notations, deux propriétaires.
- **Les partenaires ne devaient pas tous payer une licence** : une application sans code, synchronisée avec le CRM,
  leur aurait donné accès à leurs seules données.
- **La suite après la vente** (accueil du partenaire, bilan, validation, lancement, résultats) a été décrite comme un
  modèle de projet, déclenché par l'affaire gagnée.

## Pourquoi il s'est arrêté

Le projet était planifié de bout en bout quand il s'est arrêté. Les sources ne disent pas la cause ; trois signaux
s'y lisent, qui valent pour d'autres projets :

1. **Deux chaînes d'outils pour un même contact** : marketing et ventes avaient chacun leur outil de référence, et
   la correspondance des champs entre eux restait à écrire. Un projet CRM qui ne tranche pas la source qui fait foi
   (question `CR03` de la base) en hérite le coût à chaque intégration.
2. **Trois publics dans un seul projet** : entreprises, vendeurs et acheteurs n'ont ni le même cycle ni les mêmes
   utilisateurs. Un premier lot limité à un public aurait donné un résultat plus tôt.
3. **Des accès partenaires sans modèle de licence tranché** : le surcoût par partenaire poussait vers une
   application à part, donc un second chantier.

## Ce que le cas a ajouté à la méthode

- Le fichier de réponses par atelier, organisé comme le cahier des charges : la trame (`trame-cahier-des-charges.md`).
- Le choix entre un pipeline par public et un pipeline unique étiqueté, et la règle « des étapes identiques se
  fusionnent » : la grille (`grille-audit.md`, volet 4).
- La boîte de prospects avant le pipeline, et l'attribution par zone ou par secteur : question `CR12`.
- Le prérequis des accès avant le lancement : étape 1 de la compétence.
