---
name: mesurer-gains
description: >-
  Quand la solution est en service et qu'il faut savoir ce qu'elle rapporte vraiment (« ça a marché ? »,
  « on a gagné combien ? », « le business case tient-il ? », « on continue, on corrige, on étend ou on
  arrête ? ») → comparer des relevés réels à la mesure de départ et au business case, sur des périodes
  comparables, avec le temps humain complet, les coûts réels, l'adoption active, les incidents et de
  vrais cas lus (les échecs silencieux comptent) ; ne déclarer un gain observé que sur relevé, dire ce
  qui ne l'est pas et ce qu'il faut relever ; puis proposer continuer, corriger, étendre ou arrêter, et
  dire ce que la mesure change pour le portefeuille. Étape 95 du pack consultant-ia, après la mise en
  service. Triggers : « mesurer le gain », « gain réel », « ROI réel », « bilan après déploiement »,
  « revue d'indicateurs », « le business case tient-il », « continuer ou arrêter », « post-deployment
  review », « realized benefits », « actual vs expected ROI ».
metadata:
  scope: "la mesure, après mise en service, de ce qu'une solution rapporte et coûte vraiment : lecture des relevés réels, comparaison au départ et au business case, décision sur la suite"
  owns: "la lecture des relevés réels (pas leur collecte), le statut [F] d'un gain observé, la comparaison à la mesure de départ et au business case, les coûts, l'adoption et les incidents réels, la lecture de vrais cas et le classement des échecs, la décision continuer · corriger · étendre · arrêter, l'effet de la mesure sur le portefeuille"
  consumes: "mission/cas-<slug>/20-diagnostic.md (mesure de départ) ; 30-exigences.md §10 ; 40-solutions.md §1 ; 50-rentabilite.md (hypothèses, scénarios, point mort) ; 60-specification.md §12 et §14 ; 70-plan.md (rythme des revues, protocole de mesure, pré-mortem) ; 90-mise-en-service.md (début de période, versions en service, changements) ; mission/sources/ (les relevés que le client dépose) ; mission/journal.md ; en porte découverte 02-portefeuille.md, 03-chiffrage.md et 04-feuille-de-route.md"
---

# Mesurer les gains

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/95-mesure.md`. Preuve : le décideur tranche entre continuer,
> corriger, étendre et arrêter, et la décision s'inscrit dans `mission/journal.md` ; chaque `[F]` renvoie à un relevé déposé
> dans `mission/sources/`. Contrôle de forme : les dix rubriques du modèle sont présentes ; chaque `IND-xx` de 60 §14 figure
> (lu, ou « non relevé » avec ce qu'il faut relever) ; aucun `[F]` n'est sans période, sans source ni méthode ; aucun gain n'est
> déclaré observé sans mesure de départ datée ; l'estimation de 50 n'est pas réécrite ; chaque nombre a son statut `[F]`, `[H]`
> ou `[E]` (définis dans `ARCHITECTURE.md`) ; chaque renvoi porte la version lue. Exemple de référence : `examples/` du pack
> (mission fictive, mesure simulée). **Boucle** : aucune.

## Ce que cette compétence résout

Un gain annoncé avant la mise en service est une estimation. Six mois plus tard, on cite souvent le même chiffre : personne n'a
comparé, ou on a comparé des périodes qui ne se ressemblent pas, ou on a pris pour un gain ce que disent les traces de l'outil
(« 3 000 exécutions réussies »). Un dispositif peut tourner sans erreur et ne rien rapporter ; il peut aussi se tromper longtemps
sans qu'aucune alerte ne parte.

Cette compétence est le seul endroit du pack où un gain devient `[F]`. Elle relit les relevés que le client fournit, les compare à la
mesure de départ et au business case sur des périodes comparables, recalcule le gain net avec les coûts réels, lit de vrais cas, puis
propose une décision parmi quatre. Elle ne collecte rien elle-même : elle dit quoi relever, et ce qui n'est pas relevé reste `[H]` ou `[E]`.

Résultat attendu : un livrable qui dit, chiffre par chiffre, ce qui est observé, ce qui est estimé et ce qui manque ; l'écart avec le départ
et avec le business case ; une décision que le décideur peut renverser.

## Stratégie

1. **`[F]` sur relevé seulement, et seulement ici.** Une valeur est `[F]` quand elle est comptée ou chronométrée sur une période datée, avec
   sa source, sa méthode et son propriétaire ; un résultat calculé avec des termes tous `[F]` de la même période l'est aussi, calcul montré.
   Dès qu'un terme reste supposé, le résultat est `[E]` et le terme est nommé. Une projection est `[E]`. Sans relevé, rien n'est `[F]` : le
   livrable le dit et liste ce qu'il faut relever (`references/mesure.md`, §1).
2. **Les mêmes mesures, sur des périodes comparables.** Même définition, même méthode, même source qu'au départ, même saison, volume corrigé (on
   compare des minutes par occurrence, pas des heures totales). La mesure de départ doit être datée et antérieure au pilote ; sans elle, aucun
   écart ne se déclare observé.
3. **Tout le travail humain compte.** Retouches, supervision, traitement des exceptions et des erreurs du dispositif compris ; et on cherche le
   travail déplacé ailleurs (support, relecteurs, aval).
4. **Les traces techniques disent que ça tourne, pas que ça rapporte.** Exécutions, volumes, jetons : sources d'activité, d'adoption et de coût.
   Un gain se prouve sur un résultat côté métier (temps, erreurs, délai, argent, satisfaction), relevé hors du dispositif ou recoupé.
5. **Lire de vrais cas, surtout les échecs.** Un échec silencieux ne déclenche aucune alerte : seuls un échantillon lu par un humain ou une
   réclamation le montrent. Les échecs se classent par catégorie et par façon dont on les a trouvés.
6. **Écarter les cas atypiques en le disant, avant de voir le résultat.** Les règles d'exclusion s'écrivent avec la demande de données ; le résultat
   se montre avec et sans. Avec peu d'observations, on écrit leur nombre et leurs extrêmes, pas seulement la moyenne.
7. **Le coût réel est complet.** Construction réelle, fonctionnement et coûts d'usage (appels, jetons, crédits), maintenance (heures notées), temps
   interne, incidents. Un gain net sans maintenance observée se trompe dans le sens qui rassure.
8. **L'estimation reste intacte, le réel s'écrit à côté.** `50-rentabilite.md` garde l'estimation sur laquelle on a décidé d'y aller ; l'écart se lit
   terme par terme dans `95-mesure.md`.
9. **Une décision parmi quatre, avec ce qui la renverserait.** Continuer, corriger, étendre ou arrêter. Les seuils sont ceux de 60 §14 et de 40 §1 ; on
   ne les refait pas. Arrêter est un résultat, pas un échec. L'humain tranche (règle 3).
10. **On mesure le travail, pas les personnes** (règle 4). L'adoption se lit en occurrences et par rôle ; aucun classement individuel.

## Étapes

1. **Lire ce qui existe et fixer la période.** `20-diagnostic.md` (mesure de départ), `30-exigences.md` §10 et `60-specification.md` §14 (`IND-xx` : source,
   méthode, rythme, qui mesure, seuils, attribution), `50-rentabilite.md` (§2 hypothèses, §4 scénarios et point mort), `70-plan.md` (§6 rythme des revues et
   actions aux seuils, §8 pré-mortem), `90-mise-en-service.md` (début de période, versions en service, changements), le journal ; en porte découverte `02`, `03`,
   `04`. Sans `90-mise-en-service.md`, la solution n'est pas en service : proposer `piloter-mise-en-service`. Un seuil absent de 60 §14 est un trou de 60 : le corriger
   par version datée avant de lire les chiffres. Une lecture du pilote vaut pour son périmètre et sa période, sans extrapolation. Mesure de départ non datée ou postérieure
   au pilote : dire ce qui reste possible (équipe témoin, période de repli) ; sinon l'écart reste `[H]` ou `[E]`.
2. **Dresser la demande de données, avant de lire quoi que ce soit.** Pour chaque `IND-xx` et chaque terme de `50-rentabilite.md` §2 : ce qu'on relève, le rôle qui
   relève, la méthode (celle du départ), la période, le dépôt dans `mission/sources/`, la règle d'exclusion écrite d'avance. Neuf familles à couvrir (par un `IND-xx`, un terme
   de 50 §2 ou un relevé de 70 §5) ou à déclarer « non relevées : raison » : volume · temps humain complet · erreurs · qualité · satisfaction · adoption active · coûts d'usage ·
   incidents · maintenance. Un indicateur d'adoption, de coût ou de maintenance absent de 60 §14 se signale comme trou de 60. Le client
   remet des compteurs et des durées, jamais des données personnelles. **Sans données**, le livrable s'arrête là : c'est la demande, rien n'est `[F]`, la prochaine lecture
   est datée.
3. **Contrôler les relevés avant de les croire.** Cohérence (volumes contre l'export, semaines manquantes, doublons), comparabilité (méthode, période, périmètre, saison),
   version en service contre la dernière version validée au registre de 90 : une différence marque la période « version non validée ». Un relevé incomparable est marqué tel,
   jamais corrigé en silence.
4. **Comparer au départ et au business case.** Par indicateur : départ, observé (période, source, statut), écart, seuils franchis ou non. Par terme de `50-rentabilite.md`
   §2 : estimé (bas, central, haut), observé, position dans l'éventail ; puis chaque condition du point mort de `50-rentabilite.md` §4, qui passe ou non. Attribution : celle de
   60 §14, sinon « a contribué à » ; lister les autres changements de la période. Le gain partagé entre simplifications et construction garde la répartition de
   `20-diagnostic.md` §9 : une minute ne se compte qu'une fois (`references/mesure.md`, §2).
5. **Recalculer le gain et les coûts réels** avec les formules de `chiffrer-rentabilite` (`references/formules.md`, qu'on ne redéfinit pas) et les valeurs observées : gain brut,
   construction réelle (payée, mobilisée), fonctionnement et coûts d'usage, maintenance, incidents, gain net observé, retour constaté (cumul réel), projeté `[E]` (formule de 50 §4) ou « pas de retour ». Calcul montré.
   Un terme observé en exploitation contient déjà l'adoption : ne pas la lui réappliquer. Le temps libéré n'est de l'argent que si l'usage nommé a eu lieu (`references/mesure.md`, §3).
6. **Lire de vrais cas.** Échantillon tiré avant lecture (au hasard, plus les réclamations et les cas à risque de 60 §12), lu par un rôle du client, jamais par le dispositif.
   Classer les échecs par catégorie (celles de la recette ; pour l'IA, celles des `EV-xx`) et par mode de découverte : alerte, lecture, réclamation. Un échec trouvé hors alerte est
   un échec silencieux : il appelle une alerte de plus. Rapprocher des histoires du pré-mortem (70 §8) et des risques `R-xx` : lesquels se sont produits, quel signal a parlé. Si la
   solution contient de l'IA, demander à `tester-solution` de rejouer le jeu d'évaluation sur la version en service (`references/mesure.md`, §4).
7. **Passer les trois cas difficiles** : adoption nulle ou presque, gain net devenu négatif, changement non approuvé. Pour chacun, écrire « non constaté », ou le constat et la
   conduite (`references/mesure.md`, §5).
8. **Proposer la décision.** Règles par défaut `[H]` à confirmer par le décideur (`references/mesure.md`, §6) : continuer · corriger (révision : action, rôle, date de re-mesure) ·
   étendre (candidat nommé, nouveau business case avec les valeurs observées) · arrêter (retrait, fin des coûts récurrents). Pour arbitrer, appeler `router-consulting-strategy`
   (lentille options stratégiques, hypothèses restantes) ; le livrable reste celui de cette étape. Écrire la décision en tête, trois raisons au plus, ce qui la renverserait. Les actions
   sur les outils réels (correction, extension, retrait) passent par `piloter-mise-en-service`.
9. **Dire ce que la mesure change pour le portefeuille.** Quels paramètres communs sont maintenant observés (part réemployée, adoption, maintenance, fonctionnement, montée en charge),
   quels cas de `02`, `03` et `04` en dépendent, lesquels se reclassent ou se rouvrent. La correction d'un de ces livrables se fait par version datée et ligne « correction » au journal,
   par la compétence qui le possède. Sans porte découverte : ce qui servira aux cas suivants du même client (`references/mesure.md`, §7).
10. **Dater, versionner, finir par la décision attendue.** Chaque revue produit une nouvelle version de `95-mesure.md` (période, décision, historique des revues) ; le journal reçoit une ligne
    par décision. Le cas se clôt (`router-mission-ia`) quand la mesure en régime établi est rendue et la décision prise. Si le client renonce à fournir des relevés, le journal le dit : le gain
    reste estimé, rien n'est `[F]`, et le cas peut se clore sans mesure.

## Le livrable

Le modèle complet, les tableaux, la demande de données et les pièges sont dans `references/modeles.md` : l'ouvrir pour rédiger. La méthode (statuts, comparabilité, recalcul avec un exemple, échecs,
cas difficiles, règles de décision, portefeuille) est dans `references/mesure.md`. Les titres ci-dessous sont ceux du modèle.

Squelette de `mission/cas-<slug>/95-mesure.md` :

```markdown
# Mesure — <titre court du cas>
Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle) · Rédigé par · Version · Période mesurée (du … au …, périmètre) · Sources : 20, 50, 60 §14, 70 §6, 90 (versions lues)
Lecture : première lecture | revue n° k — données reçues le … | aucune donnée : ce document est la demande de relevés
## 1. Données reçues et leurs limites — qui a relevé, quelle période, quelle méthode, version en service, ce qui manque
## 2. Indicateurs — départ, observé, écart, seuils de 60 §14, par famille de mesure
## 3. Business case terme par terme — estimé, observé, point mort
## 4. Gain et coûts réels — gain brut, coûts, gain net observé, retour constaté ou projeté
## 5. Adoption et usage — occurrences passées par le dispositif, contournements, par rôle
## 6. Cas lus, échecs et incidents — échantillon, catégories, mode de découverte
## 7. Cas difficiles — adoption nulle · gain devenu négatif · changement non approuvé
## 8. Décision — continuer · corriger · étendre · arrêter, ce qui la renverserait, actions
## 9. Ce que la mesure change pour le portefeuille
## 10. Historique des revues — version, date, période, décision
## Décision attendue
```

Lignes de journal, au moment où le décideur tranche (exemples fictifs, une par décision possible) :

```markdown
- 2027-01-12 · cas-saisie-commandes · 95-mesure, première lecture : « corriger » décidé par la direction commerciale · « adoption à 72 %, maintenance à 6 h par mois ; formation de la seconde équipe, relecture du modèle ; nouvelle lecture le 2027-02-09 »
- 2027-02-09 · cas-saisie-commandes · 95-mesure version 1.1 : « continuer » décidé par la direction commerciale · « seuils respectés deux lectures de suite ; extension à rediscuter à la revue de juin »
- 2027-06-08 · cas-saisie-commandes · 95-mesure version 1.2 : « étendre » décidé par la direction commerciale · « la seconde équipe entre par chiffrer-rentabilite avec les valeurs observées »
- 2027-03-09 · cas-saisie-commandes · 95-mesure : « arrêter » décidé par la direction commerciale · « retrait par les actions A-12 à A-15 de 90-mise-en-service ; retour à l'option 0 »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Le réel s'écrit dans 95, l'estimation de 50 reste intacte | on doit pouvoir dire sur quelle estimation on a décidé, et d'où vient l'écart | remplacer `[E]` par `[F]` dans 50 | jamais |
| `[F]` seulement sur relevé daté, avec source, méthode et propriétaire | un chiffre de mémoire rassure et ne se défend pas six mois plus tard | accepter les déclarations de l'équipe comme mesures | la déclaration est signée par le rôle qui mesure, avec sa méthode : elle devient un relevé |
| Les traces techniques ne prouvent pas un gain | une exécution réussie peut produire un mauvais résultat | compter exécutions et volumes comme gain | la trace porte elle-même le résultat métier (un temps horodaté par le processus) : elle devient une source de mesure |
| Un échantillon de cas lus par un humain | un échec silencieux ne déclenche aucune alerte | se fier aux alertes et aux tableaux de bord | une alerte éprouvée couvre déjà tous les cas |
| Règles d'exclusion écrites avant la lecture | écarter après coup les mauvaises semaines fabrique un bon résultat | nettoyer les données au fil de la lecture | jamais |
| Décision par règles écrites `[H]`, confirmées par le décideur | des règles évitent de décider selon l'humeur de la revue | une décision libre à chaque revue | le décideur fixe d'autres règles par écrit : elles remplacent celles-ci |
| Une version de 95 par revue | une mesure se suit dans le temps | un fichier par revue | le cas dure assez pour qu'un fichier par période soit plus lisible |
| Arrêter est une décision normale | un dispositif qui coûte plus qu'il ne rapporte se paie chaque mois | poursuivre par défaut | jamais |

## Frontières

- La mesure de départ, les causes → `auditer-processus`. Les formules, les hypothèses, le point mort, le business case → `chiffrer-rentabilite`. Les indicateurs, leurs seuils et leur
  attribution → `rediger-cahier-des-charges` (60 §14) ; un seuil manquant se corrige là, par version datée. Le rythme des revues, les actions aux seuils, le pré-mortem → `planifier-deploiement`.
- Les actions de correction, d'extension ou de retrait sur des outils réels → `piloter-mise-en-service`. Une correction technique → `construire-solution`, puis `tester-solution`.
- Le portefeuille : `02` → `decouvrir-cas-usage`, `03` → `chiffrer-rentabilite`, `04` → `planifier-deploiement`. L'état de la mission et le journal → `router-mission-ia`.
- Hors du pack : installer des compteurs et collecter les données à la place du client, évaluer des personnes, conclure sur la conformité. Pour un outil de mesure précis ou un composant d'IA en
  production : `COMPAGNONS.md` du pack, ligne de l'étape 95 ; sans compagnon, la méthode ci-dessus est le repli maison.

## Preuves restantes

- Écrite le 2026-10-12 pour le pack V2. Essayée une fois sur la mission fictive de `examples/` : demande de relevés (version 1.0), première lecture (version 1.1), puis une correction datée (version 1.2),
  sur des relevés inventés (« simulée ») mais avec un calcul réel (`95-mesure/calculs-v1.2.py` redonne chaque nombre du document). Trois cas difficiles lus : gain net négatif (constaté, −129 € décomposé
  terme par terme, retour écrit « pas de retour »), changement non approuvé (constaté, écrit comme incident avec sa suite en `A-xx`), adoption nulle (examinée, non constatée : 75 %). Une lecture de 54 cas
  a trouvé 3 échecs silencieux ; la décision « corriger » porte sa règle d'arrêt. La version 1.1 avait inventé des « régimes corrigés » pour projeter un retour : la règle d'une seule formule les a retirés.
  Non essayés : « étendre », « arrêter », la seconde lecture et la qualité des relevés d'un vrai client.
- NON MESURÉ : le premier cas réel dira si le client fournit les relevés demandés, si l'échantillon de cas lus est tenable, si les règles de décision par défaut départagent bien, et si dix rubriques
  sont trop ou trop peu. Le chiffre d'un gain ne vaut que par la qualité du relevé : un client qui ne relève rien ne reçoit qu'une demande de relevés.
- Sources et crédits : les compagnons de cette étape et leurs licences sont dans `COMPAGNONS.md`. La méthode est écrite avec nos mots : comparaison avant et après sur périodes comparables, témoin,
  lecture d'échantillon et revue de bénéfices sont des pratiques courantes, aucun texte repris. Les formules viennent de `chiffrer-rentabilite`.
