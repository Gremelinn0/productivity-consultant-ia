# Méthode de mesure — statuts, comparabilité, recalcul, échecs, cas difficiles, décision

À ouvrir pour : décider du statut d'un nombre (§1), vérifier qu'une comparaison tient (§2), recalculer le gain et les coûts avec un exemple complet (§3), lire de vrais cas (§4), traiter
l'adoption nulle, le gain négatif ou le changement non approuvé (§5), proposer la décision (§6), dire ce que la mesure change pour le portefeuille (§7). La méthode générale est dans `SKILL.md`,
les modèles de livrable dans `modeles.md`. Les formules viennent de `chiffrer-rentabilite` (`references/formules.md`) et ne sont pas redéfinies ici.

## 1. Les statuts dans 95

`ARCHITECTURE.md` définit `[F]`, `[H]` et `[E]`. Dans `95-mesure.md` seulement, un gain peut être `[F]`, aux conditions suivantes :

| Ce qu'on a | Statut | Pourquoi |
|---|---|---|
| Valeur comptée ou chronométrée sur une période datée, avec source et méthode, relevée hors du dispositif ou recoupée | `[F]` | observée |
| Résultat calculé avec des termes tous `[F]` de la même période, calcul montré | `[F]` « observé sur la période » | un calcul sur des faits n'ajoute aucune supposition |
| Résultat dont un terme reste supposé (part réemployée sans usage constaté, coût d'une erreur non relevé) | `[E]` | le terme supposé se nomme |
| Projection au-delà de la période (retour projeté, gain annuel) | `[E]` | l'avenir n'est pas observé |
| Valeur donnée de mémoire, ou relevé sans période, sans source ou sans méthode | `[H]` | déclarée ; écrire le rôle qui peut la remplacer par un relevé |
| Volume, nombre d'exécutions, jetons lus dans les traces du dispositif | `[F]` comme activité, jamais comme gain | une trace dit que ça tourne |
| Relevé du pilote | `[F]` pour son périmètre et sa période | non extrapolé |

Une trace technique devient une source de mesure d'un gain seulement si elle porte elle-même le résultat métier (par exemple le temps entre deux événements horodatés par le processus, hors dispositif), ou
si elle est recoupée par un relevé côté métier. Sans mesure de départ datée d'avant le pilote, aucun écart ne se déclare observé.

## 2. Comparer ce qui est comparable

- **Même définition, même méthode, même source.** Si la méthode a changé depuis le départ (autre export, autre définition du temps), l'écart mesure ce changement : refaire la mesure de départ de la même
  façon quand c'est encore possible, sinon écrire « non comparable ».
- **Le départ de comparaison est le plus solide d'avant le pilote.** Une re-mesure sur plusieurs occurrences (par exemple les relevés du premier lot de 70) vaut mieux qu'une observation unique ; écrire les deux.
- **Par occurrence.** Comparer des minutes par occurrence, des erreurs pour cent occurrences, des coûts par occurrence : un volume qui bouge ne doit pas passer pour un gain ou une perte.
- **Saison et calendrier.** Même rythme (fin de mois, clôture, vacances, pointe annuelle) ; sinon la même période de l'an passé quand elle existe.
- **Montée en charge.** Les premiers mois ne représentent pas le régime établi : on les exclut de la lecture du régime établi et on les garde dans le retour constaté (le manque à gagner m de `formules.md` §4).
- **Attribution.** Par ordre de préférence : un témoin (équipe, site ou entité non concernés, même période) ; la même période de l'an passé ; avant et après, volume corrigé et autres changements listés ; à défaut
  « a contribué à ». Lister les autres changements de la période (simplifications, embauche, prix, saison) ; si on ne peut pas les séparer, le dire.
- **Simplifications et construction.** Garder la répartition de `20-diagnostic.md` §9 et de `50-rentabilite.md` §3 : la re-mesure faite après les simplifications et avant la construction sépare les deux effets ;
  sans elle, le gain reste global (« simplifications et construction ensemble ») et ne s'attribue pas à la seule construction.
- **Peu d'observations.** Écrire leur nombre, leur minimum et leur maximum. Quatre lundis ne font pas une loi : on écrit « sur 4 lundis » et on ne présente pas leur moyenne comme plus précise qu'elle n'est.
- **Cas atypiques.** Règles d'exclusion écrites avant la lecture (semaine de panne du système source, jour férié, fin d'exercice) ; on montre le résultat avec et sans.
- **Biais à nommer.** Nouveauté (on va plus vite quand on est observé), montée en charge, auto-déclaration (celui qui a construit ou qui y gagne mesure), survivants (les cas difficiles contournent le
  dispositif et sortent de la mesure), travail déplacé (le gain ici, la charge là : support, relecteurs, aval — le mesurer aussi).
- **Qui mesure.** Les relevés viennent des systèmes de l'entreprise (exports, compteurs) ou d'un rôle qui n'a pas construit le dispositif ; le propriétaire de la qualité de la donnée est nommé (60 §14).

**Les neuf familles de mesure.** Chacune est couverte par un `IND-xx` de 60 §14, par un terme de 50 §2 ou par un relevé de 70 §5, ou écrite « non relevée : raison ». Pour chacune : un propriétaire, une période, une méthode, la même qu'au départ.

| Famille | Ce qu'on lit | Piège |
|---|---|---|
| Volume | occurrences traitées, au total et par le dispositif | un volume qui bouge passe pour un gain : ramener le reste à l'occurrence |
| Temps humain complet | minutes par occurrence, retouches, supervision et exceptions comprises ; charge en aval | oublier la relecture ; ne pas voir le temps déplacé |
| Erreurs | nombre pour cent occurrences, par catégorie, reprises comprises | ne compter que celles que les alertes voient |
| Qualité | conformité du résultat à la règle, sur un échantillon lu par un humain | une qualité déclarée par le dispositif lui-même |
| Satisfaction | retours des utilisateurs et, si le processus les touche, des clients ; par groupe ou par rôle, jamais par personne | pas de départ, donc rien à comparer ; une enquête de plus que personne n'a demandée |
| Adoption active | occurrences passées par le dispositif ÷ occurrences totales, par rôle | les comptes ouverts, les formations suivies |
| Coûts d'usage | exécutions, appels, jetons, crédits × tarif daté | tarif non daté ; palier dépassé en fin de mois |
| Incidents | nombre, durée, effet, cause, mode de détection | incidents jamais déclarés |
| Maintenance | heures notées × taux de celui qui la fait | heures non notées |

## 3. Recalculer le gain et les coûts réels

- **Formules.** `chiffrer-rentabilite`, `references/formules.md` : §2 (gain brut), §3 (coûts), §4 (montée en charge et retour), §6 (point mort), §8 (arrondis). Aucune n'est redéfinie ici.
- **Gain brut observé** = valeur du temps libéré réemployé + valeur des erreurs évitées + autres gains justifiés, avec :
  - occurrences passées par le dispositif (occurrences totales × adoption active) × minutes gagnées par occurrence en temps complet ÷ 60 × part réemployée observée × coût horaire chargé ;
  - erreurs évitées observées (écart en nombre avec le départ) × coût d'une erreur. Ce nombre est déjà observé en exploitation : l'adoption n'est pas réappliquée.
- **Part réemployée.** Observée seulement si l'usage nommé a eu lieu (appels passés, heures supplémentaires évitées, volume absorbé sans embauche). Sinon c'est du temps libéré non réemployé : valeur non
  financière, zéro euro de gain. L'écrire, puis demander l'usage.
- **Coûts réels.** Construction payée (la facture, pas le devis) et mobilisée (heures notées de pilote, recette, formation × taux) ; fonctionnement (factures de la période) ; coûts d'usage (unités consommées ×
  tarif daté : exécutions, appels, jetons, crédits) ; maintenance (heures notées × taux de celui qui la fait) ; incidents (heures de reprise × taux, coûts directs). Chaque ligne a sa source.
- **Gain net observé** = gain brut − fonctionnement − coûts d'usage − maintenance − incidents.
- **Retour constaté** : le premier mois où le cumul des gains nets observés atteint la construction réelle. Sinon **retour projeté** `[E]`, par une seule formule, celle de 50 (`chiffrer-rentabilite`,
  `formules.md` §4), appliquée aux termes observés : (construction payée + construction mobilisée réelles + gain brut observé × m) ÷ gain net mensuel observé. `m` est le manque à gagner de montée en
  charge de 50 (`[H]`) ; une fois le régime établi observé, il se recalcule sur les mois lus. Aucune autre formule de retour n'est écrite ici. Un gain net observé nul ou négatif n'a pas de délai de
  retour : on écrit « pas de retour », jamais un nombre de mois, et la décision suit les règles du §5 (gain net devenu négatif) puis du §6.
- **Point mort recalculé.** Celui de `50-rentabilite.md` §4 suppose les autres termes au central ; avec le réel, on le recalcule (`formules.md` §6, point 4).

**Exemple de calcul** — suite de l'exemple de `chiffrer-rentabilite/references/formules.md` §9 (saisie des bons de commande). Nombres fictifs, à ne reprendre dans aucune mission. Quatrième mois après la bascule.

| Terme | Estimé (central) | Observé au mois 4 | Statut et source |
|---|---|---|---|
| Occurrences par mois | 1 000 | 960 | `[F]` export |
| Adoption active | 80 % | 72 % | `[F]` occurrences passées par le dispositif ÷ occurrences totales |
| Minutes gagnées par occurrence, temps complet | 6 | 4,5 | `[F]` 10,0 min au départ (40 occurrences, avant le pilote) contre 5,5 min au mois 4 (40 occurrences), retouches et relecture comprises |
| Part du temps libéré réemployée | 50 % | 35 % | `[F]` heures supplémentaires évitées, relevé agrégé du service paie : 18,1 h sur 51,8 h libérées |
| Erreurs évitées par mois | 20 | 14 | `[F]` 38 erreurs par mois au départ contre 24 au mois 4 |
| Coût d'une erreur | 25 € | 25 € | `[H]` non relevé |
| Coût horaire chargé | 50 € | 50 € | `[F]` |
| Fonctionnement par mois | 150 € | 165 € | `[F]` factures : 100 € d'abonnement + 24 € d'exécutions + 41 € de modèle d'IA |
| Maintenance par mois | 150 € (3 h) | 300 € (6 h) | `[F]` heures notées × 50 € |
| Incidents du mois | non estimés | 100 € (2 h de reprise) | `[F]` |
| Construction | 7 200 € payée + 500 € mobilisée | 7 200 € + 620 € | `[F]` facture ; heures notées (12,4 h × 50 €) |

- Occurrences passées par le dispositif : 960 × 0,72 = 691,2. Heures libérées : 691,2 × 4,5 ÷ 60 = 51,84 h. Réemployées à 35 % : 18,144 h × 50 € = **907,20 €** `[F]` (tous les termes sont `[F]`).
- Erreurs évitées : 14 × 25 € = **350 €** `[E]`, parce que le coût d'une erreur reste `[H]`. Gain brut : 907,20 + 350 = **1 257,20 €** `[E]`, dont 907,20 € `[F]`. Estimé : 2 400 €.
- Gain net : 1 257,20 − 165 − 300 − 100 = **692,20 €** `[E]`. Estimé : 2 100 €. Écart : −1 407,80 € (−67 %).
- Construction réelle : 7 200 + 620 = 7 820 €. Gains nets observés mois par mois (même calcul chaque mois) : 150, 380, 560 et 692,20 € ; cumul après quatre mois 1 782,20 € : le retour n'est pas encore constaté.
  Retour projeté, formule de 50 §4 avec m = 1,5 mois `[H]` conservé : (7 820 + 1 257,20 × 1,5) ÷ 692,20 = environ **14,0 mois** `[E]`, contre 5,4 mois estimés.
- Point mort recalculé pour un retour en 12 mois (`formules.md` §6, avec C = 7 820 €, F = 165 + 300 = 465 € par mois, m = 1,5 mois `[H]` conservé) : gain brut minimal = (7 820 + 12 × 465) ÷ (12 − 1,5) = environ
  1 276 €. Observé : 1 257 € `[E]`. Le point mort ne tient plus, de peu.
- Position dans l'éventail de 50 : minutes (3 à 8) entre le bas et le central ; part réemployée (25 à 80 %) entre le bas et le central ; adoption (60 à 90 %) entre le bas et le central ; gain net 692 € entre le bas
  (375 €) et le central (2 100 €). Si tout le temps libéré était réemployé il vaudrait 2 592 € par mois ; passer de 35 à 50 % de réemploi ajouterait environ 389 € par mois `[E]`.
- Décision proposée : **corriger**. Raisons : le point mort pour douze mois ne tient plus (1 257 € contre 1 276 €) et le retour projeté (environ 14,0 mois) plus que double l'estimation (5,4 mois) ; trois causes réparables sont nommées, l'adoption (72 %),
  le réemploi (35 %) et la maintenance (6 h au lieu de 3) ; aucun seuil d'arrêt n'est franchi et le gain net est positif. Ce qui la renverserait : vers « arrêter », une lecture où le gain net tombe au niveau du bas de 50
  (375 €) sans cause réparable ; vers « continuer », une lecture où le gain brut dépasse 1 276 €.

## 4. Lire de vrais cas et classer les échecs

- **Pourquoi.** Les alertes voient ce qu'on a prévu de surveiller. Un échec silencieux (un résultat faux ou incomplet, sans erreur technique) ne lève rien : seuls la lecture de cas réels ou une plainte le montrent.
- **L'échantillon**, tiré avant la lecture, de taille `[H]` (celle qu'un lecteur peut lire sans bâcler ; la taille s'écrit) : un tirage au hasard des cas de la période, qui sert à estimer le taux d'échec courant ; tous les cas
  signalés (réclamations, retouches importantes, rejets, retours) ; les cas à risque (le cas limite critique et les limites de 60 §12, les premiers jours après un changement).
- **Qui lit.** Un rôle du client qui connaît le travail et n'a pas construit le dispositif. Le dispositif ne se relit pas lui-même ; un modèle qui jugerait un autre modèle suit les conditions de calibration de 85.
- **Classement.** Les catégories de la recette (par exemple : mauvaise cible, mauvaise valeur, oubli, doublon, hors règle, hors périmètre, retard) ; pour un composant d'IA, les familles d'erreurs des `EV-xx`. Un échec
  d'une catégorie nouvelle crée sa catégorie et revient en 85 comme nouveau cas de test.
- **Mode de découverte.** Alerte · lecture · réclamation (ou retour d'un tiers). Chaque échec compte une fois, par le premier mode qui l'a trouvé.
- **Ce qu'on en tire.** Le taux d'échec estimé (échecs ÷ n de l'échantillon au hasard : un petit n donne une fourchette large, on écrit n et on ne promet pas une précision que l'échantillon n'a pas) ; la part des échecs
  vus par une alerte ; les échecs silencieux, qui appellent chacun une alerte ou un contrôle de plus, à tester. Un échec qui atteint un client ou une écriture irréversible appelle une action immédiate (suspendre : `A-xx`).
- **Composant d'IA.** À chaque revue et après tout changement de modèle ou de consignes, demander à `tester-solution` de rejouer le jeu d'évaluation sur la version en service : l'écart avec le résultat de la recette est
  la dérive. Les cas réels échoués, anonymisés, s'ajoutent au jeu.
- **Pré-mortem et risques.** Rapprocher les échecs et les incidents des histoires de 70 §8 et des `R-xx` : lesquelles se sont produites, quel signal a parlé. Une histoire non prévue s'ajoute au pré-mortem à la revue suivante.
- **Incidents.** Une ligne datée par incident (détecté par, durée, effet, cause) ; leur coût de reprise alimente la ligne « incidents » du gain net ; un défaut de la solution prend un `D-xx`, un risque réalisé renvoie à son `R-xx`.

## 5. Les trois cas difficiles

**Adoption nulle ou presque.**
- *Reconnaître.* Aucune occurrence ne passe par le dispositif, ou une part sous le seuil de correction de l'indicateur d'adoption de 60 §14 (à défaut, sous la moitié du taux supposé en 50 §5 `[H]`), ou une équipe entière qui contourne.
- *Écrire.* L'adoption telle quelle (zéro est un résultat) ; le gain observé nul ou proportionnel, jamais calculé sur des occurrences qui n'ont pas utilisé le dispositif ; le gain net négatif de ce que coûtent fonctionnement,
  maintenance et incidents. Ne pas redéfinir l'adoption pour la relever.
- *Chercher la cause avant de conclure*, par rôle et sans désigner personne : accès ou droits manquants ; formation absente ou jamais essayée ; une étape ajoutée à ceux qui n'y gagnent rien ; la confiance perdue après des
  résultats faux ; l'ancienne voie toujours imposée ou plus simple ; un processus qui a changé ; une charge déplacée. Appuis : les six questions d'adoption de 70 §4, l'histoire « adoption » du pré-mortem, un court entretien
  par rôle (guide préparé par le pack, réponses du client).
- *Conduite.* Corriger si la cause est réparable et qu'une re-mesure courte est posée (action, rôle, date) ; arrêter si deux lectures de suite sans reprise, ou si la cause est de fond (le dispositif n'aide pas le travail réel :
  retour à `20-diagnostic.md`). Le retrait passe par `piloter-mise-en-service`.
- *Piège.* Compter l'adoption en accès ou en formations suivies ; mettre sur le compte de la « résistance au changement » un défaut du dispositif.

**Gain net devenu négatif.**
- *Reconnaître.* Gain net observé inférieur à zéro sur une période comparable, alors que l'estimation ou la lecture précédente était positive.
- *Décomposer avant de conclure* : volume (moins d'occurrences) · adoption · minutes gagnées en temps complet (retouches, exceptions, qualité) · réemploi · coûts (tarif, coûts d'usage, maintenance, incidents). Un seul terme
  en cause se corrige ; plusieurs signalent un dispositif mal calibré. Sous le seuil de rentabilité mensuelle (gain brut inférieur à fonctionnement plus maintenance), il coûte chaque mois plus qu'il ne rapporte.
- *Distinguer accident et tendance.* Une période négative isolée (mois creux, incident majeur : dire lequel) ne vaut pas arrêt ; deux périodes comparables de suite, oui. Comparer au scénario bas de 50 §4 : « ne se rembourse pas » était-il prévu ?
- *Conduite.* Corriger (cause isolée, action, date de re-mesure) ou arrêter (deux périodes de suite sans correction crédible). Écrire dans la décision le coût de poursuite par mois `[E]` (fonctionnement + maintenance) pour que
  poursuivre ou arrêter se choisisse en connaissance de cause. Le retour s'écrit « pas de retour » : un gain net négatif n'a pas de délai.
- *Piège.* Un temps libéré sans usage donne zéro euro de gain alors que du temps est libéré : dire les deux, mettre le temps en valeur non financière, demander l'usage.

**Changement non approuvé.**
- *Reconnaître.* La version en service diffère de la dernière version validée au registre de `90-mise-en-service.md` (historique de versions de la plateforme, journal d'exécution) ; une règle ou un paramètre modifié sans date ;
  des droits ou des utilisateurs nouveaux ; des coûts ou des résultats qui bougent sans cause ; un modèle d'IA remplacé ou mis à jour par le fournisseur ; un processus amont qui a changé (nouvelle règle, nouveau format d'export).
- *Effet sur la mesure.* La période concernée ne mesure plus la solution validée : elle est marquée « version non validée », ses indicateurs se lisent à part, et son gain ou sa perte ne s'attribue pas à la solution recettée.
- *Conduite.* Dire le changement (date de la découverte, ce qui a changé, par qui si on le sait, effet sur les indicateurs) ; il s'écrit au journal comme un incident daté, rien n'est régularisé après coup. Demander au
  propriétaire de choisir la suite, que `piloter-mise-en-service` inscrit en `A-xx` nouvelles, validées avant d'être faites : garder (tests concernés rejoués par `tester-solution`) ou défaire (retour arrière). Rappeler la
  règle : tout changement passe par une `A-xx` validée avant.
- *Changement subi* (éditeur, fournisseur, processus amont) : même conduite, sans désigner de faute ; l'écrire à la date où on le constate, rejouer les tests, décider d'accepter ou de revenir.
- *Approuvé mais non enregistré* : le propriétaire l'a décidé hors registre. Le journal l'écrit comme un incident daté ; la suite (garder ou défaire) est une `A-xx` validée avant d'être faite ; la mesure ne redevient
  comparable qu'à partir de la date de mise en service de cette `A-xx`, si les tests ont été rejoués.
- *Piège.* « Neutraliser » le changement par un calcul, ou le taire parce que les résultats sont bons.

## 6. Décider

Règles par défaut `[H]`, que le décideur confirme ou remplace par écrit. Les seuils ne sont pas refaits : ceux de `60-specification.md` §14 (production) et de `40-solutions.md` §1 (condition d'arrêt) ; les seuils du pilote ne servent plus
après la bascule.

| Décision | Quand | Ce qui suit |
|---|---|---|
| Arrêter | un seuil d'arrêt de 60 §14 franchi (la suspension de 70 §6 est déjà faite) sans cause réparable à court terme, ou deux lectures de suite sans reprise ; ou la condition d'arrêt de 40 §1 réalisée ; ou un gain net observé négatif sur deux périodes comparables de suite sans correction datée possible ; ou une adoption nulle après une correction essayée | retrait par des actions `A-xx` dans 90 (désactivation, retour à l'option de repli, révocation des accès, abonnement, données selon leur durée de conservation) ; clôture du cas ; ce qu'on retient pour le portefeuille |
| Corriger | un seuil de correction ou d'alerte franchi ; ou un terme du business case sous son bas ; ou un point mort de 50 §4 qui ne tient plus pour le critère de l'entreprise, avec une cause réparable nommée ; ou un échec silencieux trouvé ; ou un changement non approuvé dont la suite reste à décider (garder ou défaire) | une action par cause (rôle, date, date de re-mesure) ; les actions sur outils réels passent par 90 ; la correction technique par 80 puis 85 |
| Étendre | tous les seuils respectés sur au moins deux lectures comparables ; gain net observé au moins égal à ce que le point mort de 50 §4 exige pour le critère de l'entreprise ; indicateurs de qualité dans leurs seuils ; adoption active au niveau visé par 50 §5 ; aucun échec silencieux ouvert ; un candidat nommé (seconde phase, équipe, cas) | nouveau business case avec les valeurs observées en `[F]` (`chiffrer-rentabilite`) ; plan de l'extension (`planifier-deploiement`) ; spécification de la seconde phase si elle est nouvelle (`rediger-cahier-des-charges`) ; 80 à 90 repartent pour elle |
| Continuer | sinon : seuils respectés, gain net positif, point mort tenu ; pas de candidat d'extension, ou conditions d'extension pas encore réunies | prochaine lecture datée au rythme de 70 §6 ; rien d'autre à changer |

- **Cas partagé** (un seuil franchi et un business case qui tient, ou l'inverse) : le décideur tranche, et la décision écrit pourquoi.
- **Appeler `router-consulting-strategy`** pour arbitrer : la décision à prendre (une des quatre), les faits observés `[F]` de ce document, les hypothèses restantes `[H]`, les options réelles (les quatre, y compris ne rien changer),
  le contre-cas, les conditions d'arrêt (60 §14, 40 §1). Il rend une recommandation en réponse d'abord, que 95 reprend sans recopier sa méthode ; ne dire qu'on l'a appelé que si c'est fait.
- **Dire ce que coûte d'attendre** : coût mensuel de poursuite `[E]` (fonctionnement + maintenance), temps libéré non réemployé.
- **Une décision sans actions est un vœu** : « corriger » donne l'action, le rôle, la date de re-mesure et les relevés attendus ; « arrêter » donne les actions de retrait ; « étendre » nomme le candidat et la porte d'entrée.

## 7. Ce que la mesure change pour le portefeuille

- **Les paramètres communs observés** : part du temps libéré réemployée, adoption, maintenance, fonctionnement et coûts d'usage, montée en charge, coût d'une erreur, jours de construction réels contre le devis, durée réelle du pilote.
  Pour chacun : supposé dans `03-chiffrage.md` (ou dans 50), observé, cas concernés.
- **Les effets possibles** : un cas se reclasse dans `03` (solide, à mesurer d'abord, douteux) ; l'ordre de `04` change ; un cas de « ce qu'on ne fait pas maintenant » dont la condition de réouverture est remplie se rouvre ; un cas
  nouveau naît de la mesure (une cause trouvée en amont) ; la vague suivante attend ou avance. Le pré-mortem de `04` se rejoue quand `planifier-deploiement` le prévoit pour la décision de ce cas.
- **Qui corrige.** Les compétences propriétaires, par version datée et ligne « correction » au journal : `chiffrer-rentabilite` (`03`), `decouvrir-cas-usage` (`02`), `planifier-deploiement` (`04`). `mesurer-gains` écrit la proposition et son motif ;
  il ne refait pas leur travail.
- **Sans porte découverte.** Les valeurs observées, à réutiliser comme `[F]` dans les business cases suivants du même client, ou « sans objet ».
