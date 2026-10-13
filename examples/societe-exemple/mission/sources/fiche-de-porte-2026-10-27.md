> **Source fictive.** Pièce simulée pour l'exemple du pack consultant-ia : une fiche de porte inventée. Aucune personne, aucun chiffre et aucune entreprise réels.

# Fiche de porte · 2026-10-27

Constatée par le responsable financier ; la direction générale est informée (`70-plan.md`, étape 13). Porte de `40-solutions.md` §10, reprise en `60-specification.md` §1 : conditions (a), (b), (e), (f) ; autres conditions de `40-solutions.md` §1 : (c), (d), (g). Une ligne par condition, avec sa pièce.

| # | Condition | Pièce | Seuil | Constat |
|---|---|---|---|---|
| a | Moyenne des trois lundis aux phases É1, É2, É5 et É6 | relevés horodatés du tableur partagé : lundi 2026-10-12, 119 min ; lundi 2026-10-19, 113 min ; lundi 2026-10-26, 111 min. Pour chacun des trois lundis, le tableau des cinq standardisations est plein et aucune règle n'a changé dans la semaine (`70-plan.md`, étape 1) | au moins 112 min en moyenne `[E]` | moyenne 114,3 min `[F]` : remplie |
| b | Devis et maintenance estimée | devis de l'indépendant du 2026-10-20 (`devis-et-page-editeur-2026-10-21.md` §1) : 900 € HT payés, maintenance estimée à 1 h par mois | au plus 975 € payés ; au plus 1,1 h par mois `[E]` | remplie |
| c | Hébergement dans l'Union européenne | page de l'éditeur lue le 2026-10-21 (`devis-et-page-editeur-2026-10-21.md` §2) : « Vos données sont hébergées dans l'Union européenne (Francfort). » | écrit par l'éditeur | remplie |
| d | Envoi impossible depuis le compte de service (EF-10) | essai écrit du 2026-10-22 sur une boîte de test, responsable financier avec l'indépendant : brouillon créé ; envoi par le compte de service refusé ; tentative consignée au journal de la boîte | refus constaté | remplie |
| e | Colonne « litige » tenue cinq jours ouvrés de suite | message du responsable du support du 2026-10-16 ; cinq mises à jour datées, du 2026-10-12 au 2026-10-16 | cinq jours ouvrés `[H]` | remplie |
| f | Usage du temps libéré nommé | message de la direction générale au responsable financier, 2026-10-22 : le responsable financier appelle 12 clients en retard de plus de 35 jours par mois, les plus anciens d'abord, à partir du lundi 2026-12-21 | usage, nombre, date de départ | remplie |
| g | Date du dernier rapprochement disponible (Q-10) | l'extraction du 2026-10-12, ouverte avec la colonne lue, ne porte pas cette date ; repli prévu à l'étape 10 : un fichier d'une ligne, mis à jour par la comptable chaque vendredi à 16 h au lettrage | date lisible par le flux | remplie par le repli |

Sept conditions sur sept : la porte est constatée. Aucune dépense de construction n'est datée avant cette fiche.

## Questions levées avant la construction (`60-specification.md` §16)

| ? | Réponse | De qui · quand |
|---|---|---|
| Q-03 | La liste des comptes clés est l'onglet « comptes clés » du classeur de pilotage : 25 comptes, écrite le 2026-10-20 par le responsable financier, seul à pouvoir la modifier | responsable financier · 2026-10-20 |
| Q-06 | Le lettrage se fait le vendredi à 16 h, par la comptable (la séance du 2026-09-07 le montrait le jeudi) | comptable · 2026-10-14 |
| Q-07 | Les 13 réclamations d'un mois `[F]` : 7 pour une relance à un client qui avait déjà payé, 2 pour une relance à un client en litige, 4 pour une autre cause (montant contesté, facture en double) : 9 relances parties à tort par mois `[F]`, départ de l'indicateur IND-02 | responsable du support · 2026-10-15 |
| Q-09 | Plateforme P, hébergée à Francfort (`devis-et-page-editeur-2026-10-21.md`) | responsable financier · 2026-10-23 |
| Q-10 | L'extraction ne porte pas la date du dernier rapprochement : fichier d'une ligne `rapprochement.csv`, déposé avec l'extraction, mis à jour par la comptable au lettrage du vendredi | responsable financier avec la comptable · 2026-10-22 |
| Q-11 | La messagerie ne sait pas limiter l'envoi d'un dossier à un compte, et l'identifiant de relance ne figure pas sur la copie envoyée (l'essai du 2026-10-22 le montre) : repli par le numéro de facture et le niveau lus dans l'objet « Facture <numéro> — <libellé du niveau> », et contrôle des copies envoyées (alerte « envoi hors validation » quand un compte clé part d'un autre compte que celui du responsable financier) | responsable financier, indépendant · 2026-10-22 |
| Q-12 | L'historique d'exécution de la plateforme est conservé 30 jours et supprimable sous 30 jours à la résiliation ; la trace durable reste le journal du classeur du dispositif | indépendant · 2026-10-21 |

Restent ouvertes : Q-05 (base légale et durée de conservation de l'historique, bloquante avant la production), Q-13 (alerte de silence sur un déclencheur distinct, avant le pilote), Q-08 et Q-02 (non bloquantes).
