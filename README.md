# Site_e_commerce_flask

## Contexte
Ce projet fait partie des différents projets de **SAE (Situation d'Apprentissage en Entreprise)** lors de mon cursus. Durant mon semestre 2, nous avions dû réaliser, dans un groupe de 4 étudiant, un site web de e-commerce sous **Flask**, un framework HTML + Python pour faire des pages web HTML sous **un serveur**, contenant une base de donnée **SQ**L. Les pages HTML et du codes python étaient déjà créées par le professeur, nous avons donc dû réaliser la base de données puis dans le python, réaliser du code pour pouvoir insérer les bases de données et réaliser différentes actions (Ajouter un article, supprimer un article, etc) côté client et admin.

## Objectifs du projet
Pour ce projet, il y avait **plusieurs objectifs** à réaliser mais je vais expliquer dans les grandes lignes les objectifs.

Tout d'abord, comme nombreux sites de e-commerce, il y a une partie **authentification** pour pouvoir se connecter et réaliser des achats -> **Côté client**. La **partie client** donc, l'objectif était de pouvoir ajouter, supprimer un article du panier, ajouter dans une liste d'envie, valider sa commande en y mettant son adresse de livraison, pouvoir regarder un article et y mettre une note, un commentaire, etc.

**Remarque** : *Chaque étudiants devait réaliser une tâche importante comme par exemple, la gestion du panier.*

Comme autre objectif, il y avait également la **partie administrateur** pour pouvoir gérer les commandes qui ont été passées (les valider ou les refuser), gérer les articles (ajouter un stocks, modifier un prix, ajouter un article, etc), regarder les avis laissés par les utilisateurs, etc -> **Côté admin**

**Remarque** : *Même chose ici, chaque étudiant avait une tâche à faire*

Tout ceci était donc gérer grâce à **une base de données** ainsi qu'avec **du code python**.

## Mon objectif
Mon objectif lors de ce projet était la **gestion du stock des articles ainsi que la gestion de leur déclinaison (variance de l'article) selon le stock**. En effet, cette réalisation a été longue et assez complexe mais j'ai pu m'en sortir.
### Côté client
Du côté client, je devais faire en sorte que l'utilisateur puisse **sélectionner le stock voulu** lors de son achat ainsi que de pouvoir choisir dans **quelle déclinaison** il désire acheter l'article puis, lors de l'affichage de la commande, il fallait faire en sorte que la **déclinaison soit affiché avec le stock choisi**, de plus, lorsque l'article était en rupture de stock, l'**afficher dans la boutique au niveau du stock**.

### Côté administrateur
Dans cette partie, je devais également gérer la même chose, le **stock et la déclinaison**. Il fallait que l'administrateur puisse **ajouter du stock, ajouter une déclinaison, supprimer une déclinaison, la modifier, etc** puis ces différentes déclinaison, les **afficher dans une liste déroulante** lorsqu'il **ajoute ou modifie** un article et dans la partie des articles pouvoir **rajouter du stock** si une déclinaison était **en rupture**. Dans la gestion des commandes, il fallait qu'il puisse **voir la déclinaison et le stock que l'utilisateur a commandé**.

**Note** : *J'ai expliqué l'objectif qui m'a le plus marqué. En effet, avant de pouvoir réaliser cette objectif, nous devions d'abord coder la gestion du panier, afficher la boutique côté client, etc.*

## Accès au site
Voici l'accès au site : [Site de vente](https://lfulcran2.pythonanywhere.com/)

Côté client -> Lorsque vous arrivez sur la page de connexion, créez un nouvelle utilisateur **Inscription** pour pouvoir acheter vos articles. 
<br>
Côté admin -> Ici, au lieu de créer un utilisateur, connectez vous en temps qu'admin avec *admin* pour le pseudo et *admin* pour le password. Vous pourrez ainsi être du côté administrateur et gérer les articles.
