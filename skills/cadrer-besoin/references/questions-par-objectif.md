# Questions par objectif

À ouvrir quand l'objectif de la mission est nommé (porte « besoin connu ») et qu'on prépare l'entretien qui le
précise, mené par le consultant ou par une IA (`mener-entretien-ia`, questionnaire préparé). Le cadrage tient
dans les huit questions de l'étape 3 de `cadrer-besoin` ; l'automatisation d'un processus, dans les huit de
l'étape 9 d'`auditer-processus`. Ce fichier ajoute ce qui dépend du domaine.

## Mode d'emploi

- **Le cadrage, puis un seul module** : celui de l'objectif. Deux modules, c'est deux objectifs, donc deux cas.
- **Ne poser que ce qui manque.** Chaque question cherche d'abord sa réponse dans ce qui a été lu (la demande,
  `mission/sources/`, le site de l'entreprise, ses exports, ses outils quand ils sont lisibles) : sûre, elle ne se pose pas ; incertaine, elle se
  fait confirmer ; absente, elle se pose. La méthode : `mener-entretien-ia/references/questionnaire-prepare.md`.
- **Au premier contact, deux questions au plus** (étape 3) : celles qui changent le périmètre, le coût ou les
  conditions de réussite. Le reste attend l'entretien.
- **Chaque question demande l'occurrence réelle et l'ordre de grandeur** (règles communes de
  `decouvrir-cas-usage/references/guides-entretien.md`). Observer vaut mieux que se souvenir : quand c'est
  possible, relever soi-même les derniers cas dans l'outil avant l'entretien ; sinon, les passer avec la
  personne (`auditer-processus`, étape 2).
- Les questions marquées « retour d'expérience » viennent d'un cas publié par un praticien ; le lien est la
  source, pas une preuve de résultat.

## Service client et demandes entrantes

- Combien de demandes arrivent par semaine, et par où : email, formulaire du site, chat, téléphone, réseaux
  sociaux ? Quels jours, quelles heures, quels pics ?
- Dans quel outil les lit-on, qui y répond aujourd'hui, et combien de temps un client attend-il sa réponse ?
- Quelles sont les dix questions qui reviennent le plus, et combien de fois chacune par semaine environ ?
  (Si la boîte ou le CRM est lisible, les relever avant l'entretien, `auditer-processus` étape 2 : ces trois
  premières questions ne portent plus que sur ce qui n'arrive pas dans l'outil. Sinon, en direct : ouvrir la
  boîte et passer les quinze derniers messages, type par type.)
- Des réponses types existent-elles ? Où sont-elles, qui les a écrites, quel ton, quelle signature ?
- Pour répondre à une demande courante, quelles informations faut-il aller chercher, et dans quels outils
  (commandes, transporteur, facturation) ? Retour d'expérience : [Dust, support](https://dust.tt/blog/how-dust-runs-support-on-dust).
- Les règles de livraison, de retour, de remboursement et d'annulation sont-elles écrites ? Où ?
- Dans quels cas précis faut-il passer la main à une personne, à qui, sous quel délai et avec quelles
  informations déjà réunies ? Retour d'expérience : [Fin, politique d'escalade](https://fin.ai/blog/blueprint/how-to-set-your-escalation-policy).
- Quelles réponses ne doivent jamais partir sans qu'une personne les relise ?
- Dans quelles langues les clients écrivent-ils ?
- Qu'est-ce qui serait un échec : une information fausse, un ton froid, une promesse faite par erreur ?

Pièces à demander, pour ce que la lecture n'a pas couvert : 50 à 100 messages récents avec les réponses données ; les réponses types ; les règles
écrites ; un accès en lecture aux commandes, ou quelques commandes de test.

## Prospection et acquisition

- Quelles actions de prospection sont menées aujourd'hui, sur quelles cibles, par quels canaux, avec quels
  résultats, cible par cible ?
- Quelle cible doit être prioritaire pour un premier essai, et pourquoi celle-ci ?
- Si deux cibles sont envisagées, partagent-elles la même offre, les mêmes décideurs, les mêmes données et les
  mêmes messages ? La seconde est-elle une variante ou une campagne distincte ?
- Quelles listes, sources de données, exclusions et historiques de contact existent déjà ?
- Quels arguments, objections et déclencheurs d'achat reviennent dans les affaires gagnées ?
- Quels outils et comptes sont déjà en place, et quels abonnements ou crédits resteraient à prévoir ?
- Comment la réussite de l'essai sera-t-elle jugée, à quelle échéance, sur quels signaux ?
- Les informations utiles au ciblage et à la rédaction existent-elles, ou faut-il les reconstruire ?
- Quel calendrier laisse le temps de valider la cible, les messages et les accès avant le lancement ?
- Quel exemple permet de vérifier une bonne qualification, qui tranche les désaccords, et comment une
  correction améliore-t-elle le passage suivant ? Retour d'expérience : [Nooks et Vapi](https://www.revopscoop.com/webinar-series/ai-agents-revops-accuracy-improvement).

## CRM et suivi commercial

- Quel est le parcours réel d'un contact jusqu'au client, et où les passages de relais se dégradent-ils ?
- Quelles étapes, propriétés et règles du pipeline l'équipe utilise-t-elle vraiment ?
- Quelle source fait foi pour les contacts, les entreprises, les opportunités, les activités et le chiffre ?
- Quels doublons, données manquantes ou incohérences empêchent aujourd'hui le suivi ou l'automatisation ?
- Quelles intégrations alimentent le CRM, et lesquelles écrivent ou modifient des données ?
- Quels rôles ont besoin de quelles vues, alertes, tâches ou automatisations ?
- Qui reçoit une recommandation ou une alerte, dans quel outil, et à quel moment doit-il réellement agir ?
  Retour d'expérience : [Quavo et Bloomreach](https://www.revopscoop.com/webinar-series/ai-myths-revenue-teams-wrong).
- Quelle partie doit être corrigée maintenant, et quelle refonte peut attendre ?
- Comment l'adoption du CRM se mesure-t-elle, et qui en est propriétaire après la mission ?

## Données, enrichissement et segmentation

- Quelles sources sont disponibles, à jour et légalement exploitables ?
- Quels champs sont indispensables pour décider, segmenter ou personnaliser ?
- Quels taux de complétude, formats et règles de normalisation faut-il atteindre ?
- Comment sont traités les doublons, les exclusions, les adresses invalides, les clients et opportunités en cours ?
- Quelle différence fait-on entre données brutes, enrichies et validées ?
- Quelles règles de segmentation sont communes, et lesquelles varient vraiment selon la cible ?
- Qui détecte une donnée fausse, comment la corrige-t-on, et quelle source et quelle date disent si elle
  reste utilisable ? Retour d'expérience : [Rubrik](https://www.revopscoop.com/webinar-series/clay-openprise-gtm-data-scale).
- Quelle source l'emporte quand deux systèmes se contredisent ?

## Reporting et indicateurs

- Quelle décision chaque indicateur doit-il permettre de prendre ?
- Quelle mesure de départ existe, et sur quelle période est-elle fiable ?
- Quels indicateurs mesurent l'activité, la qualité, la conversion et le résultat final ?
- Comment attribuer un résultat à une source, une campagne ou une cible sans inventer de lien de cause ?
- Dans ce reporting, quelle part relève de la collecte, du recalcul, de la copie, des contrôles et de
  l'analyse ? Retour d'expérience : [Cribl](https://www.revopscoop.com/webinar-series/automate-executive-reporting-revops).
- À quelle fréquence lire les résultats pour agir sans surinterpréter ?
- Qui répond de la qualité des données qui alimentent le reporting ?
- Quels seuils déclenchent une correction, une alerte ou l'arrêt d'un essai ?

## Contenu

- Quelle décision éditoriale demande encore un jugement humain après la recherche et la rédaction ?
  Retour d'expérience : [Dust, SEO](https://dust.tt/blog/ai-agents-seo-workflow).

Module à compléter par les questions qui auront servi (« Ajouter une question »).

## Transmission et adoption

- Qui reprendra le dispositif, et avec quelle autonomie ?
- Quels gestes l'équipe devra-t-elle savoir faire sans le consultant ?
- Quels rôles ont besoin d'une formation, d'un mode d'emploi, d'une vidéo ou d'une documentation technique ?
- Quels accès, propriétaires de comptes et procédures de secours faut-il transmettre ?
- Comment vérifier que l'équipe a compris et sait corriger une erreur courante ?
- Quelle méthode marche déjà chez une personne, et qu'est-ce qui empêche les autres de s'en servir : données,
  droits, installation, absence de mode d'emploi ? Retour d'expérience : [Decagon](https://dust.tt/blog/how-to-ai-pill-an-ai-company).
- Quel soutien est prévu après la transmission, et qu'est-ce qui relève d'une nouvelle mission ?

## Les domaines sans module

Finance, ressources humaines, juridique, opérations : le cadrage et l'audit du processus suffisent. Un module
naît des questions qui ont servi, pas d'une liste écrite d'avance.

## Ajouter une question

1. Ne garder qu'une question qui a réellement changé le cadrage, le coût ou la réussite d'une mission.
2. Vérifier qu'elle n'existe pas déjà : les huit du cadrage, les huit de l'audit, le module concerné.
3. La réécrire pour qu'elle serve ailleurs, sans le nom du client ni de ses outils.
4. L'ajouter au seul module pertinent ; sinon, ne rien ajouter.
