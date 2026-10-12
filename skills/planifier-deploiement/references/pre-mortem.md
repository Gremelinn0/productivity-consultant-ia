# Pré-mortem — déroulé, familles d'échec et gabarit

Ouvrir ce fichier pour conduire le pré-mortem d'une feuille de route ou d'un plan de déploiement :
déroulé, familles d'échec à parcourir, façon d'écrire une condition d'arrêt, gabarit de sortie. Le
principe et le verdict sont dans `SKILL.md`. Crédits de la méthode : section « Preuves restantes » de
`SKILL.md`.

## 1. Pourquoi une consigne explicite

Un modèle de langage, comme une équipe soucieuse de rester loyale, tend à approuver ce qu'on lui
soumet. Demander « ce plan tient-il ? » produit des raisons d'être d'accord. Le pré-mortem renverse
la question : l'échec est acquis, il s'agit de l'expliquer. Cette consigne autorise à démolir ; sans
elle, personne ne le fait.

## 2. Déroulé

1. **Figer la thèse** en une ou deux phrases falsifiables : « ce plan mène à <résultat> d'ici
   <échéance> grâce à <dispositif>, utilisé par <équipes> ». Si on ne sait pas l'écrire, le plan est
   trop flou pour être attaqué : le préciser d'abord.
2. **Poser la question au passé** : « nous sommes dans six mois, le projet a échoué : racontez
   pourquoi ». Puis pour couper l'attribution à l'extérieur : « imaginez que l'échec soit entièrement
   de notre fait : qu'avons-nous mal fait ? ».
3. **Écrire seul, puis confronter.** La compétence rédige les histoires à partir du dossier. Si des
   personnes de l'entreprise sont disponibles (utilisateurs, propriétaire du processus, responsable
   technique), chacune écrit seule ses raisons d'échec avant de lire les nôtres, pour ne pas être
   ancrée ; les rôles les moins élevés parlent en premier ; leurs apports sont cités avec leur rôle.
   Si l'environnement permet un second agent, lui confier l'écriture des histoires sans lui montrer
   les parades déjà prévues.
4. **Raconter chaque histoire retenue** comme un récit concret (qui, quoi, quand, avec quel effet),
   puis noter : vraisemblance et gravité (haut / moyen / bas), signal d'alerte précoce (ce qu'on
   verrait avant l'échec), parade (ce qu'on fait maintenant), condition d'arrêt, propriétaire (rôle).
5. **Classer** chaque objection : *bloquante* (la thèse ne tient pas, ou on vise la mauvaise cible ;
   aucune parade possible dans le plan actuel), *à mitiger* (réelle, mais une garde, un test ou un
   ajustement de périmètre la neutralise), *écartée* (théorique, hors périmètre ou déjà couverte :
   nommée avec sa raison, pour ne pas y revenir).
6. **Rendre le verdict.** *Engager* : rien de bloquant, et chaque objection à mitiger a déjà sa
   parade dans le plan. *Durcir* : au moins une objection à mitiger sans parade ; ajouter l'étape, le
   test, le seuil ou la condition d'arrêt, et écrire la version durcie. *Pivoter* : au moins une
   objection bloquante réelle ; changer d'approche (autre cas, autre option de `40-solutions.md`,
   mesurer d'abord). Si rien de bloquant n'apparaît, le dire : inventer des objections pour faire
   sérieux est une faute, comme en taire une.
7. **Rejouer aux jalons** : fin du pilote, avant la mise en production, après la montée en charge.
   Une nouvelle information change le paysage des risques ; un pré-mortem fait une fois et jamais
   relu est un rituel.

Doser selon l'enjeu : un lot réversible qui touche une seule équipe tient sur une demi-page ; un plan
qui touche plusieurs équipes, des données sensibles ou une dépense importante passe les familles
ci-dessous une à une, avec les personnes concernées si possible.

## 3. Les sept familles d'échec d'un plan de déploiement

Parcourir chaque famille, garder celles qui mordent sur ce cas et écrire l'histoire avec ses mots.
Les seuils sont à fixer avec le propriétaire métier (`<seuil>`, `<délai>`, `<multiple>`, `<n>`), à noter
`[H]` jusqu'à validation, jamais empruntés à une moyenne de marché. Un seuil qui porte sur un indicateur
de la spécification n'est pas redéfini ici : citer l'identifiant de l'indicateur et reprendre son seuil.

| Famille | Histoire type (au passé) | Signal d'alerte précoce | Parade | Condition d'arrêt |
|---|---|---|---|---|
| Adoption | l'équipe avait repris l'ancienne méthode : le dispositif ajoutait une étape à ceux qui n'y gagnaient rien | usage sous la cible ; un tableur parallèle réapparaît ; mêmes questions chaque semaine | utilisateur réel dans le pilote ; retirer l'ancienne voie après la bascule ; référent dans chaque équipe | adoption sous `<seuil>` après `<délai>` de correction |
| Qualité des données | les erreurs venaient de données d'entrée incomplètes ou en double, que personne ne possédait | corrections manuelles en hausse ; champs vides ; rejets | propriétaire de la donnée nommé ; contrôle à l'entrée ; échantillon réel au pilote | taux d'erreur au-dessus de `<seuil>` sur `<n>` relevés de suite |
| Processus qui a changé | le processus avait évolué (règle, organisation, produit) ; le dispositif automatisait l'ancienne version | changement annoncé dans le périmètre ; demandes de dérogation | vérifier la stabilité avant de lancer ; propriétaire du processus prévenu de tout changement ; revue à chaque jalon | processus modifié sans mise à jour du dispositif sous `<délai>` |
| Outil ou fournisseur qui change | le fournisseur avait modifié tarifs, conditions ou interface : le dispositif ne marchait plus ou coûtait plus | avis de changement ; erreurs d'authentification ; facture en hausse | suivre les annonces ; option de repli de `40-solutions.md` documentée ; aucun compte personnel au cœur du dispositif | coût mensuel au-delà de `<seuil>`, ou fonction retirée sans contournement |
| Dérive des coûts | la facture d'exécution et de modèles d'IA avait grimpé avec le volume ; personne ne la regardait | coût réel supérieur à l'estimation de `50-rentabilite.md` | relevé mensuel ; plafond ou alerte de dépense ; unité de facturation recalculée au volume réel | coût réel au-delà de `<multiple>` de l'estimation `<n>` mois de suite |
| Panne silencieuse | le traitement s'était arrêté depuis des semaines sans que personne le voie ; on croyait qu'il tournait | résultat attendu absent à l'heure attendue ; compte rendu de succès manquant | alerte sur l'échec et sur l'absence de résultat ; destinataire nommé ; vérification manuelle périodique ; interrupteur | alerte non traitée sous `<délai>` : suspendre et revenir à l'ancienne méthode |
| Départ du responsable | la personne qui faisait vivre le dispositif avait changé de poste ; personne d'autre ne savait le corriger | un seul nom dans la documentation ; accès sur un compte personnel | suppléant formé ; procédure d'une page essayée par un tiers ; comptes de l'entreprise | pas de propriétaire désigné sous `<délai>` après un départ |

## 4. Trois familles de plus pour une feuille de route

| Famille | Histoire type (au passé) | Signal d'alerte précoce | Parade | Condition d'arrêt |
|---|---|---|---|---|
| Trop de cas à la fois | plusieurs cas démarrés ensemble, aucun terminé : l'attention de chaque équipe était dispersée | plus de cas en cours que la première vague prévue ; jalons repoussés | limite de cas simultanés ; un cas ne démarre que quand le précédent a passé sa décision de pilote | tout nouveau départ suspendu tant que la première vague n'a pas décidé |
| Prérequis jamais levé | la donnée ou l'accès commun n'a jamais été traité : tous les cas attendaient | prérequis sans propriétaire ni date | prérequis inscrit comme ligne datée de la feuille de route, avec responsable | non levé à `<date>` : les cas qui en dépendent sortent de la vague |
| Le premier cas déçoit | le premier cas, mal choisi, a déçu et discrédité les suivants | critères de succès flous ; indicateur non suivi | premier cas à forte valeur et faible effort, avec un indicateur déjà suivi | pilote non concluant : revoir l'ordre avant de lancer la suite |

## 5. Ce qui compte comme objection

Une objection ne compte que si elle est concrète : un scénario, une observation ou un fait du dossier.
« Le gain dépend d'une part de temps réemployé que personne n'a confirmée » est une objection ;
« l'adoption pourrait poser problème » n'en est pas une tant qu'elle ne dit ni qui, ni quoi, ni quand.
Une objection qui porte sur une hypothèse `[H]` du business case ne se débat pas : elle devient une
mesure à relever (`chiffrer-rentabilite`) ou un critère de réussite du pilote.

Une parade écrite mais jamais essayée ne rassure pas : chaque parade est soit déjà dans le plan (une
étape avec sa preuve), soit une action datée avec un propriétaire. Et un pré-mortem ne trouve que ce
que ses participants peuvent imaginer : il ne prouve pas l'absence d'autres risques.

## 6. Écrire une condition d'arrêt

Une condition d'arrêt est un fait observable, relevé à une fréquence connue, avec un seuil fixé à
l'avance, un propriétaire et une action : corriger, suspendre avec l'interrupteur, ou arrêter et
revenir à l'ancienne méthode. Exemple de forme : « si l'usage hebdomadaire reste sous `<seuil>` après
`<délai>` de correction, le propriétaire du processus suspend le dispositif et réunit le décideur ».
Sans seuil, sans fréquence ou sans propriétaire, ce n'est qu'une intention. Quand le fait est un
indicateur de `60-specification.md`, citer son identifiant : son seuil est celui de la spécification,
jamais un second.

## 7. Gabarit de sortie

```markdown
## Pré-mortem

Thèse attaquée : …
Contributions : rôles consultés, ou « rédigé par le consultant seul ».

| # | Histoire d'échec (au passé) | Vraisemblance | Gravité | Signal d'alerte précoce | Parade | Condition d'arrêt | Propriétaire (rôle) | Classement |
|---|---|---|---|---|---|---|---|---|

Écartées : objection — raison.
Verdict : engager | durcir | pivoter — en une phrase.
Version durcie (si durcir) : ce qui s'ajoute au plan, étape par étape.
À rejouer : aux jalons suivants.
```
