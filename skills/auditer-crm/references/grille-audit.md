# Grille d'audit CRM

La grille que le consultant remplit lui-même, en lisant le CRM en lecture seule ; les questions à poser à
l'entreprise sont dans la base (`mener-entretien-ia/references/base-questions/crm.md`). Chaque constat porte un
statut et un témoin, chaque nombre son statut `[F]`, `[H]` ou `[E]`.

## Les quatre statuts d'un constat

| Statut | Sens | Ce qui le fait changer |
|---|---|---|
| `confirmé` | vu sur deux témoins concordants (écran et export, outil et entretien) | un témoin contraire |
| `à vérifier` | un seul témoin, ou un écran qui peut mentir (chargement, filtre actif, panneau qui masque) | le second témoin |
| `incohérent` | deux témoins qui se contredisent (la configuration dit une chose, l'usage une autre) | l'entretien qui tranche |
| `à mettre en place` | absent du CRM et demandé par le besoin ; jamais réalisé pendant l'audit | l'action `A-xx` de `90-mise-en-service` |

Règles de lecture : la configuration n'est pas l'usage ; aucun constat sur un seul écran ; un « 0 » lu juste après
un changement de vue est souvent un chargement (relire deux fois) ; un volume faible peut être une niche voulue
(lire les critères avant de dire « inutile ») ; un chiffre se relève dans l'outil, jamais dans la réponse d'un
assistant intégré, bon pour raisonner, pas pour compter.

## 1. Vue d'usage

Une ligne par quota ou volume que l'abonnement limite ; la colonne « Lecture » dit sous-utilisé, normal, proche de
la limite ou limite atteinte.

| Quota ou volume | Valeur | Limite de l'abonnement | Lecture |
|---|---|---|---|
| Contacts et affaires actifs | | | |
| Affaires en cours | | | |
| Utilisateurs et licences | | | |
| Champs personnalisés | | | |
| Équipes, groupes de visibilité, ensembles de droits personnalisés | | | |
| Rapports et tableaux de bord par utilisateur | | | |
| Messageries synchronisées par utilisateur | | | |
| Formules ou champs calculés | | | |
| Appels d'API consommés | | | |
| Stockage de fichiers | | | |

Un quota atteint bloque une évolution ; un module payé et jamais utilisé (rapports, synchronisation, API) est une
économie ou une adoption à reprendre.

## 2. Automatisations, intégrations et outils

- **Cartographier les flux** : chaque source qui écrit dans le CRM (formulaires, publicité, prospection, import,
  outil d'automatisation, rendez-vous, téléphonie) et chaque sortie (emailing, facturation, outils métiers). Un
  schéma des flux, une ligne par flux : sens, déclencheur, objet touché, outil, état.
- **Pour chaque automatisation** : déclencheur, actions, volume d'enrôlés (total, sept derniers jours), créateur,
  état. Signaux : éteinte (saisonnière ou oubliée ?), brouillon abandonné (sans nom et éteint), aucune action, déjà
  marquée archivée, appel sortant vers un outil tiers (boîte noire côté CRM : en demander l'accès, n'y rien toucher),
  deux automatisations au même déclencheur (double sollicitation), un parcours sans automatisation (trou de
  couverture), un volume effondré (filtre trop étroit, public injoignable).
- **Lire deux familles à part** : le métier (ce que le client veut voir arriver : relances, alertes, parcours) et la
  plomberie de données (propriétaires, associations, copies d'identifiants). On les rend dans deux tableaux.
- **Pour chaque intégration** : connectée, en erreur, déconnectée ou jamais installée ; scénario de l'outil
  d'automatisation actif, dernière erreur.
- **Problème signalé** (un contact non enrichi, un lead qui n'arrive pas) : historique de la propriété (qui l'a
  modifiée, quand, avant et après), état de l'intégration, historique des imports (colonnes associées : l'e-mail
  est-il présent ? sans e-mail, aucun enrichissement ne travaille). Rendre : périmètre, outil en cause, état, cause
  (donnée manquante, mauvaise correspondance, outil cassé, quota dépassé), recommandation et qui la porte.

## 3. Données

- **Sources** : d'où viennent les contacts et les entreprises, lu dans les champs de source et leurs valeurs ;
  quelles sources fonctionnent, lesquelles ne remontent plus ; les filtres qui reconnaissent une source mal
  renseignée (une marque distinctive suffit souvent à la requalifier).
- **Champs** : pour chaque objet (contacts, entreprises, affaires, et objets propres au client), la liste des champs
  avec, pour chacun, le taux de remplissage, les valeurs possibles et le volume par valeur. Une vue par champ (un
  diagramme) ou un export avec tableau croisé : le second est complet mais demande de reprendre les formats.
  Ce que chaque mesure décide : le taux de remplissage montre les trous (enrichissement, formulaire,
  automatisation) ; les valeurs montrent la cohérence, les formats et les champs en double ; les volumes par valeur
  font l'inventaire des segments utiles (clients, prospects, abonnés).
- **Champs critiques** : ceux qui qualifient et priorisent un compte (taille, chiffre d'affaires, croissance,
  secteur) et un contact (fonction, e-mail, téléphone, entreprise) ; leur voie d'enrichissement, champ par champ.
- **Ordre de travail** : vérifier que les champs importants existent, puis que leurs valeurs sont complètes, puis
  qualifier ce qui ne l'est pas (enrichir, segmenter automatiquement, mettre à jour les statuts).
- **Doublons et exclusions** : la clé d'unicité d'un contact par source, les doublons potentiels, les contacts sans
  propriétaire, les e-mails sans téléphone, les rebonds et désinscriptions, la donnée brute, enrichie ou validée.
- **Segments et listes** : vide, statique ou dynamique, jamais référencé, nom en double, « statique déguisée » (son
  filtre n'est que l'appartenance à un import). Un segment peut en lire un autre : sans référence ne veut pas dire
  libre, on archive.
- **Indicateurs de qualité** suivis après le nettoyage : en existe-t-il ?

## 4. Ventes

- **Pipelines** : un pipeline par offre ou catégorie d'offres dont les étapes diffèrent ; deux pipelines aux étapes
  identiques se fusionnent et se distinguent par une étiquette ou un champ. Un pipeline ne sert pas à trier ce
  qu'un filtre trie.
- **Étapes** : chacune est un statut atteint par le prospect, avec l'action qui la fait franchir, un délai au-delà
  duquel l'affaire est oubliée et une probabilité de signature. Mesurer, par étape, le taux de passage et le temps
  passé.
- **Affaires** : sans activité prévue, inactives depuis N jours, avec montant sans date de signature, propriétaire
  sans activité sur ses affaires ouvertes.
- **Raisons de perte** : renseignées ou non, liste fermée ou libre, exploitables ou non.
- **Activités, vues et filtres** : types d'activité utiles ou inutiles ; filtres et vues de suivi dont l'équipe a
  besoin et qui manquent ; règles d'attribution des leads.
- **Prospection** : la cible et les décideurs visés dans les comptes cibles, ce qui reste à identifier et enrichir.
- **Priorisation** : une notation des leads sur deux axes, adéquation à la cible et engagement, plutôt qu'un score
  unique qui mélange les deux.
- **Pratiques de l'équipe** : chez qui le suivi tient, chez qui il casse, à observer plutôt qu'à juger.

## 5. Tableaux de bord

- Chaque rapport existant : la décision qu'il permet, qui le lit, à quelle fréquence. Ceux qu'on ne lit pas sont
  un constat.
- Les rapports manquants : performance par cible et par segment, par source ou canal (salon par salon, séquence
  par séquence), conversion des leads entrants ; pour chacun, volume des ventes, taux de transformation, durée du
  cycle, nombre moyen d'interactions.
- Ce que le CRM ne sait pas produire, et la façon la plus simple de le produire ailleurs (export vers un tableur,
  outil spécialisé), comparée dans `concevoir-solution`.
- Un rapport dépend des pipelines et des segments : il se construit après eux.

## 6. Garder, changer d'édition ou changer d'outil

Critères repris par `concevoir-solution` : taille et structure de l'entreprise, clientèle (entreprises,
particuliers ou les deux), objets nécessaires au-delà des contacts, entreprises et affaires, quotas de la vue
d'usage, intégrations indispensables, modèle d'abonnement (par utilisateur, par contact, par volume d'e-mails),
compétences internes pour l'administrer, coût complet sur trois ans. « Garder et simplifier » est toujours une
option chiffrée.

## 7. Le bilan

Construit à partir des volets, sans nouvelle analyse :

| Volet | Recommandation | Plan d'action | Impact | Faisabilité | Projet qui la porte |
|---|---|---|---|---|---|
| Données | | | `[E]` ou `[H]` | rapide · moyenne · lourde | ou « sans plan d'action » |

Les gains rapides (fort impact, mise en œuvre facile) en tête ; un résumé par volet ; un rappel final des actions
prioritaires. Le bilan ne cache pas un manque : une recommandation sans plan d'action reste visible.

## Provenance

Méthode reprise et dépersonnalisée, le 29/10/2026, de : une page d'offre « Audit CRM » et son périmètre en quatre
volets ; une page de méthodologie d'audit global (champs, sources) et la vue d'usage d'un compte ; deux bilans
d'audit ; une fiche de réalisation sur un audit en quatre volets ; trois assistants conversationnels de l'auteur
(audit des données, bilan d'audit, cahier des charges) ; une boîte à outils d'audit de segments et de workflows
pour un éditeur. Les noms, chiffres et pièces des clients sont restés dans les sources privées.
