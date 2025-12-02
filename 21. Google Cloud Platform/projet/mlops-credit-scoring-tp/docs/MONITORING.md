# Documentation du Monitoring et de l'Observabilité

Ce document décrit la stratégie d'observabilité de la plateforme de Scoring de Crédit. L'objectif est de surveiller la **santé technique** de l'API et la **qualité des prédictions (drift)** en production.

## 1. La Pile de Monitoring (Monitoring Stack)

La plateforme utilise la suite standard de l'écosystème Cloud-Native (CNCF) pour la collecte et la visualisation des métriques.

| Composant | Rôle Principal | Implémentation |
| :--- | :--- | :--- |
| **Prometheus** | **Collecte de Métriques** | Scrappe en continu les métriques exposées par l'API de prédiction (via un client Python/FastAPI) et l'infrastructure K8s. |
| **Grafana** | **Visualisation** | Crée des tableaux de bord (dashboards) dynamiques pour l'analyse en temps réel des métriques collectées par Prometheus. |
| **Evidently AI** | **Détection de Drift** | Génère des rapports sur la dérive des données et du modèle, exécutés périodiquement par Airflow. |
| **Alertmanager** | **Alerting** | Gère le routage et la déduplication des alertes critiques issues de Prometheus et d'Evidently AI. |

## 2. Monitoring Technique (Santé du Service)

Le monitoring technique se concentre sur la performance et la stabilité de l'API de prédiction hébergée sur Kubernetes.

### A. Métriques de Service (Prometheus)

Ces métriques sont exposées par l'API FastAPI et scrappées par Prometheus.

| Métrique | Description | Seuil d'Alerte (Exemple) |
| :--- | :--- | :--- |
| `http_requests_total` | Taux de requêtes totales reçues par l'API. | --- |
| `http_request_duration_seconds_bucket` | **Latence** des requêtes (p95, p99). | p95 > 500 ms pendant 5 minutes. |
| `cpu_usage_percentage` | Utilisation du CPU par les Pods de l'API. | Moyenne > 85% (pour déclencher HPA et alerte). |
| `error_rate_5xx` | Taux d'erreurs du serveur (5xx). | Taux > 1% des requêtes sur 1 minute. |
| `model_version_info` | Version du modèle chargé par le Pod (métrique statique). | Changement de version inattendu. |

### B. Dashboard Grafana : Vue Opérationnelle

Un tableau de bord Grafana est dédié à la vue opérationnelle, permettant de vérifier en un coup d'œil l'état du service.

## 3. Monitoring ML et Métier (Qualité du Modèle)

Le monitoring ML se concentre sur la pertinence des prédictions et la validité des données en entrée.

### A. Métriques Métier (Prometheus/Grafana)

Ces métriques sont calculées à partir des logs de prédiction et permettent d'évaluer l'impact métier en production.

| Métrique | Description | Utilité |
| :--- | :--- | :--- |
| `accepted_credit_count` | Nombre de crédits acceptés (score < $\theta^*$). | Évaluer l'agressivité de la politique de prêt. |
| `rejected_credit_count` | Nombre de crédits refusés (score $\ge \theta^*$). | Indicateur clé de l'activité du modèle. |
| `score_distribution_mean` | Moyenne des scores de risque retournés. | Un changement soudain peut indiquer un problème de modèle ou de données. |

### B. Détection de Dérive (Drift Detection - Evidently AI)

La dérive est le signal le plus critique pour le MLOps. Une dérive importante des données ou de la performance signifie qu'un ré-entraînement est nécessaire.

Le module **Evidently AI** est exécuté selon un DAG Airflow périodique (ex: chaque semaine) pour comparer la *baseline* (données d'entraînement) avec les *current* (données de production de la dernière semaine).

#### Types de Dérive Détectés

1. **Data Drift** :
    * **Concept :** Changement de la distribution des features en entrée (ex: le revenu moyen des demandeurs a augmenté subitement).
    * **Outil :** Evidently AI (rapport `Data_Drift_Report.html`).
2. **Prediction Drift** :
    * **Concept :** Changement de la distribution des scores de risque produits par le modèle.
    * **Outil :** Evidently AI (rapport `Prediction_Drift_Report.html`).
3. **Model Performance Degradation** :
    * **Concept :** Le modèle produit plus de $\text{FN}$ et $\text{FP}$ que prévu, entraînant une hausse du **Coût Métier** réel. (Nécessite le label réel, souvent disponible avec un délai).

### C. Workflow d'Alerte de Drift

En cas de dérive significative (plus de 30% des colonnes sont en drift, selon le test de Kolmogorov-Smirnov) :

1. **Evidently AI** génère un rapport JSON.
2. Une tâche **Airflow** détecte ce signal et envoie une alerte.
3. L'alerte est envoyée à **Alertmanager** qui notifie l'équipe MLOps, signalant la nécessité de déclencher un ré-entraînement.

## 4. Stratégie d'Alerte (Alertmanager)

Alertmanager consolide les alertes de Prometheus (problèmes techniques) et les signaux de drift (problèmes ML) pour notifier les équipes concernées.

| Catégorie | Sévérité | Condition de Déclenchement | Action (Destination) |
| :--- | :--- | :--- | :--- |
| **Urgent (P0)** | `Critical` | Taux d'erreur API > 5%, ou Latence p99 > 1s. | PagerDuty / Canal Slack #OPS-CRITICAL |
| **ML-Dégénération** | `Warning` | Dérive de données détectée sur > 30% des features importantes. | Canal Slack #MLOps-Alerts |
| **Ressource** | `Warning` | Utilisation CPU > 85% pendant 10 minutes (si HPA est désactivé ou inefficace). | Canal Slack #OPS-ALERTS |
| **Métrique Métier** | `Info` | Taux de refus > 20% (changement de comportement). | Email/Rapport Hebdomadaire |
