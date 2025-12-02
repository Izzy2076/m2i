# Exercice 5

## Partie 1

- En utilisant votre machine Windows, lancez le service Docker, s’il n’est pas lancé.

- Créer une image Docker sur votre machine du jeu 2048 : oats87/2048

- Vérifier que l’image est bien présente sur votre machine.

- Lancer ce jeu sur un port disponible au travers d’un conteneur que vous allez appeler «jeu-votre-nom ».

- Vérifier que le conteneur est bien lancé avec la commande adaptée.

- Créer un second conteneur qui va lancer le même jeu mais avec un nom différent «jeu2-votre-nom ».

- Les 2 jeux sont fonctionnels en même temps sur votre machine, effectuez la commande pour vérifier la présence des conteneurs.

- Ouvrez les 2 jeux sur votre navigateur.

- Stopper les 2 conteneurs et assurez-vous que ces 2 conteneurs sont arrêtés.

- Relancez le conteneur «jeu2-votre-nom » et aller vérifier dans votre navigateur s’il fonctionne bien. Effectuez la commande pour voir s’il a bien été relancé. Puis stopper le.

- Supprimez l’image du jeu 2048 et les conteneurs associés.

- Vérifiez que les suppressions ont bien été faite.

```bash
docker run -d -p 8080:80 --name jeuChristophe oats87/2048
docker run -d -p 8081:80 --name jeuChristophe2 oats87/2048
docker ps
docker stop jeuChristophe
docker stop jeuChristophe2
docker rm jeuChristophe
docker rm jeuChristophe2
```

## Partie 2

- Répétez 3 fois la même opération que pour le début de la partie 2, il faudra juste appelez vos conteneurs :

- « nginx-web3 ».

- « nginx-web4 ».

- « nginx-web5 ».

- Il faudra faire en sorte que les pages html présente dans les fichiers ci-dessous s’affiche dans chacun des navigateurs en lien avec vos conteneurs :

- html5up-editorial-m2i.zip pour nginx-web3

- html5up-massively.zip pour nginx-web4

- html5up-paradigm-shift.zip pour nginx-web5

- Stopper, ensuite, ces différents conteneurs.

```bash
docker run -d -p 5000:80 --name nginx-web3 nginx
docker cp .\html5up-editorial-m2i.zip nginx-web3:/tmp
docker exec -it nginx-web3 bash
# Dans le conteneur :
cd /tmp
apt upgrade & apt update -y
apt install unzip
unzip /tmp/html5up-editorial-m2i.zip -d ./
mv html5up-editorial/* /usr/share/nginx/html
exit
```

## mêmes étapes pour le 2 & 3