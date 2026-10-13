# Modèles — mise en service

À ouvrir pour rédiger `mission/cas-<slug>/90-mise-en-service.md` : la partie A donne le modèle du livrable, la partie B la
fiche d'une action, la partie C les lignes de journal, la partie D les pièges et le test du lecteur froid. Les titres et
numéros de rubrique sont ceux du squelette de `SKILL.md`. Les phrases en italique sous un titre sont des consignes de
remplissage : elles disparaissent du document rendu. Les exemples sont fictifs.

Règles de remplissage :

- Chaque nombre porte son statut, ceux d'`ARCHITECTURE.md` : `[F]` fait (relevé, pièce, décision énoncée par son détenteur),
  `[H]` hypothèse (avec le rôle qui confirme), `[E]` estimation (calcul montré). Les dates prévues sont des propositions `[H]` que
  le décideur confirme ; une date réelle est un fait, avec sa pièce. Un relevé du pilote est `[F]` pour son occurrence : ce n'est
  jamais un gain.
- Des rôles, jamais des noms de personnes. Aucune donnée personnelle, aucun chemin de poste, aucun secret : le document nomme les
  secrets et dit où ils sont rangés, jamais leur valeur.
- Identifiants : `A-xx` action sur un outil réel, numérotée une fois pour tout le cas ; `D-xx` défaut (une seule série par cas, définie dans
  `ARCHITECTURE.md` : un défaut trouvé en pilote ou en exploitation prend le numéro suivant et est marqué tel) ; `T-xx`, `CA-xx`, `IND-xx`,
  `R-xx`, `Q-xx` se citent tels quels.
- Un renvoi cite le livrable, le § et la version lue (« 60-specification §13, v1.1 ») ; sans version, il vise la version 1.
- Le document se tient à jour au fil des actions et des décisions : chaque ligne porte sa date. Une décision déjà inscrite qui change
  (critère, périmètre, action validée) prend une version datée et une ligne « correction » au journal (`ARCHITECTURE.md`).
- Tableaux : toujours la ligne de séparation `|---|` sous l'en-tête.

## A. Modèle de `mission/cas-<slug>/90-mise-en-service.md`

```markdown
# Mise en service — <titre court du cas>

Date de mise à jour · Demandeur (rôle) · Responsable du cas (rôle) · Décideur de la mise en service (rôle) · Rédigé par · Version · Sources : 60-specification, 70-plan, 80-construction, 85-recette (version lue de chacun)
*Une ligne d'annonce : la solution mise en service (nom, version construite), l'environnement réel, les étiquettes S1… reprises de 30-exigences §6, et « les dates prévues sont des propositions `[H]` que le décideur confirme ; une date réelle est un fait, avec sa pièce ».*

## 1. Point de départ
*Ce que la mise en service reçoit. La colonne « Conséquence » dit ce qui doit être fait avant la première action.*

| Élément | Lu | Pièce (livrable § · version) | Conséquence |
|---|---|---|---|
| Verdict de la recette | prêt · prêt avec réserves · pas prêt | 85-recette | « pas prêt » : arrêt, retour à construire-solution ou tester-solution |
| Réserves | | 85-recette | fermée avant le feu vert, ou acceptée par <rôle> le <date> comme condition du pilote |
| Défauts `D-xx` ouverts | | 85-recette | aucun défaut bloquant avant le feu vert |
| Porte (40-solutions §10) | constatée le <date> · sans objet | ligne du journal | non constatée : la faire constater avant toute action |
| Lot de simplifications seules (option 0) | oui · non | 70-plan, journal | oui : ni 80 ni 85 ; le registre ne porte que les actions sur les outils que ces simplifications modifient, validées à part |
| Écarts avec le plan | échéance passée, rôle absent, valeur contredite | 70-plan | redaté (ancienne date écrite) · correction de 70 par version datée |

## 2. Registre des actions
*Une ligne par action sur un outil réel, numérotée `A-01`… Une action sur l'environnement d'essai n'y figure pas (elle relève de 80 et 85).
Action : un verbe, un objet, une version (« Importer la version 1.0 du flux, inactive »). Effet externe : « non », ou le public touché, un
plafond (nombre au plus, période) et le rôle qui répond de la relation. Réversible : « oui » avec le retour arrière (comment, qui, temps
mesuré, où il a été essayé), « prêt » quand il est écrit pas à pas et essayé ; « non » avec « aucun » et ce qui limite les dégâts (plafond,
premier lot réduit, simulation lue, correctif possible). Valideur : le rôle qui administre l'outil touché ou répond de la donnée ou de la
relation ; exécutant : un rôle du client. Preuve : l'effet constaté dans l'outil, par qui et quand, jamais « fait ».*

| ID | Action | Où (outil · environnement) | Effet externe | Réversible · retour arrière prêt | Valideur · exécutant (rôles) | Validée le · valable jusqu'au | État | Preuve |
|---|---|---|---|---|---|---|---|---|
| A-01 | Créer le compte de service « saisie-commandes », lecture seule sur le dossier de dépôt | S2 · réel | non | oui · retirer le compte, 5 min `[H]`, essayé sur la boîte de test le 2026-11-05 · prêt | responsable des opérations · administrateur de la messagerie | 2026-11-09 · 2026-11-20 | validée | |
| A-02 | Importer la version 1.0 du flux, inactive | plateforme · réel | non | oui · supprimer la version importée, 2 min `[H]` · prêt | responsable des opérations · responsable des opérations | | proposée | |
| A-05 | Envoyer un premier lot de 20 confirmations de commande, lot choisi par le valideur | S3 · réel | oui · 20 clients au plus, un seul jour · directeur commercial | non · aucun ; limite : lot réduit, simulation lue le 2026-11-13 (T-14), message rectificatif prêt | directeur commercial et responsable des opérations · gestionnaire des commandes | | proposée | |
| A-08 | Activer le déclencheur du lundi pour l'équipe pilote | plateforme · réel | non | oui · désactiver le déclencheur, 1 min `[H]`, essayé le 2026-11-26 · prêt | responsable des opérations · responsable des opérations | 2026-11-30 · 2026-12-04 | revenue en arrière (faite le 2026-12-01, défaite le 2026-12-02) | déclencheur lu actif le 2026-12-01 ; désactivé et vérifié le 2026-12-02 |

*États (cinq) : proposée (écrite, en attente) · validée (le valideur a répondu oui, date) · faite (effet constaté) · annulée (abandonnée avant d'être
faite) · revenue en arrière (faite, puis défaite par son retour arrière : la ligne garde les deux dates). Règles qui se vérifient sur le tableau : la
validation précède l'exécution, sans exception (aucune action n'est « faite » sans validation antérieure) ; une action réversible n'est validée que si
son retour arrière est prêt ; une action non réversible n'est validée qu'après lecture de la simulation ; un effet externe n'est validé qu'avec son
public et son plafond ; passé « valable jusqu'au », l'action revient à « proposée ». Une action validée ne se modifie pas : on l'annule et on propose
une nouvelle `A-xx` qui renvoie à elle. Une action d'urgence faite par le client lui-même hors des actions validées (par exemple couper l'interrupteur
sur un signal que la fiche n'avait pas prévu) ne se régularise pas après coup : le journal l'écrit comme un incident daté (qui, quoi, quand, effet
constaté), et le registre propose la suite en `A-xx` nouvelles (la garder, la défaire, la corriger), validées avant d'être faites.*

*Mesure d'attente. Tant qu'un défaut bloquant est ouvert en exploitation, les mesures de confinement (suspendre, retirer, prévenir) sont des `A-xx`
marquées « mesure d'attente » dans la colonne Action : elles ne modifient ni la solution ni ses règles, se proposent et se valident comme les autres
(retour arrière prêt, public et plafond d'un message), et leur levée est une `A-xx` de plus, après la correction recettée. Le verdict de 85 rendu sur la
version en service est relu au journal (« verdict relu : pas prêt pour la version en service ») jusqu'à cette correction.*

## 3. Feu vert du pilote
*Décision go/no-go écrite. Le décideur est celui de 60-specification §13. Les critères sont ceux de 60-specification §13, cités, jamais
recopiés. Une condition « non » n'est pas effacée : elle devient une condition du feu vert (propriétaire, échéance) ou un pas de feu vert.*

| Condition | Pièce | Remplie ? |
|---|---|---|
| Recette prononcée : « prêt », ou « prêt avec réserves » acceptées en rubrique 1 | 85-recette, version … | |
| Aucun défaut bloquant ouvert | liste des `D-xx` | |
| Porte constatée, si 40-solutions §10 en pose une | ligne du journal du … | |
| Fiche des critères du pilote signée, sans changement depuis | fiche du … (60-specification §13) | |
| Actions de préparation faites, chacune avec sa preuve | `A-xx` à l'état « faite » | |
| Interrupteur essayé en conditions réelles, retour à l'ancienne méthode décrit | `T-xx`, essai du … | |
| Alertes essayées de bout en bout, destinataires et suppléants joignables | message d'alerte reçu le … | |
| Mode opératoire déroulé par quelqu'un qui ne l'a pas écrit | rubrique 8 | |
| Surveillance renforcée organisée | rubrique 4 | |
| Utilisateurs du pilote prévenus et formés au niveau requis | rubrique 7 | |
| Sauvegarde datée de ce que le pilote modifie ; plafonds des effets externes en place | `A-xx` | |
| Pour tout effet externe : simulation lue par le valideur, premier lot réduit choisi, message rectificatif prêt | `T-xx`, `A-xx` | |

Décision : feu vert · feu vert avec conditions · pas de feu vert — décideur (rôle), date. Conditions : … (propriétaire, échéance).

## 4. Pilote
*Périmètre, dates et mode viennent de 70-plan §3 et de 60-specification §13 : les citer, ne pas les recopier. Une ligne par séance ou par jour.
Mode : parallèle (l'ancienne méthode produit le résultat, le dispositif une proposition qu'on compare : aucun effet réel), préparation avec validation
(le dispositif prépare, une personne valide chaque action), ou réel. En parallèle, dire pour chaque étape à effet sortant si elle est active, désactivée ou observée ce jour-là, et le test qui le vérifie
(60-specification §4). Un relevé est un fait d'occurrence `[F]` avec sa source. Un écart sans explication arrête la montée en charge.*

| Date | Séance ou jour | Mode | Relevés (`IND-xx` · valeur · source) | Écarts expliqués un à un | Incidents · `D-xx` | Décision du jour |
|---|---|---|---|---|---|---|
| | | | | | | |

**Surveillance renforcée** — *du premier jour du pilote jusqu'à un critère de sortie écrit, après la bascule.*

| Ce qu'on lit | Qui (rôle) | Rythme | Seuil qui déclenche | Action |
|---|---|---|---|---|
| | | | | |

Durée et critère de sortie `[H]` (par exemple : n lectures de suite sans alerte non traitée et indicateurs dans leurs seuils) : … Constructeur joignable
jusqu'au : … Retour au rythme de revue de 70-plan §6 à la sortie.

## 5. Fin du pilote
*Les critères sont ceux de la fiche signée (60-specification §13), cités. La mesure de chaque critère est jointe, avec sa période et sa source.*

| Critère (cité) | Seuil (cité) | Mesuré (période · source · statut) | Atteint ? |
|---|---|---|---|
| | | | |

Hypothèses `[H]` de 50-rentabilite levées par le pilote : … Non levées : … (elles passent à `mesurer-gains`).
Décision : continuer · prolonger · arrêter — décideur (rôle), date, motif. « Continuer » exige aussi les conditions du plan (par exemple : le suppléant a tenu
une séance de pilote). « Arrêter » : retour à l'option de repli de 40-solutions par des actions de retrait (`A-xx`).

## 6. Bascule
*Reprend 70-plan §3 : jour et ordre, retour arrière, interrupteur. Rien ne bascule pendant une période que le plan déclare à éviter.*

| Élément | Contenu |
|---|---|
| Jour et heure `[H]` | |
| Ordre des étapes | |
| Actions du jour | `A-xx`, dont la sauvegarde datée de la veille |
| Version mise en service | |
| Retour arrière | signal · qui le déclenche · comment · comment on vérifie que l'ancienne méthode a repris |
| Lectures du premier jour | qui · à quelle heure · quoi |
| Seuils d'arrêt en vigueur | `IND-xx` · seuil (60-specification §14, cité) |
| Ancienne méthode | conservée jusqu'à la sortie de la surveillance renforcée : date |
| Communication | `A-xx` |

Décision : bascule · pas de bascule — décideur (rôle), date.

## 7. Adoption
*La conduite du changement. Les six questions viennent de 70-plan §4 : on les cite par leur numéro et on y ajoute ce qui est fait, on ne recopie pas les
réponses du plan. L'adoption se compte en occurrences passées par le dispositif, par rôle.*

**Impact par rôle**

| Rôle | Ce qui change | Ce qui disparaît | Ce qui reste | Formation ou guide (forme · quand) | Qui approuve ce changement | Vérifié par un essai sans le consultant |
|---|---|---|---|---|---|---|
| | | | | | | |

*Approbations : le responsable d'équipe et la direction concernée. Si le dispositif touche des données personnelles, l'organisation du travail ou des conditions
de travail, la question est posée au rôle compétent de l'entreprise (conformité, juridique, représentation du personnel) : le pack écrit la question, le rôle
et la réponse reçue, il ne conclut pas.*

**Les six questions d'adoption**

| # | Réponse du plan (renvoi) | Fait le | Pièce | Reste |
|---|---|---|---|---|
| 1 | Qui reprend, avec quelle autonomie (70 §4, 1) | | | |
| 2 | Gestes à savoir faire sans le consultant (70 §4, 2) | | | |
| 3 | Formation, guide, documentation par rôle (70 §4, 3) | | | |
| 4 | Accès, propriétaires de comptes, procédures de secours (70 §4, 4) | | | |
| 5 | Comment on a vérifié que l'équipe sait corriger une erreur courante (70 §4, 5) | | | |
| 6 | Support après la transmission et nouvelle mission (70 §4, 6) | | | |

**Formation et communication** — *chaque message envoyé ou publié est une action : le pack le rédige, un rôle du client l'envoie après validation.*

| Public | Message ou formation | Canal | Moment `[H]` | `A-xx` | Fait le · pièce |
|---|---|---|---|---|---|
| | | | | | |

Support de transition : qui répond, jusqu'au …, pour quoi ; ce qui relève d'une nouvelle mission : …

## 8. Exploitation et transfert
*Le mode opératoire est la fiche d'exploitation de 80-construction (`80-construction/fiche-exploitation.md`, révision lue) : il n'existe qu'à cet endroit.
Ici on vérifie qu'elle répond aux quatre questions et qu'un tiers l'a déroulée. Une lacune se corrige dans la fiche par une révision datée (ligne
« correction » au journal), et la rubrique 10 de 80-construction cite la nouvelle révision.*

| Question du mode opératoire | Réponse (fiche d'exploitation de 80, rubrique 1 à 4) | Déroulé par (rôle, autre que l'auteur) le | Lacune → révision de la fiche (numéro) |
|---|---|---|---|
| Comment vérifier que ça marche ? (quoi regarder, où, quand, résultat attendu) | | | |
| Que faire en cas d'incident ? (par symptôme : première action, qui prévenir, quand suspendre) | | | |
| Qui joindre ? (rôles, suppléants, escalade) | | | |
| Comment revenir en arrière ? (interrupteur, version précédente, ancienne méthode) | | | |

Accès et comptes : liste relue le …, comptes de l'entreprise, aucun compte personnel. Secrets : noms et endroits (60-specification §9), jamais leur valeur. Version en service : …

| Rôle | Tenu par (rôle) | Suppléant (rôle) | Accepté par écrit le |
|---|---|---|---|
| Propriétaire (décide des règles, détient les comptes) | | | |
| Exploitant (maintenance courante, 60-specification §17) | | | |

Revues datées : accès (…), coût de fonctionnement (…), plan avant toute échéance externe (…). La mise en service ne clôt pas le cas : la clôture vient après la mesure.

## 9. Ce que reçoit la mesure

| Élément | Contenu |
|---|---|
| Début de la période de mesure | date de la bascule |
| Versions en service | liste datée, tirée du registre |
| Changements depuis le feu vert | `A-xx`, ou « aucun » ; incidents datés (changements faits hors registre) ; mesures d'attente en vigueur |
| Hypothèses de 50-rentabilite restées ouvertes | |
| Relevés à fournir | indicateur · rôle · rythme · dépôt (70-plan §6) |

## Décision attendue
Valider les actions proposées (liste d'identifiants) avant leur exécution ; décider la prochaine porte (feu vert du pilote, fin du pilote ou bascule) — ou la corriger ;
accepter le transfert (exploitant, propriétaire et suppléants nommés).
```

## B. Fiche d'une action

À écrire pour toute action qui n'est pas triviale (réversible en un geste, sans effet externe) : un tiers doit pouvoir la faire sans la personne qui l'a écrite.

```markdown
### A-xx — <action>
Prérequis : <A-xx faites, T-xx passés, décisions du journal> · Exécutée par : <rôle du client> · Durée prévue `[H]` : …
Pas à pas : 1. … 2. … (trois à sept gestes, chacun vérifiable)
Effet attendu : ce qu'on doit constater après, et où.
Si ça se passe mal — signal : … · retour arrière pas à pas : 1. … · temps mesuré à l'essai `[F]` : … · comment on vérifie que l'état d'avant est revenu : …
Aucun retour arrière (action non réversible) : ce qui limite les dégâts — plafond, premier lot, simulation faite le … (T-xx), correctif possible : …
Secrets : nom, endroit, propriétaire (jamais la valeur).
```

## C. Lignes de journal

Une par décision du client : une validation (une ou plusieurs actions, même valideur, même jour), le feu vert, la fin du pilote, la bascule, le transfert. Un retour arrière
exécuté, un incident (changement fait hors registre) et un verdict relu s'écrivent aussi :

```markdown
- 2026-11-12 · cas-saisie-commandes · A-01 à A-04 validées par la direction des opérations · « compte de service, droits en lecture, sauvegarde, import de la version 1.0 inactive ; retour arrière prêt et essayé pour chacune »
- 2026-11-16 · cas-saisie-commandes · feu vert du pilote donné par la direction commerciale · « une réserve acceptée (D-04) ; une équipe, mode parallèle le premier jour »
- 2026-11-23 · cas-saisie-commandes · incident : règle de relance modifiée dans l'outil par le responsable des opérations, hors registre · « effet constaté le jour même ; suite proposée en A-06 (garder ou défaire), validée avant d'être faite ; test T-12 rejoué par tester-solution »
- 2026-12-02 · cas-saisie-commandes · retour arrière de A-08 exécuté par le responsable des opérations · « signal : alerte non traitée à 12 h ; ancienne méthode reprise le jour même, vérifiée au soir »
- 2026-12-09 · cas-saisie-commandes · fin du pilote : continuer, décidé par la direction commerciale · « critères de la fiche signée atteints, relevé joint »
- 2026-12-14 · cas-saisie-commandes · bascule faite · « sauvegarde du vendredi jointe ; surveillance renforcée jusqu'au 2027-01-15 »
- 2027-01-11 · cas-saisie-commandes · verdict relu : pas prêt pour la version en service (D-09, bloquant) · « A-12 et A-13 (mesures d'attente) validées par le responsable des opérations ; correction à recetter par tester-solution »
- 2026-12-15 · cas-saisie-commandes · transmission acceptée par le propriétaire et l'exploitante · « mode opératoire déroulé par la suppléante ; support de l'indépendant jusqu'au 2027-01-13 »
```

## D. Pièges fréquents et test du lecteur froid

| Piège | Comment le repérer | Correction |
|---|---|---|
| Validation en bloc | une ligne de journal « on lance » sans identifiant d'action | une validation par action, ou une liste d'identifiants |
| Retour arrière imaginé, jamais essayé | « on réimporte l'ancienne version » sans temps mesuré | l'essayer sur copie ou en environnement d'essai ; sinon l'action n'est pas validable |
| Effet externe sans plafond | « envoyer les confirmations » | public, nombre au plus, période, premier lot réduit |
| Activation à l'import | l'import lance une exécution sur le stock | importer inactif, activer par une action séparée |
| Secret dans le dossier | une clé ou un jeton dans un message, une capture, une pièce | le retirer, faire changer le secret ; le dossier ne garde que son nom |
| Compte personnel | le dispositif tourne avec l'accès d'une personne | compte de service, droits minimaux |
| Critères du pilote ajustés en route | le seuil bouge après la première semaine | critères signés avant ; un jour où une règle change ne compte pas |
| Ancienne voie retirée trop tôt | plus de repli le jour de la bascule | la garder jusqu'à la sortie de la surveillance renforcée |
| Formation sans essai | « formés » veut dire invités à une réunion | essai sans le consultant (70 §4, 5), fait par chaque rôle concerné |
| Mode opératoire écrit et relu par son seul auteur | aucun tiers ne l'a déroulé | un tiers le suit ; chaque question qu'il pose est une correction |
| Transfert par envoi de document | aucun accusé de réception | acceptation écrite de l'exploitant et du propriétaire |
| Changement hors registre | version en service différente de la version validée | incident daté au journal, suite proposée en `A-xx` nouvelle et validée avant d'être faite ; signalé à `mesurer-gains` |
| Défaut bloquant laissé en service | le flux tourne pendant que `D-xx` est ouvert, sans mesure écrite | mesures d'attente (`A-xx`) validées ; verdict relu au journal jusqu'à la correction recettée |
| Donnée personnelle dans les relevés | export brut déposé dans `mission/sources/` | agréger ou anonymiser avant dépôt |
| Clôture à la bascule | « terminé » écrit le jour J | le cas reste ouvert jusqu'à la mesure |

**Test du lecteur froid.** Donner à quelqu'un qui n'a pas écrit la fiche d'action, le mode opératoire ou le tableau d'adoption la seule page concernée, et lui demander de
dérouler : faire l'action (sur la copie ou en essai), vérifier que ça marche, réagir à un incident choisi, joindre la bonne personne, revenir en arrière. Chaque question
qu'il pose est une rubrique à compléter ; chaque geste qu'il ne sait pas faire est une action à reformuler. Si personne n'est disponible pour jouer ce rôle, l'écrire en rubrique 8
et marquer le mode opératoire « non essayé » : le feu vert du pilote ne se donne pas sur un mode opératoire non essayé sans une condition écrite.
