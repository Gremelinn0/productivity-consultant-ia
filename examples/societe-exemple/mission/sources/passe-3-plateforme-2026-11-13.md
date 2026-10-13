> **Source fictive.** Compte rendu simulé pour l'exemple du pack consultant-ia : la passe 3 de la recette sur une plateforme inventée. Aucune personne, aucun chiffre et aucune entreprise réels.

# Passe 3 de la recette sur la plateforme P · 2026-11-13

Réserve 1 de `85-recette.md` (version 1.0) : les 43 tests rejoués sur l'espace d'essai de la plateforme, un résultat écrit par test, la durée de la liste mesurée, la liste des droits accordés rendue. Exécutée par l'indépendant, la gestionnaire clients et le responsable financier présents ; lue et signée par les deux le jour même.

## 1. Ce qui a été testé

- Version : `flux_relances` 1.1 assemblée dans l'espace « essai-relances » selon `fiche-de-montage.md` (révision 2), à partir de l'export de la version 1.1 ; règles R1 et trois modèles identiques à ceux de la maquette (empreintes lues au classeur d'approbation de l'espace d'essai).
- Données : le rejeu des 61 factures fictives de `donnees-essai/` chargé dans un classeur et une boîte de messagerie de test ; aucune donnée réelle.
- Tests d'arrêt net (T-15b, T-29, T-31, T-40) : l'exécution est interrompue à la main depuis la console de la plateforme, entre deux modules, à l'endroit que le test décrit ; l'indépendant a noté l'heure de l'arrêt et du module.
- Opérations consommées par la passe : 120, ajoutées au quota du compte (la page de l'éditeur compte les opérations de tous les espaces).

## 2. Résultat par test

| Test | Résultat | Note |
|---|---|---|
| T-01 | réussi | 61 factures traitées, niveaux conformes au fichier d'attendus |
| T-02 | réussi | |
| T-03 | réussi | |
| T-04 | réussi | |
| T-05 | réussi | |
| T-06 | réussi | brouillon retiré 7 min après la saisie du litige |
| T-07 | réussi | alerte « envoi hors validation » reçue 8 min après l'envoi par un autre compte |
| T-08 | réussi | 0 écart sur les 42 brouillons |
| T-09 | réussi | |
| T-10 | réussi | refus d'envoi constaté, tentative au journal de la boîte de test |
| T-11 | réussi | |
| T-12 | réussi | |
| T-13 | réussi | |
| T-13b | réussi | jours fériés lus dans l'onglet « règles » |
| T-14 | réussi | |
| T-15 | réussi | reprises à 1 min et 5 min observées |
| T-15b | réussi | arrêt après 10 propositions, relance : 42 clés distinctes |
| T-16 | réussi | alerte reçue 2 min après l'échec |
| T-17 | réussi | 150 factures, 90 propositions : liste prête en 4 min 03 s (marge de 57 s sur les 5 min) ; 101 propositions : arrêt avant création, alerte « volume anormal » |
| T-18 | réussi | |
| T-19 | réussi | |
| T-20 | réussi | |
| T-21 | réussi | |
| T-22 | réussi | |
| T-23 | réussi | |
| T-24 | réussi | |
| T-25 | réussi | |
| T-26 | réussi | |
| T-27 | réussi | |
| T-28 | réussi | |
| T-29 | réussi | arrêt juste après la création d'un brouillon, avant l'écriture de sa clé |
| T-30 | réussi | |
| T-31 | réussi | deux points d'arrêt essayés |
| T-32 | réussi | |
| T-33 | réussi | balayage de l'export : rien à relire ; clé fictive glissée dans une copie : trouvée |
| T-34 | réussi | retour de la 1.1 vers la 1.0 par réimport : 22 min |
| T-35 | réussi | écriture refusée hors des onglets du dispositif |
| T-36 | réussi | |
| T-37 | réussi | |
| T-38 | réussi | |
| T-39 | réussi | |
| T-40 | réussi | refus à 1 min et à 29 min, acceptation à 31 min |
| T-41 | réussi | |

Compte : 43 tests joués, 43 réussis.

## 3. Mesures demandées par la réserve 1

| Mesure | Valeur |
|---|---|
| Durée de la liste du lundi sur le rejeu des 61 factures (ENF-05, moins de 5 min `[H]`) | 42 brouillons créés en 1 min 52 s |
| Pointe (T-17) | 90 propositions en 4 min 03 s |
| Retour arrière de la version (T-34) | 22 min pour revenir de la 1.1 à la 1.0 |
| Droits accordés au compte de service « flux-relances » (liste rendue par l'indépendant) | dépôt et classeur de pilotage : lecture ; classeur du dispositif : lecture et écriture limitée à ses onglets ; boîte partagée : création et suppression de ses brouillons dans deux dossiers, lecture de « Envoyés », aucun droit d'envoi |

## 4. Signature

Lu et accepté le 2026-11-13 par la gestionnaire clients et par le responsable financier : « les 43 tests rendus et réussis, la durée de la liste sous les 5 minutes ».
