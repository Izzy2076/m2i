# Documentation de l'API de Prédiction

Cette documentation décrit l'API REST de Scoring de Crédit en temps réel, implémentée avec **FastAPI**. Elle est conçue pour être performante (faible latence) et hautement disponible, s'exécutant sur un cluster **Kubernetes** avec auto-scaling.

## 1\. Vue d'Ensemble du Service

| Caractéristique | Valeur | Remarques |
| :--- | :--- | :--- |
| **Framework** | **FastAPI** | Utilisation d'Uvicorn pour le serving asynchrone. |
| **Endpoint de Base** | Dépendant de l'Ingress K8s (ex: `/api/v1`) | |
| **Latence Cible** | **p95 \< 200 ms** | Mesuré en production via Prometheus. |
| **Modèle Chargé** | Le modèle tagué **"Production"** du MLflow Registry. | |
| **Documentation Auto** | Swagger UI (`/docs`) et Redoc (`/redoc`) | Accessible une fois le service déployé. |

## 2\. Endpoints de l'API

L'API expose deux endpoints principaux pour le monitoring et la prédiction.

### 2.1 Endpoint de Santé (Health Check)

Utilisé par Kubernetes (Liveness et Readiness probes) et les outils de monitoring pour vérifier l'état du service.

| Attribut | Détail |
| :--- | :--- |
| **Méthode** | `GET` |
| **Chemin** | `/health` |
| **Description** | Vérifie si l'API est démarrée et si le modèle **"Production"** est correctement chargé depuis MLflow. |
| **Réponse 200** | `{"status": "ok", "model_version": "v1.2.5"}` (Statut et version du modèle chargé) |
| **Réponse 503** | `{"status": "error", "message": "Model not loaded"}` |

### 2.2 Endpoint de Prédiction

Utilisé par les applications clientes pour obtenir un score de risque et une décision.

| Attribut | Détail |
| :--- | :--- |
| **Méthode** | `POST` |
| **Chemin** | `/predict` |
| **Description** | Calcule le score de risque (probabilité de défaut) et retourne la décision binaire (Accepté/Refusé) ainsi que la justification SHAP. |

-----

## 3\. Schémas de Données (Pydantic)

Les schémas sont définis dans `src/api/schemas.py` pour garantir la validation stricte des données d'entrée et de sortie.

### A. Schéma d'Entrée (`CreditApplicationInput`)

Le corps de la requête JSON doit contenir les features clés du client. Seules les données non-agrégées sont requises à l'entrée, car l'API effectue une partie du *Feature Engineering* simple en interne.

| Champ | Type | Description |
| :--- | :--- | :--- |
| `SK_ID_CURR` | `int` | Identifiant unique de l'application (clé de jointure interne). |
| `AMT_INCOME_TOTAL` | `float` | Revenu total du demandeur. |
| `AMT_CREDIT` | `float` | Montant du crédit demandé. |
| `DAYS_BIRTH` | `int` | Âge du client en jours (négatif). |
| `NAME_CONTRACT_TYPE` | `str` | Type de prêt (Cash / Revolving). |
| `FLAG_OWN_CAR` | `str` | Indicateur de possession d'une voiture (Y/N). |
| $\dots$ | $\dots$ | *[Les 30-40 features les plus critiques et faciles à collecter]* |

> **Validation :** Si le schéma d'entrée n'est pas respecté (champ manquant, type incorrect), l'API retourne une erreur **422 Unprocessable Entity**.

### B. Schéma de Sortie (`PredictionOutput`)

| Champ | Type | Description |
| :--- | :--- | :--- |
| `SK_ID_CURR` | `int` | Identifiant du client soumis. |
| `risk_score` | `float` | **Probabilité de défaut** prédite par le modèle (entre 0 et 1). |
| `decision` | `str` | **Décision finale** basée sur le seuil optimal $\theta^*$ (ex: "ACCEPTED" ou "REJECTED"). |
| `decision_threshold` | `float` | Le seuil $\theta^*$ utilisé pour la décision (Ex: 0.125). |
| `justification` | `list[dict]` | **Explication SHAP locale** : les 3 principales features ayant influencé la décision. |

**Exemple de Corps de Réponse (200 OK) :**

```json
{
  "SK_ID_CURR": 123456,
  "risk_score": 0.087,
  "decision": "ACCEPTED",
  "decision_threshold": 0.125,
  "justification": [
    {
      "feature": "AMT_CREDIT_RATE",
      "impact": "POSITIVE",
      "value": 0.55
    },
    {
      "feature": "DAYS_EMPLOYED",
      "impact": "NEGATIVE",
      "value": -1200
    },
    {
      "feature": "EXT_SOURCE_3",
      "impact": "POSITIVE",
      "value": 0.75
    }
  ]
}
```

## 4\. Performance et Monitoring

L'API est instrumentée pour exposer les métriques de performance à **Prometheus** (via `src/api/prometheus_metrics.py`).

| Objectif de Performance | Détail |
| :--- | :--- |
| **Latence p95** | Inférieure à 200 ms. Les requêtes qui dépassent ce seuil déclenchent un *Warning* dans Grafana. |
| **Taux d'Erreur** | Maintenu sous **1%** (erreurs 5xx). |
| **Scalabilité** | L'**HPA** est configuré pour maintenir l'utilisation du CPU des Pods à **70%**. |

L'endpoint `/metrics` (non listé pour le public) est utilisé par l'outil de scraping Prometheus pour collecter ces données de latence et de charge.
