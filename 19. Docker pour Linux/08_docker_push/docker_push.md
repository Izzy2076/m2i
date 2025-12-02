1. Connexion à docker hub :

```bash
docker login
```

2. construire l'image

```bash
docker build -t nomutilisateur/my-app:1.0 .
```

3. pousser l'image sur docker hub

```bash
docker push nomutilisateur/my-app:1.0
```