# README.md : Plateforme MLOps pour Scoring de Crédit

## 1. Description du Projet : Scoring de Crédit Industrialisé

Ce projet est un Travail Pratique (TP) fil rouge visant à construire une plateforme **MLOps industrielle et complète** pour le déploiement et la gestion d'un système de **scoring de crédit**.

L'entreprise **"Prêt à dépenser"** cible des clients avec un historique de crédit limité. L'enjeu est de fournir une infrastructure **scalable, automatisée et traçable** pour minimiser les risques (faux négatifs) tout en maximisant les opportunités (vrais positifs), en utilisant un modèle optimisé selon un **coût métier** spécifique.

Le projet met un accent fort sur le **Data Engineering (60%)** et l'automatisation de l'infrastructure via **Kubernetes** et **Airflow**.

### Objectifs Clés

* **Pipeline ETL** : Ingestion, agrégation (100+ features), validation, et stockage optimisé (Parquet) des 2.5 GB de données multi-sources.
* **Modélisation** : Entraînement de LightGBM/XGBoost, optimisation du seuil de décision basée sur la fonction de coût $C = 10 \times \text{FN} + 1 \times \text{FP}$.
* **Industrialisation** : Containerisation (Docker), Orchestration (Docker Compose), Déploiement Cloud-Native (Kubernetes/Helm, HPA).
* **Automatisation** : CI/CD complète (GitHub Actions) et orchestration de workflow (Airflow).
* **Observabilité** : Monitoring technique (Prometheus/Grafana) et détection de dérive (Evidently AI).

-----

## 2. Architecture Overview

La plateforme est construite autour du principe du **pipeline end-to-end** et repose sur un ensemble d'outils Open Source orchestrés par Kubernetes.

| Composant | Rôle | Technologie(s) |
| :--- | :--- | :--- |
| **Data Layer** | Ingestion, transformation, stockage des features. | Pandas, Parquet, Great Expectations |
| **ML Tracking** | Versioning des modèles, tracking des expériences. | MLflow (Tracking Server & Registry) |
| **API/Serving** | Point d'accès pour les prédictions en temps réel. | FastAPI, Uvicorn, Pydantic |
| **Orchestration** | Gestion et planification du pipeline ML périodique. | Apache Airflow |
| **DevOps/Infra** | Build, test, déploiement continu, scalabilité. | Docker, Kubernetes, Helm, GitHub Actions |
| **Monitoring** | Surveillance de la santé de l'API et de la performance du modèle (drift). | Prometheus, Grafana, Evidently AI |

Le flux de travail principal est géré par Airflow pour le ré-entraînement périodique, et par Kubernetes pour le serving en temps réel et la scalabilité.

-----

## 3. Instructions d'Installation et Prérequis

Pour déployer la plateforme localement ou sur un cluster Cloud (GKE, par exemple), les outils suivants sont requis.

### Prérequis Logiciels

1. **Git** : Système de contrôle de version.
2. **Python 3.9+** : Environnement d'exécution principal.
3. **Docker** : Pour la containerisation.
4. **Docker Compose** : Pour l'orchestration locale des services de base (MLflow, PostgreSQL).
5. **Kubernetes CLI (`kubectl`)** : Pour interagir avec le cluster.
6. **Minikube / Kind** : (Optionnel) Pour un cluster K8s local.
7. **Helm 3+** : Pour le packaging et le déploiement sur Kubernetes.

### Étapes de Configuration

#### A. Clonage du Répertoire

```bash
git clone https://github.com/votre_repo/mlops-credit-scoring-tp.git
cd mlops-credit-scoring-tp
```

#### B. Préparation des Données

1. Téléchargez les 8 fichiers CSV du jeu de données "Home Credit Default Risk" (Kaggle).
2. Placez tous les fichiers dans le répertoire dédié :

    ```bash
    mkdir -p infra/data/raw
    # Copiez vos 8 fichiers CSV ici
    ```

#### C. Configuration de l'Environnement Python

```bash
# Créez un environnement virtuel (recommandé)
python3 -m venv venv
source venv/bin/activate
# Installez les dépendances
pip install -r requirements.txt
# Installez les hooks de qualité (Partie 6)
pip install pre-commit
pre-commit install
```

-----

## 4. Guide de Démarrage Rapide

Ce guide permet de lancer la pile complète des services nécessaires (Postgres, MLflow) et de démarrer l'API pour un test rapide.

### Étape 1 : Démarrage des Services de Base (Local)

Utilisez Docker Compose pour lancer la base de données (PostgreSQL) et le serveur de tracking MLflow.

```bash
# 1. Build des images (API et MLflow)
docker-compose build

# 2. Lancement des services (Postgres, MLflow)
docker-compose up -d postgres mlflow-server
```

### Étape 2 : Exécution du Pipeline ETL et Entraînement

Exécutez le script d'entraînement pour générer les features, entraîner le modèle, l'évaluer, et l'enregistrer dans le MLflow Registry.

```bash
# 1. Exécution du pipeline Data + Feature Engineering (Partie 1)
python src/data/ingestion.py
python src/features/engineering.py

# 2. Entraînement et Enregistrement du Modèle (Partie 2)
# Cela trackera l'expérimentation et enregistrera le meilleur modèle
python src/model/train.py

# Vérifiez le résultat sur l'interface MLflow : http://localhost:5000
```

### Étape 3 : Démarrage de l'API de Prédiction (Local)

Une fois le modèle enregistré dans MLflow Registry, démarrez l'API pour le serving local.

```bash
# Lancer l'API FastAPI avec Uvicorn
uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

Vous pouvez maintenant tester l'endpoint `/health` : `curl http://localhost:8000/health`

### Étape 4 : Déploiement sur Kubernetes (Production)

Pour le déploiement complet sur un cluster K8s (Minikube/GKE), utilisez le Helm Chart :

```bash
# 1. Créer le namespace (si non existant)
kubectl create namespace mlops-credit-scoring

# 2. Déploiement initial en staging/dev
helm install credit-scoring infra/helm/credit-scoring-chart -f infra/helm/credit-scoring-chart/values-dev.yaml -n mlops-credit-scoring
```

> 💡 **Note Importante :** La pipeline CI/CD via GitHub Actions gère l'étape de déploiement réelle et automatisée (GitOps).
