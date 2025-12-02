1. Création du network & volume 

```bash
docker network create my-net 
docker volume create mysql-data   
```

2. lancement du container mysql

```bash
docker run -d \
--name myMysql \
--network my-net \
-e MYSQL_ROOT_PASSWORD=root \
-e MYSQL_DATABASE=testdb \
-v mysql-data:/var/lib/mysql \
mysql:8
```

3. lancement du script python

```bash
docker run -d --network my-net python-app
```