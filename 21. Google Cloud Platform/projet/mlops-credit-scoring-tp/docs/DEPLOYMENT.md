# Guide de Déploiement : Plateforme MLOps

Ce document fournit les instructions détaillées pour déployer les différents composants de la plateforme de Scoring de Crédit : les services de base (MLflow, PostgreSQL) en local, et l'API de prédiction en environnement de production (Kubernetes) via Helm.

## 1\. Déploiement Local avec Docker Compose (Environnement de Développement)

L'utilisation de `docker-compose` est idéale pour démarrer l'environnement de développement et de testing, y compris le serveur de tracking MLflow et sa base de données PostgreSQL.

### 1.1 Prérequis

Assurez-vous que **Docker** et **Docker Compose** sont installés et en cours d'exécution.

### 1.2 Construction des Images

Avant de lancer les services, les images Docker pour l'API et pour MLflow doivent être construites.

```bash
# Se placer à la racine du projet
cd mlops-credit-scoring-tp

# Construire les images définies dans docker-compose.yml
# L'image 'api' est pour l'application FastAPI.
# L'image 'mlflow-server' est pour le tracking.
docker-compose build
```

### 1.3 Démarrage des Services de Base

Le fichier `docker-compose.yml` est configuré pour lancer :

* `postgres`: La base de données pour le backend MLflow.
* `mlflow-server`: Le serveur de tracking.

<!-- end list -->

```bash
# Lancer les services en mode détaché
docker-compose up -d postgres mlflow-server
```

### 1.4 Démarrage de l'API de Scoring (Local)

Pour tester l'API localement après l'entraînement et l'enregistrement d'un modèle dans MLflow Registry :

```bash
# Lancer uniquement le service API de scoring
docker-compose up -d api
```

| Service | Endpoint | Port |
| :--- | :--- | :--- |
| **MLflow UI** | `http://localhost:5000` | `5000` |
| **API Scoring** | `http://localhost:8000` | `8000` |

-----

## 2\. Déploiement en Production avec Kubernetes (K8s)

Le déploiement en production utilise un **Helm Chart** pour gérer l'ensemble des manifestes Kubernetes.

### 2.1 Prérequis K8s

* Un cluster Kubernetes opérationnel (GKE, AKS, EKS ou Minikube pour le test).
* `kubectl` configuré et connecté au cluster.
* **Helm 3+** installé.
* Les images Docker de l'API et de MLflow doivent être poussées vers un **Registry public ou privé** (GCR, Docker Hub).

> **Note sur le Container Registry** : La pipeline CI/CD (GitHub Actions) est responsable de la construction des images et de leur publication sur le Registry après chaque *merge* sur `main`.

### 2.2 Structure du Helm Chart

Le chart se trouve dans `infra/helm/credit-scoring-chart/` et permet de configurer le déploiement de :

* `Deployment` (API, MLflow)
* `Service` (LoadBalancer ou ClusterIP)
* `Ingress`
* `HPA` (Horizontal Pod Autoscaler)

### 2.3 Déploiement par Environnement

Le déploiement utilise des fichiers de valeurs (values files) spécifiques pour cibler différents environnements (Dev, Staging, Production).

#### A. Déploiement Dev / Staging

Utilisé pour les tests d'intégration et le QA. Les ressources K8s sont souvent limitées.

```bash
# 1. Créer le namespace (si ce n'est pas déjà fait)
kubectl create namespace staging-mlops

# 2. Déployer l'application en utilisant le fichier de valeurs "staging"
# Cela utilisera les images tagguées 'staging' ou 'latest'
helm install credit-scoring-staging \
    infra/helm/credit-scoring-chart \
    --namespace staging-mlops \
    -f infra/helm/credit-scoring-chart/values-staging.yaml
```

#### B. Déploiement Production

Utilisé pour l'environnement final, avec les configurations de scalabilité (HPA) et de performance maximales.

```bash
# 1. Créer le namespace (si ce n'est pas déjà fait)
kubectl create namespace prod-mlops

# 2. Déployer l'application en utilisant le fichier de valeurs "prod"
# Cela utilisera l'image stable, tagguée 'prod-vX.Y.Z'
helm install credit-scoring-prod \
    infra/helm/credit-scoring-chart \
    --namespace prod-mlops \
    -f infra/helm/credit-scoring-chart/values-prod.yaml
```

### 2.4 Vérification du Déploiement

Après le déploiement, vérifiez l'état des Pods et des services.

```bash
# Vérifier l'état des Pods dans le namespace de production
kubectl get pods --namespace prod-mlops

# Vérifier l'état des Services (pour trouver l'IP de l'Ingress/LoadBalancer)
kubectl get svc --namespace prod-mlops

# Vérifier l'état de l'Horizontal Pod Autoscaler
kubectl get hpa --namespace prod-mlops
```

## 3\. Déploiement et Promotion des Modèles

Le déploiement de l'infrastructure est séparé de la promotion du modèle ML.

### Flux de Promotion de Modèle

1. **Entraînement :** Le pipeline Airflow entraîne un nouveau modèle et le log dans MLflow (statut **"None"**).
2. **Validation :** Après évaluation et tests (via Airflow), l'artefact est promu à **"Staging"** dans le **MLflow Model Registry**.
3. **Mise en Production (Promote) :** Lorsqu'il est prêt, le statut du modèle est mis à jour à **"Production"** dans MLflow.
4. **Rechargement de l'API :** L'API de scoring est configurée pour lire le dernier modèle avec le tag **"Production"** du Registry. Le Pod K8s peut être redémarré (Rolling Update) ou le modèle peut être rechargé dynamiquement.

**Méthode Recommandée (Kubernetes Rolling Update) :**

Pour forcer l'API à recharger le modèle le plus récent sans attendre un redémarrage planifié, vous pouvez effectuer un *Rolling Restart* du déploiement :

```bash
# Forcer le redémarrage des Pods de l'API pour charger le nouveau modèle "Production"
kubectl rollout restart deployment/api-deployment --namespace prod-mlops
```
