# Solutions — Relances de factures échues

2026-10-06 · Demandeur : direction générale · Valideur et décideur : responsable financier (règle d'engagement : il décide sous 3 000 € de construction et 100 € de coût récurrent par mois `[F]`, la direction générale au-delà ; l'option retenue reste sous ces seuils `[H]`) · Rédigé par : consultant IA · Exigences lues : `30-exigences.md` du 2026-10-02, version 1
S1 à S4 désignent les systèmes en place de `30-exigences.md` §6 : logiciel de facturation, tableur partagé, messagerie, outil de tickets.

## 1. Recommandation

**Option retenue** : 4, workflow sans code, construit par un indépendant spécialisé, sous porte. L'option 0 s'applique dès maintenant : elle est déjà décidée avec `20-diagnostic.md`.

**Porte** : la construction ne démarre pas avant que les conditions de la rubrique 10 soient constatées, au plus tôt le 2026-10-27. Aucune dépense de construction avant elle.

**Trois raisons porteuses** :
1. Elle couvre les neuf exigences indispensables et ramène la séance du lundi de 115 min (option 0 seule) à 32 min `[E]`, sous la cible de 60 min `[F]` (acceptée le 2026-09-24, `10-besoin.md` §8 ; temps résiduel de 32 min supposé `[H]`, `20-diagnostic.md` §9).
2. Elle coûte moins et arrive plus vite que l'option 3 : 1 348 € contre 2 248 € de construction `[H]`, environ 2 semaines contre 3 `[H]`. Le responsable financier ou la gestionnaire clients peuvent lire et régler le flux.
3. Elle lit des fichiers exportés et ses règles sont écrites : elle reste portable si le logiciel de facturation est remplacé en mars 2027 (`04-feuille-de-route.md`, pré-mortem, ligne 4).

**Ce qui doit être vrai** :
1. La porte est ouverte (rubrique 10), le seuil de la re-mesure étant fixé par le point mort de `50-rentabilite.md` `[H]`. Gestionnaire clients (mesure), responsable financier (constate).
2. La plateforme héberge les données dans l'Union européenne `[H]`. Responsable financier, en lisant la page de l'éditeur avant de signer.
3. Les brouillons s'écrivent dans la boîte partagée de la finance sans que le flux puisse les envoyer (EF-10) `[H]`. Responsable financier, qui administre les accès, et l'indépendant.
4. Le rapprochement des paiements précède la séance (Q-06) `[H]`. Comptable.
5. La liste des litiges est alimentée chaque jour `[H]`. Responsable du support, confirmation écrite.
6. Le devis daté de l'indépendant ne dépasse pas 2 jours de construction pour la première phase `[H]`. Direction générale (`04-feuille-de-route.md` : devis au 2026-10-09).

**Contre-argument le plus fort** : une fois les cinq standardisations faites, la construction ne retire plus que 83 min par séance, au plus environ 172 € par mois de temps libéré `[E]`, pour 1 348 € de construction et 51 € de coûts mensuels `[H]`. S'arrêter à l'option 0 et employer les 2,7 h par mois qu'elle libère `[E]` aux appels aux retards de plus de 35 jours serait plus sûr. Il ne l'emporte pas encore, parce que l'option 0 laisse la séance à 115 min `[E]` et dépend de la discipline de chacun, y compris de la comptable pendant les cinq semaines d'absence de la gestionnaire clients `[H]`.

**Ce qui ferait changer d'avis** :
- la re-mesure ne laisse pas assez à retirer : on s'arrête à l'option 0 ;
- la page de l'éditeur ne garantit pas l'hébergement dans l'Union européenne : l'option 3 prend la place de l'option 4 ;
- le devis dépasse sensiblement 2 jours de construction : on refait le calcul de `50-rentabilite.md` ;
- la fonction de relance de S1 se révèle capable d'exclure par facture et d'attendre une validation, contre la réponse du 2026-10-05 `[H]` : l'option 1 redevient candidate.

**Condition d'arrêt** : pendant le pilote, une relance envoyée sans validation, ou deux relances à tort dans la semaine, ou une séance au-dessus de 115 min `[E]` deux lundis de suite. On suspend les envois (ENF-10) et on revient à l'option 0.

**Option de repli** : 0, ne rien construire, poursuivre selon la procédure unique, à la main. Elle vient en second parce qu'elle laisse la séance à 115 min `[E]`, contre la cible de 60 min `[F]`, et ne protège pas d'un oubli. Elle n'a aucun risque lié à un outil.

## 2. Faut-il automatiser ?

| Facteur | Valeur | Statut et source |
|---|---|---|
| Fréquence | 96 relances par mois ; une séance par semaine, soit 4 par mois | `[F]` export de facturation ; `[E]` |
| Temps gagné par occurrence | 3,5 min par relance pour la construction (83 min par séance ÷ 24) ; 1,7 min par relance pour les simplifications seules (41 ÷ 24) | `[E]` d'après `20-diagnostic.md` §9 ; temps résiduel supposé `[H]` |
| Taux d'erreur à la main | 13 réclamations après relance par mois, soit 13,5 % des relances ; une réclamation coûte 14 min d'un agent, soit 6,77 € | `[F]` export des tickets ; `[E]` ; 14 min `[H]` (responsable du support) |
| Stabilité du processus | instable aujourd'hui : trois règles non écrites, deux façons de faire déclarées, logiciel en renouvellement en mars 2027 ; cinq standardisations décidées, datées du 2026-10-05 et du 2026-10-09 | `[F]` et `[H]`, `20-diagnostic.md` §5 |

Verdict : standardiser d'abord, puis construire l'option 4 sous la porte de la rubrique 10. Le processus est fréquent et utile à automatiser, mais deux réponses du test de stabilité sont négatives. L'option 0 s'applique dès maintenant ; la construction attend la porte, constatée au plus tôt le 2026-10-27, et aucune dépense de construction ne la précède. La fiche prépare pourtant l'option construite pendant ce délai, parce que la direction générale veut le plan validé avant le 2026-10-16 `[H]`.

## 3. Le chemin le plus simple

Question : quel est le chemin le plus simple pour que les relances partent au bon moment, vers les bons clients, validées par un humain ?

Réponse : supprimer les deux contrôles que les causes rendent inutiles. Le contrôle du relevé disparaît si le rapprochement des paiements précède la séance. Les messages aux commerciaux disparaissent si le support partage la liste des litiges. S'y ajoutent trois écritures : la procédure unique, la liste des comptes clés, un historique à format fixe (`20-diagnostic.md` §7).

Option 0, précisément. Ce qui change : ces cinq points, tenus par l'équipe interne. Ce qu'elle règle des exigences : EF-02, EF-04 et EF-06 par des règles de travail, ENF-09 par l'ordre des tâches. Ce qu'elle ne règle pas : EF-07 (52 min de rédaction à la main `[F]`), la recherche des doubles à la main (EF-03), la consignation et le compte rendu (EF-11, EF-14). Résultat : la séance passe de 156 à 115 min `[E]`, soit 41 min de moins.

## 4. Où l'humain reste dans la boucle

| Étape du processus cible (`30-exigences.md` §3) | Niveau | Pourquoi | Rôle qui valide |
|---|---|---|---|
| 1 Rapprocher les paiements | humaine | écriture comptable ; jugement sur les paiements non reconnus | comptable |
| 2 Signaler les litiges | humaine | appréciation du support | responsable du support |
| 3 Établir la liste du lundi | automatisée | même schéma chaque fois, règles écrites | la liste est relue à l'étape 7 |
| 4 Contrôler la fraîcheur des paiements | automatisée | comparaison de dates ; en cas de doute, arrêt et avertissement | gestionnaire clients, avertie |
| 5 Écarter les factures non justifiées | automatisée | le jugement est déjà écrit en règles ; le motif de chaque exclusion se lit | gestionnaire clients, à l'étape 7 |
| 6 Préparer les courriels | automatisée | trois modèles, trois champs, aucun texte libre | gestionnaire clients, à l'étape 7 |
| 7 Valider | humaine | acte vers l'extérieur ; règle de la direction `[F]` | gestionnaire clients ; responsable financier pour les comptes clés |
| 8 Envoyer et consigner | préparée puis validée | l'envoi est irréversible : il suit la validation ; la consignation est automatique | gestionnaire clients |
| 9 Reporter et lister | automatisée | règle de report simple | aucun |
| 10 Rendre compte | automatisée | comptage | responsable financier, lecteur |

## 5. Les options examinées

| N° | Famille | Retenue pour la matrice ? | Pourquoi |
|---|---|---|---|
| 0 | Ne rien construire | oui | référence et repli ; déjà engagée |
| 1 | Configurer un outil déjà en place | oui, puis éliminée | la fonction de relance de S1 existe, désactivée `[F]` ; elle n'offre ni validation avant envoi ni exclusion par facture `[H]` |
| 2 | Brique existante | non | aucune brique existante vérifiée : recherche non faite, non vérifié `[H]` ; à faire avant de signer (rubrique 9) |
| 3 | Script ou petit service | oui | logique simple, mais maintenance par un tiers et coût de construction plus élevé |
| 4 | Workflow sans code | oui | quelques applications avec connecteurs ; un métier peut lire le flux ; premier résultat rapide |
| 5 | Assistant IA, humain dans la boucle | non | la préparation est déterministe : trois modèles, trois champs, règles écrites. Un modèle d'IA ajouterait du coût et un risque, et exigerait que les données ne quittent pas l'Union européenne (ENF-02) |
| 6 | Agent IA à autonomie bornée | non | le chemin est connu et les actions sont irréversibles : un workflow suffit |
| 7 | Hybride | non | deux technologies pour un besoin simple |

- **Option 0** : les cinq standardisations. Construite par l'équipe interne (responsable financier, gestionnaire clients, comptable, responsable du support). Réutilise S1, S2 et S3 tels qu'ils sont. Vérifié par l'observation de la séance du 2026-09-07 `[F]` ; effets chiffrés en plafond `[E]`.
- **Option 1** : la fonction de relance de S1, présente et désactivée `[F]`. Construite par l'éditeur ou configurée par le responsable financier. Réponse du responsable financier le 2026-10-05, d'après la documentation de l'éditeur, non revérifiée `[H]` : elle relance à J+7, J+21 et J+35 sur l'état de paiement rapproché, envoie sans validation, exclut par client et non par facture. Le responsable financier relie l'essai de 2024 à cet état de paiement, rapproché une fois par semaine `[H]`.
- **Option 3** : un petit service lisant les fichiers exportés et écrivant des brouillons. Construit par un indépendant ; hébergé dans l'Union européenne par l'entreprise. Rien d'existant à réutiliser que S1, S2 et S3 ; aucune page d'éditeur lue `[H]`.
- **Option 4** : un flux sur plateforme sans code, lisant les fichiers exportés de S1 et les listes de S2, écrivant les brouillons dans S3. Construit par un indépendant spécialisé, en deux phases : première phase, les neuf exigences indispensables (2 jours `[H]`) ; seconde phase, les six autres (1 jour `[H]`, décidée après le pilote). Maintenance après la livraison : le responsable financier est propriétaire et décide des changements de règles ; la gestionnaire clients assure la maintenance courante (1 h par mois `[H]`) ; la comptable est suppléante. Plateforme non choisie ; aucune page d'éditeur lue `[H]`.

## 6. Matrice

Éliminatoires. Option 0 : aucune fonction indispensable ne manque, tout reste à la main ; EF-07 ne donne pas son gain (séance à 115 min `[E]`, au-dessus des 60 min visées `[F]`) ; gardée comme référence et repli. Option 1 : éliminée, EF-10 non couverte (envoi direct `[H]`), EF-04 non couverte (exclusion par client `[H]`), contrainte ferme « validation humaine de chaque envoi » `[F]` violée. Options 3 et 4 : aucune ; pour la 4, l'hébergement dans l'Union européenne (ENF-02, ferme) et les brouillons sans envoi (EF-10) sont à vérifier avant de signer.

| Critère | 0 Ne rien construire | 1 Fonction de S1 (éliminée) | 3 Petit service, indépendant | 4 Workflow, indépendant |
|---|---|---|---|---|
| Couverture des exigences | acceptable : EF-01 à EF-04, EF-06, EF-08, EF-10, EF-11 tenues à la main ; EF-07 en 52 min `[F]` ; EF-09 et EF-12 à EF-15 non couvertes | non évalué | favorable : les neuf indispensables, puis les six autres | favorable : les neuf indispensables en première phase, les six autres en seconde |
| Coût de construction | favorable : 383 € mobilisés `[H]`, rien de payé | non évalué | défavorable : 2 248 € `[H]` (4 jours × 450 € + 448 € mobilisés) | acceptable : 1 348 € `[H]` (2 jours × 450 € + 448 € mobilisés) ; seconde phase 450 € `[H]` |
| Coût de fonctionnement (unité × volume) | favorable : 0 €, outils déjà payés | non évalué | favorable : 10 € par mois d'hébergement `[H]` | acceptable : 600 actions par mois `[E]`, 20 € par mois `[H]` |
| Maintenance | acceptable : 0,5 h par mois du responsable financier `[H]`, soit 26 € `[E]` | non évalué | défavorable : 2 h par mois `[H]`, soit 62 € `[E]` ; chaque changement de règle passe par l'indépendant | acceptable : 1 h par mois `[H]`, soit 31 € `[E]` ; le flux se lit et se règle en interne |
| Fiabilité et risque | acceptable : repose sur la discipline ; un rapprochement oublié ramène les relances à tort | non évalué | favorable : versionné, testé, rejouable ; alerte sur silence | acceptable : pannes visibles dans le journal ; file des échecs, alerte sur silence, interrupteur (ENF-10) ; connecteurs qui évoluent `[H]` |
| Sécurité et lieu des données | favorable : rien ne change | non évalué | favorable : hébergement choisi par l'entreprise | acceptable : les contacts transitent par la plateforme ; hébergement dans l'Union européenne à lire sur la page de l'éditeur `[H]` |
| Dépendance et portabilité | favorable : aucune | non évalué | acceptable : code de l'entreprise, repris par un autre indépendant sur la spécification | acceptable : flux exportable `[H]` ; entrées en fichiers, règles écrites ; remplaçable par l'option 3 |
| Compétences internes pour maintenir | favorable : aucune compétence nouvelle | non évalué | défavorable : aucune compétence de code en interne | acceptable : une demi-journée de formation de la gestionnaire clients `[H]` |
| Délai | favorable : terminée le 2026-10-09 `[H]` | non évalué | acceptable : environ 3 semaines après la porte `[H]` | favorable : environ 2 semaines après la porte `[H]` |

Lecture. L'option 4 n'a aucun critère défavorable ; ses deux critères à surveiller sont le lieu des données et la fiabilité. L'option 3 est défavorable sur trois critères (coût, maintenance, compétences) : elle ne passe devant que si le lieu des données de l'option 4 n'est pas garanti.

## 7. L'option de repli

Option 0, examinée avec la même grille.

- **Raisons** : déjà engagée, 383 € mobilisés `[H]` ; retire 41 min par séance, soit environ 85 € par mois de temps au plus `[E]`, sans dépendance ; traite les causes des relances à tort (ordre du rapprochement, litiges invisibles, règles non écrites) que ni l'option 3 ni l'option 4 ne règlent.
- **Conditions** : rapprochement avant la séance (comptable, Q-06) ; liste des litiges alimentée chaque jour (responsable du support) ; procédure unique appliquée de la même façon par la comptable (responsable financier).
- **Contre-argument** : la séance reste à 115 min `[E]`, presque le double de la cible ; le risque revient pendant les cinq semaines d'absence de la gestionnaire clients `[H]`.
- **Pourquoi elle vient en second** : elle ne tient pas la cible de temps.

## 8. Plateforme ou code

Pour l'option 4.

- Unité de facturation : à l'action, une action par étape exécutée `[H]` (tarif non lu).
- Volume : environ 150 actions par séance `[E]` (61 factures évaluées + 24 brouillons + 24 envois + 24 lignes d'historique + 17 étapes fixes `[H]`), soit 600 par mois `[E]`, 660 avec la croissance de 10 % `[E]`.
- Ordre de grandeur du coût mensuel : 20 € `[E]`, premier palier d'une offre à l'action. Tarif et quota inclus non lus : `[H]`.
- Page de l'éditeur lue : non, `[H]`. À lire et dater par le responsable financier avant le 2026-10-09 : unité, quota, limites, région des données, export, engagement.
- Façon d'en sortir : exporter le flux ; les entrées sont des fichiers, les règles et modèles sont écrits dans la spécification ; l'option 3 peut le remplacer en 3 jours environ `[H]`.

## 9. À vérifier avant de signer

| Hypothèse `[H]` | Qui la confirme | Avant quand |
|---|---|---|
| Hébergement dans l'Union européenne, unité, quota et prix de la plateforme, lus et datés | responsable financier | 2026-10-09 |
| Devis daté de l'indépendant (première phase : 2 jours) et recherche d'une brique existante avant de signer | direction générale | 2026-10-09 |
| Brouillons écrits dans la boîte partagée sans envoi possible par le flux | responsable financier, indépendant | 2026-10-09 |
| Confirmation écrite de la liste des litiges alimentée chaque jour | responsable du support | 2026-10-09 |
| Minutes gagnables par séance et temps résiduel supposé de 32 min | gestionnaire clients (re-mesure), puis pilote | 2026-10-26, puis fin du pilote |
| Maintenance d'une heure par mois | responsable financier | à relever au pilote |

## 10. Porte

L'option 4 est retenue sous condition (standardiser, puis construire). L'option 0 s'applique dès maintenant ; la construction attend que les quatre conditions ci-dessous soient constatées.

| Condition de démarrage | Mesure (qui, comment) | Agrégation | Seuil | Date au plus tôt | Constatée par |
|---|---|---|---|---|---|
| La procédure unique tient et la séance laisse assez à retirer | gestionnaire clients : relevé horodaté des phases É1, É2, É5 et É6, un par lundi (2026-10-12, 2026-10-19, 2026-10-26) | moyenne des trois lundis | au moins 112 min `[E]` (80 gagnables + 32 résiduelles `[H]`), seuil du point mort de `50-rentabilite.md` §4 | 2026-10-27 | responsable financier |
| Le devis et la maintenance restent sous le point mort | devis daté de l'indépendant ; estimation écrite de la maintenance | chaque pièce | devis d'au plus 975 € payé ; maintenance d'au plus 1,1 h par mois `[E]` (`50-rentabilite.md` §4) | 2026-10-09 pour le devis | responsable financier |
| L'usage du temps libéré est nommé | message daté de la direction générale : qui appelle, combien de clients par mois, à partir de quel lundi | une pièce | les trois réponses | 2026-10-09 | responsable financier |
| La colonne « litige » est alimentée chaque jour | confirmation écrite du responsable du support, puis cinq jours ouvrés consécutifs avec une mise à jour datée dans la colonne | chaque jour | cinq jours sur cinq `[H]` | 2026-10-16 | responsable financier |

Tant que la porte est fermée : l'option 0 s'applique, la gestionnaire clients mesure les trois lundis, la spécification et le devis se préparent. Ne se dépense pas : le devis ne se signe pas, aucune plateforme ne s'ouvre, rien ne se construit. Un lundi ne compte que si les cinq standardisations sont en place ce jour-là et qu'aucune règle n'a changé dans la semaine. La porte se constate avec les autres conditions de la rubrique 1, avant toute signature : hébergement dans l'Union européenne (condition 2), envoi impossible depuis le compte de service (condition 3) et date du dernier rapprochement lue dans l'extraction (Q-10, `60-specification.md` §16). Si une condition de la porte est « non » : la construction ne démarre pas et l'option 0 reste en place.

## 11. Questions ouvertes

| ? | Question | Rôle qui répond | Statut |
|---|---|---|---|
| Q-01 | La fonction de relance de S1 sait-elle exclure, attendre une validation, lire l'état du rapprochement ? | responsable financier | répondue le 2026-10-05 `[H]` (rubrique 5, option 1) ; `30-exigences.md` garde la question telle que posée le 2026-10-02 |
| Q-04 | Pourquoi l'essai de 2024 a-t-il écrit à des clients qui avaient payé ? | responsable financier | répondue le 2026-10-05 `[H]` : état de paiement rapproché une fois par semaine |
| Q-02 | Quel seuil de montant ? | responsable financier | ouverte, échéance 2026-10-09 `[H]` |
| Q-03 | Qui tient la liste des comptes clés ? | responsable financier | ouverte, échéance 2026-10-09 `[H]` |
| Q-06 | Le rapprochement avant la séance a-t-il été tenu le lundi 2026-10-05, et à quel jour et quelle heure le fixer ? | comptable | ouverte, constat attendu `[H]`, bloquante avant le pilote |
| Q-09 | Quelle plateforme, quel éditeur, quelle région d'hébergement ? | indépendant, après lecture des pages des éditeurs | ouverte, avant le devis du 2026-10-09 `[H]` |

## Décision attendue

Choisir l'option retenue, le repli ou l'option 0 (ne rien construire), et dire qui construit.
