# Critères et options — le détail de la conception de solution

À ouvrir à l'étape 2 (partie 1, porte d'entrée), à l'étape 5 (parties 2 et 3, options et qui construit)
et à l'étape 7 (parties 4 et 5, critères, plateforme ou code). La partie 6 liste les pièges.

Statut des contenus : les exemples de calcul sont fictifs ; les listes de plateformes sont des exemples
de catégorie ; les capacités et les prix des plateformes bougent en quelques mois et se vérifient sur
la page de l'éditeur au moment du choix, sinon ils restent `[H]`.

## 1. La porte d'entrée en détail

| Facteur | Ce qu'on demande | Freine l'automatisation | Pousse à automatiser |
|---|---|---|---|
| Fréquence | combien de fois par semaine ou par mois | quelques fois par trimestre | des dizaines de fois par semaine |
| Temps gagné par occurrence | minutes de travail retirées | quelques secondes, « c'est déjà rapide » | plusieurs minutes, ou une interruption de travail évitée |
| Taux d'erreur à la main | à quelle fréquence on se trompe, et ce que coûte une erreur | rare et sans conséquence | fréquent, ou coûteux quand il arrive |
| Stabilité | à quelle fréquence changent les étapes, les systèmes, les règles | change presque chaque mois | inchangé depuis plusieurs mois |

Les valeurs viennent de `20-diagnostic`, avec leur statut. La stabilité se déduit des variantes
constatées, des changements récents et des migrations en cours, ou se demande au responsable du
processus. Une valeur absente est `[H]`, avec le rôle qui peut la relever, ou « à mesurer avant tout
lancement ».

Les quatre verdicts :

- **Automatiser** : fréquent, stable, et soit un gain de temps réel, soit des erreurs coûteuses supprimées.
- **Standardiser d'abord** : fréquent mais instable, ou fait de trois façons par trois personnes.
  Écrire le processus, choisir une façon, l'exécuter à la main selon l'écrit jusqu'à ce qu'il tienne,
  puis seulement l'automatiser. La recommandation est l'option 0 ; la suite retourne à `auditer-processus`.
- **Assister seulement** : forte valeur, mais jugement à chaque occurrence ou action irréversible. Le
  dispositif prépare (brouillon, tri, extraction), une personne décide : option 5, ou une part de la 7.
- **Ne rien construire** : rare, ou gain faible. Liste de contrôle, modèle de document, délégation,
  suppression de l'étape.

**Pourquoi la stabilité départage.** Automatiser fige le processus d'aujourd'hui : chaque changement
ensuite devient une modification à faire, à tester et à redéployer. Sur un processus stable c'est
rare ; sur un processus mouvant, c'est un second travail. À égalité, la stabilité passe d'abord, puis
la fréquence.

**Le piège du processus cassé.** Automatiser un processus mal fait produit les mauvais résultats plus
vite, et une machine les cache à ceux qui les sentaient. On n'est pas prêt quand : les étapes ne
s'écrivent pas sans « en général » ni « ça dépend » ; deux personnes tirent des résultats différents de la
même entrée ; les systèmes concernés sont en cours de migration.

**La porte d'entrée est qualitative, le garde-fou financier vient après.** Elle ne fixe aucun seuil
chiffré universel. Le retour sur investissement, maintenance comprise, se calcule avec les chiffres du
cas dans `chiffrer-rentabilite`, qui conclut « y aller », « mesurer d'abord » ou « ne pas y aller » ;
ses repères d'alerte et leur statut s'y trouvent, pas ici.

## 2. Le catalogue des huit familles d'options

| N° | Famille | En quoi elle consiste | Gagne quand | Perd quand | Question de vérification |
|---|---|---|---|---|---|
| 0 | Ne rien construire | simplifier, fusionner ou supprimer l'étape ; déléguer ; clarifier une règle ; fournir un modèle de document ou une liste de contrôle | le problème vient du processus ou de l'organisation ; gain immédiat, coût quasi nul | l'étape est indispensable, volumineuse et déjà simple | que perdrait-on si l'étape disparaissait ? qui en dépend ? |
| 1 | Configurer un outil déjà en place | activer une fonction, une règle, un module déjà inclus dans une licence existante | la fonction existe et couvre les Indispensables | elle n'en couvre qu'une partie, ou son réglage est fragile | a-t-on lu la documentation des fonctions déjà payées ? |
| 2 | Brique existante | modèle, blueprint, extension ou application du marché | le besoin est courant ; la brique est maintenue et paramétrable | adaptation lourde, éditeur fragile, données sensibles | existe-t-il un modèle publié pour ce cas ? où a-t-on cherché, quand ? |
| 3 | Script ou petit service | code sur mesure, hébergé et maintenu | logique complexe, volume élevé, tests et suivi de version exigés | personne n'est en mesure de le maintenir | qui le maintiendra dans deux ans ? |
| 4 | Workflow sans code | plateforme d'orchestration visuelle qui relie des applications (par exemple n8n, Make, Zapier, Power Automate) | quelques applications avec connecteurs ; un métier doit lire et modifier le flux ; premier résultat rapide | logique complexe ; volume où la facturation à l'unité domine | quelle unité de facturation, pour quel volume ? |
| 5 | Assistant IA, humain dans la boucle | un modèle prépare (rédige, classe, résume, extrait), une personne valide | jugement requis, entrées non structurées, enjeu élevé | le volume rend la validation impossible ; données sensibles sans garanties sur leur traitement | quel taux d'erreur sur un échantillon de cas réels ? |
| 6 | Agent IA à autonomie bornée | un modèle choisit ses étapes dans une liste fermée d'actions, avec plafonds et journal complet | le chemin varie d'un cas à l'autre et ne peut pas s'écrire d'avance | le chemin est connu (un workflow suffit, moins cher et plus prévisible) ; actions irréversibles | quelles actions permises, quels plafonds, quand passe-t-il la main ? |
| 7 | Hybride | un orchestrateur plus un petit service pour la partie difficile, ou un workflow dont une étape est confiée à un modèle | une partie simple et lisible, une partie dure | deux technologies pour un besoin simple | quelle partie justifie la seconde technologie ? |

Les noms de plateformes sont des exemples de catégorie, pas une liste à jour du marché.

- **Chercher l'existant** : outils déjà connectés à la session (lecture seule), fonctions incluses
  dans les licences en place, documentation et catalogues de modèles des éditeurs. Noter où et quand
  on a cherché ; une recherche non faite s'écrit « non vérifié `[H]` ».
- **Assistant ou agent** : un agent n'est justifié que si le chemin varie d'un cas à l'autre. Sinon, un
  workflow qui confie une étape précise à un modèle coûte moins, se prévoit mieux et se teste. Les
  bornes d'un agent : liste fermée d'actions, plafond d'étapes et de coût par exécution, journal de
  chaque décision, passage à un humain sous un seuil de confiance, aucune action irréversible sans
  validation.
- **Fiabilité d'une option IA** : elle se mesure sur un échantillon de cas réels du client, pas sur des
  exemples de démonstration. Sans échantillon, le taux d'erreur est `[H]` et le pilote le mesure.

## 3. Qui construit

| Qui | Gagne quand | Perd quand |
|---|---|---|
| Équipe interne | profils motivés, formation possible, modèles disponibles ; le savoir doit rester dans l'entreprise | personne n'a le temps ; compétences à acquérir sur un sujet critique |
| Éditeur de l'outil | l'option est une configuration poussée ou une extension de son produit | la dépendance se renforce ; son coût de service peut dépasser celui d'un indépendant |
| Recrutement | besoin durable, plusieurs automatisations à suivre | besoin ponctuel ; délai de recrutement |
| Indépendant spécialisé | besoin net et circonscrit, livraison courte | le sujet traverse plusieurs équipes ; la maintenance après son départ n'est pas prévue |
| Prestataire (cabinet, intégrateur) | le sujet traverse plusieurs équipes et exige gestion de projet et conduite du changement | petit périmètre : le coût de coordination dépasse le gain |

Dans tous les cas, nommer le rôle qui maintient après la livraison : la spécification l'exigera
(`rediger-cahier-des-charges`, rubrique 17).

## 4. Les neuf critères de la matrice

| Critère | Ce qu'on regarde | Comment le renseigner |
|---|---|---|
| Couverture des exigences | chaque Indispensable et chaque Important : couvert entièrement, en partie, pas du tout | tableau exigence × option ; une Indispensable non couverte élimine l'option, sauf si le client la déclasse : c'est sa décision, pas la nôtre |
| Coût de construction | jours de travail ou prix, selon le profil qui construit | `[E]` d'après un devis ou l'estimation de l'équipe ; sinon `[H]` |
| Coût de fonctionnement | abonnements, appels de modèle, hébergement : unité facturée × volume réel ; coût marginal si l'outil est déjà payé, à dire | volume `[F]` du diagnostic ; tarif daté de la page de l'éditeur ou `[H]` ; résultat `[E]` |
| Maintenance | heures par mois : changements d'interface chez les fournisseurs, accès à renouveler, règles à ajuster ; qui s'en charge | `[H]` tant qu'aucun dispositif comparable n'a tourné ; c'est la ligne qu'on oublie facilement |
| Fiabilité et risque | comment ça tombe en panne, si on le voit, ce que coûte une erreur silencieuse ; pour une option IA, le taux d'erreur sur échantillon réel | `[F]` si mesuré, sinon `[H]` ; la parade (validation, file des échecs, interrupteur d'arrêt) |
| Sécurité et lieu des données | où les données transitent et sont stockées ; ce qui part vers un service tiers ou un modèle ; durée de conservation ; sous-traitants | documentation de l'éditeur lue et datée ; conformité à confirmer par le responsable concerné `[H]` |
| Dépendance et portabilité | si l'éditeur change de prix, de conditions ou disparaît : export possible, coût de sortie | conditions de l'éditeur ; test d'export si possible |
| Compétences internes pour maintenir | qui sait faire, qui peut apprendre, formation nécessaire | échange avec le responsable de l'équipe concernée ; des rôles, pas des noms |
| Délai | jusqu'à une première version utilisable, puis jusqu'à la production | `[E]` ; compter les accès à obtenir et les validations |

**Lire la matrice.**

- Les éliminatoires d'abord : exigence Indispensable non couverte, contrainte ferme de `30-exigences` §8
  violée (outil imposé, budget plafond, lieu des données).
- Ensuite colonne par colonne : une option est un profil de forces et de risques, pas une somme.
- Trois appréciations (favorable, acceptable, défavorable) et une raison courte. Pas de note sur dix :
  elle ferait croire à une précision qu'aucun critère n'a.
- Pas de total. En cas de désaccord, faire classer les trois critères les plus importants : une option
  défavorable sur l'un d'eux est écartée, ou doit porter une parade écrite.

## 5. Plateforme ou code

| Une plateforme sans code gagne quand… | Le code gagne quand… |
|---|---|
| on relie quelques applications qui ont des connecteurs | la logique est complexe, algorithmique, avec des états à conserver |
| un responsable métier doit lire et modifier le flux | on veut versionner, tester, relire, déployer par étapes |
| la rapidité de la première version prime sur la maîtrise | le volume est tel que la facturation à l'unité domine le coût |
| le volume est modeste et les connecteurs existent | il n'y a pas de connecteur, ou il faut piloter finement une interface |

Beaucoup de dispositifs mûrs sont hybrides : la plateforme orchestre et se lit, un petit service fait la
partie difficile, volumineuse ou algorithmique. Ne pas forcer l'un des extrêmes.

**Les unités de facturation.** C'est l'axe qui décide du coût à l'échelle ; le connaître avant de comparer.

| Unité facturée | Ce qui compte pour une unité | Forme de flux favorisée | Surprise typique |
|---|---|---|---|
| À l'exécution | un passage complet du flux, quel que soit le nombre d'étapes | flux longs et complexes, volume élevé | un événement très fréquent qui déclenche le flux |
| À l'action (crédit, opération ou tâche selon l'éditeur) | chaque étape exécutée, parfois pondérée : un crédit peut valoir plus d'une action | flux courts, peu d'étapes | un flux long multiplié par un fort volume ; lire la table de consommation, pas seulement le prix du crédit |
| À la licence (par utilisateur ou par flux) | une personne ou un flux autorisé | équipes déjà licenciées chez le même éditeur | fonctions ou connecteurs « premium » en supplément |
| À l'appel de modèle d'IA | le volume de texte lu et écrit à chaque appel | volume modéré, textes courts | longs documents traités en masse ; plusieurs appels par élément |
| Auto-hébergement | pas d'unité : un coût d'infrastructure et du temps de maintenance | volume élevé, données qui doivent rester chez soi | le temps de maintenance, rarement compté |

Exemple de calcul (chiffres fictifs) : un flux de dix étapes exécuté dix mille fois par mois. Facturé à
l'exécution : dix mille unités. Facturé à l'action : cent mille unités. Facturé à la licence : le volume
n'apparaît plus, le nombre de personnes et de flux si. Le même flux peut coûter dix fois plus ou presque
rien selon l'unité. Ici on identifie l'unité et son ordre de grandeur pour comparer ; le calcul complet du
coût de fonctionnement, avec ses scénarios, appartient à `chiffrer-rentabilite`.

**Pistes de départ selon le contexte `[H]`** — des pistes de recherche, pas des réponses : chacune se
vérifie sur la page de l'éditeur à la date du choix.

- L'entreprise vit déjà dans l'écosystème d'un éditeur (messagerie, documents, travail collaboratif) :
  regarder d'abord l'outil d'automatisation du même éditeur : licences et connecteurs y sont peut-être déjà.
- Les données doivent rester sur l'infrastructure de l'entreprise : plateforme auto-hébergeable, ou code.
- Application rare, responsable non technique : plateforme au catalogue de connecteurs le plus large.
- Volume élevé de flux longs : plateforme facturée à l'exécution, ou code.
- Automatisations à gérer comme du code (versions, déploiement) : plateforme qui le permet, ou code.

**Capacités à ne pas supposer `[H]`.** Au moment des sources (2026), certaines plateformes ne
permettaient pas de créer une automatisation par programme : elle se construisait dans l'interface. Si
le plan suppose de créer ou de déployer des automatisations en série (modèles réutilisés chez plusieurs
clients, déploiement automatisé), vérifier que l'éditeur le permet avant de retenir l'option.

**Lire la page d'un éditeur.** Noter l'adresse de la page et la date de lecture ; l'unité de facturation
et le quota inclus ; les limites (taille des données, durée d'exécution, nombre d'étapes, appels par
minute) ; les régions et le lieu de stockage des données ; la possibilité d'exporter ; les conditions de
l'offre (engagement, évolution des prix). Ce qu'on n'a pas pu lire reste `[H]`.

## 6. Pièges de l'évaluation

- **Choisir par familiarité** : la facture « explose » parce que l'unité facturée ne correspond pas à la
  forme du flux.
- **Comparer un prototype à un produit** : une démonstration fluide n'est pas un dispositif exploité ;
  compter les erreurs, les accès à renouveler, la maintenance.
- **Oublier la maintenance** : la ligne qu'on omet facilement, et qui fait mentir les gains.
- **Noter une capacité non vérifiée** : une fonction lue dans un article ressemble à une fonction mesurée.
- **Ignorer le coût de sortie** : l'option la moins chère aujourd'hui peut être la plus chère à quitter.
- **Un agent là où un workflow suffit** : plus de variabilité, plus de coût, moins de tests.
- **Additionner des notes pour masquer un arbitrage** : le désaccord se règle en classant les critères.
- **Laisser les options à construire l'emporter** parce qu'on n'a pas cherché l'existant.
- **Un repli de façade** : un nom sans la grille, qui rend la condition d'arrêt théorique.
- **Tout faire reposer sur le compte d'une personne** : prévoir un compte de service et un propriétaire.
