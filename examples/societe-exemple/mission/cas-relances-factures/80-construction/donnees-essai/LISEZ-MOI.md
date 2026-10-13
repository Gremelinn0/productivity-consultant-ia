# Données d'essai — environnement `essai-relances`

Tout ce dossier est fictif. Aucune personne, aucune facture, aucun client et aucune adresse ne sont réels : les contacts s'appellent « Contact C026 », les clients « C026 », les factures « FA-2026-1200 », et toute adresse de courriel finit par `.invalid`, domaine réservé qui ne reçoit jamais rien. Le jeu reproduit la **structure et les proportions** de la séance du lundi 2026-09-07 (`mission/sources/seance-finance-2026-09-07.md`), pas ses lignes.

## Ce que contient le jeu (`espace-modele/`)

| Dossier | Contenu | Rôle dans l'essai |
|---|---|---|
| `depot/` | `extraction-2026-09-07.csv` (61 factures), `rapprochement.csv` (une ligne : vendredi 2026-09-04) | dépôt de la gestionnaire clients et de la comptable |
| `pilotage/` | litiges (6 de la séance, 4 anciens), mises à jour de la liste, comptes clés (25), règles R1, modèles de courriel, approbation | classeur de pilotage, en lecture seule pour le flux |
| `dispositif/` | historique (relances déjà consignées), case « Suspendre » | classeur du dispositif, seul lieu où le flux écrit |
| `attendu/` | `rejeu-2026-09-07.csv` : pour chacune des 61 factures, sa catégorie, son niveau, son issue (proposée, mise à part, payée, déjà relancée, litige) et son dossier | attendu de la recette, **indépendant du flux** |

Décompte de la séance reproduit `[F]` : 61 factures ; 24 relances envoyées (14 de niveau 1, 7 de niveau 2, 3 de niveau 3) ; 9 payées ; 4 déjà relancées ; 6 en litige ; 5 comptes clés ; 7 en attente d'une réponse du commercial ; 6 sous 15 €. Première phase, le flux en propose 42 : 61 − 9 − 4 − 6, comptes clés compris `[E]` (`60-specification.md` §7).

## Comment il a été produit

`jeux.py` fabrique tout, avec un générateur congruentiel linéaire à graine fixe (20260907) : mêmes valeurs sur toutes les versions de Python. Il **n'importe jamais le flux** : l'attendu vient du décompte de la séance, pas de la sortie du programme. Chaque ligne de l'attendu est écrite au moment où la facture est fabriquée, avec la catégorie qu'on lui a donnée. Les « bruits » sont ajoutés pour que le jeu ne soit pas trop propre : 30 anciennes relances et 4 anciens litiges sur des factures absentes de l'extraction.

Régénérer : `python -X utf8 jeux.py` (réécrit `espace-modele/`). Vérifier que le jeu rangé est celui que produit `jeux.py` : `python -X utf8 empreintes_jeu.py --verifier`.

Empreintes (2026-10-13) :
- `jeux.py` : SHA-256 `cffc39fb4d09ee7fea2303153fd0c8f981c8115ecedb99aa0e2d2dd550eec9ff`
- `espace-modele/` (13 fichiers, arbre) : SHA-256 `22544607f1f11dec05263e98f3234a7ab0beb3613f381ad9d227569ba1c909b4`

## Comment lancer ce qui est ici

Toutes les commandes se lancent depuis ce dossier, avec Python 3.14.6 et sa seule bibliothèque standard.

| Commande | Ce qu'elle fait |
|---|---|
| `python -X utf8 controles_tranches.py` | les contrôles du constructeur, tranche par tranche (28 contrôles) ; code de sortie 0 si tous passent |
| `python -X utf8 mesure_operations.py [--pas 30]` | la consommation d'une semaine type, en opérations, avec la cadence de 10 min de la spécification ou une autre |
| `python -X utf8 produire_sorties.py` | rejoue la séance en mode simulation et range ce que la maquette a écrit dans `../sorties-simulees/rejeu-2026-09-07/` |
| `python -X utf8 balayer.py` | balaie le dossier `80-construction/` : secrets et données personnelles |
| `python -X utf8 geler_version.py` | écrit le manifeste et l'archive de la version courante de `../livraison/` |
| `python -X utf8 essai_retour_arriere.py 1.0` | restaure l'archive d'une version dans un dossier neuf, la contrôle, la fait rejouer la séance, chronomètre |
| `python -X utf8 ../livraison/flux_relances.py verifier-livraison` | compare ce qui est livré au manifeste de la version approuvée |

## Ce que les doubles de S2 et de S3 font et ne font pas

Les doubles sont dans `../livraison/essai_s2_s3.py`. Le classeur est un dossier de fichiers CSV ; la boîte partagée est un dossier de fichiers texte, un fichier par message. Ils portent les propriétés que `60-specification.md` §6 exige : le compte de service crée des brouillons et lit « Envoyés » mais n'envoie jamais ; le classeur de pilotage et le dépôt sont en lecture seule ; le flux n'écrit que dans les onglets de son classeur ; une seule exécution à la fois (verrou). Ils savent tomber en panne (jusqu'à une heure donnée, ou à un rang donné) et s'arrêter net.

Ils ne disent rien du vrai connecteur de la plateforme P : ni sa latence, ni ses limites de cadence, ni son format exact. Une « opération » y est un appel au double, comptée comme la page de l'éditeur compte les siennes (`mission/sources/devis-et-page-editeur-2026-10-21.md` §2) : c'est un ordre de grandeur `[F]` pour l'essai et `[H]` pour la production.

## Balayage

`python -X utf8 balayer.py` cherche, dans tout `80-construction/`, un mot de secret suivi d'une valeur, une chaîne longue faite de lettres et de chiffres mélangés, un fichier d'environnement ou une clé privée, une adresse de courriel hors `.invalid`, un numéro de téléphone, une adresse postale. Résultat à chaque version : `../sorties-simulees/balayage-v<x.y>.txt`. Le balayage ne prouve pas l'absence : il réduit le risque, et il se refait à chaque version. Il n'affiche jamais une valeur en entier : un début (préfixe, 4 caractères, « … ») suffit pour retrouver la ligne. Le témoin positif de la recette, une fausse clé de forme réaliste, n'est écrit nulle part : `85-recette/test_recette.py` et `sabotage.py` le composent à l'exécution.
