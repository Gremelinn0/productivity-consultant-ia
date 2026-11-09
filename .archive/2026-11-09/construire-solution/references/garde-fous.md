# Garde-fous, plateformes et données d'essai — le détail de la construction

À ouvrir à l'étape 2 (partie 6, modèle existant), à l'étape 3 (partie 3, essai et données), à l'étape 4
(parties 1 et 5, contrat commun et méthode de repli), à l'étape 6 (parties 2 et 4, garde-fous et étape d'IA)
et à l'étape 9 (partie 7, balayage de la livraison). Le principe de chaque point est dans `SKILL.md`.

Statut des contenus : les exemples sont fictifs ; les noms de plateformes sont des catégories (flux sans code,
scénario, script, agent, serveur d'outils), pas une liste à jour du marché ; ce qu'une plateforme sait faire se
lit dans son outil à la date de la construction, sinon c'est `[H]`.

## 1. Le contrat commun à toute plateforme

Huit règles, les mêmes pour un flux sans code, un scénario, un script, un agent ou un serveur d'outils. Un
compagnon (`COMPAGNONS.md`) ou la méthode de repli (partie 5) les applique à son outil ; il n'en change aucune.

| Règle | Ce que cela veut dire | Comment on le prouve |
|---|---|---|
| Versions fixées | plateforme, connecteurs ou composants, bibliothèques, modèle d'IA : une version ou un identifiant relu, jamais « la dernière » | rubrique 4 de `80-construction.md` remplie avec la date de lecture ; les versions figurent dans l'export |
| Identifiants réels relus dans l'outil | identifiants de flux, de connexions, de tableaux, de dossiers, noms de champs : lus dans l'outil au moment de construire, jamais déduits d'une documentation, d'un exemple ou d'un autre environnement | une date de lecture par identifiant ; un identifiant introuvable est un écart, pas une invention |
| Secrets dans le coffre de la plateforme | le flux ne connaît que le nom d'un secret ; la valeur reste chez le client | balayage de la livraison (partie 7) |
| Simulation ou environnement isolé | aucun effet externe réel possible depuis l'essai | essai d'isolement ; sortie simulée présente, effet réel absent |
| Changements relus avant d'être appliqués | avant de modifier un flux, un tableau ou des règles, lire ce qui va changer (différence entre l'ancienne et la nouvelle version) ; pour une modification en masse, commencer par un seul élément | la différence relue est notée dans `journal-versions.md` |
| Autorisation avant tout effet externe | importer en production, activer, envoyer, écrire chez un tiers, publier : action proposée en 90 et faite après validation ; dans l'essai, seulement vers des cibles de test | aucune action hors essai dans le journal d'exécution ; liste « ce qui reste au client » (rubrique 10) |
| État enregistré relu après chaque écriture | après avoir écrit (brouillon, ligne, fichier, enregistrement), relire l'objet réellement stocké et le comparer à l'intention ; un code de retour « OK » n'est pas l'état | contrôle de tranche qui relit ; le test « lecture après écriture » de 85 |
| Sauvegarde et retour arrière définis avant la mise en service | export de ce qui sera modifié, version précédente connue, durée du retour | retour arrière essayé une fois dans l'essai, durée `[F]` relevée |

Une plateforme choisie par `concevoir-solution` ne se remplace pas pendant la construction : si elle ne sait pas
faire ce que `60-specification` exige, c'est un écart (rubrique 8), la tranche s'arrête et le décideur tranche.

## 2. Les garde-fous de la spécification, un par un

Pour chacun : ce qu'on construit, puis ce qu'on contrôle. Les valeurs (délais, plafonds, noms) viennent de
`60-specification` §7 à §11 ; on ne les invente pas ici.

**Simulation des envois.** À chaque effet externe (envoyer, écrire chez un tiers, publier, payer), un aiguillage :
en simulation, l'effet est écrit dans un lieu de preuve (fichier, onglet, boîte de test) et journalisé ; en réel,
il agit. Dans l'essai, la connexion réelle n'existe pas. *Contrôle* : lancer un traitement ; la sortie simulée est
présente, l'effet réel est absent côté cible, le journal dit « simulé ». Le passage au réel est une action de 90.

**Dédoublonnage.** La clé est celle de `60-specification` §8, stable (jamais un horodatage). Avant l'écriture non
répétable : chercher la clé ; présente, ne rien écrire et journaliser « déjà fait ». Après la réussite : l'enregistrer.
Reste le trou entre l'écriture et l'enregistrement. Si le traitement s'arrête juste après l'écriture, la clé n'existe
pas et le rejeu écrit une seconde fois ; si on enregistre la clé avant d'écrire, un arrêt juste après perd l'élément
sans bruit. Parade : écrire par clé (mise à jour plutôt qu'insertion) quand l'outil le permet, sinon noter
l'intention (« en cours ») avant d'agir, la confirmer après, et à la reprise relire l'état réellement enregistré pour
réconcilier : l'objet existe, on confirme ; il n'existe pas, on l'écrit. *Contrôle* : lancer deux fois ; arrêter le
traitement juste avant puis juste après l'écriture, relancer : une seule écriture à la fin, aucun élément perdu.

**Journal d'exécution.** Une ligne par élément et par étape : clé, étape, résultat, horodatage, version du
dispositif et des règles ; aucune donnée personnelle au-delà du nécessaire (`60-specification` §10). Des compteurs
par exécution. *Contrôle* : à partir du seul journal d'un rejeu, reconstituer le sort d'un élément précis.

**Erreurs et reprise.** Passagère (délai dépassé, service surchargé, limite de débit) : reprises espacées, délai qui
s'allonge avec un peu de variation, nombre et durée maximums, puis file des échecs. Définitive (donnée invalide,
droit refusé, élément introuvable) : aucune reprise, qui retarderait l'alerte ; file des échecs et alerte. La file
est durable, consultable, rejouable, sans donnée inutile. Un élément qui échoue n'arrête pas les autres : l'état
reste cohérent et reprenable (traitement partiel). *Contrôle* : provoquer une erreur de chaque type, un délai
dépassé, un lot interrompu à moitié ; vérifier file, alerte, reprise sans doublon.

**Interrupteur, verrou, plafonds.** Un interrupteur lu avant chaque étape ; suspendu, rien de neuf n'est créé et
ce qui est en cours est traité comme `60-specification` §7 le dit. Un verrou : une seule exécution à la fois.
Plafonds de volume, de cadence, d'étapes, de coût ; protection contre les boucles (un traitement qui en redéclenche
un autre qui le redéclenche). *Contrôle* : cocher l'interrupteur en cours d'exécution ; dépasser un plafond ;
lancer deux exécutions ensemble.

**Secrets.** Références par nom vers le coffre de la plateforme, ou variable d'environnement du poste du client
pour un script. *Contrôle* : balayage de la livraison, des journaux, des sorties simulées et des captures (partie 7).

**Moindre privilège.** Les comptes d'essai ont les droits « strictement nécessaires » de `60-specification` §6, pas
plus, même « pour tester ». *Contrôle* : lister les droits réellement accordés et les comparer au tableau de §6 ;
tenter une action interdite.

**Sauvegarde, versions, retour arrière.** Export avant toute modification ; version numérotée ; version précédente
restaurée une fois dans l'essai et un contrôle relancé dessus. *Contrôle* : la durée du retour est relevée `[F]` et
inscrite à la fiche d'exploitation.

**Observabilité et alerte sur silence.** Les alertes de `60-specification` §10 sont construites avec des
destinataires de test : échec, silence (une exécution attendue qui n'a pas eu lieu dans sa fenêtre), liste vide
suspecte, double envoi, volume anormal. *Contrôle* : provoquer chacune et voir arriver le message au bon rôle.

**Règles qui changent (processus instable).** Seuils, délais, modèles sont des données datées, lues au début de
chaque exécution ; l'exécution note la version des règles appliquées et garde celles du début jusqu'à sa fin. Une
règle modifiée sans mise à jour du dispositif lève une alerte. *Contrôle* : modifier une règle en cours
d'exécution ; l'exécution en cours ne bouge pas, la suivante applique la nouvelle version.

**Changement non approuvé.** La version approuvée a une empreinte ; qui peut modifier le flux, les règles ou les
consignes est limité (`60-specification` §17) ; la fiche dit comment comparer ce qui tourne à la version approuvée.
*Contrôle* : modifier un modèle de message hors procédure ; la différence est visible ou la modification refusée.

## 3. L'environnement d'essai et les données

**Nommer et isoler.** Le nom (`essai-<slug>`) est donné une fois. L'essai a ses comptes (de service, jamais
personnels), ses connexions de test créées par le client, ses cibles de test (classeur, boîte de messagerie,
dossier). Il ne contient aucun secret de production. L'isolement se prouve : un accès de test à la production
échoue ; une exécution en simulation produit une sortie simulée.

**Si la plateforme n'offre aucun espace séparé.** L'essai est alors un espace nommé et marqué à l'intérieur de
l'instance de production : tout y est désactivé par défaut, les cibles sont des cibles de test, aucune connexion
d'envoi n'y est créée. Le dire en tête de `80-construction.md` comme un risque, avec l'accord du décideur, et
reporter à `90-mise-en-service` toute activation.

**Données fictives.** À préférer. Elles reproduisent la structure et les proportions d'une situation observée
(par exemple les 61 factures d'une séance) et les cas limites : valeurs vides, très longues, caractères spéciaux,
dates de fin de mois, jours fériés, changement d'heure, doublons, éléments hors périmètre. Un nom de client ou une
adresse inventés ne désignent personne ; on vérifie qu'ils ne coïncident pas avec un vrai. Les adresses
électroniques fictives utilisent un domaine réservé aux exemples (par exemple `example.com`, ou le suffixe
`.invalid`) : aucun message ne peut alors arriver chez quelqu'un, même si une simulation échoue.

**Données anonymisées.** Seulement quand la forme réelle compte. Le client anonymise, ou le fait avec le pack :
suppression ou remplacement des noms, adresses, numéros, identifiants ; généralisation des valeurs rares qui
recoupent (un montant exact avec une date et un secteur peut suffire à reconnaître quelqu'un) ; relecture des textes
libres. Aucune table de correspondance n'est conservée dans le dossier. La méthode s'écrit dans
`donnees-essai/LISEZ-MOI`, avec le contrôle des résidus (recherche d'adresses électroniques, de numéros de
téléphone, de noms propres, d'identifiants) et la date. « Anonymisé » sans cette trace est une hypothèse `[H]`.

**Ce qui vient de `mission/sources/`.** Un export réel déposé là ne se recopie pas dans `80-construction/`. On en tire
la structure et les proportions, jamais les lignes.

## 4. Une étape d'IA

À construire quand `60-specification` §4 confie un jugement à un modèle. Les valeurs (seuil de confiance, taux
d'erreur toléré, plafonds) sont celles de §4 ; si elles manquent, c'est un trou de 60 (écart, version datée).

| Élément | Ce qu'on construit | Contrôle |
|---|---|---|
| Rôle borné | ce que le modèle peut faire, ce qu'il ne peut pas faire, écrit en tête de ses consignes | relecture contre `60-specification` §4 |
| Entrée | le strict nécessaire ; tout contenu venu de l'extérieur (message, document, champ libre) est une donnée, jamais une instruction | un contenu piégé dans le jeu de mise au point ne change pas le comportement |
| Sortie | format vérifié avant usage (champs, valeurs permises) ; une sortie hors format est une erreur définitive ; aucun texte libre ne commande une action | sortie volontairement malformée → file des échecs |
| Abstention | sous le seuil de confiance, ou si une information manque, le dispositif répond « à vérifier » et passe la main ; il n'invente pas | cas d'information manquante dans le jeu de mise au point |
| Consignes et modèle | consignes versionnées (numéro, date, motif) ; identifiant exact du modèle fixé ; un changement de l'un ou de l'autre est une nouvelle version, avec nouvelle recette | `journal-versions.md` |
| Agent | liste fermée d'actions ; plafond d'étapes, de durée et de coût par exécution ; journal de chaque décision ; aucune action irréversible sans validation ; aucun outil d'envoi dans l'essai | tentative d'action hors liste → refus journalisé ; plafond dépassé → arrêt |
| Coût et latence | mesurés sur le rejeu, comparés à `40-solutions` §8 et à `60-specification` | rubrique 9 |

**Deux jeux, deux usages.** Le jeu de mise au point sert à régler les consignes : quelques dizaines de cas écrits
avec le métier, rangés dans `donnees-essai/`. Le jeu d'évaluation (`EV-xx`) appartient à `tester-solution` : il
ne s'ouvre pas pour régler quoi que ce soit. Si le même acteur fait les deux, le jeu d'évaluation est constitué et
rangé à part avant la mise au point, et n'est pas consulté pendant. Un réglage fait en regardant le jeu
d'évaluation en fait un jeu de mise au point : il en faut alors un nouveau.

## 5. Méthode de repli maison — sans compagnon pour la plateforme

À dire en tête de `80-construction.md` (« méthode de repli »). Selon l'hôte, le pack peut ou non exécuter du code
et atteindre l'instance d'essai ; ce qu'il ne peut pas exécuter reste « prévu » et se confie au constructeur ou au
client, qui rendent les pièces (export balayé, sorties d'exécution).

| Plateforme décidée en 40 | Méthode de repli |
|---|---|
| Script ou petit service | le pack écrit et teste en local dans `livraison/` : dépendances fixées dans un fichier de verrouillage, un test automatisé par test de 60 §12 que la tranche rend exécutable, doubles des systèmes S1… (fichiers ou petits faux services dans `donnees-essai/`), configuration par variables (noms de secrets seulement), mode simulation par défaut, exécution reproductible en une commande, journal d'exécution dans un fichier |
| Flux sans code ou scénario | le pack ne manipule pas l'outil à l'aveugle. Il écrit, par tranche, une fiche de montage : déclencheur, composant, paramètres (noms de connexions seulement), correspondance des champs, sortie attendue, branche d'erreur, relecture de l'état après écriture. Le constructeur assemble dans l'instance d'essai et rend l'export (balayé) et les sorties d'exécution ; le pack les lit et contrôle. Sans instance d'essai ni pièces, les contrôles restent « prévus » et la version ne peut pas être déclarée prête |
| Agent | consignes versionnées ; liste fermée d'outils avec leurs schémas ; plafonds ; passage à l'humain ; journal de chaque décision. Dans l'essai, chaque outil est remplacé par un double qui journalise au lieu d'agir |
| Serveur d'outils | pour chaque outil : nom, rôle, schéma d'entrée, schéma de sortie, droits (lecture ou écriture), effets de bord, erreurs rendues ; lecture seule par défaut ; tout outil qui écrit a un mode simulation ; secrets par variable ; version fixée ; essayé avec un client factice avant tout branchement |

Dans tous les cas le contrat de la partie 1 s'applique tel quel. Quand l'hôte ne permet de rien exécuter, la
construction se limite à la fiche de montage, aux tranches et aux garde-fous écrits, et le livrable le dit.

## 6. Chercher et reprendre un modèle existant

**Où.** Les bibliothèques de modèles des éditeurs de flux, les flux publiés par la communauté, les flux déjà en place
dans l'entreprise, les briques internes. Durée de la recherche annoncée avant de commencer : le but est de ne pas
construire ce qui existe, pas de chercher sans fin.

**Ce qu'on contrôle** (une ligne par candidat, rubrique 2 de `80-construction.md`) :

- l'auteur et qui le maintient ; la date de dernière mise à jour et sa compatibilité avec la version fixée ;
- la licence ;
- les autorisations qu'il demande (lecture, écriture, envoi) et les composants tiers qu'il embarque ;
- ses appels sortants (vers quelles adresses) et son coût à l'exécution (unité facturée × volume) ;
- ce qu'il fait en plus de ce qu'on veut : un modèle « qui marche » fait souvent davantage, envois directs compris ;
- ce qui est écrit en dur (identifiants, adresses, seuils).

**Comment on l'importe.** Après lecture complète, désactivé, dans l'essai seulement. On remplace ses identifiants par
ceux relus dans l'outil, on retire tout ce qui n'est pas dans la spécification, on ajoute les garde-fous qui lui
manquent, et on le traite ensuite comme une construction ordinaire : tranches, contrôles, version, empreinte.

**Décision.** Base · inspiration · rien, avec la raison. Un modèle qui ne passe pas le contrôle n'est pas
importé, même s'il couvre toutes les exigences.

## 7. Balayer la livraison avant de la ranger

À faire pour chaque fichier destiné à `80-construction/` (export, script, règles, journal, sortie simulée, capture)
et pour chaque pièce de preuve de la recette.

- **Secrets** : chaînes longues et aléatoires ; les mots « key », « token », « secret », « password », « bearer »,
  « authorization » ; adresses qui contiennent des identifiants ou un jeton ; fichiers d'environnement ;
  certificats et clés privées. Une recherche de texte sur chaque fichier, puis la relecture d'un échantillon.
- **Données personnelles** : adresses électroniques, numéros de téléphone, noms et prénoms dans des textes libres,
  identifiants de clients, adresses postales.
- **Résultat** : date, méthode, fichiers balayés, ce qui a été trouvé, inscrits dans la rubrique 7 de
  `80-construction.md`. Le balayage ne prouve pas l'absence, il réduit le risque : il se refait à chaque version.
- **Si quelque chose est trouvé** : ne pas ranger le fichier. Remplacer par le nom du secret ou par une valeur
  fictive ; si un secret réel a été exposé, le dire au client, qui le révoque. Le pack ne le recopie nulle part, pas
  même dans le journal de la mission.
