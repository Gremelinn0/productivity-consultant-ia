# La charte d'usage : le modèle

Elle tient en une page et se remet à chaque personne avant son premier accès. Elle dit ce qu'on fait, pas ce qu'on
craint : une liste d'interdits que personne ne relit protège moins qu'une habitude prise le premier jour. Elle vaut
pour tout assistant ; les noms de réglages changent d'un éditeur à l'autre, pas les règles.

## Comment l'écrire

- Partir des tâches de l'équipe relevées à l'étape 2 : chaque exemple de la charte vient de son travail réel.
- Remplir chaque `<...>`, retirer ce qui ne s'applique pas, ajouter ce que le métier impose, garder l'ordre.
- Deux assistants autorisés (une licence déjà payée et le candidat retenu) : la charte les nomme tous les deux.
- Une charte informatique existe déjà : compléter ce texte plutôt que d'en poser un second. Une charte qui impose des
  obligations ou annonce des sanctions peut relever du règlement intérieur : la question se pose au rôle compétent
  (`dossier-conformite.md`, partie 5), le pack ne conclut pas.
- Elle se relit à chaque revue trimestrielle ; chaque version porte sa date.

## Le modèle, à recopier dans `mission/cas-<slug>/90-mise-en-service/charte-usage.md`

```markdown
# Notre usage de <assistant> · version <n> du <date>

Pour qui : les personnes de <équipe> qui ont un compte. Tenue par : <rôle>, suppléant <rôle>. Relue chaque trimestre.

## 1. Le compte
- On travaille avec le compte de l'entreprise, jamais avec un compte personnel, même gratuit.
- Un compte par personne, jamais partagé, protégé par <connexion unique ou double authentification>.
- Un outil IA qui n'est pas sur cette page se demande à <rôle> avant de s'en servir pour le travail.

## 2. Avant de coller quelque chose
Trois questions, dans cet ordre :
1. Ce contenu permet-il de reconnaître une personne (nom, adresse, téléphone, numéro de compte) ?
2. Est-il couvert par une clause de confidentialité, avec le nom de l'autre partie ?
3. Touche-t-il à la paie, à une sanction, à la santé, à un dossier juridique, à des marges ou à des prix non publics ?

Un oui : on remplace les noms et les montants avant de coller (« Client A », « Salarié B », un ordre de grandeur), ou
on ne colle pas.
Jamais, même anonymisé : mots de passe, clés et jetons d'accès, numéros de sécurité sociale, ce qui relève d'un secret
professionnel, <ce que retirer le nom ne protège pas : plans, pièces techniques, formules>.

## 3. Ce que l'assistant peut faire dans nos outils
| Ce qu'il ferait | Réglage | Chez nous |
|---|---|---|
| Lire des données peu sensibles | Autoriser | <agenda, documents publics internes> |
| Lire des données sensibles | Demander | <messagerie, CRM> |
| Écrire, envoyer, modifier | Demander à chaque fois | <envoyer un mail, changer une fiche> |
| Supprimer, payer, tout ce qui ne se défait pas | Bloquer | <supprimer un contact, vider une boîte> |
| Toucher aux dossiers de paie, de personnel, juridiques | Bloquer | <dossiers nommés> |

Un connecteur de plus se demande à <rôle>, qui vérifie trois choses : qui l'héberge, quels droits il réclame, ce qu'il
fait qu'aucune fonction déjà en place ne fait.

## 4. Les contenus venus de l'extérieur
Un document, un mail ou une page web peut cacher des instructions adressées à l'assistant.
- Dès qu'il travaille sur un contenu qu'on n'a pas écrit, il demande avant d'agir.
- S'il propose une action qu'on n'a pas demandée, on refuse et on le signale.
- S'il répond à côté de la question, on relit le contexte avant de continuer.

## 5. L'extension du navigateur
<Autorisée ou non.> Jamais sur : la banque, la paie et les ressources humaines, les consoles d'administration, les
gestionnaires de mots de passe, les portails d'identité. Quand un connecteur existe pour un outil, on le préfère.

## 6. Ce qu'on relit
Celui qui envoie répond de ce qui part. On relit les chiffres, les noms et les citations ; une réponse de l'assistant
n'est pas une source. Aucune décision sur une personne (recrutement, évaluation, sanction) ne se prend sur sa seule
réponse.

## 7. Ce qu'on suit
<Ce que l'entreprise suit, par équipe, et à quoi cela sert. Ce qu'elle a décidé pour les statistiques par personne.>

## 8. En cas de doute ou d'incident
1. On arrête : on ferme la session, on coupe le connecteur.
2. On note : la date, l'outil, ce qui a été collé ou touché.
3. On prévient <rôle> le jour même, même pour un doute. On ne cherche pas de coupable.
```

## Ce qui ne va pas dans la charte

- Le nom d'un plan, un prix, une option de l'éditeur : ces faits vivent dans `assistant-ia.md`, datés.
- Une promesse de gain ou un objectif individuel d'usage.
- Une base légale : elle se décide dans le dossier de conformité, par le rôle compétent.
