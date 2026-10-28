# Base de questions : l'essai et la mise en service

Avant un essai ou une mise en service : imaginer l'échec pour le prévenir (le pré-mortem de
`planifier-deploiement`), poser les conditions de l'essai, et vérifier qu'on peut toucher à ce qui tourne déjà.
Les critères de réussite se posent au cadrage (CA01) ; la reprise par l'équipe, dans `transmission`.

## 1. Le pré-mortem

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| ES01 | Nous sommes dans six mois et le projet a échoué : que s'est-il passé ? | Les histoires d'échec, les signaux d'alerte et leurs parades | la personne |
| ES02 | Imaginez que l'échec soit entièrement de notre fait : qu'avons-nous mal fait ? | Les erreurs à éviter de notre côté | la personne |

## 2. L'essai

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| ES03 | Acceptez-vous un essai de quelques jours sur des cas réels, sans aucun envoi à un client ? | Le feu vert et le périmètre de l'essai | la personne |
| ES04 | Combien de clients servez-vous en ce moment, et lequel prendre comme pilote ? | Le client pilote du premier essai | la personne |
| ES05 | Vos équipes valideraient-elles ce que l'agent prépare, avant tout envoi ? | Le niveau d'autonomie de l'agent | la personne |

## 3. Toucher à ce qui tourne

| # | Question | Ce qu'elle décide | D'abord |
|---|---|---|---|
| ES06 | Vos outils sont-ils stables aujourd'hui : tout fonctionne-t-il ? | Le moment où l'on peut y toucher | la personne |
| ES07 | Votre prestataire peut-il modifier le site ou l'outil concerné, et sous quel délai ? | La faisabilité et le délai d'une correction chez un tiers | la personne |
| ES08 | Acceptez-vous qu'on modifie une automatisation déjà en service ? | L'accord avant de toucher à ce qui tourne | la personne |

## Pièces à demander

- Un jeu d'essai fictif, ou des cas réels anonymisés par l'entreprise ou avec elle.
- Des comptes et un accès d'essai (préproduction), fournis par l'entreprise.
- La fiche des critères du pilote (poursuite, prolongation, arrêt), signée avant de commencer.
- L'accord écrit pour créer des vues et des automatisations dans ses outils.
