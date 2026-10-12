---
name: chiffrer-rentabilite
description: >-
  Quand on se demande si une automatisation ou un agent IA vaut son coût (« est-ce rentable ? »,
  « combien ça coûte, combien ça rapporte ? ») → chiffrer gains et coûts avec des hypothèses
  visibles : un ordre de grandeur par cas à creuser pour classer un portefeuille, ou un business case
  en trois scénarios pour décider d'une option, maintenance comprise, selon le critère
  d'investissement de l'entreprise quand elle en a un. Étape de chiffrage des deux portes du pack
  consultant-ia, après le tri des cas (porte « aucun besoin ») ou la comparaison des solutions
  (porte « besoin connu »). Triggers : « chiffrer », « rentabilité », « ROI », « business case »,
  « retour sur investissement », « délai de retour », « payback », « analyse coûts-bénéfices »,
  « est-ce que ça vaut le coup », « TCO », « cost-benefit ».
metadata:
  scope: "le chiffrage de cas d'automatisation ou d'IA : ordre de grandeur des cas à creuser d'un portefeuille, ou business case d'une option retenue et de son option de repli"
  owns: "gains, coûts de construction (payé et mobilisé), de fonctionnement et de maintenance, délai de retour, apport d'une option qui en suit une autre, trois scénarios, point mort, classement selon le critère de l'entreprise, valeur non financière nommée, valeurs à relever avant et après déploiement"
  consumes: "mission/02-portefeuille.md et 01-cartographie-taches.md (porte aucun besoin) ; mission/cas-<slug>/10-besoin.md, 20-diagnostic.md et 40-solutions.md (porte besoin connu) ; mission/sources/ (tarifs, devis, coût horaire chargé, critère d'investissement de l'entreprise)"
---

# Chiffrer la rentabilité

<!-- capitaliser:squelette-v1 -->

<!-- dev-qa-link -->
> 🔗 **Lien Dev / Test / QA.** Produit `mission/03-chiffrage.md` (ordre de grandeur) ou
> `mission/cas-<slug>/50-rentabilite.md` (business case). Preuve : le décideur tranche — y aller, ne
> pas y aller ou mesurer d'abord — et la décision s'inscrit dans `mission/journal.md`. Contrôle de
> forme : le modèle est complet (cinq rubriques pour l'ordre de grandeur, sept pour le business case),
> chaque nombre a son statut `[F]`, `[H]` ou `[E]` (définis dans `ARCHITECTURE.md`), la ligne de
> maintenance est présente, un business case porte trois scénarios et un point mort, et les dérivés
> sont calculés sur des valeurs non arrondies. Exemple de référence : `examples/` du pack.
> **Boucle** : aucune.

## Ce que cette compétence résout

Le gain annoncé d'une automatisation est la partie visible d'un calcul ; ce qui le fait mentir, ce
sont les lignes oubliées : maintenance, coût à plein volume, équipe qui ne s'en sert qu'à moitié,
temps libéré sans usage. Ce chiffrage pose le calcul complet, avec des hypothèses contestables une
à une.

Il travaille à deux niveaux. L'**ordre de grandeur** (porte « aucun besoin ») donne à chaque cas que la
direction décide de creuser des fourchettes qui suffisent à classer et à choisir ceux qui méritent une
étude. Le **business case** (porte « besoin connu ») compare l'option retenue et son option de repli en
trois scénarios, et dit où la décision bascule.

Résultat attendu : un tableau ou une fiche où chaque nombre dit d'où il vient, et une
recommandation — y aller, ne pas y aller ou mesurer d'abord — que le décideur peut renverser.

## Stratégie

1. **Deux niveaux, deux précisions.** Un portefeuille se classe avec des fourchettes larges, et
   seulement pour les cas que la direction décide de creuser : chiffrer finement un cas qui sera
   peut-être écarté est du temps perdu. Une décision d'investissement demande l'inverse. Un ordre de
   grandeur ne se présente jamais comme un business case.
2. **Chaque terme porte son statut.** `[F]` fait (relevé, pièce, devis daté, critère ou contrainte
   énoncés par leur détenteur, valeur proposée puis acceptée à la validation) ; `[H]` hypothèse, avec
   le rôle qui peut la confirmer ; `[E]` estimation, calcul montré. Définitions : `ARCHITECTURE.md`.
   Tout résultat est `[E]` : il hérite de la fragilité de son terme le plus faible, et le livrable le dit.
3. **Le coût complet, avec la ligne qu'on oublie.** Construction (payée et mobilisée), fonctionnement et
   maintenance figurent toujours, même pour un outil du marché : sans la maintenance, l'erreur va dans
   le sens qui rassure. La maintenance se chiffre au coût horaire de celui qui la fait.
4. **Du temps gagné n'est de l'argent que s'il est réemployé.** On dit ce que devient le temps
   libéré ; sans usage nommé, il compte comme valeur non financière, pas comme euros. Même règle pour
   l'adoption : si seule une partie de l'équipe s'en sert, on ne compte que cette part du gain.
5. **Un même gain ne se compte qu'une fois.** Quand une option en suit une autre (simplifier, puis
   construire), le gain se répartit entre les deux, et la seconde se juge sur son apport, pas sur le
   gain total.
6. **Des fourchettes et un point mort, pas un chiffre.** Trois scénarios qui font varier les deux ou
   trois hypothèses les plus incertaines, et le seuil où la décision bascule (« reste rentable tant
   que le temps gagné dépasse N minutes par occurrence »). Le décideur voit ce qu'il parie.
7. **Estimé n'est pas mesuré.** On décide vite sur des estimations à la louche, puis on les corrige
   avec le réel : mesure de départ définie avant le déploiement, valeurs relues après.
8. **La valeur non financière se nomme, elle ne se convertit pas.** Qualité, risque, satisfaction,
   délai client : écrits à côté du calcul, pas transformés en euros, qui auraient l'air d'un fait.

## Étapes

1. **Choisir le niveau.** Un portefeuille à trier (`mission/02-portefeuille.md`) → ordre de grandeur, pour
   les seuls cas que la validation du portefeuille a décidé de creuser ; les autres ne sont pas chiffrés et
   le livrable le dit. Un cas dont `40-solutions.md` désigne une option retenue et une option de repli →
   business case, qui fait alors foi pour ce cas même s'il a déjà un ordre de grandeur (resté comme trace
   du tri). Le business case explique en une phrase l'écart avec cet ordre de grandeur (phases, périmètre,
   hypothèses) ; si l'écart révèle un trou de `03-chiffrage.md`, on le corrige par une version datée et une
   ligne « correction » au journal (`ARCHITECTURE.md`).
2. **Lire ce qui existe.** Volumes, temps, erreurs : `01-cartographie-taches.md` ou
   `20-diagnostic.md` ; critères de succès et mesure de départ : `10-besoin.md` ; options :
   `40-solutions.md` ; tarifs, devis, coût horaire : `mission/sources/`. Un `[H]` recopié reste `[H]`.
3. **Fixer les paramètres communs** : coût horaire chargé par rôle (`[F]` s'il vient de l'entreprise,
   sinon `[H]` avec son confirmateur ; jamais une moyenne de marché), base HT ou TTC (la même
   partout), taux d'adoption, montée en charge, horizon de lecture (douze mois, vingt-quatre au plus :
   au-delà, le processus et les outils auront changé). Si l'entreprise a un critère d'investissement
   (« retour en dix-huit mois »), l'écrire ici en `[F]`, avec sa source : l'entretien ou le journal.
4. **Poser les gains et les coûts** avec les formules suivantes. Chaque terme d'entrée est `[F]` ou
   `[H]` ; chaque ligne de résultat est `[E]`.

   ```text
   gain brut mensuel      = ( occurrences/mois × minutes gagnées ÷ 60 × part réemployée × coût horaire chargé
                              + erreurs évitées/mois × coût d'une erreur
                              + autres gains mensuels, chacun justifié ) × taux d'adoption
   coût de construction   = payé (jours × taux journalier, ou devis, + coûts uniques annexes)
                            + mobilisé (heures des équipes : pilote, recette, formation)
   fonctionnement/mois    = abonnements + exécutions (selon l'unité de facturation) + modèles d'IA
   maintenance/mois       = heures de maintenance × coût horaire chargé de celui qui la fait
   gain net mensuel       = gain brut − fonctionnement − maintenance
   délai de retour (mois) = coût de construction ÷ gain net mensuel (+ manque à gagner de la montée en charge)
   ```

   Le délai de retour compte le payé et le mobilisé ; le délai « payé seul » s'affiche à côté. Les
   « minutes gagnées » comptent la relecture humaine. Un autre gain (délai, chiffre d'affaires) se justifie
   par un mécanisme et se compte en marge. Montants à l'euro, durées à la minute, délais au dixième de mois ;
   les dérivés se calculent sur les valeurs non arrondies, et un arrondi s'écrit « environ ». Ouvrir
   `references/formules.md` pour les unités de facturation, la montée en charge, l'option qui en suit une
   autre, le point mort, les arrondis et un exemple de calcul.
5. **Séparer trois lectures du coût** : payé (devis, abonnements) ; mobilisé (heures des équipes pour
   le pilote, la recette, la formation : sans facture, mais réelles) ; optimisé (remise ou volume
   non signés : scénario haut seulement). Un outil déjà en place coûte peu à la marge, pas rien :
   décider sur le coût marginal, afficher le coût complet. Tout tarif relevé porte sa date.
6. **Faire varier.** Ordre de grandeur : une fourchette bas–haut par cas, écrite « bas–haut (central) » ;
   trois hypothèses communes la font varier (minutes gagnées, part réemployée, taux d'adoption), les autres
   termes restent au central, sans classement de sensibilité à ce niveau. Business case : bouger chaque
   hypothèse seule pour repérer les deux ou trois qui déplacent le résultat (elles peuvent différer de celles
   de l'ordre de grandeur : le business case fait foi), construire bas, central et haut avec elles, puis
   calculer le point mort (méthode en référence). Un scénario bas dont le gain net est négatif s'écrit « ne se
   rembourse pas » ; on dit alors sous quel gain brut mensuel le dispositif coûte plus qu'il ne rapporte.
7. **Chiffrer une option qui en suit une autre.** Si l'option retenue vient après des simplifications (option
   0 de `40-solutions.md`), la situation de référence de la seconde est l'état après la première. Le calcul
   gagne une colonne « apport de l'option » : ce que la seconde ajoute à la première. Le gain se répartit
   entre les deux comme dans `20-diagnostic.md` §9, chaque minute n'étant comptée qu'une fois ; la décision
   d'investir se lit sur l'apport.
8. **Classer ou recommander.** La logique est fixe. *Solide* : même le scénario bas passe → recommander d'y
   aller. *À mesurer d'abord* : le central passe, le bas non, et une mesure courte peut lever l'hypothèse
   fragile. *Douteux* : le central ne passe pas. Ce que « passe » veut dire dépend du critère. Par défaut, deux
   repères d'alerte (issus d'une source citée en « Preuves restantes » ; non mesurés ici) : un délai de retour
   au-delà d'environ douze mois rend le cas douteux ; une maintenance au-delà de 30 à 50 % du gain brut
   signale une charge, pas un outil. Si l'entreprise a son propre critère (étape 3), il remplace ces repères
   dans la même logique, et les repères du pack restent affichés à côté, en alerte. Le décideur peut renverser
   la recommandation : sa décision s'inscrit au journal. « Mesurer d'abord » n'empêche pas de préparer la
   spécification quand la mesure est déjà au calendrier ; la construction, elle, attend la porte.
9. **Définir la mesure** : avant le déploiement, les valeurs `[H]` à relever (comment, par qui) ;
   après, les valeurs à relire pour remplacer l'estimation par le réel. Indicateurs et seuils :
   `rediger-cahier-des-charges` (spécification) ; rythme des revues et action à chaque seuil :
   `planifier-deploiement`.
10. **Nommer la valeur non financière**, rédiger avec le modèle ci-dessous, finir par la décision
    attendue. Suite : `planifier-deploiement` (feuille de route) après un ordre de grandeur ;
    `rediger-cahier-des-charges` (mode spécification) après un business case « on y va ». Quand le
    décideur tranche, ajouter une ligne à `mission/journal.md`.

## Le livrable

Le modèle complet, ses consignes de remplissage et ses tableaux sont dans `references/modeles.md` : l'ouvrir
pour rédiger. Les titres ci-dessous sont ceux du modèle.

Squelette de `mission/03-chiffrage.md` (ordre de grandeur, porte « aucun besoin ») :

```markdown
# Chiffrage — ordre de grandeur du portefeuille
Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle) · Rédigé par · Sources lues
## 1. Paramètres communs — valeur, statut, source ; le critère d'investissement de l'entreprise s'il existe
## 2. Un cas par ligne, en fourchettes bas–haut — chaque cellule en bas–haut (central), les cas à creuser seulement
## 3. Classement — solides · à mesurer d'abord · douteux, une raison par cas
## 4. Hypothèses à confirmer
## 5. Hors chiffrage
## Décision attendue
```

Squelette de `mission/cas-<slug>/50-rentabilite.md` (business case, porte « besoin connu ») :

```markdown
# Rentabilité — <titre court du cas>
Date · Demandeur (rôle) · Valideur (rôle) · Décideur (rôle) · Rédigé par · Options chiffrées (de `40-solutions.md`) : <retenue> / <repli>
## 1. Situation de référence
## 2. Hypothèses et mesure
## 3. Calcul par option — retenue, repli, et l'apport de l'option quand elle en suit une autre
## 4. Trois scénarios et point mort
## 5. Temps libéré et adoption
## 6. Valeur non financière
## 7. Recommandation
## Décision attendue
```

Lignes de journal, au moment où le décideur tranche (étiquette « découverte » pour `03-chiffrage.md`) :

```markdown
- 2026-10-21 · découverte · 03-chiffrage validé par la direction des opérations · « les cas solides sont retenus, celui qui dépend d'une hypothèse attend une mesure »
- 2026-10-28 · cas-saisie-commandes · 50-rentabilite : « mesurer d'abord » décidé par la direction commerciale · « relever le temps réel et nommer l'usage du temps libéré »
- 2026-11-05 · découverte · 03-chiffrage corrigé (version 1.1 : un central réunit deux effets que le diagnostic sépare) · confirmé par la direction des opérations
```

## Décisions et rejets

| Décision | Pourquoi | Option écartée | Se rouvre si |
|---|---|---|---|
| Fourchettes pour trier, trois scénarios pour décider ; l'ordre de grandeur ne chiffre que les cas à creuser | un portefeuille ne se chiffre pas au détail, une décision d'investissement ne se prend pas sur un ordre de grandeur | un seul niveau de détail pour tous les cas, ou le chiffrage de tout le portefeuille | le portefeuille ne compte qu'un ou deux cas : on passe directement au business case |
| La maintenance est une ligne obligatoire, même pour un outil du marché | c'est la ligne qu'on oublie, et l'omettre fausse le calcul dans le sens qui rassure | la fondre dans le fonctionnement sans la montrer | un engagement écrit d'un fournisseur couvre corrections et évolutions `[F]` : la ligne reste, réduite à la supervision interne |
| Le délai de retour compte la construction payée et mobilisée ; le délai « payé seul » s'affiche à côté | les heures des équipes sont réelles même sans facture ; le payé seul dit ce que le décideur sort de sa poche | le payé seul pour tous les calculs | l'équipe n'a aucun autre usage de ces heures et l'entreprise décide sur le coût marginal : le payé seul porte la décision, le complet reste affiché |
| Une option qui en suit une autre se juge sur son apport | le gain total attribuerait à la construction ce que les simplifications retirent seules | chiffrer chaque option contre l'état d'origine | les deux options portent sur des étapes différentes et leurs gains s'additionnent sans recouvrement |
| Le temps libéré sans usage nommé ne compte pas en euros | du temps qui se dilue dans l'agenda ne réduit aucune dépense et n'augmente aucune recette | compter toutes les heures au coût horaire chargé | le responsable de l'équipe nomme l'usage (volume absorbé sans embauche, heures supplémentaires évitées…) |
| La valeur non financière se nomme, sans équivalent en euros | un chiffre inventé a l'air d'un fait et fausse la comparaison | chiffrer la satisfaction ou le risque | l'entreprise dispose d'une valeur interne établie, par exemple le coût d'un incident passé `[F]` |
| Le critère de l'entreprise remplace les repères du pack dans la même logique de classement ; les repères restent en alerte | douze mois et 30 à 50 % viennent de la pratique d'un auteur, pas d'une mesure ; un cas un peu au-delà peut être juste s'il est stratégique | un rejet automatique au-delà des repères, ou deux verdicts qui se contredisent | l'entreprise n'a pas de critère : les repères du pack s'appliquent seuls |
| Décider sur des estimations, puis corriger avec le réel | attendre des mesures complètes retarde une décision souvent réversible | exiger des mesures avant tout chiffrage | la décision est coûteuse ou difficile à défaire : « mesurer d'abord » devient la recommandation |

## Frontières

- Les temps, volumes et erreurs actuels, et leurs causes → `auditer-processus`.
- Le tri des cas et leur portefeuille → `decouvrir-cas-usage` ; les options à comparer et la
  recommandation de solution → `concevoir-solution`.
- Le critère d'investissement de l'entreprise est une contrainte du cadrage (`cadrer-besoin`) : ici on
  l'applique, on ne le fixe pas.
- Les exigences, la spécification, les indicateurs et leurs seuils → `rediger-cahier-des-charges`.
- L'ordre de mise en œuvre, les jalons, le rythme des revues et l'action à chaque seuil →
  `planifier-deploiement`.
- L'état de la mission et le journal des décisions → `router-mission-ia`.
- Facultatif : `router-consulting-strategy` (lentille « business case ») et `automation-strategy`
  (décision d'automatiser, choix de plateforme selon l'unité de facturation) s'ils sont installés
  dans la session. Ne dire qu'on les a utilisés que s'ils ont réellement été appelés.

## Preuves restantes

- Éprouvée sur la mission fictive du 12/10/2026 (`examples/`, ordre de grandeur et business case), qui a
  relevé 94 frictions dans le pack ; celles qui touchent le chiffrage sont corrigées ici (colonne du
  central, cas à creuser, construction payée et mobilisée, apport d'une option, arrondis, critère de
  l'entreprise).
- NON MESURÉ sur une mission réelle : le premier cas réel dira si les fourchettes tiennent, si
  l'entreprise fournit un coût horaire chargé, si les repères de douze mois et de 30 à 50 % aident le
  décideur, si la colonne « apport de l'option » se lit sans effort, et quel écart sépare le gain estimé
  du gain relevé (le pack n'a pas de boucle de mesure après déploiement : c'est l'entreprise qui mesure).
- Sources et crédits : adapté d'Eric Risco, « automation-strategy » (licence MIT,
  https://github.com/ericrisco/rsc-harness) : formule de retour avec ligne de maintenance, repères de
  douze mois et de 30 à 50 % ; et de gcamilo, « management-consulting » (licence MIT,
  https://github.com/gcamilo/management-consulting) : fourchettes bas–central–haut, sensibilité,
  normes de preuve. Les exemples chiffrés de ces sources ne sont pas repris.
