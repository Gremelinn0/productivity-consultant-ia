---
name: auditer-processus
description: >-
  Quand un besoin est cadré et qu'il faut comprendre comment le travail se fait vraiment avant de
  décider quoi que ce soit (« comment ça se passe aujourd'hui ? », « où perd-on du temps ? », « est-ce
  prêt à être automatisé ? ») → décrire le processus actuel, le mesurer, trouver goulets et
  gaspillages, remonter à des causes sur lesquelles on peut agir, tester sa stabilité, trier chaque
  étape (éliminer, simplifier d'abord, automatiser, déléguer à l'IA, garder) et fixer ce qu'il faut
  simplifier ou standardiser avant toute automatisation. Deuxième étape de la porte « besoin connu »
  du pack consultant-ia, après cadrer-besoin ; alimente rediger-cahier-des-charges (mode exigences).
  Triggers : « audit de processus », « cartographier le processus », « process mapping », « où
  perd-on du temps », « goulet d'étranglement », « avant d'automatiser », « le processus est-il
  stable », « process audit ».
metadata:
  scope: "un processus nommé et cadré, de la description de l'existant au diagnostic, avant tout choix de solution"
  owns: "le diagnostic : carte du processus actuel, mesures, goulets, causes, test de stabilité, tri par étape en cinq issues, simplifications à faire d'abord, opportunités classées"
  consumes: "mission/cas-<slug>/10-besoin.md ; mission/sources/ ; la fiche du cas dans mission/02-portefeuille.md et ses lignes de 01-cartographie-taches.md ; les réponses des personnes qui font le travail"
---

# Auditer le processus

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/cas-<slug>/20-diagnostic.md`. Preuve : le demandeur valide
> les causes à traiter et les simplifications à faire avant toute automatisation, et la décision
> s'inscrit dans `mission/journal.md`. Contrôle de forme : le diagnostic porte ses neuf rubriques, chaque
> étape son issue parmi cinq (ou « hors périmètre »), chaque nombre son statut `[F]`, `[H]` ou `[E]`
> (définis dans `ARCHITECTURE.md`). Exemple de référence : `examples/` du pack. **Boucle** : aucune.

## Ce que cette compétence résout

Une fiche besoin dit ce qu'on veut obtenir ; elle ne dit pas comment le travail se fait aujourd'hui. Un processus
décrit de mémoire donne la version théorique, celle des procédures, pas celle des contournements — or c'est le
travail réel qu'il faudra transformer. Automatiser la version théorique construit un outil qui ne colle pas au
travail ; automatiser un processus instable donne un chaos automatisé, avec une facture de maintenance.

Cette compétence décrit le processus tel qu'il se déroule, le mesure, repère où le temps et la qualité se perdent,
remonte aux causes, et dit ce qu'il faut supprimer, simplifier ou standardiser avant de penser à automatiser.
Résultat attendu : un diagnostic qui permet de décider quelles causes traiter et quelles simplifications faire
d'abord.

## Stratégie

1. **Observer plutôt que se faire raconter.** L'enregistrement d'une personne qui fait la tâche (vidéo ou partage
   d'écran, avec son accord) montre ce qu'on omet par habitude : contrôles informels, copier-coller, fichiers « à
   côté ». Ces contournements sont l'information ; aucune procédure écrite ne les contient.
2. **Mesurer avant de changer.** Sans point de départ, aucun gain ne se démontre. Chaque nombre porte son statut :
   `[F]` fait (relevé, pièce, observation, règle énoncée par son détenteur), `[H]` hypothèse (avec qui la confirme),
   `[E]` estimation (calcul montré) ; définitions dans `ARCHITECTURE.md`. Ce qui n'est pas mesuré se dit, avec le moyen
   de le mesurer.
3. **Chercher des causes, pas des coupables.** On demande « pourquoi » jusqu'à une cause sur laquelle on peut agir,
   et on nomme sa nature (processus, organisation, donnée ou outil) : elle dit qui peut agir. Les personnes ne sont
   jamais jugées ; on écrit des rôles.
4. **Tester la stabilité avant de parler d'automatisation.** Si trois personnes font la tâche de trois façons, ou si
   les règles ne sont écrites nulle part, on standardise d'abord : automatiser le chaos donne un chaos automatisé.
5. **Supprimer, simplifier, standardiser — puis automatiser.** Les simplifications passent avant les
   automatisations, même quand leur gain est plus petit : elles conditionnent le reste.
6. **Un diagnostic n'est pas une solution.** On classe des opportunités, on ne choisit pas l'outil : la comparaison
   des options appartient à `concevoir-solution`, qui doit pouvoir conclure qu'il ne faut rien construire.

## Étapes

1. **Lire ce qui existe** : `10-besoin.md` (périmètre, critères de succès, mesures de départ connues),
   `mission/sources/` et, si le cas vient de la porte découverte, sa fiche dans `02-portefeuille.md` et ses lignes
   de `01-cartographie-taches.md`. Ne pas redemander ce qui s'y trouve.
2. **Choisir la source de la description**, par ordre de préférence : l'enregistrement d'une personne qui fait
   réellement la tâche (transcription déposée dans `mission/sources/`, protocole dans `decouvrir-cas-usage`) ; un
   entretien sur la dernière occurrence réelle (« la dernière fois que… ») ; une procédure écrite, notée `[H]`
   « théorique » tant qu'elle n'est pas confrontée au réel. Observer deux personnes quand c'est possible : leurs
   écarts nourrissent le test de stabilité.
3. **Décrire le processus** : étapes (un verbe, un objet), rôle, outil, entrées et sorties, passages de main,
   attentes, points de décision, exceptions (et la conduite à tenir quand elles arrivent), variantes (ce qui
   change d'une personne, d'un client ou d'un cas à l'autre), étapes hors périmètre comprises. Ajouter un schéma Mermaid si le flux
   comporte des branches. Faire relire la description par une personne qui fait le travail, pas seulement par son
   responsable, et écrire dans l'en-tête qui a relu et quand ; sans relecture possible, l'écrire.
4. **Mesurer** : volume, fréquence, temps par étape, délai total comparé au temps de travail effectif, taux d'erreur
   ou de reprise (part des occurrences qui reviennent à une étape précédente), temps d'attente. Séparer cas simples
   et cas complexes : une moyenne cache la variabilité. Une durée chronométrée sur une seule occurrence est `[F]`
   pour cette occurrence et `[H]` comme durée typique ; une ligne par mesure et par statut. Si rien n'est mesuré,
   écrire comment le faire — chronométrer un échantillon d'occurrences, compter pendant une semaine, demander un
   export. Cette mesure de départ précède tout changement.
5. **Repérer goulets et gaspillages** : ressaisie, copier-coller entre outils, attente de validation, contrôles en
   double, recherche d'information, rapports manuels, exceptions traitées au cas par cas. Les situer sur une étape
   et leur donner un coût `[E]` quand les mesures le permettent. Un délai fait d'attente ne se réduit pas en
   automatisant le travail qui l'entoure.
6. **Remonter aux causes** : demander « pourquoi » jusqu'à une cause sur laquelle quelqu'un peut agir, puis
   l'étiqueter processus, organisation, donnée ou outil (la dominante). Une cause d'organisation (« personne ne
   tient la liste ») ne se règle pas avec un outil.
7. **Tester la stabilité** avec les quatre questions de la rubrique 5. Une réponse négative ne bloque pas le
   diagnostic : elle fait de la standardisation la première opportunité — écrire le mode opératoire du processus
   cible (rubrique 7 : étapes, rôle de chacune, exceptions et conduite à tenir, variantes gardées ou supprimées,
   indicateur de suivi), le tester à la main sur quelques occurrences, re-mesurer, puis seulement automatiser. Si
   une seule personne a été observée, le dire et garder les deux versions du récit.
8. **Trier chaque étape en cinq issues**, avec les critères de la découverte (fréquence, coût, valeur, risque si
   ça se trompe), dans cet ordre de questions :
   - **Éliminer** : prend du temps, apporte peu, personne ne remarquerait sa disparition, ou naît d'une cause qu'on
     peut supprimer (à tester avant « Automatiser ») ;
   - **Simplifier d'abord** : règles floues, étape mécanique d'un processus instable, tâche faite de plusieurs façons :
     standardiser ou simplifier, re-mesurer, puis reclasser l'étape dans une des quatre autres issues ;
   - **Automatiser** : même schéma à chaque fois, relie plusieurs outils, règles stables ;
   - **Déléguer à l'IA** : processus clair, résultat contrôlable ; l'IA prépare ou exécute, un humain valide si
     nécessaire ;
   - **Garder** : jugement, relation, négociation, décision importante ; l'IA peut préparer, comparer, challenger,
     sans porter la responsabilité.

   Pas de « Automatiser » si le test de stabilité est négatif : l'étape reçoit « Simplifier d'abord ». Une étape
   irréversible ou à fort impact (envoi vers l'extérieur, paiement, suppression, décision sur une personne) reste
   sous validation humaine : l'automatisation prépare, un humain valide. Une étape hors périmètre est décrite à la
   rubrique 1 et marquée « hors périmètre » ici, sans issue.
9. **Poser les huit questions d'automatisation qui manquent**, en une seule fois, après avoir cherché la réponse
   dans le besoin, les sources et l'observation :
   1. Quel événement déclenche le processus, et quel résultat doit-il produire ?
   2. Quelles étapes sont stables et répétitives, lesquelles exigent une décision humaine ?
   3. Quels systèmes, comptes et droits faut-il lire ou modifier ?
   4. Quel volume, quelle fréquence, quel niveau de criticité ?
   5. Quelles erreurs sont acceptables, lesquelles doivent bloquer, et qui alerter ?
   6. Quelles données sensibles, règles de conformité ou validations humaines doivent encadrer l'IA ?
   7. Quel cas limite doit absolument fonctionner avant de généraliser ?
   8. Qui maintiendra automatisations, prompts, modèles et accès après livraison ?

   Une réponse manquante devient une hypothèse `[H]` avec la personne qui peut la confirmer. Ces réponses sont
   l'entrée de `rediger-cahier-des-charges` (mode exigences).
10. **Classer les opportunités.** Chaque opportunité (supprimer, simplifier, standardiser, configurer un outil déjà
    en place, automatiser, déléguer à l'IA) reçoit une valeur (gain mensuel `[E]` tiré des mesures de l'étape 4),
    une facilité (données disponibles, règles stables, accès aux outils, peu d'exceptions) et un risque, notés haut,
    moyen ou bas avec une raison d'une ligne, puis une classe :
    - **Gains rapides** : valeur notable, facilité haute, risque bas ou couvert par une validation ; une opportunité
      sans gain direct qui conditionne une autre (procédure unique, liste écrite) porte cette classe, notée « valeur
      indirecte » ;
    - **Projets** : valeur haute mais facilité moyenne ou basse, ou risque qui impose des garde-fous ;
    - **À creuser** : une donnée manquante empêche de classer — écrire laquelle et qui la fournit ;
    - **À écarter** : valeur faible, risque disproportionné ou besoin déjà couvert — écrire la raison.

    Partager le gain entre ce que retirent les simplifications et ce que retire l'automatisation en plus, sans compter
    deux fois les mêmes minutes ; dire quelles opportunités portent sur les mêmes étapes et ne s'additionnent pas.
11. **Rédiger, puis s'arrêter sur la décision.** Remplir le modèle et finir par la décision attendue. Quand le
    demandeur valide, ajouter une ligne à `mission/journal.md`, puis proposer `rediger-cahier-des-charges` en mode
    exigences. Si les mesures ou le partage du gain contredisent un livrable déjà validé (l'ordre de grandeur de
    `03-chiffrage.md`), le corriger par une version datée et une ligne « correction » (`ARCHITECTURE.md`).

## Le livrable

Le modèle complet, ses consignes de remplissage et ses tableaux sont dans `references/modeles.md` : l'ouvrir pour
rédiger. Les titres ci-dessous sont ceux du modèle.

Squelette de `mission/cas-<slug>/20-diagnostic.md` :

```markdown
# Diagnostic — <processus>
Date · Demandeur (rôle) · Valideur (rôle) · Rédigé par · Source de la description · Relue par (rôle, date)
## 1. Le processus tel qu'il se fait — une ligne par étape, hors périmètre comprises ; schéma facultatif
## 2. Mesures — une ligne par mesure et par statut
## 3. Goulets et gaspillages
## 4. Causes — la chaîne des pourquoi, la cause actionnable, sa nature
## 5. Stabilité — quatre questions, un verdict
## 6. Tri des étapes — cinq issues, ou « hors périmètre »
## 7. À simplifier et à standardiser d'abord — l'effet attendu, la mesure, l'échéance ; le mode opératoire du processus cible
## 8. Les huit questions d'automatisation
## 9. Opportunités classées
## Décision attendue
```

Ligne de journal, au moment où le demandeur tranche :

```markdown
- 2026-10-21 · cas-relances-factures · 20-diagnostic validé par la direction financière · « on supprime le double contrôle, puis on écrit la procédure unique avant d'automatiser »
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Observer d'abord, interroger ensuite | un processus décrit de mémoire est la version théorique ; les contournements n'apparaissent qu'à l'écran | un questionnaire adressé au responsable | personne ne peut être enregistré ou le cas est trop rare : entretien sur la dernière occurrence, nombres en `[H]` |
| Mesure de départ avant toute recommandation | sans point de départ, aucun gain ne se démontre | estimer d'abord, mesurer plus tard | le processus est trop rare pour un échantillon : estimation assumée, marquée `[H]` |
| Test de stabilité avant tout « Automatiser » ; sinon « Simplifier d'abord » | automatiser un processus instable fige le chaos et coûte en maintenance | automatiser puis corriger ; ranger une étape mécanique instable dans « Garder » | l'entreprise impose l'automatisation : le risque est écrit dans le diagnostic, la décision est la sienne |
| Causes classées par nature (processus, organisation, donnée, outil) | la nature dicte qui peut agir ; un problème de donnée ne se règle pas par un outil | une liste plate de problèmes | jamais |
| Huit questions posées seulement quand elles manquent | ne pas redemander ce que le besoin ou les sources disent | un questionnaire complet et systématique | le besoin vient d'une source pauvre : les huit passent en questions ouvertes |
| Le diagnostic classe, il ne choisit pas l'outil | choisir ici fermerait les options avant leur comparaison | proposer l'outil dès l'audit | jamais : la comparaison appartient à `concevoir-solution` |

## Frontières

- Le besoin, son périmètre et ses critères de succès → `cadrer-besoin`. Aucun besoin nommé → `decouvrir-cas-usage`.
- Les exigences que la solution doit satisfaire → `rediger-cahier-des-charges` (mode exigences), qui reçoit ce
  diagnostic.
- La décision d'automatiser, la comparaison d'options et le choix d'une plateforme → `concevoir-solution`.
- Le gain et le coût → `chiffrer-rentabilite` ; le calendrier, dont le plan des simplifications →
  `planifier-deploiement`.
- L'état de la mission et le journal des décisions → `router-mission-ia`.
- Pour rédiger le mode opératoire du processus cible, un compagnon existe : `COMPAGNONS.md` du pack, ligne
  « Diagnostiquer ». On ne dit s'en être servi que si on l'a réellement appelé ; sans lui, la rubrique 7 du modèle
  est le repli maison.

## Preuves restantes

- Éprouvée sur la mission fictive du 12/10/2026 (`examples/`), qui a relevé 94 frictions ; celles qui touchent le
  diagnostic sont corrigées ici.
- NON MESURÉ sur une mission réelle : le premier cas réel dira si le diagnostic reste lisible quand le processus
  compte beaucoup d'étapes, si le test de stabilité à quatre questions suffit et si les neuf rubriques sont toutes
  utiles.
- Sources et crédits : les compagnons de cette étape et leurs licences sont dans `COMPAGNONS.md` ; les méthodes
  dont elle s'inspire (description du processus, analyse des gaspillages, test de stabilité, garde-fou humain) sont
  créditées dans la section « Sources et crédits » du `README.md`. Méthode réécrite avec nos mots, aucun passage
  repris.
