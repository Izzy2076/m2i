La commande `docker cp` est utilisée pour copier des fichiers/dossiers entre un conteneur et la machine local

1. Copier de la machine local vers un conteneur :

```bash
docker cp [chemin_fichier_local] [nom_conteneur]:[chemin_dans_le_conteneur]
docker cp c:/user/test.csv mynginx:/tmp/
```

2. Inverse

```bash
docker cp [nom_conteneur]:[chemin_dans_le_conteneur] [chemin_fichier_local] 
docker cp mynginx:/tmp/ c:/user/test.csv 
```