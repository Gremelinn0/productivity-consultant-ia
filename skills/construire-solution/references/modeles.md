# Modèles — construction, fiche d'exploitation, journal des versions

À ouvrir pour rédiger : la partie A pour `80-construction.md`, la partie B pour
`80-construction/fiche-exploitation.md`, la partie C pour `80-construction/journal-versions.md`, la partie D
avant de geler une version, la partie E pour le rangement du dossier et les lignes de journal, la partie F
pour les relectures, la partie G pour les pièges. Les titres et numéros de rubrique sont ceux du squelette
de `SKILL.md`. Les phrases en italique sous un titre sont des consignes de remplissage : elles disparaissent
du document rendu. Les lignes d'exemple illustrent le cas fictif des relances de factures (`examples/`) :
aucune n'a été exécutée, les chiffres sont fictifs, les crochets `<…>` sont à remplir.

Règles de remplissage :

- Chaque nombre porte son statut, ceux d'`ARCHITECTURE.md` : `[F]` fait (relevé, pièce, observation, ou
  décision énoncée par son détenteur, avec sa source), `[H]` hypothèse (avec le rôle qui peut la confirmer),
  `[E]` estimation calculée. Une durée ou une consommation mesurée dans l'essai est `[F]` pour l'essai et
  `[H]` comme valeur de production : volumes, charge et comptes y sont différents.
- Des rôles, jamais des noms de personnes. Aucune donnée personnelle, aucun secret, même partiel, aucune
  adresse qui en porte un : on écrit le nom du secret, jamais sa valeur.
- Un contrôle est **exécuté** (commande ou procédure, sortie, date, version) ou **prévu**. Jamais « réussi »
  sans exécution ; « ça marche », sans pièce, ne vaut pas exécution.
- Les identifiants EF, ENF, CA, T, Q, S1… sont ceux de 30 et de 60, cités tels quels. Les écarts n'ont pas
  d'identifiant propre : on les désigne par la rubrique de 60 qu'ils touchent ; une décision à prendre devient
  une question `Q-xx`, à la suite de la série de `60-specification` §16.
- Un renvoi cite le livrable, le § et la version lue (« 60-specification §8, v1.1 »).
- Tableaux : toujours la ligne de séparation `|---|` sous l'en-tête.
- Empreinte : somme de contrôle (par exemple SHA-256) de l'export ou de l'archive de la version, calculée par un
  outil standard au moment du gel et recopiée dans le journal des versions. Elle prouve que le fichier testé
  est le fichier livré.

## A. Modèle de `mission/cas-<slug>/80-construction.md`

```markdown
# Construction — <titre court>

Date · Option construite (40-solutions, décision du <date>) · Construit par (rôle ou équipe) · Valideur (rôle) · Décideur (rôle) · Rédigé par · Version de la construction · Spécification lue (60-specification, version)
Mode : <le pack construit seul | le pack construit avec un compagnon | un tiers construit, le pack prépare et contrôle> · Porte : <constatée le <date>, pièce : <…> | sans objet | sautée à la demande de <rôle>, inscrit au journal>
Pour l'équipe qui teste et qui exploite. Écrit pour être suivi sans avoir assisté à la construction.

## 1. Point de départ
*Les livrables lus, avec leur version : 60, 40, 70 (et 30, 50 si utiles). La phase construite et les exigences
qu'elle sert. « Ce qu'on ne fait pas dans ce lot » de 70, repris mot pour mot comme limites de la construction.
Les étiquettes S1… de 30 §6, pour qui n'a pas lu 30.*

Exemple : lus — 60-specification v1 précisée le 2026-10-12, 40-solutions du 2026-10-06, 70-plan du 2026-10-12.
Phase construite : première phase (EF-01 à EF-04, EF-06 à EF-08, EF-10, EF-11). Limites (70, lot 3) : aucune
relance réelle envoyée par le flux ; aucune connexion à S1 ; aucun changement des critères du pilote une fois
signés.

## 2. Ce qui existait déjà
*Où et quand on a cherché : bibliothèques de modèles des éditeurs de flux, flux publics, brique interne. Un
candidat par ligne. « Non vérifié `[H]` » avec le rôle et la date si la recherche n'a pas pu se faire.*

| Candidat (adresse, lu le) | Auteur · dernière mise à jour · licence | Exigences couvertes | Autorisations demandées · coût à l'exécution | Fait en plus | Décision et raison |
|---|---|---|---|---|---|
| modèle de relance de factures de la bibliothèque de l'éditeur, lu le <date> | <auteur> · <date> · <licence> | EF-07 seulement | écriture dans la messagerie · 1 action par message `[H]` | envoie directement les courriels | inspiration seulement : l'envoi direct contredit EF-10 |

## 3. Environnement d'essai
*Son nom, donné une fois et repris tel quel en 85 et 90. Le lieu, le détenteur, les comptes de test (de service,
droits minimaux, jamais personnels), ce qui n'y existe pas, la preuve d'isolement, le mode simulation, les
données et ce que le client a mis à disposition. Si la plateforme n'offre aucun espace séparé : le dire ici
comme un risque, avec l'accord du décideur (`references/garde-fous.md`, partie 3).*

| Élément | Valeur | Preuve |
|---|---|---|
| Nom | `essai-relances` | repris en 85 et 90 |
| Lieu · détenteur | espace d'essai de la plateforme, classeur et boîte de test · responsable financier | liste des accès relue le <date> |
| Comptes de test | un compte de service d'essai : lecture des listes, création de brouillons dans la boîte de test, aucun droit d'envoi | export des droits, <date> |
| Absent de l'essai | envoi réel, écriture chez un tiers, secret de production | essai d'isolement du <date> : l'accès à la production est refusé |
| Mode simulation | actif par défaut ; sortie simulée dans `80-construction/sorties-simulees/` | contrôle de la tranche 0 |
| Données | 61 factures fictives qui reproduisent le décompte de la séance du 2026-09-07, motifs compris `[F]` | `donnees-essai/LISEZ-MOI` : comment produites ; balayage des noms, adresses et identifiants le <date> |
| Mis à disposition par le client | instance d'essai, comptes de test, connexions de test (leur nom seulement) | <rôle> · <date> |

## 4. Plateforme et compagnon
*La plateforme décidée en 40, jamais une autre. La ligne de `COMPAGNONS.md` lue, et si le compagnon a réellement
été appelé ; sinon « méthode de repli maison » (`references/garde-fous.md`, partie 5). Les versions fixées, avec
la date de lecture.*

| Composant | Version ou identifiant fixé | Lu le · dans quoi |
|---|---|---|
| Plateforme | <version de l'instance d'essai> | <date> · page d'administration |
| Connecteur de messagerie | <version> | <date> |
| Modèle d'IA (s'il y en a un) | <identifiant exact> | <date> · réglages du fournisseur |

## 5. Tranches
*Tranche 0 = le socle. Une ligne par tranche. « Contrôle de tranche » : exécuté (commande ou procédure, résultat,
date) ou prévu. Le constructeur ne déclare aucun critère d'acceptation réussi. Une tranche n'est pas un lot de
70. Après le tableau, la table exigence → tranche.*

| Tranche | Étapes de 60 §4 · exigences servies | Ce qu'elle livre (entrée → sortie lisible) | Garde-fous posés | Tests de 60 §12 rendus exécutables | Contrôle de tranche | Version |
|---|---|---|---|---|---|---|
| 0 Socle | — · ENF-06, ENF-10 | essai nommé ; mode simulation ; journal d'exécution ; case « Suspendre » lue avant chaque étape ; verrou d'exécution unique | simulation, journal, interrupteur, verrou | T-18 (interrupteur) | exécuté : lancement à vide, une ligne au journal, sortie simulée écrite, case cochée → rien de créé · <référence> | 0.1 |
| 1 Lire et contrôler | 1, 2, 3 · EF-01, ENF-09 | extraction du jour → liste candidate avec niveau, ou avertissement « rapprochement trop ancien » | erreurs définitives vers la file des échecs | T-01, T-02, T-13 | <exécuté · prévu> | 0.2 |
| 2 Écarter | 4 · EF-02, EF-03, EF-04, EF-06 | liste candidate → propositions, écarts avec motif, comptes clés à part | — | T-03, T-04, T-05, T-07 | <exécuté · prévu> | 0.3 |
| 3 Brouillons simulés | 5 · EF-07, EF-08, EF-10 | propositions → brouillons dans la boîte de test | clé de dédoublonnage vérifiée avant création ; aucun droit d'envoi ; état relu après écriture | T-08, T-09, T-10, T-12 | <exécuté · prévu> | 0.4 |
| 4 Historique et litiges | 8, 9 · EF-11, EF-04 | courriel envoyé → ligne d'historique ; litige saisi → brouillon retiré | clé de l'historique ; réglage du pilote (étape 8 activable) | T-06, T-11, T-19 | <exécuté · prévu> | 0.5 |
| 5 Erreurs et alertes | §7, §10 · ENF-08 | file des échecs, reprises, alertes, plafond | reprise, alerte sur silence, plafonds | T-14 à T-17 | <exécuté · prévu> | 1.0 |

| Exigence de la phase | Tranche | Remarque |
|---|---|---|
| EF-01 | 1 | |
| EF-02, EF-03, EF-04 | 2 | EF-04 : retrait en cours de séance en tranche 4 |
| EF-06 | 2 | |
| EF-07, EF-08, EF-10 | 3 | |
| EF-11 | 4 | |
| ENF-08, ENF-09, ENF-10 | 5, 1, 0 | |

## 6. Garde-fous
*Une ligne par garde-fou de 60 §7 à §11 (et §4, §6, §13 pour la simulation, les droits et le pilote). « Écarté » n'est
admis qu'avec un écart tracé en rubrique 8.*

| Garde-fou (60 §) | Exigence | Comment il est construit | Tranche | Contrôle |
|---|---|---|---|---|
| Simulation et absence de droit d'envoi (§4, §6) | EF-10 | le compte d'essai ne crée que des brouillons, dans la boîte de test ; la sortie simulée garde la trace | 0, 3 | <exécuté : envoi refusé, tentative au journal · prévu> |
| Dédoublonnage (§8) | EF-03, EF-11 | clé = numéro de facture + niveau ; cherchée avant création, enregistrée après la réussite ; à la reprise, l'objet réellement enregistré est relu avant de recréer | 3, 4 | <flux lancé deux fois ; arrêt entre l'écriture et l'enregistrement> |
| Journal d'exécution (§10) | ENF-06 | une ligne par facture et par étape : clé, étape, résultat, heure, version des règles ; ni nom ni adresse | 0 | <relecture d'un rejeu> |
| Erreurs, file des échecs, alerte (§7) | ENF-08 | reprises espacées puis file des échecs (passagère) ; aucune reprise puis alerte (définitive) | 5 | <une erreur de chaque type provoquée> |
| Interrupteur et plafonds (§7) | ENF-10 | case « Suspendre » lue avant chaque étape ; verrou ; 100 propositions au plus `[H]` | 0, 5 | <case cochée en cours d'exécution ; plafond dépassé> |
| Secrets (§9) | — | accès-listes, accès-messagerie, accès-alerte référencés par leur nom, dans le coffre de la plateforme | 0 | <balayage de la livraison, date, résultat> |
| Sauvegarde, versions, retour arrière (§11) | — | export numéroté à chaque version ; version précédente restaurée une fois | toutes | <durée du retour arrière `[F]`> |
| Alerte sur silence (§10) | — | alerte si aucune exécution le lundi à 10 h `[H]` | 5 | <exécution volontairement non lancée> |
| Réglage du pilote (§4, §13) | — | paramètre « étape 8 active », désactivable le premier lundi | 4 | <T-19 prévu en recette> |

## 7. Livré
*Où est quoi, en quelle version, avec quelle empreinte. Ce qui n'est pas livré, dit. Le balayage des secrets et des
données personnelles de chaque fichier rangé (partie 7 de `references/garde-fous.md`) : date et résultat.*

| Fichier (dans `80-construction/livraison/`) | Version | Empreinte | Contenu | Balayé le · résultat |
|---|---|---|---|---|
| `flux-relances-v1.0.json` | 1.0 | <empreinte> | export du flux ; connexions par leur nom | <date> · aucun secret, aucune donnée personnelle |
| `regles-v1.0.csv` | 1.0 | <empreinte> | seuils, délais, modèles de courriel | <date> · aucun |

Journal des versions : `80-construction/journal-versions.md`. Non livré : <seconde phase, accès à S1>.

## 8. Écarts avec la spécification
*Chaque endroit où la construction diffère de 60 ou la complète. Traitement : précision → version datée de 60 et
ligne « correction » au journal ; trou à trancher → `Q-xx` ; chose que la plateforme de 40 ne sait pas faire →
la tranche s'arrête, retour à `concevoir-solution`. Un écart soupçonné qu'on ne peut pas confirmer à la construction
s'écrit aussi : état « soupçon », avec le test de 85 qui le tranchera (le soupçon ne bloque pas le gel, il se solde en
recette). Un choix de réalisation sans effet visible n'est pas un écart.*

| Rubrique de 60 | Constat | Traitement | État |
|---|---|---|---|
| §7 reprises | le connecteur de messagerie limite la cadence : trois reprises espacées de 1, 5 et 15 min `[H]` ne suffisent pas au-delà de quelques dizaines de brouillons | 60 v1.1 : cadence plafonnée et reprise réécrites ; ligne « correction » au journal ; valideur de 60 informé | corrigé |
| §4 étape 6 | l'avertissement part par la messagerie : à qui s'il n'y a ni proposition ni compte clé ? | question Q-13, responsable financier, non bloquante | ouvert |
| §11 sauvegarde | la sauvegarde datée du flux n'est pas exportable avec l'offre d'entrée de la plateforme `[H]` | la tranche s'arrête ; retour à `concevoir-solution` (critère « dépendance et portabilité ») ; le responsable financier tranche | à trancher |
| §6 règle du litige | l'écriture de la règle laisse penser qu'une facture à litige partiel serait relancée quand même ; l'essai ne le confirme pas sans la source réelle | soupçon : test à écrire en 85 (une facture à litige partiel ne reçoit aucune relance) | soupçon |

## 9. Chiffres relevés
*Ce que la construction a appris, comparé aux estimations de 40 §8 et aux seuils de 50 (point mort). Un
dépassement est dit au décideur, avec renvoi à `chiffrer-rentabilite`. Sans relevé : `[H]` et le rôle qui peut
le fournir. Ces relevés servent à `mesurer-gains`.*

| Grandeur | Estimation (source) | Relevé dans l'essai | Seuil de 50 (point mort) | Lecture |
|---|---|---|---|---|
| Effort de construction, première phase | 2 jours payés `[H]` (50 §2) | 2,5 jours `[F]` pour cette construction, feuille de temps du constructeur | devis au plus 980 € payé, soit 2,2 jours `[E]` (50 §4) | au-dessus du seuil : dit au décideur |
| Consommation du rejeu | 150 actions par séance `[E]` (40 §8) | 140 actions `[F]` pour le rejeu de 61 factures ; `[H]` en production | coût de fonctionnement au plus 24 € par mois `[E]` (70 §5) | sous l'estimation |
| Maintenance pressentie | 1 h par mois `[H]` (50 §2) | non relevable dans l'essai | au plus 1,1 h par mois `[E]` | à relever au pilote |

## 10. Fiche d'exploitation et ce qui reste au client
*La fiche est un fichier à part (partie B), citée ici avec sa version : on ne la recopie pas. Elle répond toujours
aux quatre questions que `90-mise-en-service` vérifie (rubriques 1 à 4 de la fiche) ; on les cite ici pour qu'il les
retrouve. Elle a été essayée par un tiers : non / oui, le <date>, par <rôle> (l'essai est une étape de 70). Puis la
liste de ce que le client fera dans ses propres outils : chaque ligne deviendra une action `A-xx` de
`90-mise-en-service`, avec son retour arrière. Le pack ne fait rien de cela.*

Fiche : `80-construction/fiche-exploitation.md`, révision 1, décrit la version 1.0. Ses quatre réponses : comment
vérifier que ça marche (rubrique 1), que faire en cas d'incident (2), qui joindre (3), comment revenir en arrière (4).
Essayée par un tiers : <non | oui, le <date>, par <rôle>>.

| Action pressentie | Où | Réversible ? | Retour arrière prévu | Rôle qui décidera |
|---|---|---|---|---|
| importer la version 1.0 dans l'espace de production de la plateforme | plateforme | oui | désactiver et supprimer le flux importé ; sauvegarde datée | responsable financier |
| poser les trois secrets de production dans le coffre | coffre de la plateforme | oui | révoquer et recréer | responsable financier |
| passer le mode simulation à réel (création de brouillons dans la boîte partagée) | réglage du flux | oui | remettre en simulation, supprimer les brouillons créés | responsable financier |

## 11. Questions ouvertes
*À la suite de la série de 60 §16.*

| ? | Question | Rôle qui répond | Bloquante pour la recette ? |
|---|---|---|---|
| Q-13 | À qui l'avertissement va-t-il quand il n'y a ni proposition ni compte clé ? | responsable financier | non |

## Décision attendue
Déclarer la version <x.y> prête pour la recette — ou trancher les écarts de la rubrique 8 ; confirmer qui
exécutera la recette et qui la prononcera (un rôle métier, pas le constructeur).
```

## B. Modèle de `80-construction/fiche-exploitation.md` — une page

Écrite pour quelqu'un qui n'a pas construit le dispositif. C'est ce que `90-mise-en-service` appelle le mode
opératoire : il n'existe qu'ici. Elle répond toujours à quatre questions, dans cet ordre et sous ces titres :
**comment vérifier que ça marche, que faire en cas d'incident, qui joindre, comment revenir en arrière**. Aucune
n'est supprimée ni renvoyée à l'oral ; une ligne qui ne s'applique pas dit pourquoi (« sans objet : … »). `90`
la fait dérouler par un tiers et renvoie ici toute lacune : elle se corrige dans cette fiche par une révision
datée (ligne « correction » au journal), et la rubrique 10 de `80-construction.md` cite la nouvelle révision.
Tient sur une page : si elle déborde, la raccourcir plutôt que de la faire courir sur deux. Elle ne contient
aucun secret (seulement leur nom) ni aucun nom de personne (des rôles).

```markdown
# Fiche d'exploitation — <dispositif> · décrit la version <x.y> · fiche du <date>, révision <n>
Propriétaire (rôle) · Suppléant (rôle) · Maintenance courante (rôle) · Essayée par un tiers : <non | oui, le <date>, par <rôle>>

## Ce que fait le dispositif, et ce qu'il ne fait pas
<trois à cinq lignes : déclencheur, ce qu'il produit, qui valide ; ce qu'il n'envoie ni ne modifie>

## 1. Comment vérifier que ça marche
*Quoi regarder, où, quand, et à quoi ressemble un jour normal. Avec une étape d'IA : une ligne de plus pour
l'identifiant exact du modèle, relu à chaque revue.*

| Signal | Où le lire | Quand | Résultat normal | Anormal quand | Qui regarde (suppléant) |
|---|---|---|---|---|---|
| exécution du lundi | journal d'exécution, compteurs | chaque lundi à 10 h `[H]` | une exécution ; autant de brouillons que de propositions | aucune exécution à 10 h | gestionnaire clients (comptable) |
| file des échecs | onglet « échecs » | à chaque séance | vide | une ligne ou plus | gestionnaire clients (comptable) |
| alertes | messagerie | à réception | aucune, ou traitée dans la journée | alerte non traitée à 12 h le lundi `[H]` | responsable financier (gestionnaire clients) |

## 2. Que faire en cas d'incident
| Symptôme | Cause probable | Première action | Qui prévenir | Suspendre quand |
|---|---|---|---|---|
| alerte « rapprochement trop ancien » | lettrage non fait avant la séance | ne rien envoyer ; demander le lettrage à la comptable | gestionnaire clients | pas de lettrage à 11 h `[H]` |
| alerte « échec », motif « droit refusé » | secret expiré ou droit retiré | cocher « Suspendre » | responsable financier (il détient les comptes) | tout de suite |
| rien reçu le lundi à 10 h | flux non lancé, connecteur modifié | lancer à la main | gestionnaire clients | non résolu à 12 h `[H]` : séance à la main (méthode de repli) |
| deux copies pour une même facture | envoi hors brouillon ou double envoi | cocher « Suspendre » ; alerte « double envoi » ; prévenir le client si besoin | responsable financier | tout de suite |

## 3. Qui joindre
| Rôle | Pour quoi | Suppléant | Escalade si pas de réponse sous 1 h ouvrée `[H]` |
|---|---|---|---|
| responsable financier (propriétaire) | règles, comptes et secrets, suspension durable, retour arrière | gestionnaire clients | — : c'est le dernier échelon |
| gestionnaire clients (exploitant) | file des échecs, alertes, séance à la main | comptable | responsable financier |
| support de la plateforme | panne de la plateforme ou du connecteur | — | gestionnaire clients, qui prévient le responsable financier |

Rôles seulement : les coordonnées sont dans l'annuaire de l'entreprise, jamais dans cette fiche.

## 4. Comment revenir en arrière
- **Suspendre (interrupteur)** : case « Suspendre » (qui peut la cocher ; ce qu'elle fait des éléments en cours).
- **Revenir à l'ancienne méthode** : <la méthode d'avant, où elle est écrite, qui la reprend>.
- **Revenir à la version précédente** : <où est l'export, comment le réimporter, durée mesurée `[F]` dans l'essai ; comment vérifier que l'ancienne version a repris>.
- **Reprendre ensuite** : <rejouer la file des échecs : geste exact>. Un élément rejoué ne double rien (clé de dédoublonnage).

## Ce qu'on ne touche pas sans demande
Les règles (seuils, délais, modèles) : une demande au propriétaire, un test dans l'essai, une version numérotée.

## Comptes et secrets (noms seulement)
| Secret (nom) | Ce qu'il permet | Où il est conservé | Propriétaire | Échéance |
|---|---|---|---|---|
| accès-listes | lire les listes, écrire dans le classeur du dispositif | coffre de la plateforme | responsable financier | revue tous les 6 mois `[H]` |

## Dépendances
S1 à S4 et la plateforme ; ce qui les change (renouvellement, évolution du connecteur) et qui le sait.
```

## C. Modèle de `80-construction/journal-versions.md`

Une ligne par version, jamais modifiée après coup. Une correction après le gel est une nouvelle ligne.

| Version | Date | Changement | Raison (tranche · écart · défaut `D-xx` de recette, de pilote ou d'exploitation) | Export · empreinte | Contrôles passés | Gelée pour la recette |
|---|---|---|---|---|---|---|
| 0.1 | <date> | socle | tranche 0 | `flux-relances-v0.1.json` · <empreinte> | lancement à vide | non |
| 1.0 | <date> | toutes les tranches de la phase | écarts de la rubrique 8 | `flux-relances-v1.0.json` · <empreinte> | contrôles de tranche, balayage | oui |
| 1.1 | <date> | filtre « litige » corrigé | `D-03` | `flux-relances-v1.1.json` · <empreinte> | T-05, T-06 rejoués ; sabotage refait | oui, nouvelle passe de recette |

## D. Liste « prêt pour la recette »

Chaque ligne : oui ou non, et la pièce. Une case « non » : la version n'est pas gelée.

1. Chaque tranche de la phase a son contrôle exécuté (preuve) ou prévu avec sa raison.
2. La table exigence → tranche n'a aucune exigence Indispensable ou Importante sans tranche, ni tranche sans exigence.
3. Chaque garde-fou de 60 §7 à §11 est construit, ou écarté par un écart tracé en rubrique 8.
4. L'isolement et le mode simulation sont prouvés par un essai (rien de réel ne peut partir).
5. Le retour arrière a été essayé une fois dans l'essai, durée relevée.
6. La livraison est balayée : aucun secret, aucune donnée personnelle, méthode et date écrites.
7. La version est numérotée, exportée, son empreinte notée, et rien n'a changé depuis.
8. Les écarts sont traités : version datée de 60, question `Q-xx`, retour à `concevoir-solution` décidé, ou soupçon écrit avec son test de 85.
9. Les réglages du pilote (60 §4, §13) sont construits et contrôlés.
10. La fiche d'exploitation est écrite avec ses quatre réponses (vérifier que ça marche, incident, qui joindre, revenir en arrière), sans rubrique vide ; l'essai par un tiers est prévu au plan.
11. Les chiffres relevés sont comparés aux seuils de 50, les dépassements dits au décideur.
12. Si une étape d'IA existe : consignes versionnées, modèle fixé, jeu de mise au point rangé à part, jeu d'évaluation non consulté.

**Quand la construction est une maquette** (un programme qui reproduit la logique hors de la plateforme décidée en 40), une ligne qui demande la
plateforme (isolement du mode réel, retour arrière d'un import, réglages du pilote dans l'outil) se coche « maquette seulement », avec ce que la
maquette a prouvé et ce que seule la plateforme prouvera. La version se gèle « pour la recette de la maquette » (colonne « Gelée pour la recette » du
journal des versions), et `85-recette` prévoit la recette sur la plateforme : passes à venir, niveau d'environnement atteint par critère.

## E. Rangement du dossier et lignes de journal

```text
mission/cas-<slug>/
  80-construction.md
  80-construction/
    journal-versions.md      une ligne par version
    fiche-exploitation.md    la fiche d'une page
    donnees-essai/           le jeu d'essai fictif ou anonymisé et son LISEZ-MOI (comment il a été produit)
    sorties-simulees/        ce que la simulation a écrit à la place des effets réels (preuves)
    livraison/               code, export du flux sans secret, règles, modèles de messages — un fichier par version
```

Lignes de journal (exemples fictifs) :

```markdown
- 2026-11-10 · cas-saisie-commandes · 80-construction validé par le responsable des opérations · « version 1.0 gelée pour la recette ; deux écarts traités, une question ouverte »
- 2026-11-06 · cas-saisie-commandes · 60-specification corrigée (version 1.1 : cadence des brouillons plafonnée) · confirmée par le responsable des opérations · « écart trouvé à la tranche 3 »
- 2026-11-08 · cas-saisie-commandes · retour à concevoir-solution décidé par la direction commerciale · « la plateforme choisie n'exporte pas ses sauvegardes ; l'option de repli est examinée »
- 2026-10-27 · cas-saisie-commandes · construction lancée, porte sautée à la demande de la direction commerciale · « l'essai ne coûte aucune dépense ; la fiche de porte suit »
```

## F. Les trois relectures

- **Relecture du testeur.** Quelqu'un qui n'a pas construit peut-il lancer chaque test de 60 §12 avec ce seul dossier,
  sans demander où est quoi ni quel état de départ prendre ? Sinon, `donnees-essai/` ou la rubrique 3 est incomplète.
- **Relecture du client.** Avec la liste de la rubrique 10, le client peut-il préparer ses secrets, ses comptes et
  les actions de `90-mise-en-service` sans le constructeur ? Sinon, une ligne manque ou n'a pas de retour arrière.
- **Relecture du suppléant.** Avec la seule fiche, quelqu'un qui n'a jamais vu le dispositif peut-il vérifier que ça
  marche, réagir à un incident choisi, savoir qui joindre, l'arrêter, rejouer la file des échecs et revenir à la version
  précédente ? Sinon, la fiche est à réécrire, pas à compléter à l'oral.

## G. Pièges fréquents

| Piège | Comment le repérer | Correction |
|---|---|---|
| Garde-fous « à la fin » | ni journal ni interrupteur avant la dernière tranche | socle en tranche 0 ; chaque garde-fou avec la première tranche qui agit |
| Essai relié à la production | un compte de test lit ou écrit dans la production ; mêmes noms des deux côtés | comptes séparés ; essai d'isolement écrit |
| Déclencheur actif à l'import | planification ou lien d'appel actifs après import d'un modèle | importer désactivé ; lire les déclencheurs ; activer dans l'essai seulement |
| Secret dans l'export | chaîne qui ressemble à une clé, adresse qui porte un jeton | le retirer, écrire son nom ; faire révoquer s'il a circulé |
| Règles dans la logique | un seuil ou un délai écrit dans le code ou le flux | règles en données datées, lisibles par leur propriétaire |
| Identifiant supposé | un identifiant copié d'une documentation ou d'un autre environnement | le relire dans l'outil, noter la date ; introuvable → écart |
| Écriture non relue | on prend le « OK » de l'appel pour l'état enregistré | relire l'objet réellement enregistré |
| Écart enterré | le comportement diffère de 60 sans trace | rubrique 8 ; version datée de 60 |
| Version qui bouge | on corrige pendant la recette sans nouvelle version | nouvelle version, empreinte, tests rejoués |
| Plateforme remplacée en douce | le compagnon propose un outil « plus simple » | écart → `concevoir-solution`, décision du décideur |
| Modèle importé sans lecture | un flux public tel quel, avec ses appels sortants | le lire en entier ; vérifier auteur, autorisations, coûts |
| Donnée réelle « juste pour voir » | un export réel dans l'essai ou dans `sources/` recopié | jeu fictif ; sinon le client rejoue chez lui |
| IA réglée sur le jeu d'évaluation | le score monte sur les mêmes cas | jeu de mise au point à part ; nouveau lot d'évaluation |
| Fiche à trois réponses sur quatre | aucune ligne « qui joindre », ou aucun « résultat normal » dans « comment vérifier » | les quatre rubriques sont obligatoires ; une ligne sans objet dit pourquoi, une rubrique ne disparaît pas |
