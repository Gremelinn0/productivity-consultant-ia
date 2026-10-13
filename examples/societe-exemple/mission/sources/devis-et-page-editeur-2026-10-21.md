> **Source fictive.** Pièces simulées pour l'exemple du pack consultant-ia : un devis et une page d'éditeur inventés. Aucune personne, aucun chiffre et aucune entreprise réels. La plateforme est appelée « plateforme P » : aucun produit existant n'est visé.

# Devis de l'indépendant et page de l'éditeur · lus les 2026-10-20 et 2026-10-21

Pièces demandées par `70-plan.md` aux étapes 7 et 8, pour constater la porte de `40-solutions.md` §10 et lever la question bloquante Q-09 de `60-specification.md` §16. Le devis est remis à la direction générale ; la page de l'éditeur est lue et datée par le responsable financier.

## 1. Devis de l'indépendant · daté du 2026-10-20 (étape 7)

Objet : construction de la première phase du flux de relances sur la plateforme P (EF-01 à EF-04, EF-06 à EF-08, EF-10, EF-11), selon `60-specification.md` version 1.2.

| Ligne | Contenu | Montant |
|---|---|---|
| Construction | 2 jours à 450 € HT, dans l'espace d'essai puis en production, tests T-01 à T-21 exécutés avant la recette, fiche d'exploitation d'une page | 900 € HT, ferme |
| Garantie | correction des défauts de la version livrée pendant 30 jours après la bascule, sans frais | 0 € |
| Maintenance | estimée à 1 h par mois (changement de règle, évolution d'un connecteur), facturée seulement sur demande | 0 € sans demande |

Recherche d'une brique existante, faite par l'indépendant : un modèle « relance de factures » de la bibliothèque de l'éditeur. Il lit le tableur, écrit les courriels et les envoie directement, sans clé de dédoublonnage ni journal. Écarté comme base (il contredit EF-10) ; sa mise en forme du courriel sert d'inspiration.

Suppléant de l'indépendant (R-08) : une consœur de son réseau, qui connaît la plateforme P et reçoit la spécification et la fiche d'une page à la signature. Rôle : suppléant de l'indépendant.

Dépendances que le devis attend du client : un espace d'essai séparé et ses comptes de test, un compte de service nommé pour la production, les trois secrets déposés par le client lui-même dans le coffre de la plateforme, les jeux d'essai.

Lecture du responsable financier : 900 € payés (au plus 975 €, `50-rentabilite.md` §4) ; maintenance estimée à 1 h par mois (au plus 1,1 h) ; région d'hébergement nommée à l'article 4 (page de l'éditeur, ci-dessous).

## 2. Page de l'éditeur de la plateforme P · lue le 2026-10-21 (étape 8)

Lue par le responsable financier, copiée telle que l'éditeur la publie ; les rubriques correspondent à `40-solutions.md` §8.

| Rubrique | Texte de l'éditeur (résumé fidèle) |
|---|---|
| Hébergement | « Vos données sont hébergées dans l'Union européenne (Francfort). » |
| Unité de facturation | l'opération : « une action exécutée par un scénario » ; une lecture ou une écriture de tableur, la création, la lecture ou la suppression d'un message, l'envoi d'un message d'alerte comptent chacune pour une opération |
| Paliers | « Entrée : 20 € par mois, 1 000 opérations. Équipe : 35 € par mois, 5 000 opérations. Au-delà du quota, le compte passe automatiquement au palier supérieur pour le mois en cours. » |
| Espaces | plusieurs espaces de travail par compte (essai, production) ; les opérations de tous les espaces s'ajoutent sur le quota du compte |
| Coffre | « Les connexions et leurs secrets sont chiffrés ; aucun export de scénario ne les contient. » |
| Export | export d'un scénario en fichier JSON, sans secrets, depuis le palier d'entrée |
| Historique d'exécution | conservé 30 jours ; supprimable à la demande, sur la résiliation, sous 30 jours |
| Engagement | mensuel, sans durée minimale ; préavis de résiliation de 30 jours |
| Support | courriel, réponse sous 2 jours ouvrés |
| Déclencheurs | planification à la minute, ou surveillance d'un dossier de messagerie ; un second scénario peut porter un déclencheur distinct |

Lecture du responsable financier :
- hébergement dans l'Union européenne, tel que publié : condition (c) de la porte remplie ;
- le quota du palier d'entrée (1 000 opérations par mois) remplace l'hypothèse « 600 actions par mois » de `40-solutions.md` §8, dont le tarif et le quota inclus n'étaient pas lus : le palier d'entrée convient si la consommation reste sous 1 000 `[H]` ;
- l'historique d'exécution est conservé 30 jours : la trace durable reste le journal du classeur du dispositif (Q-12) ;
- un second scénario peut porter l'alerte de silence avec son propre déclencheur ; il ne couvre pas une panne de la plateforme elle-même (Q-13).
