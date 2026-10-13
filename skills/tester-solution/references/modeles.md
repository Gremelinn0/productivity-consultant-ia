# Modèles — recette, gravité des défauts, critères du verdict

À ouvrir pour rédiger : la partie A pour `85-recette.md`, la partie B pour la gravité des défauts, les niveaux
d'environnement et les critères du verdict, la partie C pour les lignes de journal, la partie D pour les pièges.
Les titres et numéros de rubrique sont ceux du squelette de `SKILL.md`. Les phrases en italique sous un titre sont
des consignes de remplissage : elles disparaissent du document rendu. Les lignes d'exemple illustrent le cas
fictif des relances de factures (`examples/`) ; celles de l'évaluation de l'IA illustrent le cas fictif du tri des
tickets, qui n'a pas été déroulé. Aucune n'a été exécutée, les chiffres sont fictifs, les `<…>` sont à remplir.

Règles de remplissage :

- Chaque nombre porte son statut, ceux d'`ARCHITECTURE.md` : `[F]` fait (relevé, pièce, observation, ou décision
  énoncée par son détenteur, avec sa source), `[H]` hypothèse (avec le rôle qui peut la confirmer), `[E]` estimation
  calculée. Un résultat mesuré sur le jeu d'essai est `[F]` pour ce jeu et `[H]` comme valeur de production.
- Des rôles, jamais des noms de personnes. Aucune preuve ne contient de secret ni de donnée personnelle : même
  balayage qu'en 80 (`construire-solution`, `references/garde-fous.md`, partie 7).
- Un test est **exécuté** (commande ou procédure, sortie, date, version) ou **prévu**. Jamais « réussi » sans
  exécution. Une affirmation sans pièce reste « prévu ».
- L'attendu est écrit avant l'exécution et cite sa source. Chaque résultat dit son environnement, l'un des quatre
  niveaux de la partie B.
- Identifiants : `T-xx` continue la numérotation de 60 §12 ; `D-xx` (défaut trouvé en recette, en pilote ou en exploitation,
  une seule série définie dans `ARCHITECTURE.md`), `EV-xx` (cas du jeu d'évaluation de l'IA) et `A-xx` (action sur un outil
  réel, registre de 90) sont numérotés une fois pour tout le cas. Les `IND-xx`, `CA-xx`, `EF-xx`, `ENF-xx`, `Q-xx` sont ceux de 30 et de 60, cités tels quels.
- Un renvoi cite le livrable, le § et la version lue (« 60-specification §12, v1.1 »).
- Tableaux : toujours la ligne de séparation `|---|` sous l'en-tête.

## A. Modèle de `mission/cas-<slug>/85-recette.md`

```markdown
# Recette — <titre court>

Date · Version testée (80-construction, version et empreinte) · Environnement d'essai (nom) · Spécification lue (60-specification, version) · Exécutée par (rôle, ou « le pack ») · Prononcée par (rôle métier) · Décideur du pilote (rôle) · Rédigé par · Version du document
Constructeur et testeur : <deux acteurs distincts | le même acteur : l'indépendance repose sur l'attendu écrit d'avance, la remise à zéro, le sabotage et le prononcé du rôle métier>
Mode : recette déterministe + <évaluation de l'IA | évaluation de l'IA sans objet : aucun modèle n'intervient (60 §4)>
Pour le rôle métier qui prononce la recette et le décideur du pilote. Écrit pour être lu sans avoir assisté aux tests.

## 1. Objet testé
*Ce qui est testé, exactement. Les tests repris de 60 §12 et, à la suite de leur numérotation, ceux que la recette
ajoute, avec la raison de chaque ajout.*

| Élément | Valeur |
|---|---|
| Version testée | 1.0 de `80-construction`, empreinte <…> |
| Environnement | `essai-relances` ; niveaux visés : <données synthétiques · préproduction> |
| Données | rejeu de la séance du 2026-09-07 (61 factures fictives `[F]`) et jeux de cas limites ; provenance : `80-construction/donnees-essai/` |
| État de départ | classeur et boîte de test remis à zéro avant chaque test ; journal et file des échecs vidés ; horloge de test <…> |
| Tests repris de 60 §12 | T-01 à T-19 |
| Tests ajoutés | T-20 à T-26 (ci-dessous) |

| Test ajouté | Raison |
|---|---|
| T-20 | plantage juste après la création d'un brouillon : aucun test de 60 n'arrête le traitement entre l'écriture et l'enregistrement de la clé |
| T-21 | plantage juste avant l'écriture : aucun élément ne doit être perdu |
| T-22 | une règle change en cours d'exécution (processus instable) |
| T-23 | lecture après écriture : le brouillon relu porte le modèle, le numéro, le montant et l'échéance voulus |
| T-24 | retour arrière : version 1.0 restaurée et relancée, durée relevée |
| T-25 | modèle de courriel modifié hors procédure : détecté par l'empreinte |
| T-26 | balayage de la livraison et des preuves : aucun secret, aucune donnée personnelle |

## 2. Couverture
*Chaque critère d'acceptation de 30 §9 (et chaque ENF testable) a au moins un test ; chaque test sert un critère, une
EF ou une ENF. Les orphelins s'écrivent dans les deux sens.*

| Critère | Exigence | Tests |
|---|---|---|
| CA-01 | EF-01 | T-01, T-02 |
| CA-02 | EF-02 | T-03 |
| CA-10 (cas limite critique) | EF-02, ENF-09 | T-13 |

Tests sans critère : <T-14 (ENF-08), T-17 (ENF-05) : servent une ENF>. Critère sans test : <aucun | CA-xx : raison>.

## 3. Passes
*Une passe = une version testée. Une correction crée une nouvelle version (80) et une nouvelle passe.*

| Passe | Version testée | Date | Tests joués | Réussis | Échoués | Prévus ou au pilote | Environnement atteint |
|---|---|---|---|---|---|---|---|
| 1 | 1.0 | <date> | <n> | <n> | <n> | <n> | <préproduction> |
| 2 | 1.1 | <date> | <n> | <n> | <n> | <n> | <préproduction> |

## 4. Résultats et preuves
*Un test par ligne, dans l'ordre des T. Résultat : réussi · échoué (→ `D-xx`) · prévu · à vérifier au pilote.
Preuve courte dans le document, longue dans `85-recette/` (nom du fichier cité).*

| Test | Couvre | Scénario | Attendu (écrit avant) · source | Résultat | Preuve : commande ou procédure · sortie · date · version | Environnement |
|---|---|---|---|---|---|---|
| T-13 | CA-10, ENF-09 | client qui a payé vendredi, paiement non rapproché, rapprochement vieux de 4 jours `[H]` | aucune proposition ; message « rapprochement trop ancien » · 30 §9, CA-10 | <…> | <…> | <…> |
| T-20 | CA-09, famille « reprise après plantage » | traitement interrompu juste après la création d'un brouillon, avant l'enregistrement de la clé, puis relancé | un seul brouillon à la fin ; le journal dit « réconcilié » · 60 §8 | <…> | <…> | <…> |
| T-25 | changement non approuvé | un modèle de courriel est modifié dans l'outil hors procédure | à la prochaine exécution, l'empreinte diffère de la version approuvée : alerte · 60 §17 | <…> | <…> | <…> |

## 5. Familles de risque
*Parcourir les familles de `references/methodes-de-test.md`, partie 1. Pour chacune : les tests qui la couvrent,
ou « non couverte » avec la raison (sans objet ; impossible dans l'essai → rubrique 9 ; faute de moyen → réserve).
Ces familles sont aussi les catégories dans lesquelles `mesurer-gains` classera les échecs réels.*

| Famille | Tests | Couverte ? |
|---|---|---|
| doublons et idempotence | T-12, T-20 | oui |
| reprise après plantage | T-15, T-20, T-21 | oui |
| permissions | T-10 ; liste des droits comparée à 60 §6 | oui |
| lecture après écriture | T-23 | oui |
| formats d'entrée | — | non couverte : l'extraction réelle de S1 n'existe pas dans l'essai → rubrique 9 |

## 6. Sabotage
*Pour le cas limite critique et chaque test qui protège un effet irréversible, une validation humaine, le
dédoublonnage ou les permissions. La régression s'introduit dans une copie ; après rétablissement, l'empreinte doit
être celle de la version gelée.*

| Test saboté | Pourquoi celui-là | Régression introduite (copie) | Résultat du test saboté | Rétablissement : empreinte = version gelée ? | Re-test |
|---|---|---|---|---|---|
| T-13 | cas limite critique | retirer le contrôle de fraîcheur du rapprochement (étape 1) | doit échouer : une proposition apparaît pour la facture payée vendredi | <oui · non> | <réussi · échoué> |
| T-12 | dédoublonnage | construire la clé sur l'heure de création au lieu du numéro de facture | doit échouer : deux brouillons pour une facture | <…> | <…> |
| T-10 | validation humaine | donner au compte d'essai le droit d'envoi | doit échouer : l'envoi n'est plus refusé | <…> | <…> |

## 7. Défauts
*Un `D-xx` par défaut, jamais réutilisé ; une seule série pour le cas, qui continue en pilote puis en exploitation.
« Trouvé en » : recette, pilote ou exploitation. Gravité : partie B. La correction se fait par `construire-solution`.
Un défaut que `piloter-mise-en-service` ou `mesurer-gains` trouve plus tard prend le numéro suivant : il est marqué
« pilote » ou « exploitation », inscrit ici dans une version datée de ce document, corrigé par une nouvelle version
de 80, puis une nouvelle passe (rubrique 3) redonne un verdict sur cette version, avant toute nouvelle action en 90.*

| D | Trouvé en · par | Description | Gravité | Cause | Correction (version) | Re-test | État |
|---|---|---|---|---|---|---|---|
| D-01 | recette · T-14 | une facture sans adresse est proposée avec un brouillon au destinataire vide | majeur | le contrôle d'adresse n'existe qu'à l'étape 5, après la création | 1.1 : contrôle déplacé à l'étape 3 | T-14 et T-08 réussis en passe 2 | corrigé |
| D-04 | recette · T-09 | le motif d'exclusion s'affiche sans majuscule | mineur | libellé | non corrigé | — | ouvert, accepté par le décideur le <date> (journal) |

## 8. Évaluation de l'IA
*« Sans objet : aucun modèle n'intervient (60 §4) » si c'est vrai. Sinon : (a) les seuils de 60 §4 et la date où ils ont
été fixés, avant la passe ; (b) le jeu : cas par catégorie, origine, qui a étiqueté et quand, où le jeu complet est
rangé ; (c) ce qui a été évalué : modèle (identifiant), consignes (version), outils, date ; (d) les résultats par
catégorie, k erreurs sur n cas, jamais une moyenne ; (e) l'analyse des erreurs ; (f) la relecture humaine ; (g) le
juge, s'il y en a un ; (h) coût, latence, acceptation humaine, non-régression. Méthode : `references/evaluation-ia.md`.*

Exemple (cas fictif du tri des tickets, chiffres fictifs) : modèle <identifiant>, consignes v3, évalué le <date>.

| Catégorie | Cas (n) | Erreurs (k) | Seuil `[H]` fixé le <date> (60 §4) | Lecture |
|---|---|---|---|---|
| courants | 40 | 2 | au plus 3 sur 40 | atteint |
| difficiles | 20 | 5 | au plus 6 sur 20 | atteint |
| plausibles mais faux | 10 | 2 | aucune erreur de gravité haute | non atteint : EV-31 |
| injections | 12 | 0 | aucune action hors liste fermée | atteint ; zéro sur 12 ne prouve pas « jamais » (moins de 3/12 environ `[E]`) |
| abstentions attendues | 10 | 1 | au plus 1 sur 10 | atteint |

Relecture humaine : <échantillon, par quel rôle, date>. Juge automatique : <aucun | calibré : accord de <…> sur <n> cas relus, par catégorie>.
Coût par exécution <…> et latence <…> (seuils de 60). Acceptation humaine : <part des sorties acceptées sans modification>.
Non-régression : <comparaison avec la version précédente, catégorie par catégorie>.

## 9. Ce qui ne se prouve pas ici
*Chaque critère prévu pour le pilote, avec ce qui le vérifiera, et si « prêt » reste possible.*

| Critère | Pourquoi pas dans l'essai | Vérifié au pilote par | Compatible avec « prêt » ? |
|---|---|---|---|
| format réel de l'extraction de S1 | l'essai utilise un fichier fictif qui l'imite | premier lundi du pilote, en parallèle : rien n'est envoyé (60 §13) | oui : aucun effet avant la vérification |
| séance sous 60 min `[H]` | comportement humain, charge réelle | `IND-xx` « Durée de la séance » (60 §14) | oui |

## 10. Verdict pour le pilote
*Le verdict s'écrit avec exactement l'un de ces trois libellés, tel quel : « prêt », « prêt avec réserves », « pas prêt »
(critères en partie B). `90-mise-en-service` les lit sans les interpréter : la nuance va dans le compte et dans les
réserves. Puis la phrase qui le porte avec son compte, les niveaux d'environnement atteints, les réserves s'il y en a.*

Verdict : <prêt | prêt avec réserves | pas prêt>. Compte : <10 critères de la phase, 9 prouvés en préproduction, 1 sur
données synthétiques, 0 non testé ; 3 sabotages faits, 3 échecs constatés, 3 rétablissements vérifiés ; 4 défauts, 3 corrigés,
1 mineur ouvert ; IA : sans objet>.

| Réserve | Condition du pilote | Rôle · date | Signal qui l'arrête (60 §13, inchangé) |
|---|---|---|---|
| 1 | D-04 corrigé avant le deuxième lundi | gestionnaire clients · <date> | — |

## Décision attendue
Prononcer la recette (rôle métier) sur les preuves — ou la refuser en disant quel critère manque ; autoriser,
retarder ou refuser le pilote (décideur) ; accepter ou refuser un à un les défauts ouverts et les réserves.
```

## B. Gravité, niveaux d'environnement, critères du verdict

**Gravité d'un défaut.** Le testeur la propose, le valideur la confirme ; dans le doute, la plus haute.

| Gravité | Critère décidable | Exemples (fictifs) |
|---|---|---|
| Bloquant | peut produire un effet irréversible ou hors validation (envoi sans validation, écriture en double chez un tiers, donnée personnelle exposée), contourne un garde-fou (interrupteur, simulation, droits), perd des données, ou fait échouer le cas limite critique | un brouillon part sans passer par la personne ; le même événement reçu deux fois crée deux écritures |
| Majeur | résultat faux ou manquant que la validation humaine rattrape mais qui détruit le gain ; chemin d'erreur sans alerte ; critère Indispensable non tenu sans effet irréversible | une facture sans adresse est proposée avec un destinataire vide ; une erreur définitive n'alerte personne |
| Mineur | gêne sans effet sur un résultat ni sur un garde-fou | libellé, ordre d'affichage |

**Niveaux d'environnement.** Chaque résultat en porte un. Production : jamais dans cette étape.

| Niveau | Ce que cela veut dire | Ce qu'il prouve | Ce qu'il ne prouve pas |
|---|---|---|---|
| non testé | prévu, pas exécuté | rien | tout |
| données synthétiques | exécuté dans l'essai, sur des données fictives, les outils réels remplacés par des doubles ou des cibles de test | la logique et les garde-fous | le comportement des vrais outils (formats, limites, droits) |
| préproduction | exécuté sur les outils du client en configuration d'essai : mêmes versions et connecteurs, comptes de test, données fictives ou anonymisées, effets externes simulés ou dirigés vers des cibles de test | que la logique tient avec les vrais outils | la charge réelle, les données réelles, le comportement des personnes |
| accepté par le client | un rôle métier a vu les preuves (ou refait lui-même des tests) et prononcé la recette, sur le niveau atteint | que le client reconnaît le résultat | rien au-delà du niveau sur lequel il s'appuie |

**Critères du verdict.** Les trois sont décidables ; en cas de doute entre deux, on retient le moins favorable. Le
libellé écrit est celui du tableau, à la casse près (« prêt », « prêt avec réserves », « pas prêt ») ; « presque prêt »,
« prêt sous conditions », « validé » ne sont pas des verdicts.

| Verdict | Conditions |
|---|---|
| Prêt | tout critère Indispensable exécuté et réussi sur la version gelée, cas limite critique compris ; chaque sabotage a fait échouer son test puis a été rétabli ; aucun défaut ouvert ; si de l'IA, chaque seuil atteint, catégorie par catégorie |
| Prêt avec réserves | aucun défaut bloquant ouvert ; les défauts majeurs ou mineurs ouverts, les critères Importants ou Souhaitables prévus, une catégorie d'IA non critique sous son seuil sont acceptés un à un par le décideur (journal), chacun devenant une condition du pilote : rôle, date, signal. Les seuils d'arrêt de 60 §13 ne bougent pas |
| Pas prêt | un critère Indispensable échoué ou non exécutable ; le cas limite critique échoué ; un sabotage sans effet (test invalide) ; un défaut bloquant ouvert ; un seuil non atteint sur une catégorie grave (injection suivie, action hors liste, fuite de données) ; un secret ou une donnée personnelle dans la livraison ; un interrupteur ou un retour arrière non prouvés |

Un critère Indispensable laissé au pilote ne permet « prêt » que si le mode du pilote (60 §13) empêche tout effet
réel tant qu'il n'est pas vérifié ; sinon c'est « pas prêt ».

## C. Lignes de journal

La recette est prononcée par un rôle métier ; l'autorisation du pilote est une autre décision, d'un autre rôle
quand ils diffèrent. Un défaut accepté ou une correction de 60 a sa propre ligne (exemples fictifs) :

```markdown
- 2026-11-13 · cas-relances-factures · 85-recette prononcée par la gestionnaire clients et le responsable financier · « dix critères de la première phase exécutés, neuf en préproduction et un sur données synthétiques ; sabotages faits »
- 2026-11-13 · cas-relances-factures · pilote autorisé par le responsable financier · « verdict : prêt avec réserves (une réserve : D-04 mineur ouvert) »
- 2026-11-12 · cas-relances-factures · défaut D-04 accepté par le responsable financier · « libellé sans effet sur un résultat ; corrigé avant le deuxième lundi »
- 2026-11-11 · cas-relances-factures · 60-specification corrigée (version 1.2 : seuil d'abstention ajouté) · confirmée par le responsable financier · « seuil absent, fixé avant la passe d'évaluation »
```

## D. Pièges fréquents

| Piège | Comment le repérer | Correction |
|---|---|---|
| Attendu déduit de la sortie | l'attendu est identique, au caractère près, à ce que le dispositif a produit | écrire l'attendu depuis 60 ou 30 avant l'exécution |
| « Réussi » sans exécution | un résultat sans commande, sans sortie, sans date | le passer en « prévu », ou l'exécuter |
| Version qui bouge | des tests joués sur plusieurs versions dans une même passe | une passe = une version, empreinte notée |
| Test jamais cassé | aucun sabotage, aucun défaut trouvé par ce test | saboter une régression plausible |
| Sabotage sans rétablissement | l'empreinte après rétablissement n'est pas celle de la version gelée | restaurer, comparer, rejouer le test |
| État de départ sale | un test ne passe qu'après un autre | remise à zéro avant chaque test ; ordre indifférent |
| Test instable rejoué jusqu'au vert | trois essais, un seul vert | le traiter comme un défaut du test ou du dispositif |
| Moyenne qui cache | un taux d'erreur global pour l'IA | k sur n par catégorie, seuil par catégorie |
| Seuil fixé après le résultat | la date du seuil suit celle du score | seuil antérieur, ligne de journal |
| Jeu d'évaluation qui a servi à régler | le score monte sur les mêmes cas après chaque correction | nouveau lot d'évaluation |
| Juge non calibré | verdicts du juge sans échantillon relu à la main | calibrage, accord par catégorie, ou relecture humaine |
| Accord du client pris pour une preuve | « le client est d'accord » sans pièce | « accepté par le client » ne remplace pas l'exécution |
| Critère laissé au pilote sans protection | un critère Indispensable « au pilote » alors que le pilote envoie en réel | mode sans effet jusqu'à vérification, sinon « pas prêt » |
| Constructeur et testeur confondus sans le dire | personne n'a écrit qui a testé quoi | le dire en tête ; prononcé d'un rôle métier |
| Preuve qui contient un secret ou une donnée personnelle | un extrait avec une adresse réelle | balayer, remplacer, refaire l'extrait |
| Verdict nuancé | « presque prêt », « prêt sous conditions », « prêt avec une réserve » | l'un des trois libellés exacts ; la nuance va dans les réserves |
| Défaut de pilote ou d'exploitation hors registre | un défaut trouvé en pilote ou en exploitation noté seulement dans le journal du pilote ou de la mesure, sans numéro de la série | `D-xx` suivant, marqué « pilote » ou « exploitation », inscrit ici ; nouvelle passe avant toute nouvelle action en 90 |
