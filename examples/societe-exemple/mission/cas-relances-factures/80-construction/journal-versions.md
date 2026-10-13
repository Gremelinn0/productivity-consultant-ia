# Journal des versions — maquette exécutable du flux de relances

Une ligne par version, jamais modifiée après coup ; une correction après le gel est une nouvelle ligne. Les dates sont celles du calendrier de la mission (fictif). Les commandes citées dans « Contrôles passés » ont été réellement exécutées le 2026-10-13 sur la machine de l'auteur du pack : la date réelle d'une exécution est toujours écrite à côté de sa sortie dans `sorties-simulees/`.

Les tranches 0 à 5 se sont construites dans l'ordre, sur une copie de travail ; aucune version intermédiaire n'a été exportée ni gelée. Seules les versions de ce tableau existent comme livraison.

| Version | Date | Changement | Raison (tranche · écart · défaut `D-xx`) | Export · empreinte | Contrôles passés | Gelée pour la recette |
|---|---|---|---|---|---|---|
| 1.0 | 2026-11-10 | maquette des six tranches : étapes 1 à 6, 8 et 9 de `60-specification.md` v1.3 ; règles R1 et modèles des trois niveaux ; garde-fous du socle | tranches 0 à 5 ; écarts de la rubrique 8 de `80-construction.md` | `livraison/archives/flux-relances-v1.0.zip` · SHA-256 `dbaa825a79ee8413b0e645c509e96db03ebb75ac20c45ef51967c935fb01ada8` ; manifeste `livraison/MANIFESTE.sha256` · SHA-256 `782e7da35dcab25163266e12edb6c862b77b59578bb9fa5a4002945a5165dec5` | `controles_tranches.py` : 28 sur 28 (sortie : `sorties-simulees/controles-tranches-v1.0.txt`) ; balayage : rien à relire (`balayage-v1.0.txt`) ; retour arrière essayé : 0,48 s (`retour-arriere-v1.0.txt`) ; mesure de consommation (`mesure-operations-v1.0.txt`) | oui |
| 1.1 | 2026-11-12 | quatre corrections de la logique, trouvées par la passe 1 de la recette : une facture dont le brouillon a été supprimé à la main revient (D-03) ; une erreur définitive de l'étape 5 alerte la gestionnaire clients, et le responsable financier pour un compte clé (D-04) ; les écritures dans S2 et la suppression d'un brouillon reprennent quand S2 ou S3 est coupé en cours d'exécution (D-05) ; un brouillon déjà parti ou déjà supprimé n'est plus annoncé « retiré » à la gestionnaire clients (D-06) | `85-recette.md` rubrique 7 · tests T-26, T-27, T-28 et T-39, échoués en passe 1 | `livraison/archives/flux-relances-v1.1.zip` · SHA-256 `8408d8b7321f3c12bc1f9222e30637aa9898b3844bc8d21586ed8f6a6b2d1c9c` ; manifeste `livraison/MANIFESTE.sha256` · SHA-256 `829258c36d5ad24fffd7402c1e78cb29bf9bf49aea1cea7ed717ef22ad111181` | `controles_tranches.py` : 28 sur 28 (`sorties-simulees/controles-tranches-v1.1.txt`) ; balayage : rien à relire (`balayage-v1.1.txt`) ; retour arrière de 1.1 vers 1.0 essayé : 0,49 s (`retour-arriere-v1.1-vers-v1.0.txt`) ; consommation inchangée : 342, 267 et 236 opérations par semaine (`mesure-operations-v1.1.txt`) ; recette, passe 2 : 43 tests sur 43 (`85-recette/passe-2-v1.1.txt`) | oui |

## Différence relue avant le gel (1.0)

Première version : il n'y a pas de version précédente à comparer. Les règles R1 (`livraison/regles-v1.0.csv`, 7, 21 et 35 jours, 60 jours, plafond de 100) et les trois modèles de courriel sont ceux que `donnees-essai/jeux.py` copie dans l'espace d'essai, avec leur approbation (version R1, empreintes des règles et des modèles : `espace-modele/pilotage/approbation.csv`). Sur la plateforme, c'est le responsable financier qui relira ces textes et notera l'approbation de la version (action de `90-mise-en-service.md`). Le flux refuse de s'exécuter quand règles et modèles ne sont plus ceux de cette approbation (`60-specification.md` v1.3, T-22).

## Différence relue avant le gel (1.1)

Seul `flux_relances.py` change : 58 lignes ajoutées et 19 retirées sur 1 015 (`diff` de l'archive 1.0 contre le fichier courant, relu avant le gel). `essai_s2_s3.py`, `regles-v1.0.csv` (version de règles R1) et les trois modèles sont identiques octet pour octet, donc l'approbation du responsable financier reste valable. Les cinq endroits touchés :

- `_creer_brouillon` : une proposition « brouillon créé » dont le brouillon n'est plus dans la boîte est constatée ; si le courriel est dans « Envoyés », elle reste « déjà faite » (l'étape 8 le consignera), sinon la facture est traitée comme non relancée et un nouveau brouillon est créé. Une lecture de « Envoyés » de plus, seulement dans ce cas (D-03).
- `_etape5` : une erreur définitive sur une proposition envoie l'alerte « erreur définitive » (D-04).
- `_ecrire_proposition`, `_retirer_brouillons`, `_supprimer_brouillon_de`, `_consigner_envois`, `rejouer` : les écritures dans S2 et les suppressions de brouillons passent par les reprises de 60 §7 (D-05).
- `_supprimer_brouillon_de` et `_retirer_brouillons` : le brouillon absent n'est plus compté ni annoncé comme « retiré » ; le journal écrit « déjà absent » (D-06).
- `VERSION` passe à « 1.1 ».

Aucun comportement validé de 60 ne change. Les pièces de `sorties-simulees/rejeu-2026-09-07/` restent celles de la version 1.0 : le rejeu de la séance donne les mêmes brouillons, seule la colonne `version_flux` du journal diffère.

## Après le gel : les programmes de la recette

2026-10-13 (date réelle de l'exécution, hors calendrier de la mission) · témoin du balayage réécrit pour ne ressembler à aucune vraie clé ; passe 2 et sabotages rejoués.
Aucune version du flux ne change : `livraison/` et son manifeste sont identiques (flux 1.1 `83f1698c…`, manifeste `829258c3…`). Seuls changent les programmes de la recette : le texte de la fausse clé qui sert de témoin positif à T-33 et à S-13 n'est plus écrit dans aucun fichier, il se compose à l'exécution, et `donnees-essai/balayer.py` n'affiche plus une valeur en entier (début de valeur seulement). Nouvelles empreintes : `85-recette/test_recette.py` `3862d438…`, `85-recette/sabotage.py` `fda4eb05…` (anciennes : `b139eec2…` et `c2399111…`) ; remettre les anciennes lignes du témoin redonne les anciennes empreintes. Sorties régénérées : `85-recette/passe-2-v1.1.txt` (15 h 41), `85-recette/sabotages-v1.1.txt`, `85-recette/balayage-v1.1.txt` (15 h 56) ; bilans inchangés (43 sur 43, 17 sabotages sur 17, rien à relire). La passe 1 (`85-recette/passe-1-v1.0.txt`, version 1.0) ne contient aucun texte de clé : elle reste telle quelle et garde l'ancienne empreinte de `test_recette.py`, puisqu'elle date d'avant la réécriture.

Les deux versions ci-dessus sont gelées « pour la recette de la maquette » : la plateforme n'a pas été touchée par ces contrôles, et `85-recette.md` prévoit la recette sur la plateforme (passes 3 à 5).
