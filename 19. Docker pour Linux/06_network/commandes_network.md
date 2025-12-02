### 1. **Créer un Réseau**

```bash
docker network create [OPTIONS] NETWORK_NAME
```

- **Exemple** : Créer un réseau bridge personnalisé nommé `my_bridge_network`
  ```bash
  docker network create my_bridge_network
  ```

### 2. **Lister les Réseaux**

```bash
docker network ls
```

- **Exemple** : Afficher tous les réseaux Docker disponibles
  ```bash
  docker network ls
  ```

### 3. **Inspecter un Réseau**

```bash
docker network inspect NETWORK_NAME
```

- **Exemple** : Inspecter les détails du réseau `my_bridge_network`
  ```bash
  docker network inspect my_bridge_network
  ```

### 4. **Supprimer un Réseau**

```bash
docker network rm NETWORK_NAME
```

- **Exemple** : Supprimer le réseau `my_bridge_network`
  ```bash
  docker network rm my_bridge_network
  ```

### 5. **Connecter un Conteneur à un Réseau**

```bash
docker network connect NETWORK_NAME CONTAINER_NAME
```

- **Exemple** : Connecter le conteneur `my_container` au réseau `my_bridge_network`
  ```bash
  docker network connect my_bridge_network my_container
  ```

### 6. **Déconnecter un Conteneur d’un Réseau**

```bash
docker network disconnect NETWORK_NAME CONTAINER_NAME
```

- **Exemple** : Déconnecter le conteneur `my_container` du réseau `my_bridge_network`
  ```bash
  docker network disconnect my_bridge_network my_container
  ```

### 7. **Voir les Réseaux d’un Conteneur**

```bash
docker inspect --format '{{json .NetworkSettings.Networks}}' CONTAINER_NAME
```

- **Exemple** : Afficher les réseaux auxquels le conteneur `my_container` est connecté
  ```bash
  docker inspect --format '{{json .NetworkSettings.Networks}}' my_container
  ```
