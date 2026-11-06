# Le dossier de conformité : ce qu'on prépare

Ce dossier réunit des pièces et pose des questions au rôle compétent : le délégué à la protection des données s'il y en
a un, sinon le responsable désigné par l'entreprise, avec son conseil. Personne n'est désigné : le décideur nomme ce rôle
avant le pilote, et c'est la première `Q-xx`. Il ne contient ni avis juridique, ni base légale
toute faite, ni conclusion du type « c'est conforme ». Le décideur et le rôle compétent répondent ; une réponse absente
reste une `Q-xx` ouverte, et le pilote n'est pas daté avant les réponses marquées « avant le pilote ».

Une question est marquée « avant le pilote » quand sa réponse peut changer le plan retenu, retirer des données du pilote
ou imposer une démarche préalable. Dans le doute, elle l'est ; le rôle compétent peut la retirer.

Les textes se relisent le jour de la mission. Les liens ci-dessous ont été lus le 06/11/2026, sauf mention contraire.

## Partie 1. Les pièces à réunir

| Pièce | Où la trouver | Pourquoi |
|---|---|---|
| L'accord de sous-traitance (DPA) signé ou intégré aux conditions | Page officielle de l'éditeur (`fiches-assistants.md`) | RGPD, article 28 : https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4 |
| La liste des sous-traitants et les lieux de traitement | Page officielle de l'éditeur | Pour répondre sur les transferts hors de l'Union |
| Les durées de conservation du plan choisi | Page officielle de l'éditeur | Pour remplir le registre |
| Les réglages proposés (rubrique 6) | `assistant-ia.md` | Ce qui est réellement activé |
| La charte, version datée | `charte-usage.md` | L'information des personnes |
| Les textes déjà en place : charte informatique, règlement intérieur | L'entreprise (AS09) | Compléter, ne pas doubler |

## Partie 2. Le registre et l'analyse d'impact

Questions au rôle compétent :

1. **Le registre** : ce nouvel usage y entre-t-il, sous quelle finalité et avec quelle base légale ? L'entreprise décide,
   le pack ne propose rien. Sous 250 salariés, la CNIL indique que le registre porte les traitements non
   occasionnels et ceux à risque (https://www.cnil.fr/fr/RGPD-le-registre-des-activites-de-traitement).
2. **L'analyse d'impact** : est-elle nécessaire pour les usages prévus ? Tout système d'IA n'en déclenche pas une ; les
   usages sur des données sensibles, ou qui évaluent des personnes, sont ceux à examiner
   (https://www.cnil.fr/fr/realiser-une-analyse-dimpact-si-necessaire). À regarder aussi, le guide de la CNIL :
   https://www.cnil.fr/fr/comment-deployer-une-ia-generative-la-cnil-apporte-de-premieres-precisions.
3. **Les données des tiers** : que disent les contrats clients ou fournisseurs sur le recours à un sous-traitant ?

Ce qui décide les réponses : les données relevées à AS05 et les clauses relevées à AS06.

## Partie 3. L'information et le suivi des salariés

- **Avant toute collecte** : le texte à lire est le L1222-4 du code du travail, sur les informations collectées par un
  dispositif (https://code.travail.gouv.fr/code-du-travail/l1222-4). Question : s'applique-t-il aux statistiques par
  personne de l'assistant, et comment l'équipe en est-elle informée ?
- **La décision à écrire (AS11)** : qui peut voir l'usage par personne, dans quel but, et comment c'est annoncé. La
  charte le dit en section 7.
- **Là où l'éditeur ne permet pas de couper cette vue** (`fiches-assistants.md`), la décision porte sur ce qu'on en
  fait : qui ouvre ces écrans, et jamais comme indicateur de performance. La mesure du module lit par équipe.

## Partie 4. Le comité social et économique

Dès 11 salariés sur douze mois consécutifs, l'entreprise a un CSE (L2311-2). Questions au rôle compétent, avant le
pilote :

- Le comité doit-il être informé et consulté avant la mise en œuvre, parce que l'outil peut permettre un contrôle de
  l'activité (L2312-38 : https://code.travail.gouv.fr/code-du-travail/l2312-38) ?
- Dans une entreprise de 50 salariés ou plus, le déploiement touche-t-il l'organisation du travail ou les conditions de
  travail (L2312-8) ?

Le calendrier part de la réponse : une consultation prend du temps, et elle se fait avant le pilote.

## Partie 5. La charte et le règlement intérieur

Un document qui fixe des obligations générales et permanentes dans les matières du règlement intérieur compte comme une
adjonction à celui-ci, et suit ses règles (L1321-5 : https://code.travail.gouv.fr/code-du-travail/l1321-5).

Question au rôle compétent, même sans règlement intérieur : le même article vise ces documents « en toute hypothèse ». La
charte, telle qu'elle est écrite, en relève-t-elle, et par quel circuit passe-t-elle, CSE compris ? Une charte qui prévoit
des sanctions rend la question plus pressante. Le rôle compétent dit si le groupe pilote peut démarrer avant.

## Partie 6. Le règlement européen sur l'IA

Deux points à vérifier, à la date du jour :

- **La maîtrise de l'IA (article 4)** : selon la Commission, l'obligation reste pour les fournisseurs et les déployeurs,
  sans niveau imposé depuis le Digital Omnibus
  (https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers). La formation par rôle et sa trace
  (qui, quand, sur quoi) sont la pièce à garder.
- **La transparence (article 50)** : elle s'applique depuis le 2 août 2026, avec une période de grâce limitée à relire.
  La foire aux questions de la Commission traite le cas des salariés qui agissent sous l'autorité de l'entreprise
  (https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act). Question : un texte
  ou un agent publié avec l'assistant doit-il porter une mention ? Une présentation d'un chatbot aux clients se traite
  à part ; elle sort du parcours court.

Le classement en haut risque se pose si un usage touche le recrutement, l'évaluation ou l'accès à un droit : le module
n'en prévoit aucun (charte, section 6), et un tel usage repart par le parcours normal.

## Le modèle, rubrique 5 de `assistant-ia.md`

```markdown
## 5. Le dossier de conformité
Rôle compétent : <nom> · Lu le <date>
| Sujet | Pièce ou question | Réponse | Par qui, quand | Avant le pilote ? |
|---|---|---|---|---|
Q-xx ouvertes : <liste>
Ce qui précède le pilote : <liste>
```
