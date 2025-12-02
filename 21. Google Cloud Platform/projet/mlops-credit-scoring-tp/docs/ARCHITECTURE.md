# Architecture MLOps pour le Scoring de Crédit

Ce document décrit l'architecture complète de la plateforme MLOps, illustrant les composants, leurs rôles, et le flux de données et de contrôle tout au long du cycle de vie du Machine Learning (ML).

## 1. Description Détaillée des Composants

La plateforme est construite sur une architecture microservices et organisée en trois plans logiques pour garantir la ségrégation des responsabilités et la scalabilité.

---

### A. Plan de Données et de Modélisation (Data & ML Layer)

Ce plan est le cœur de la connaissance et de l'intelligence métier.

| Composant | Technologie(s) | Rôle Industriel Clé |
| :--- | :--- | :--- |
| **Data Source** | Fichiers CSV (Kaggle) | Les 8 sources de données brutes ($\sim 2.5$ GB) servant de point de départ à l'ETL. |
| **Feature Store** | **Pandas, Parquet, Cloud Storage** | Module central de *Feature Engineering*. **Stockage optimisé** (Parquet) et **versionné** des 100+ features agrégées. |
| **Data Quality Check** | **Great Expectations / Pydantic** | Assure la validation du **schéma** et des **contraintes métier** (non-nullité, plages de valeurs) sur les jeux de données critiques. |
| **MLflow Tracking Server** | **MLflow, PostgreSQL** | **Traçabilité complète** : enregistrement des paramètres, métriques (AUC-ROC, Coût Métier) et des artefacts de chaque *run* d'entraînement. |
| **MLflow Model Registry** | **MLflow** | **Catalogue central** des modèles. Gère le cycle de vie du modèle : Versioning et **promotion des statuts** (Staging $\rightarrow$ Production). |
| **Model Development** | **LightGBM, Optuna, SHAP** | Code Python pour l'entraînement, l'optimisation des hyperparamètres, et l'**interprétabilité locale et globale** du modèle final. |

---

### B. Plan de Serving et d'Infrastructure (Serving Layer)

Ce plan assure la livraison du modèle en tant que service à haute performance et disponibilité.

| Composant | Technologie(s) | Rôle Industriel Clé |
| :--- | :--- | :--- |
| **Kubernetes (K8s)** | **GKE / Minikube** | Plateforme d'orchestration pour l'hébergement de tous les conteneurs. Garantit la **Haute Disponibilité** et la gestion des ressources. |
| **API de Prédiction** | **FastAPI, Uvicorn** | L'interface REST pour le **scoring en temps réel** ($\text{Latence } < 200 \text{ms}$). Charge dynamiquement le modèle **Production** depuis MLflow. |
| **Helm** | **Helm Charts** | **Packaging standardisé** de tous les manifestes K8s (Deployments, Services, ConfigMaps, etc.) pour un déploiement reproductible. |
| **Horizontal Pod Autoscaler (HPA)** | **K8s** | Assure la **Scalabilité Horizontale** de l'API en ajustant le nombre de réplicas (Pods) en fonction de la charge CPU/mémoire (ex: cible CPU 70%). |
| **Ingress** | **K8s** | **Routeur de trafic externe** unique. Expose les services (API, MLflow UI, Grafana) via une seule adresse IP publique. |

---

### C. Plan de Contrôle et d'Observabilité (Control Layer)

Ce plan gère l'automatisation des opérations et la surveillance de la santé et de la performance du système.

| Composant | Technologie(s) | Rôle Industriel Clé |
| :--- | :--- | :--- |
| **CI/CD Pipeline** | **GitHub Actions** | **Automatisation complète** du cycle Build, Test, Push Image, Déploiement multi-environnement (**GitOps**). |
| **Workflow Orchestration** | **Apache Airflow** | **Planification périodique** et gestion des dépendances du **pipeline ML End-to-End** (Ingestion $\rightarrow$ Feature Store $\rightarrow$ Train $\rightarrow$ Promote). |
| **Monitoring Metrics** | **Prometheus, Grafana** | **Collecte** des métriques techniques et métier (latence, taux d'erreur, taux d'acceptation crédit). **Visualisation** et création de dashboards en temps réel. |
| **Drift Detection** | **Evidently AI** | Exécuté par Airflow pour comparer les distributions de **données** et la **performance du modèle** en production par rapport à la baseline. |
| **Alerting** | **Alertmanager** | Envoie des notifications ciblées (Email/Slack) lorsque les métriques atteignent des seuils critiques (API down, Latence élevée, Drift détecté). |
| **Artifact Registry** | **Docker Registry / GCR** | Stockage sécurisé des images Docker versionnées, utilisées par K8s pour le déploiement. |

---

## 2. Flux de Données et de Contrôle

L'architecture est régie par deux flux principaux pour garantir que le modèle est toujours à jour et que le service est stable.

### A. Flux d'Entraînement (Piloté par Airflow)

> 1. **Orchestration** : **Airflow** déclenche le DAG selon le *schedule* (mensuel) ou un événement (drift de données).
> 2. **Préparation** : Les tâches **ETL** s'exécutent (conteneurs Docker), valident les données avec **Great Expectations**, créent les features et stockent le résultat dans le **Feature Store** (Parquet).
> 3. **Entraînement & Tracking** : Le script d'entraînement s'exécute, utilisant **Optuna** pour l'optimisation. Les résultats (modèle, seuil optimal, Coût Métier) sont loggés dans **MLflow Tracking**.
> 4. **Promotion** : Le meilleur modèle passe en statut **"Staging"** dans le **Model Registry**. Après validation, il est promu à **"Production"**.
> 5. **Mise à Jour** : La promotion peut déclencher une étape de **CD** (via GitHub Actions ou K8s Rolling Update) pour recharger le modèle en production sans interruption de service.

### B. Flux de Scoring (Temps Réel)

> 1. **Requête** : L'utilisateur envoie une requête de scoring à l'adresse de l'**Ingress K8s**.
> 2. **Scalabilité** : L'**HPA** assure que l'API est capable de gérer la charge en ajustant le nombre de **FastAPI Pods**.
> 3. **Prédiction** : L'API charge le modèle **"Production"** actif depuis **MLflow Registry**, effectue le scoring, et répond avec la décision (Accepté/Refusé).
> 4. **Observabilité** : La latence et l'utilisation de la ressource sont exposées à **Prometheus** pour le monitoring en temps réel via **Grafana**
>