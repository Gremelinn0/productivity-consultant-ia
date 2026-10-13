# Exigences — Relances de factures échues

2026-10-02 · Demandeur, valideur et décideur : direction générale · Rédigé par : consultant IA · Version 1.1, précisée le 2026-10-09 : EF-01, étape 3 du processus cible et CA-01 (voir la note sous le tableau de la rubrique 4)
Version 1.2, précisée le 2026-11-12, en écrivant la recette (`85-recette.md`, défaut D-01) : CA-08 et la dernière phrase d'ENF-07. Le critère demandait le refus d'un envoi que la messagerie ne sait pas empêcher (Q-11, levée le 2026-10-22) et d'une « relance modifiée après validation », cas que le dispositif ne voit pas puisque la validation est l'envoi par la personne. Aucune autre exigence ni aucun autre critère ne change.
Mode exigences : écrit le 2026-10-02, avant la validation de `40-solutions.md` et de `50-rentabilite.md`.
Écrit pour être lu par quelqu'un qui n'a pas vécu la mission : prestataire ou équipe interne.

## 1. Contexte et objectifs

Problème (`10-besoin.md`). Des relances de factures échues partent chez des clients qui ont déjà payé ou qui sont en litige. La direction veut des relances qui partent au bon moment, vers les bons clients, seulement quand elles sont justifiées, avec un humain qui valide chaque envoi. Un essai de 2024 a été coupé après quelques semaines : il écrivait à des clients qui avaient déjà payé `[H]` (responsable financier).

État actuel mesuré (`20-diagnostic.md`). 96 relances par mois `[F]`, 13 réclamations après relance par mois `[F]`, une séance hebdomadaire de 156 min `[F]` dont 76 min de contrôles à la main `[E]`. Les causes sont l'ordre des tâches de rapprochement et de relance, des litiges invisibles de la finance, un historique sans format et trois règles non écrites. Le diagnostic conclut « à standardiser d'abord ».

Décision servie. Comparer des solutions sur un même énoncé (`concevoir-solution`), y compris celle qui ne change que le processus et celle qui ne construit rien. Ces exigences valent pour toute option.

Vocabulaire. « Dispositif » désigne ce qui sera mis en place, quelle que soit la solution. « J+7 » désigne sept jours après l'échéance de la facture ; les niveaux 1, 2 et 3 se déclenchent à J+7, J+21 et J+35. « HT » signifie hors taxes. Les identifiants sont : EF (exigence fonctionnelle), ENF (non fonctionnelle), CA (critère d'acceptation), IND (indicateur), Q (question ouverte) ; chaque série est numérotée une fois pour tout le cas. S1 à S4 : voir la rubrique 2.

Objectifs, comme résultats attendus :
- Réclamations après relance : au plus 7 par mois `[F]` (cible acceptée par la direction générale le 2026-09-24 : journal, `10-besoin.md` §8). Départ : 13 par mois `[F]`.
- Séance du lundi : sous 60 min `[F]` (même acceptation). Départ : 156 min `[F]`, une seule occurrence observée.
- Envois validés par un humain : 100 % `[F]` (règle de la direction). Départ : tout est envoyé à la main.
- Temps libéré réemployé aux appels aux clients en retard de plus de 35 jours : nombre d'appels par mois, à mesurer avant tout lancement. Stock de départ : 33 factures `[E]`.

## 2. Utilisateurs et rôles

S1 à S4 désignent les systèmes en place, décrits en rubrique 6.

| Rôle | Ce qu'il fait avec le dispositif | Nombre de personnes | Accès nécessaire |
|---|---|---|---|
| Gestionnaire clients | relit la liste, les motifs d'exclusion et les courriels ; corrige ; valide les envois | 1 `[F]` | S1 en lecture ; S2 en lecture et écriture ; S3 en écriture et envoi |
| Comptable | rapproche les paiements avant la séance ; remplace la gestionnaire clients en son absence, avec la même procédure | 1 `[F]` | S1 en lecture et rapprochement ; S2 en lecture ; S3 en écriture et envoi |
| Responsable financier | valide les relances des comptes clés ; tient la liste des comptes clés et les règles ; administre S1 ; reçoit le compte rendu | 1 `[F]` | S1 ; S2 en lecture et écriture |
| Support (responsable et agents) | signale chaque litige dans la journée ; reçoit les réclamations | 8 `[F]` | S4 ; écriture de la liste des litiges dans S2 |
| Commerciaux (touchés) | ne sont plus interrogés sur chaque client ; répondent seulement pour un litige absent de la liste | 10 `[F]` | aucun |
| Clients (destinataires) | reçoivent les relances | non compté | aucun |
| Direction générale | décide au-delà de 3 000 € ou de 100 € par mois `[F]` ; lit le compte rendu | direction : 3 `[F]` | lecture du compte rendu |

## 3. Processus cible

Le processus suppose les cinq standardisations de `20-diagnostic.md` (rubrique 7) : rapprochement des paiements avant la séance, liste des litiges partagée, procédure unique, liste des comptes clés, historique à format fixe.

1. Rapprocher les paiements. Déclencheur : avant la séance du lundi, jour et heure à fixer. Sortie : paiements à jour. [humain] la comptable.
2. Signaler les litiges. Déclencheur : l'ouverture d'un litige, chaque jour ouvré. Sortie : liste des litiges à jour. [humain] le support.
3. Établir la liste du lundi. Déclencheur : la demande de la gestionnaire clients. Sortie : les factures qui ont atteint le niveau 1, 2 ou 3 sans relance consignée à ce niveau, y compris celles écartées ou reportées une semaine précédente, chacune avec son niveau. Décident : les règles écrites.
4. Contrôler la fraîcheur des paiements. Si le dernier rapprochement date de plus d'un jour ouvré `[H]`, aucune relance n'est proposée et la gestionnaire clients est avertie.
5. Écarter les factures non justifiées. Sont écartées, avec leur motif : facture payée, déjà relancée au même niveau, en litige, sous le seuil de montant. Les factures de comptes clés sont mises à part. Sortie : relances proposées, comptes clés à valider, factures écartées avec motif.
6. Préparer les courriels. Un courriel par relance proposée, au modèle de son niveau, avec les données de la facture. Sortie : brouillons.
7. Valider. [humain] La gestionnaire clients relit la liste, les motifs et les courriels, retire ou corrige ce qu'elle juge, puis valide. [humain] Le responsable financier valide chaque relance de compte clé. Décident : ces deux rôles, aucune autre instance.
8. Envoyer et consigner. Seules les relances validées partent ; chaque envoi est consigné à l'instant où il part. Sortie : historique à jour.
9. Reporter et lister. Les factures dont la validation est en attente reviennent à la séance suivante. Les retards de plus de 35 jours sont listés pour des appels [humain].
10. Rendre compte. Chaque lundi, un compte rendu des chiffres de la séance est remis au responsable financier.

## 4. Exigences fonctionnelles

| ID | Exigence (« Le dispositif doit… ») | Priorité | Pourquoi (lien avec le besoin) | Source |
|---|---|---|---|---|
| EF-01 | établir, chaque lundi, la liste des factures qui ont atteint le niveau 1, 2 ou 3 et pour lesquelles aucune relance n'est consignée à ce niveau, y compris celles écartées ou reportées une semaine précédente. | Indispensable | point de départ du processus ; remplace l'extraction et le filtre à la main (12 min par séance `[F]`) ; une facture écartée la semaine précédente (litige levé, compte clé non validé) ne doit pas disparaître | 10-besoin ; 20-diagnostic §1 |
| EF-02 | écarter toute facture dont le paiement est rapproché. | Indispensable | 9 factures sur 61 déjà payées à la séance `[F]` ; cause de l'essai raté de 2024 `[H]` | 20-diagnostic §3 |
| EF-03 | écarter toute facture déjà relancée au même niveau. | Indispensable | 4 doubles évités sur 61 `[F]` ; un client relancé deux fois est une relance à tort | 20-diagnostic §3 |
| EF-04 | écarter toute facture signalée en litige, y compris pendant la séance. | Indispensable | 6 litiges connus et 7 à confirmer sur 61 `[F]` | 20-diagnostic §3 |
| EF-05 | écarter toute facture dont le montant est inférieur au seuil fixé par la procédure unique. | Important | 6 factures sur 61 sous 15 € `[F]` ; le cœur marche sans seuil ; le seuil reste à trancher (Q-02) | 20-diagnostic §4 |
| EF-06 | mettre à part les factures des comptes clés, qui ne partent qu'après validation du responsable financier. | Indispensable | règle du responsable financier ; 5 comptes clés sur 61 `[F]` ; un compte clé figure parmi les plaintes de 2024 `[H]` | entretien finance ; 20-diagnostic §3 |
| EF-07 | préparer un courriel par relance proposée, au modèle de son niveau, avec le numéro, le montant et l'échéance repris de la facture. | Indispensable | 52 min de rédaction par séance `[F]` ; sans cette exigence la séance reste à 60 min `[E]` (156 − 41 − 55, temps résiduel supposé `[H]`), sans passer sous le critère | 20-diagnostic §3 et §9 |
| EF-08 | présenter à la gestionnaire clients la liste des relances proposées et leurs courriels avant tout envoi. | Indispensable | sans elle, aucune validation humaine n'est possible | 10-besoin §7 |
| EF-09 | présenter les factures écartées avec leur motif. | Important | 37 factures écartées sur 61 `[F]` : la gestionnaire clients doit pouvoir vérifier ce qui ne part pas | 20-diagnostic §2 |
| EF-10 | n'envoyer aucune relance qu'une personne n'a pas validée. | Indispensable | règle de la direction `[F]` : « Plus aucun client ne reçoit une relance qu'un humain n'a pas vue. » | entretien direction ; 10-besoin §7 |
| EF-11 | consigner chaque relance envoyée à l'instant de l'envoi : facture, niveau, date, personne qui a validé. | Indispensable | alimente EF-03 ; la recherche à la main prend 35 min par séance `[F]` | 20-diagnostic §4 |
| EF-12 | permettre à la gestionnaire clients de retirer ou de corriger une relance proposée avant l'envoi. | Important | la validation n'est pas un simple accord ; le cœur marche sans correction de texte | 20-diagnostic §6 |
| EF-13 | reporter à la séance suivante toute facture dont la validation est en attente. | Important | 12 factures reportées sur 61 `[E]` ; sans report, elles seraient oubliées | 20-diagnostic §2 |
| EF-14 | produire chaque lundi un compte rendu : factures traitées, relances envoyées, factures écartées par motif, relances retirées ou corrigées, durée de la séance. | Important | alimente les indicateurs de la rubrique 10 | 10-besoin §8 |
| EF-15 | lister chaque lundi les factures en retard de plus de 35 jours. | Souhaitable | prépare le réemploi du temps libéré voulu par la direction ; 33 factures au 2026-08-28 `[E]` | entretien direction ; 10-besoin §8 |

Neuf exigences sur quinze sont indispensables : sans elles, une relance peut partir à tort, partir sans validation, ou la séance reste trop longue. Les six autres sont Importantes ou Souhaitables : le pilote peut tourner sans elles. La proportion tient à la nature du dispositif, d'abord un dispositif de sûreté (aucun envoi à tort, aucun envoi sans validation) ; le demandeur peut accepter de livrer d'abord les neuf indispensables `[H]` (direction générale, à confirmer en validant).

Version 1.1 (2026-10-09). EF-01 disait « depuis la dernière séance » : une facture écartée la semaine précédente n'aurait jamais reparu. Le trou est apparu en écrivant `60-specification.md` (test du constructeur) ; la formulation ci-dessus corrige EF-01, l'étape 3 du processus cible et CA-01. Aucune autre exigence ne change.

## 5. Données

| Donnée | Système source | Champs indispensables | Seuil de qualité | Statut | Source qui tranche en cas de conflit | Personnelle ? |
|---|---|---|---|---|---|---|
| Factures échues | S1 | identifiant de la facture, identifiant du client, montant HT, date d'échéance | aucun champ vide ; aucun numéro en double ; extraction du jour même | brute | S1 | oui, par l'identifiant du client |
| Paiements rapprochés | S1 | numéro de facture, date du dernier rapprochement | rapprochement daté de moins d'un jour ouvré `[H]` | validée (faite par la comptable) | S1 | non |
| Historique des relances | S2 | numéro de facture, niveau, date d'envoi, personne qui a validé | une ligne par facture et par niveau ; aucune ligne sur une autre facture | brute pour l'existant, validée pour les envois consignés (EF-11) | S2 | non |
| Litiges | S2, alimenté par le support depuis S4 | numéro de facture ou identifiant du client, date d'ouverture | mise à jour chaque jour ouvré ; aucune ligne sans date | brute (signalée par un agent) | le responsable du support | non |
| Comptes clés | S2 | identifiant du client | liste écrite, avec un propriétaire, relue une fois par trimestre `[H]` | validée | le responsable financier | non |
| Règles (délais, seuil, modèles) | procédure unique écrite (`20-diagnostic.md` §7) | niveau, délai en jours après l'échéance, seuil de montant, texte du modèle | un seul exemplaire en vigueur, daté | validée | le responsable financier | non |
| Contact à relancer | S1 | nom du contact, adresse de courriel | adresse présente et plausible ; sinon la facture n'est pas proposée (ENF-08) | brute | S1 | oui |

**Exclusions** — factures au-delà de J+60 (téléphone et courrier, par le responsable financier `[H]`) ; avoirs et gestes commerciaux ; factures en contentieux.

**Volumes** — par mois : 96 relances envoyées `[F]` (niveau 1 : 58 ; niveau 2 : 28 ; niveau 3 : 10), 170 factures qui deviennent échues `[F]`, 910 factures émises `[F]`. Par lundi : 61 factures à traiter, dont 24 relancées, à la séance du 2026-09-07 `[F]` (une occurrence). En pointe (fin de mois) : non mesuré `[H]` (responsable financier). Croissance attendue : 10 % d'activité en plus l'an prochain `[F]` (objectif de la direction), soit environ 106 relances par mois `[E]` (96 × 1,1).

**Données personnelles** — nom et adresse de courriel du contact client ; finalité : envoyer la relance de la facture concernée ; conservation : à fixer, seul l'historique minimal de EF-11 est gardé. À confirmer `[H]` : la base légale et la durée de conservation, par la personne que la direction générale désigne pour la conformité. Le pack ne conclut pas sur la conformité. Tout reste dans l'Union européenne `[F]`.

## 6. Intégrations

| Système | Lire / écrire | Ce qui est lu ou modifié | Accès aujourd'hui (oui · non · à demander à <rôle>) | Limites connues |
|---|---|---|---|---|
| S1 Logiciel de facturation | lire | factures échues, paiements rapprochés, contacts à relancer | oui pour l'extraction manuelle ; accès automatique à demander au responsable financier | module de relances présent et désactivé `[F]`, capacités non vérifiées `[H]` ; renouvellement décidé en mars 2027 `[F]` |
| S2 Tableur partagé | lire et écrire | lire : litiges, comptes clés, historique ; écrire : historique des relances | oui pour les personnes ; accès pour le dispositif à demander au responsable financier | l'historique est tenu à la main, sans format imposé `[F]` |
| S3 Messagerie (boîte partagée de la finance) | écrire des brouillons ; envoyer après validation | courriels de relance | oui pour la gestionnaire clients et la comptable ; accès pour le dispositif à demander au responsable financier | trois modèles de courriel dans un document `[F]` |
| S4 Outil de tickets | lire (support seulement) | étiquette « litige » posée par les agents | oui pour le support, non pour la finance `[F]` | la finance reçoit l'information par la liste des litiges de S2, pas par S4 `[H]` |

## 7. Exigences non fonctionnelles

| ID | Domaine | Exigence | Preuve ou mesure |
|---|---|---|---|
| ENF-01 | Sécurité | Les coordonnées des contacts ne sont lisibles que par la gestionnaire clients, la comptable et le responsable financier ; le dispositif n'y accède que pour préparer un courriel. | liste des accès relue par le responsable financier avant le pilote |
| ENF-02 | Sécurité | Aucune donnée client ne quitte l'Union européenne, y compris vers un service tiers ou un modèle `[F]`. | lieu d'hébergement écrit par chaque fournisseur consulté |
| ENF-03 | Conformité | Les adresses ne servent qu'à envoyer la relance de la facture concernée. L'historique garde le minimum de EF-11, pour une durée fixée par la direction générale `[H]`. | fiche de traitement écrite avant le pilote ; durée relue par la personne désignée pour la conformité |
| ENF-04 | Disponibilité | Le dispositif est utilisable le lundi de 8 h à 12 h `[H]` (gestionnaire clients). Une panne ne bloque pas la séance : la méthode actuelle reprend. | test d'arrêt en recette |
| ENF-05 | Délai | La liste du lundi (EF-01 à EF-06) est prête moins de 5 min après la demande `[H]`. | chronométrage en recette, sur le rejeu des 61 factures |
| ENF-06 | Traçabilité | Chaque relance garde : facture, niveau, date, personne qui a validé, version du modèle et des règles. Durée de conservation : voir ENF-03. | relecture de 10 relances `[H]` en recette |
| ENF-07 | Validation humaine | La gestionnaire clients valide la liste pendant la séance. Le responsable financier valide chaque relance de compte clé dans un délai maximal de 2 jours ouvrés `[H]` ; passé ce délai, la facture est reportée (EF-13). La validation est l'envoi par la personne : ce qu'elle envoie, elle l'a lu (version 1.2). | les deux cas de CA-08 |
| ENF-08 | Politique d'erreur | Une facture que le dispositif ne sait pas traiter (donnée manquante, contact introuvable, conflit entre deux sources) n'est jamais proposée : elle va dans une liste « à traiter à la main », visible de la gestionnaire clients le jour même. | test avec trois factures sans adresse `[H]` |
| ENF-09 | Politique d'erreur | Si le dernier rapprochement des paiements date de plus d'un jour ouvré `[H]`, aucune relance n'est proposée et la gestionnaire clients en est avertie. | CA-10 |
| ENF-10 | Politique d'erreur | La gestionnaire clients et le responsable financier peuvent suspendre tous les envois à tout moment ; la méthode actuelle reprend aussitôt. | test d'arrêt en cours d'envoi |

## 8. Contraintes

| Contrainte | Ferme ou négociable | Qui peut la lever |
|---|---|---|
| Accord de la direction générale au-delà de 3 000 € par projet et de 100 € par mois de coût récurrent `[F]` | ferme | direction générale |
| Pilote et première phase de ce cas sous 3 000 € `[H]` | négociable | direction générale |
| Retour de l'investissement en 18 mois au plus, sur le scénario central `[F]` | ferme | direction générale |
| Plan validé avant le 2026-10-16 `[H]` | négociable | direction générale |
| Dispositif en service avant la décision de renouvellement du logiciel de facturation de mars 2027 `[H]` | négociable | direction générale |
| Outils imposés : logiciel de facturation (S1) jusqu'à la décision de mars 2027 `[F]` ; tableur partagé (S2) et messagerie (S3), outils de travail de la finance | ferme | direction générale |
| Validation humaine de chaque envoi `[F]` | ferme | direction générale |
| Données hébergées dans l'Union européenne `[F]` | ferme | direction générale |
| Équipe : la gestionnaire clients est absente cinq semaines par an `[H]` ; la comptable doit pouvoir tenir la séance | ferme | responsable financier |
| Gel : aucun démarrage de pilote pendant la clôture de fin de mois `[H]` | négociable | responsable financier |

## 9. Critères d'acceptation

Le rejeu est la séance du 2026-09-07 reconstituée par le responsable financier, avec le rapprochement des paiements fait et les 6 litiges connus `[F]` inscrits dans la liste des litiges. Les 7 factures en attente d'une réponse du commercial `[F]` n'y servent pas : leur sort dépend de la liste des litiges à la date du rejeu.

| ID | Exigence | Critère (Donné / Quand / Alors, ou seuil mesurable) | Données et méthode de vérification |
|---|---|---|---|
| CA-01 | EF-01 | Donné le rejeu où 61 factures atteignent un seuil `[F]`, quand la liste est établie, alors elle contient ces 61 factures, chacune au bon niveau (7, 21 ou 35 jours après l'échéance). Donné une facture écartée à la séance précédente (litige levé depuis), sans relance consignée à son niveau, quand la liste est établie, alors elle y figure. | extraction du jour reconstituée ; comparaison ligne à ligne avec le décompte de la séance ; ajout d'une facture écartée la semaine précédente |
| CA-02 | EF-02 | Donné 9 factures dont le paiement est rapproché `[F]`, quand la liste des relances est établie, alors aucune des 9 n'est proposée et chacune est écartée avec le motif « payée ». | rejeu ; contrôle des 9 numéros |
| CA-03 | EF-03 | Donné 4 factures déjà relancées à leur niveau dans l'historique `[F]`, quand la liste est établie, alors aucune des 4 n'est proposée, motif « déjà relancée ». | rejeu ; contrôle des 4 numéros |
| CA-04 | EF-04 | Donné 6 factures signalées en litige `[F]`, quand la liste est établie, alors aucune des 6 n'est proposée, motif « litige ». Donné un litige signalé pendant la séance, quand la gestionnaire clients valide, alors la facture concernée est retirée avant tout envoi. | rejeu ; ajout d'un litige en cours de séance |
| CA-05 | EF-05 | Donné un seuil de 15 € `[H]` et 6 factures de montant inférieur `[F]`, quand la liste est établie, alors aucune des 6 n'est proposée, motif « sous le seuil ». | rejeu ; seuil réglé comme dans la procédure unique |
| CA-06 | EF-06 | Donné 5 factures de comptes clés `[F]`, quand la liste est établie, alors elles figurent seulement dans la liste « à valider par le responsable financier » et aucun courriel ne part avant sa validation. | rejeu ; tentative d'envoi sans validation |
| CA-07 | EF-07 | Donné les 24 relances proposées (niveau 1 : 14 ; niveau 2 : 7 ; niveau 3 : 3) `[F]`, quand les courriels sont préparés, alors chacun porte le modèle de son niveau et le numéro, le montant et l'échéance de sa facture, sans écart (0 écart toléré `[H]`). | contrôle des 24 courriels contre la facture source par la gestionnaire clients |
| CA-08 | EF-10 | Donné une relance non validée, quand l'envoi est demandé par le compte de service, alors rien ne part et le refus est enregistré. Donné un compte clé envoyé par un autre rôle que le responsable financier, alors l'envoi n'est pas empêché (la messagerie ne limite pas l'envoi d'un dossier à un compte, Q-11), mais il est détecté au passage suivant de la veille, 10 min au plus `[H]`, et signalé au responsable financier (version 1.2). | test du cas interdit, deux cas |
| CA-09 | EF-11 | Donné 24 envois validés, quand ils sont terminés, alors l'historique contient 24 lignes, une par envoi, avec facture, niveau, date et validateur. Donné un envoi rejoué après une panne, alors aucune seconde ligne n'est créée et aucun second courriel ne part. | rejeu ; coupure volontaire pendant l'envoi |
| CA-10 | EF-02, ENF-09 (cas limite critique) | Donné un client qui a payé vendredi, paiement non rapproché, et un dernier rapprochement vieux de plus d'un jour ouvré, quand la liste est demandée, alors aucune relance n'est proposée et la gestionnaire clients lit « rapprochement trop ancien ». | test avec une date de rapprochement ancienne |
| CA-11 | EF-08 | Donné la liste des 24 relances proposées, quand la gestionnaire clients ouvre la séance, alors elle peut lire pour chacune le niveau et le courriel avant tout envoi. | recette sur les 24 relances |
| CA-12 | EF-13 | Donné 5 comptes clés non validés à la fin de la séance `[F]`, alors ils reviennent sur la liste de la séance suivante avec leur ancienneté. | rejeu sur deux lundis |
| CA-13 | EF-14 | Donné la séance rejouée, quand elle se termine, alors le compte rendu indique 61 factures traitées `[F]`, les relances envoyées, les factures écartées par motif et les relances retirées ou corrigées. | comparaison avec le décompte de la séance |

## 10. Indicateurs

Les seuils de correction, d'alerte et d'arrêt, la lecture et l'attribution ne sont pas écrits ici : ils vivent dans `60-specification.md` §14.

| ID | Indicateur | Type | Pourquoi (décision permise) | Départ et période fiable | Cible issue du besoin |
|---|---|---|---|---|---|
| IND-01 | Réclamations après relance | qualité | resserrer les règles ou arrêter le pilote | 13 par mois `[F]`, moyenne de mai à juillet 2026 ; fiable sur ces trois mois | au plus 7 par mois `[F]` (`10-besoin.md` §8, acceptée le 2026-09-24) |
| IND-02 | Relances parties à tort (facture payée, en litige ou déjà relancée à ce niveau) | qualité | poursuivre ou arrêter le pilote | à relever avant tout lancement `[H]` : classer par motif les 13 réclamations d'un mois | aucune : tout cas est un défaut |
| IND-03 | Durée de la séance du lundi | résultat | généraliser, prolonger ou arrêter | 156 min `[F]` (séance du 2026-09-07, une occurrence) ; à confirmer sur trois lundis avant le lancement | sous 60 min `[F]` (`10-besoin.md` §8, acceptée le 2026-09-24) |
| IND-04 | Relances envoyées sans validation humaine | qualité | arrêter aussitôt | 0 `[F]` : tout est envoyé à la main (entretien direction) | 100 % des envois validés `[F]` (`10-besoin.md` §8) |
| IND-05 | Part des relances proposées retirées ou corrigées | qualité | resserrer les règles ou les modèles | à relever au pilote `[H]`, aucun départ | aucune cible dans le besoin : mesure d'usage |
| IND-06 | Stock des retards de plus de 35 jours | résultat | lancer ou élargir les appels | 33 factures, 30 900 € HT `[E]` au 2026-08-28 (22 + 11 ; 20 100 + 10 800 € HT) ; relevé d'un seul jour | aucune cible chiffrée dans le besoin : indicateur de contexte |
| IND-07 | Appels aux clients en retard de plus de 35 jours | activité | vérifier que le temps libéré est réemployé comme décidé | à mesurer avant tout lancement : aucun appel régulier aujourd'hui selon la direction `[H]` | nombre d'appels par mois nommé par la direction générale (`10-besoin.md` §8) |

## 11. Hors périmètre

| Hors périmètre | Raison | Peut revenir ? |
|---|---|---|
| Téléphone et courrier recommandé au-delà de J+60 | jugement et relation, tenus par le responsable financier | oui, sur sa demande |
| Contentieux | hors du cas | non dans ce cas |
| Remplacement du système qui émet les factures | décision de mars 2027 `[F]`, autre chantier | oui, après cette décision |
| Avoirs et gestes commerciaux | décisions de la finance | non |
| Envoi sans validation humaine | interdit par la direction `[F]` | non |
| Aide à la réponse aux réclamations | cas écarté du portefeuille (`02-portefeuille.md`) | oui, si les réclamations restent au-dessus de 13 par mois `[F]` quand les relances sont corrigées |
| Rapprochement automatique des paiements | autre cas du portefeuille, à creuser | oui, quand les capacités de S1 sont connues |
| Les appels eux-mêmes aux clients en retard de plus de 35 jours | réemploi du temps libéré, pas une fonction du dispositif (EF-15 en fournit la liste) | non |

## 12. Questions ouvertes

| ? | Question | Rôle qui répond | Bloquante pour le choix d'une solution ? | Échéance ou statut |
|---|---|---|---|---|
| Q-01 | La fonction de relance déjà présente dans S1 (rubrique 6) peut-elle exclure litiges, comptes clés et petits montants, attendre une validation, lire l'état du rapprochement ? S1 offre-t-il un accès automatique en lecture ? | responsable financier (documentation de l'éditeur) | oui | 2026-10-02 `[H]` |
| Q-02 | Quel seuil de montant retenir : 15 € observé, « pas de seuil » déclaré ? | responsable financier | non | 2026-10-09 `[H]` |
| Q-03 | Qui tient la liste des comptes clés, et où est-elle écrite ? | responsable financier | non | 2026-10-09 `[H]` |
| Q-04 | Pourquoi l'essai de 2024 a-t-il écrit à des clients qui avaient payé ? | responsable financier | oui | 2026-10-02 `[H]` |
| Q-05 | Quelle base légale et quelle durée de conservation pour l'historique ? | personne désignée par la direction générale | non | 2026-10-16 `[H]` |
| Q-06 | Le rapprochement avant la séance est-il tenable pour la comptable : quel jour, quelle heure ? | comptable | non, mais bloquante avant le pilote | 2026-10-05 `[H]` |
| Q-07 | Quel est le motif des 13 réclamations d'un mois : relance à tort ou autre cause ? | responsable du support | non | 2026-10-16 `[H]` |
| Q-08 | Quelle règle suit la comptable quand elle remplace la gestionnaire clients ? | comptable | non | 2026-10-09 `[H]` |

## Décision attendue

Valider les exigences et leurs priorités — ou les corriger ; lever les questions bloquantes ; autoriser la comparaison des solutions (`concevoir-solution`) ou la consultation de prestataires.
