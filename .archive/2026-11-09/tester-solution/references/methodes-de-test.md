# Méthodes de test — familles de risque, preuves, sabotage, scénarios difficiles

À ouvrir à l'étape 3 (partie 1, familles), à l'étape 5 (parties 2 à 4, écrire un test, preuve, état de départ), à
l'étape 6 (partie 5, sabotage), à l'étape 7 (parties 6 et 7, tests instables et cycle d'un défaut) et pour
construire les cas qui font mal (partie 8). Le principe de chaque point est dans `SKILL.md`.

Statut des contenus : les exemples sont fictifs ; ils illustrent le cas des relances de factures (`examples/`), sauf
mention du cas fictif du statut de commande, qui n'a pas été déroulé. Les délais, volumes et plafonds viennent de
`60-specification` ; on ne les invente pas ici.

## 1. Les familles de risque

Parcourir les dix-huit familles, garder celles qui mordent sur ce cas, et écrire pourquoi on en écarte une. Elles
complètent les tests de `60-specification` §12 ; les tests qu'elles font ajouter continuent la numérotation `T-xx`.
Ce sont aussi les catégories de la recette : `mesurer-gains` y classe les échecs relevés en exploitation. Si le cas
en réclame d'autres (par exemple « mauvaise cible » : un message au mauvais destinataire), la famille s'ajoute ici
avec son test ; un échec qui n'entre dans aucune famille revient ici comme nouveau test.

| Famille | Ce qu'on met en scène | Attendu type | Piège fréquent |
|---|---|---|---|
| Nominal | le cas ordinaire, de bout en bout, sur le rejeu d'une situation observée | résultat conforme à 60 §12, élément par élément | s'arrêter là |
| Formats d'entrée | date de fin de mois, jour férié, changement d'heure ; montant à virgule ou à point ; encodage ; champ vide, très long, caractères spéciaux ; colonne absente ou déplacée ; extraction vide ou partielle | l'élément fautif est rejeté proprement (erreur définitive, file des échecs), jamais déformé en silence ; les autres passent | tester avec une extraction idéale |
| Hors périmètre | ce que le dispositif ne doit pas traiter (60 §2, 30 §11) | écarté avec son motif, sans effet | ces cas passent parce que personne ne les a mis dans le jeu |
| Erreurs passagère et définitive | service indisponible, délai dépassé, droit refusé, donnée invalide | passagère : reprises espacées puis file des échecs ; définitive : aucune reprise, alerte | des reprises qui retardent l'alerte d'une erreur définitive |
| Doublons et idempotence | le même événement reçu deux fois ; un appel reçu deux fois ; le flux lancé deux fois ; la file rejouée | rien n'est doublé ; la seconde fois est journalisée « déjà fait » | une clé construite sur l'horodatage |
| Reprise après plantage | arrêt au milieu d'un lot ; arrêt juste avant l'écriture ; arrêt juste après l'écriture, avant l'enregistrement de la clé | la reprise n'oublie rien et ne double rien | n'arrêter que pendant une étape, jamais entre deux |
| Traitement partiel | un élément sur dix échoue | les neuf autres sont traités, l'échec est dans la file, l'état est cohérent et reprenable | un tout-ou-rien que personne n'a voulu |
| Délai dépassé | un service répond trop lentement | reprise ou file selon 60 §7 ; aucune écriture à moitié | un délai qui bloque les éléments suivants |
| Lecture après écriture | après chaque écriture, relire l'objet réellement enregistré | l'état relu est l'état voulu (modèle, numéro, montant, destinataire) | se fier au « OK » de l'appel |
| Retour arrière | restaurer la version précédente, la relancer, rejouer un test | l'ancienne version tourne, rien n'est perdu ; durée `[F]` | un retour arrière jamais essayé |
| Permissions et validation humaine | tenter une action interdite avec le compte de service (envoyer, supprimer, écrire hors périmètre) ; modifier après validation ; valider avec le mauvais rôle ; lister les droits réellement accordés | refus et tentative au journal ; droits = droits strictement nécessaires (60 §6) | des droits larges « pour tester » |
| Secrets et données personnelles | balayer la livraison, les journaux, les sorties simulées, les preuves | aucun | oublier les captures et les journaux |
| Pointe de volume | une extraction au plafond, puis au-delà | délai sous la limite (ENF) ; au-delà du plafond, arrêt et alerte | tester à volume moyen seulement |
| Arrêt d'urgence | l'interrupteur actionné en cours d'exécution | plus rien de neuf n'est créé ; le reste suit 60 §7 | un interrupteur lu seulement au démarrage |
| Alertes | provoquer échec, silence, liste vide suspecte, double envoi, volume anormal | chaque alerte arrive au bon rôle dans le délai | une alerte jamais déclenchée en vrai |
| Mode du pilote | les réglages prévus (étape désactivée, fonctionnement en parallèle) | le réglage fait exactement ce que 60 §4 et §13 disent | ne tester que le mode normal |
| Processus instable | une règle (seuil, liste, modèle) change en cours d'exécution ou entre deux exécutions | l'exécution garde les règles du début et note leur version ; une règle modifiée sans mise à jour du dispositif alerte | des règles relues à chaque élément |
| Changement non approuvé | un flux, une règle ou une consigne modifié hors procédure | détecté (empreinte différente de la version approuvée) ou refusé par les droits | personne ne compare ce qui tourne à ce qui est approuvé |

## 2. Écrire un test

Une fiche par test, brève. Le test est écrit avant d'être exécuté.

```markdown
T-xx — <titre>
Couvre : CA / EF / ENF / R (identifiants) · Famille : …
Scénario : …
Données : lignes du jeu ou fichier (dans 80-construction/donnees-essai/)
État de départ : remise à zéro, horloge de test, version des règles
Action : commande ou procédure, pas à pas
Attendu (écrit avant) : … · Source : rubrique de 60 ou de 30, relevé [F], calcul indépendant
Preuve attendue : sortie, extrait du journal, export, capture
Niveau visé : données synthétiques | préproduction
Sabotage : oui (régression : …) | non (pourquoi : …)
```

Une exigence qui ne se teste pas telle quelle (« rapide », « fiable ») reçoit un seuil et un cas dans 30 §9 : si ce n'est
pas fait, c'est un trou de la spécification, pas un test à inventer.

## 3. Ce qui compte comme preuve

| Type d'exécution | La preuve |
|---|---|
| Commande locale | la commande exacte, la version testée (empreinte), un extrait de sortie (une vingtaine de lignes au plus), la date ; la sortie longue dans un fichier de `85-recette/` cité par son nom |
| Exécution dans une plateforme | l'identifiant de l'exécution, la date, qui l'a lancée, l'export de l'exécution (balayé), les entrées et sorties de l'étape concernée |
| Geste manuel | les étapes numérotées, ce qui a été constaté, par qui, quand |
| Exécution par un tiers | le rôle et la pièce reçue, nommée ; sans pièce, le test reste « prévu » |

Ne sont pas des preuves : « ça marche » ; un code de retour seul ; une capture sans date ni version ; un résultat
obtenu sur une autre version ; un résultat obtenu après avoir réglé l'attendu. Aucune preuve ne contient de secret ni de
donnée personnelle : on balaie comme pour la livraison.

## 4. Remise à zéro et état de départ

- Un état de départ connu : données rechargées depuis le jeu, journal et file des échecs vidés, magasin de clés vide
  (sauf si le test porte sur le doublon), règles à la version prévue, interrupteur décoché, horloge de test fixée
  (jour ouvré, fin de mois, jour férié selon le test).
- La remise à zéro s'écrit comme une procédure : quels onglets, fichiers ou enregistrements vider, quoi recharger.
- L'ordre des tests est indifférent. Un test qui dépend d'un autre est un scénario en deux temps, et il le dit.
- L'état final d'un test échoué se garde pour comprendre ; on remet à zéro avant le re-test.

## 5. Le sabotage

Un test qui n'a jamais échoué ne prouve rien : il peut regarder le mauvais objet, ou attendre trop peu. Le sabotage
le met à l'épreuve une fois.

1. Choisir le test et une régression plausible : celle qu'une modification future introduirait par mégarde.
2. Travailler sur une copie de la version gelée ; la version testée n'est jamais sabotée.
3. Introduire la régression dans la copie et l'écrire en une ligne.
4. Lancer le test sur la copie : il doit échouer. Garder la sortie.
5. Jeter la copie ou rétablir ; vérifier que l'empreinte de la version testée est inchangée ; relancer le test sur
   la version gelée : il doit réussir.
6. Si le test saboté reste vert, il est invalide : attendu trop lâche, donnée qui ne déclenche pas le cas, test qui
   regarde le mauvais objet, régression trop faible. Le réécrire et recommencer.

**Quoi saboter.** Obligatoire : le cas limite critique, et chaque test qui protège un effet irréversible, une
validation humaine, le dédoublonnage ou les permissions. Facultatif pour le reste, par échantillon. Inutile pour un
test qui a déjà échoué sur un vrai défaut (`D-xx`) : il a fait sa preuve.

| Garde-fou | Régression plausible à introduire | Test qui doit échouer |
|---|---|---|
| fraîcheur des données | retirer le contrôle de date | cas limite critique |
| exclusions | retirer un motif d'exclusion (payée, déjà relancée, litige) | tests d'exclusion |
| dédoublonnage | construire la clé sur l'heure ; sauter la recherche de clé | doublons et idempotence |
| reprise après plantage | enregistrer la clé avant d'écrire, sans réconciliation | reprise (élément perdu) |
| validation humaine, envoi | donner le droit d'envoi au compte ; passer la simulation au réel | permissions, cas interdit |
| interrupteur | ne plus lire la case en cours d'exécution | arrêt d'urgence |
| plafond | relever ou retirer la limite | pointe de volume |
| alerte sur silence | désactiver l'alerte | alertes |
| secrets | glisser dans l'export une valeur fictive qui ressemble à une clé | balayage (il doit la trouver) |
| retour arrière | supprimer l'export de la version précédente | retour arrière |
| règles qui changent | relire les règles à chaque élément | processus instable |
| changement non approuvé | supprimer la comparaison d'empreinte | changement non approuvé |
| étape d'IA | retirer la consigne d'abstention ; ajouter un outil hors liste ; neutraliser le contrôle de format ou de fidélité | abstention, action hors liste, sortie malformée, plausible mais faux |

## 6. Tests instables

Un test qui change de résultat sans changement de version dépend de l'heure, de l'ordre, d'un service extérieur, d'un
état laissé par un autre test ou, pour une IA, d'un tirage. On ne le rejoue pas jusqu'au vert : on isole la cause
(horloge fixée, remise à zéro, service remplacé par un double, nombre de tirages noté) et on enregistre le défaut du
test ou du dispositif, avec la gravité de ce qu'il masquait. Tant que le test n'est pas stable, il ne compte pas comme
réussi.

## 7. Le cycle d'un défaut

1. Constater : test, preuve, version. Un défaut trouvé hors test, en lisant ou en essayant, reçoit aussi un `D-xx`.
   Un défaut trouvé en pilote (relevé ou incident remonté par `piloter-mise-en-service`) ou en exploitation (relevé ou
   incident lu par `mesurer-gains`) reçoit le `D-xx` suivant de la même série, marqué « pilote » ou « exploitation » ;
   son cycle est le même, et aucune nouvelle action n'est validée en 90 avant la nouvelle passe de recette.
2. Écrire le `D-xx`, sa gravité (`references/modeles.md`, partie B) et sa cause en une phrase.
3. Écrire le test qui l'aurait attrapé, s'il n'existait pas (nouveau `T-xx`, avec sa raison).
4. Faire corriger par `construire-solution` : nouvelle version, ligne au journal des versions.
5. Rejouer : le test échoué, ceux de la tranche touchée, ceux des garde-fous concernés ; le sabotage à nouveau si un
   garde-fou a bougé.
6. Clore (re-test réussi, version notée) ou faire accepter par le décideur (décision écrite au journal, condition
   du pilote). Un défaut qui révèle un trou de 60 entraîne aussi une version datée de 60.

## 8. Les cinq scénarios difficiles

À construire en premier : ce sont ceux que les dispositifs ratent le plus souvent, et que l'on ne pense pas à écrire.

**Processus instable.** *Mise en scène* : pendant une exécution, le propriétaire modifie le seuil de montant dans le
tableau des règles (de 15 € à 20 € `[H]`) ; on lance ensuite une seconde exécution. *Observer* : les propositions de
la première exécution, le journal (version des règles), la seconde exécution, l'alerte de règle modifiée sans mise à
jour. *Attendu* : la première applique 15 € de bout en bout et note sa version de règles ; la seconde applique 20 € et
note la suivante ; aucune facture n'est traitée avec deux seuils dans une même exécution. *Sabotage* : relire les
règles à chaque facture ; le test doit échouer.

**Appel reçu deux fois.** *Mise en scène* : le déclencheur envoie deux fois le même événement à quelques secondes
d'écart (renvoi par la source) ; le courriel envoyé arrive deux fois. *Observer* : propositions, brouillons, lignes
d'historique, journal. *Attendu* : une proposition, un brouillon, une ligne d'historique ; la seconde occurrence est
journalisée « déjà fait » ; l'envoi doublé lève l'alerte « double envoi ». *Sabotage* : clé sur l'horodatage ; le test
doit échouer (deux brouillons).

**Plantage juste après une écriture.** *Mise en scène* : interrompre le traitement (a) juste avant de créer un
brouillon, (b) juste après l'avoir créé, avant d'enregistrer la clé ; relancer. *Observer* : le nombre de brouillons à
la fin, le journal. *Attendu* : dans les deux cas un seul brouillon à la fin ; en (a) l'élément n'est pas perdu, en (b) il
n'est pas doublé ; le journal dit que l'état a été réconcilié. *Sabotage* : enregistrer la clé avant d'écrire (en (a),
l'élément est perdu sans bruit) ; écrire sans relire l'état (en (b), il est doublé).

**Réponse d'IA plausible mais fausse** (cas fictif du statut de commande). *Mise en scène* : le suivi du transporteur
indique « expédié le 3 » ; le jeu contient aussi un suivi périmé ; l'IA rédige la réponse au client. *Observer* : la
réponse contient-elle un fait absent de la source (« livré le 3 », un numéro de suivi inventé) ? le relecteur humain la
repère-t-il ? *Attendu* : chaque fait de la réponse se retrouve dans l'entrée, sinon la réponse est écartée ou le
dispositif s'abstient ; une erreur qui passe est comptée en catégorie « fidélité aux sources », gravité haute ; la
relecture humaine est mesurée sur des erreurs glissées parmi les bonnes sorties. *Sabotage* : retirer le contrôle de
fidélité ou l'instruction d'abstention ; le résultat de la catégorie doit baisser.

**Changement non approuvé.** *Mise en scène* : quelqu'un modifie un modèle de courriel, une règle ou les consignes de
l'IA directement dans l'outil, hors procédure ; ou le fournisseur change le modèle d'IA par défaut. *Observer* : la
comparaison de l'empreinte (ou de la version) de ce qui tourne avec celle de la version approuvée ; les droits du compte ;
la non-régression de l'IA. *Attendu* : la modification est refusée par les droits, ou détectée à la prochaine exécution
(alerte) ; un changement de consigne ou de modèle déclenche une nouvelle évaluation avant usage. *Sabotage* :
supprimer la comparaison d'empreinte ; le test doit échouer.
