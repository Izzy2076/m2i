## Exercice dockerfile

- Vous allez dans ce TP, essayez de créer une image Docker d’un projet Angular.
- Vous allez utiliser pour cela un Dockerfile.
- Vous allez télécharger ce projet en local sur votre machine.
- Le projet en question. :
  - https://gitlab.com/mohamed_formation_test/aston-villa-angular-dist.git
  - N’hésitez pas pour cela à vous documenter sur un exemple de Dockerfile pour un projet Angular.
- Pour vous assurer que votre image est bien fonctionnelle, il faudra créer un container à partir de votre image.

- Important : il faudra ajouter la variable d'environnement : ENV NODE_OPTIONS=--openssl-legacy-provider pour corriger les soucis de compatibilité.

commande pour installer Angular : npm install -g @angular/cli
commande pour installer les dépendances : npm install
commande pour lancer l'application sur le serveur nginx : CMD ["ng", "serve", "--host", "0.0.0.0"]
