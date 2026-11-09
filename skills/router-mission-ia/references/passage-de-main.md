# Le passage de la main au pack Créer un agent IA

Décision du 09/11/2026 : le pack consultant-ia décide et mesure ; construire, tester et mettre en service partent au
pack Créer un agent IA (compétences globales construire-solution et tester-solution, déjà parties ; piloter-mise-en-service
reste dans ce dossier le temps que la décision soit prise). Le contrat des fichiers ne change pas : le dossier de mission reste le même, et le
journal aussi.

## Comment l'appeler

- Une solution qui est un agent, un flux ou une automatisation : le workflow du site
  https://zerogravity.builders/marketplace/workflow/creer-un-agent-ia (plugin creer-un-agent-ia).
- Une solution qui est une application : https://zerogravity.builders/marketplace/workflow/creer-une-app.
- La porte affiche ces étapes « au pack Créer un agent IA » et donne le chemin du dossier du cas ; elle ne les lance
  pas elle-même.

## Ce qui passe d'un pack à l'autre

| Sens | Quoi | Où |
|---|---|---|
| Entrée du pack Créer un agent IA | la spécification et le plan validés, la porte de `40-solutions.md` constatée ou « sans objet » | `60-specification.md`, `70-plan.md` |
| Écrit par le pack Créer un agent IA | la construction en essai, la recette, la mise en service | `80-construction.md`, `85-recette.md`, `90-mise-en-service.md` (et leurs dossiers), mêmes noms, même dossier de cas |
| Retour ici | `90-mise-en-service.md` validé au journal, la bascule inscrite : `mesurer-gains` se rouvre | `95-mesure.md` |

Les identifiants (`A-xx`, `D-xx`, `EV-xx`, `Q-xx`), la version gelée, l'environnement d'essai `essai-<slug>` et les
règles communes de `ARCHITECTURE.md` (statuts `[F]` `[H]` `[E]`, validation de chaque action sur un outil réel) restent
ceux du pack : le pack Créer un agent IA les reprend tels quels.

## Cas particuliers

- **Un verdict de recette « pas prêt »** renvoie à la construction, au pack Créer un agent IA. S'il remet l'option en
  cause, une ligne du journal renvoie à `concevoir-solution` et la porte rouvre 40.
- **Un verdict relu « pas prêt pour la version en service »** (défaut bloquant trouvé après le feu vert) ne ferme pas
  `90-mise-en-service.md` : seules les mesures d'attente y restent ouvertes.
- **Option 0 seule, ou lot de simplifications** : on passe de `70-plan.md` à la mise en service du pack Créer un agent
  IA, sans 80 ni 85 ; le registre de `90-mise-en-service.md` ne porte que les actions sur les outils réels que ces
  simplifications demandent.
- **Parcours court d'un assistant IA** : `10-besoin.md` porte la ligne `Parcours : déploiement d'un assistant`, 20 à 85
  sont « sans objet », `deployer-assistant-ia` écrit `90-mise-en-service/assistant-ia.md` et la charte ici, la mise en
  service est au pack Créer un agent IA, puis `mesurer-gains` reprend à la bascule.
- **Une correction ou une action sur un outil décidée en 95** (corriger, étendre, arrêter) repart au pack Créer un
  agent IA ; une extension se rechiffre ici avec `chiffrer-rentabilite`.

## Preuves restantes

- NON MESURÉ : ce passage n'a été parcouru sur aucune mission, même fictive. Il reprend les conditions d'ouverture
  qu'avait la porte avant la décision du 09/11/2026, sans les changer.
