# Modèles — exigences et spécification

À ouvrir pour rédiger : la partie A pour `30-exigences.md`, la partie B pour `60-specification.md`.
Les titres et numéros de rubrique sont ceux des squelettes de `SKILL.md`. Les chiffres des exemples
sont fictifs (« exemple de calcul »). Les phrases en italique sous un titre sont des consignes de
remplissage : elles disparaissent du document rendu.

Règles communes de remplissage :

- Chaque nombre porte son statut : `[F]` fait observé avec sa source, `[H]` hypothèse avec la personne
  qui peut la confirmer, `[E]` estimation calculée. Un nombre sans statut est une erreur.
- Des rôles, jamais des noms de personnes. Aucune donnée personnelle dans le document.
- Une phrase, une exigence : un « et » peut cacher deux exigences.
- Identifiants : `EF-01` (fonctionnelle), `ENF-01` (non fonctionnelle), `CA-01` (critère d'acceptation),
  `T-01` (test), `R-01` (risque). Tout renvoie à l'identifiant, jamais à « la ligne du dessus ».
- Définir chaque sigle à sa première occurrence.

## A. Mode exigences — modèle de `mission/cas-<slug>/30-exigences.md`

Si le document doit être transmis à des prestataires, c'est le client qui le transmet, après avoir
retiré ce qu'il ne veut pas partager (budget, volumes exacts, noms de clients). Le pack n'envoie rien.

```markdown
# Exigences — <titre court>

Date · Demandeur (rôle) · Rédigé par · Version
Écrit pour être lu par quelqu'un qui n'a pas vécu la mission : prestataire ou équipe interne.

## 1. Contexte et objectifs
*Le problème en trois à cinq lignes (renvoi : 10-besoin), l'état actuel mesuré (renvoi :
20-diagnostic), la décision que ces exigences servent. Les objectifs sont des résultats attendus, pas
des fonctions ; chacun avec sa mesure de départ et son statut, ou « à mesurer avant tout lancement ».*

## 2. Utilisateurs et rôles
*Qui utilise, qui valide, qui est touché sans utiliser (destinataires), qui administre.*

| Rôle | Ce qu'il fait avec le dispositif | Nombre de personnes | Accès nécessaire |
|---|---|---|---|

## 3. Processus cible
*Le processus tel qu'il doit se dérouler, en étapes numérotées, en mots, sans nom d'outil ni de
technique. Pour chaque étape : ce qui la déclenche, ce qui en sort, qui décide. Marquer « [humain] »
les étapes où une personne juge ou valide, sans dire comment.*

## 4. Exigences fonctionnelles
*Priorité : sans cette exigence, le dispositif règle-t-il encore le problème de 10-besoin ? Non →
Indispensable. Le cœur marche mais l'usage en souffre → Important. Confort → Souhaitable.*

| ID | Exigence (« Le dispositif doit… ») | Priorité | Pourquoi (lien avec le besoin) | Source |
|---|---|---|---|---|
| EF-01 | | Indispensable | | 10-besoin |

## 5. Données
*Statut : brute (telle que reçue), enrichie (complétée par un calcul, un modèle d'IA ou une source
externe), validée (confirmée par une personne ou une règle écrite). Une donnée produite par un calcul
ou un modèle reste enrichie tant qu'une validation ne l'a pas confirmée. Seuil de qualité : ce qui
rend la donnée inutilisable (champ vide, doublon, format, âge maximal), avec le taux toléré.*

| Donnée | Système source | Champs indispensables | Seuil de qualité | Statut | Source qui tranche en cas de conflit | Personnelle ? |
|---|---|---|---|---|---|---|

**Exclusions** — *catégories, périmètres ou périodes que le dispositif ne doit pas traiter.*

**Volumes** — *par mois, en pointe, croissance attendue, chacun avec son statut.*

**Données personnelles** — *lesquelles, pour quelle finalité, conservées combien de temps, et ce que
le responsable de la conformité doit confirmer `[H]`. Le pack ne conclut pas sur la conformité.*

## 6. Intégrations
*Nommer un système en place est un fait d'environnement, pas un choix de solution. Un accès qui
n'existe pas encore devient une question ouverte et pèse sur le délai.*

| Système | Lire / écrire | Ce qui est lu ou modifié | Accès aujourd'hui (oui · non · à demander à <rôle>) | Limites connues |
|---|---|---|---|---|

## 7. Exigences non fonctionnelles
*Domaines à parcourir : sécurité (qui voit quoi, ce qui ne quitte pas l'entreprise) · conformité
(RGPD ou règle locale équivalente : finalité, minimisation, durée de conservation, droits des
personnes) · disponibilité (plages, reprise acceptable) · délai de traitement (du déclencheur à la
sortie) · traçabilité (quoi, qui, quand, conservé combien de temps) · points de validation humaine
(quelles actions, quel rôle, délai maximal) · politique d'erreur (où va un cas qui ne peut pas être
traité, qui le voit, en combien de temps).*

| ID | Domaine | Exigence | Preuve ou mesure |
|---|---|---|---|
| ENF-01 | Sécurité | | |

## 8. Contraintes
*Budget (enveloppe, et ce qu'elle couvre : pilote, première phase, production) · calendrier (date
butoir et sa cause) · outils imposés (et pourquoi) · autres (équipe disponible, période de gel,
langue). Chaque contrainte : ferme ou négociable, et qui peut la lever.*

## 9. Critères d'acceptation
*Au moins un critère par exigence Indispensable. Couvrir le cas nominal, l'erreur, le cas limite et ce
qui ne doit pas arriver. Bannir « rapide », « simple », « intuitif », « fiable » sans seuil.*

| ID | Exigence | Critère (Donné / Quand / Alors, ou seuil mesurable) | Données et méthode de vérification |
|---|---|---|---|
| CA-01 | EF-01 | | |

## 10. Indicateurs
*Type : activité (volume traité), qualité (erreurs, reprises), conversion (passage à l'étape suivante),
résultat (temps, argent, satisfaction). Prévoir au moins un indicateur de résultat et un de qualité :
l'activité seule montre qu'on s'agite, pas qu'on a gagné. Départ : la mesure avant dispositif, son
statut, et la période sur laquelle elle est fiable (par exemple depuis le changement du système source).
Attribution : écrire « a contribué à » tant qu'il n'y a ni période comparable ni groupe témoin ; sinon
nommer la comparaison (même période de l'an passé, équipe pilote contre équipe témoin).*

| Indicateur | Type | Décision qu'il permet | Départ et période fiable | Lecture · responsable de la donnée | Seuils : correction · alerte · arrêt | Attribution |
|---|---|---|---|---|---|---|

## 11. Hors périmètre

| Hors périmètre | Raison | Peut revenir ? |
|---|---|---|

## 12. Questions ouvertes
*N'y mettre que ce que le dossier ne permet pas de trancher.*

| ? | Question | Rôle qui répond | Bloquante pour le choix d'une solution ? | Échéance |
|---|---|---|---|---|

## Décision attendue
Valider les exigences et leurs priorités — ou les corriger ; lever les questions bloquantes ; autoriser
la comparaison des solutions (`concevoir-solution`) ou la consultation de prestataires.
```

Exemple de lignes d'indicateurs (exemple de calcul, chiffres fictifs) :

| Indicateur | Type | Décision qu'il permet | Départ et période fiable | Lecture · responsable | Seuils : correction · alerte · arrêt | Attribution |
|---|---|---|---|---|---|---|
| Délai entre l'échéance d'une facture et la première relance | résultat | étendre ou non à d'autres entités | 9 jours `[F]`, export des six derniers mois ; fiable depuis le changement du système de facturation | chaque semaine · responsable des créances clients | correction : plus de 5 jours deux semaines de suite ; alerte : plus de 9 jours ; arrêt : plus de 15 jours | comparaison avec une entité témoin non concernée, sur la même période ; sinon « a contribué à » |
| Relances envoyées à tort (facture déjà payée ou contestée) | qualité | resserrer les règles ou arrêter | à relever avant tout lancement `[H]`, responsable des créances clients | chaque jour pendant le pilote · même rôle | alerte : un cas ; arrêt : deux cas dans la semaine | sans objet : tout cas est un défaut |

## B. Mode spécification — modèle de `mission/cas-<slug>/60-specification.md`

La spécification décrit l'option retenue dans `40-solutions`. Elle ne rouvre pas le choix ; si
l'écrire fait apparaître que l'option ne tient pas, le dire au décideur et revenir à
`concevoir-solution`.

```markdown
# Spécification — <titre court>

Date · Option retenue (40-solutions, décision du <date>) · Rédigé par · Version
Pour l'équipe qui construit. Écrit pour être suivi sans avoir assisté à la mission.

## 1. Problème et objectif
*Le problème en deux phrases (renvoi : 10-besoin), l'option retenue et pourquoi (renvoi :
40-solutions), le gain estimé et ses hypothèses (renvoi : 50-rentabilite). L'objectif est un résultat
observable, pas une fonction. Si l'option est imposée, l'écrire ici.*

## 2. Non-objectifs
*Ce que cette version ne fait pas, avec la raison (impact insuffisant, trop complexe, autre chantier,
prématuré). Reprend le hors-périmètre de 30-exigences et ajoute ce que l'option retenue exclut.*

## 3. Utilisateurs et scénarios
*« En tant que <rôle>, je veux <capacité>, afin de <bénéfice>. » Par rôle, du plus important au moins
important ; inclure les erreurs, les cas vides, les cas limites. Chaque scénario porte les EF qu'il
couvre. Il décrit un besoin, pas un bouton.*

## 4. Comportement étape par étape
*Une ligne par étape, dans l'ordre. Une étape qui écrit chez un tiers, envoie, paie, supprime ou publie
suit la validation humaine décidée dans 40-solutions ; sans décision contraire écrite, validation par
défaut. Aucune étape sans chemin d'erreur : la dernière colonne renvoie au §7. Si un élément change
d'état (à traiter, en attente de validation, traité, en échec, rejoué), lister les états et les
transitions.*

| N° | Déclencheur ou entrée | Ce que fait le dispositif | Sortie | Validation humaine (rôle · délai maximal) | Si l'étape échoue |
|---|---|---|---|---|---|

*Si une étape confie un jugement à un modèle d'IA, ajouter : son rôle (ce qu'il peut faire, ce qu'il ne
peut pas faire) ; le format de ce qu'il reçoit et de ce qu'il rend ; le seuil de confiance sous lequel
un humain prend la main ; le jeu d'exemples réels qui sert à le vérifier et le taux d'erreur toléré
`[H]` ; la version de ses consignes, notée à chaque changement ; pour un agent, la liste fermée des
actions permises, un plafond d'étapes et de coût par exécution, aucune action irréversible sans
validation.*

**Traçabilité** — *une exigence Indispensable sans étape est un manque, une étape sans exigence est
une dérive.*

| EF | Étape(s) | Test(s) |
|---|---|---|

## 5. Flux de données
*Reprend les données de 30-exigences §5. Dire à chaque point si la donnée est brute, enrichie ou
validée, et ce qui ne doit jamais quitter l'entreprise (notamment vers un service tiers ou un modèle).*

| Donnée | Origine | Traitement | Stockage et durée | Qui y accède | Sort-elle de l'entreprise ? |
|---|---|---|---|---|---|

## 6. Intégrations et droits
*Moindre privilège : lecture seule partout où l'écriture n'est pas indispensable, portée limitée aux
objets concernés. Jamais un compte personnel : le jour où la personne part ou change de mot de passe,
tout s'arrête.*

| Système | Compte utilisé (de service) | Droits demandés | Droits strictement nécessaires | Propriétaire du compte |
|---|---|---|---|---|

## 7. Gestion des erreurs
*Chaque étape du §4 renvoie ici : aucun chemin d'erreur laissé à l'improvisation.*

| Type | Exemples | Comportement exigé |
|---|---|---|
| Passagère | délai dépassé, service surchargé, limite de débit | reprises avec un délai qui s'allonge (et varie un peu), nombre maximal de reprises et durée totale fixés ; au-delà, file des échecs |
| Définitive | donnée invalide, droit refusé, élément introuvable | aucune reprise (elle retarderait l'alerte) ; file des échecs et alerte immédiate |

*File des échecs : durable, consultable, rejouable ; chaque entrée garde la donnée utile, l'erreur et
l'horodatage ; durée de conservation limitée si elle contient des données personnelles ; qui la vide et
à quel rythme.*

*Alerte : destinataire désigné par son rôle (et un suppléant), canal, contenu minimal, délai maximal.*

*Interrupteur d'arrêt : où il se trouve, qui peut l'actionner, ce qu'il fait des éléments en cours,
procédure manuelle de repli (la méthode d'avant).*

*Plafonds : traitements simultanés, cadence, volume maximal par exécution ; protection contre les
boucles (un traitement qui en redéclenche un autre qui le redéclenche).*

## 8. Dédoublonnage
*Toute écriture dont la répétition fait du mal (envoi d'un message, paiement, création d'un
enregistrement, émission d'un document) : une clé stable — identifiant de l'événement ou identifiant
externe, jamais un horodatage ni une empreinte approximative — vérifiée avant d'écrire, enregistrée
après la réussite. Raison : un même événement peut arriver plusieurs fois (renvoi par la source,
reprise, double clic). Préférer l'écriture par clé (mise à jour) à l'insertion aveugle.*

| Écriture non répétable | Clé stable | Où la clé est vérifiée, où elle est enregistrée |
|---|---|---|

## 9. Secrets
*Dans le coffre de l'outil, référencés par leur nom ; jamais en clair dans un flux, une exportation,
une capture, ni dans ce document. Le document nomme les secrets, jamais leur valeur.*

| Secret (nom) | Ce qu'il permet | Où il est conservé | Propriétaire | Échéance ou rotation |
|---|---|---|---|---|

## 10. Observabilité
*Journal : quoi (identifiant de l'élément, étape, résultat, horodatage ; pas de donnée personnelle
au-delà du nécessaire), conservé combien de temps, lisible par qui. Compteurs : réussites et échecs par
exécution et par jour. Alertes : sur échec et sur silence — pour toute tâche planifiée, une alerte si
l'exécution attendue n'a pas eu lieu dans sa fenêtre, parce qu'une tâche qui ne se lance plus ne
produit aucune erreur. Destinataire : un rôle nommé. Revue : qui lit le journal, à quel rythme.*

## 11. Environnements et versions
*Un environnement de test séparé de la production, avec des données fictives ou anonymisées ; une
sauvegarde (export ou instantané) avant toute modification du dispositif en production ; une version
numérotée à chaque changement ; un retour arrière : version précédente connue et temps nécessaire
pour y revenir.*

## 12. Plan de test et recette
*Couvrir : le nominal ; chaque chemin d'erreur (passagère, définitive) ; les cas limites ; ce qui ne
doit pas arriver ; le même événement reçu deux fois ; la reprise après panne ; la pointe de volume ;
l'arrêt d'urgence. Si le dispositif comprend un modèle d'IA : le jeu d'exemples et le taux d'erreur
mesuré.*

| ID | Exigence ou étape couverte | Scénario | Données | Résultat attendu | Environnement |
|---|---|---|---|---|---|
| T-01 | | | | | |

**Cas limite critique** — *le cas qui ferait le plus de mal s'il était mal traité, identifié avec le
responsable métier à partir de 20-diagnostic. Il a son test nommé, et la recette échoue sans lui.*

**Recette** — *qui la prononce (un rôle métier, pas le constructeur), sur quelles données, avec quels
critères (30-exigences §9).*

## 13. Pilote
*Périmètre réduit (qui, quoi, combien), durée, mode (en parallèle de la méthode actuelle, rien n'étant
envoyé ; ou en préparation avec validation systématique), mesures relevées, critères de généralisation,
de prolongation et d'arrêt écrits à l'avance, et qui décide. Le calendrier et l'accompagnement sont
dans 70-plan (`planifier-deploiement`).*

## 14. Indicateurs
*Reprend le tableau de 30-exigences §10 et fixe le protocole : source de la mesure, méthode, périodicité,
qui mesure (l'entreprise, pas le pack), mesure de départ à relever avant le pilote. Un gain reste
« estimé » tant qu'il n'est pas observé.*

## 15. Risques

| ID | Risque | Probabilité `[H]` | Impact | Parade | Signal d'alerte |
|---|---|---|---|---|---|
| R-01 | | | | | |

## 16. Questions ouvertes

| ? | Question | Rôle qui répond | Bloquante avant construction ? |
|---|---|---|---|

## 17. Propriétaire de la maintenance
*Un rôle (et un suppléant), une fiche d'une page : ce que fait le dispositif, ses dépendances, comment
le mettre en pause, comment rejouer la file des échecs. Rythme de revue (échéance des accès,
changements des systèmes reliés), comment un changement est demandé, testé, déployé. Temps de
maintenance attendu par mois `[H]`, cohérent avec 50-rentabilite.*

## Décision attendue
Valider la spécification comme entrée de l'équipe qui construit — ou la corriger ; lever les questions
bloquantes ; nommer le propriétaire de la maintenance.
```

## C. Les trois tests de relecture

- **Test de la solution nommée (exigences).** Chercher dans le document les noms d'outils, de produits,
  de techniques. Chacun est-il un système en place (rubrique 6) ou un outil imposé (rubrique 8) ? Sinon,
  réécrire en fonction attendue. Puis : si un prestataire proposait une autre technique, ce document
  permettrait-il de la juger ?
- **Test du prestataire (exigences).** Un prestataire qui n'a pas assisté à la mission pourrait-il
  chiffrer ? Noter chaque question bloquante qu'il poserait (volumes, accès, données, qui valide, que
  faire en cas d'erreur) : chacune désigne une rubrique à compléter.
- **Test du constructeur (spécification).** Imaginer une équipe qui ne verra jamais le client et lui
  faire poser ses questions : que se passe-t-il quand… ? qui valide… ? où est la donnée… ? que se
  passe-t-il si le même élément arrive deux fois ? comment l'arrête-t-on ? comment sait-on que ça a
  tourné cette nuit ? Une question sans réponse dans le document est une rubrique à compléter ou une
  question ouverte bloquante.

## D. Pièges fréquents

| Piège | Comment le repérer | Correction |
|---|---|---|
| Exigence qui est une solution | un nom d'outil ou de technique dans une exigence | réécrire en fonction attendue ; l'outil va en Contraintes s'il est imposé |
| Tout est indispensable | presque aucune ligne n'est Important ou Souhaitable | demander au demandeur ce qu'il accepterait de livrer en premier |
| Critère non testable | un adjectif sans seuil | un seuil, un cas, une méthode de vérification |
| Indicateur sans décision | la colonne « décision » est vide | supprimer l'indicateur ou trouver la décision qu'il éclaire |
| Gain attribué à tort | comparaison avant / après sur des périodes non comparables | même période de l'an passé, groupe témoin ; sinon « a contribué à » |
| Spécification sans chemin d'erreur | la rubrique 7 se réduit à « gérer les erreurs » | distinguer passagère et définitive, file des échecs, alerte, arrêt |
| Secret dans le document | une clé, un mot de passe, un jeton | le retirer, ne garder que son nom ; le faire changer s'il a circulé |
| Compte personnel | le dispositif tourne avec l'accès d'une personne | compte de service, droits minimaux |
| Pilote sans seuil d'arrêt | « on verra » | critères de généralisation, de prolongation et d'arrêt écrits à l'avance |
| Maintenance sans propriétaire | « l'équipe informatique » | un rôle, un suppléant, une fiche d'une page |
