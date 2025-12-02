#!/bin/bash

# Nom du répertoire racine
PROJECT_NAME="mlops-credit-scoring-tp"

echo "Création de la structure de répertoires pour $PROJECT_NAME..."

# Créer le répertoire principal et se déplacer à l'intérieur
mkdir -p "$PROJECT_NAME"
cd "$PROJECT_NAME"

# Création des répertoires de Configuration et CI/CD
echo "-> Création des dossiers de configuration (.github, infra)"
mkdir -p .github/workflows
touch .github/workflows/ci.yml
touch .github/workflows/cd.yml
touch .pre-commit-config.yaml
touch .gitignore
touch .gitattributes

# Création du répertoire Source (src/)
echo "-> Création du dossier source (src)"
mkdir -p src/{api,data,features,model,monitoring}

# Fichiers API
touch src/api/__init__.py
touch src/api/main.py
touch src/api/schemas.py
touch src/api/prometheus_metrics.py

# Fichiers Data
touch src/data/ingestion.py
touch src/data/preprocessing.py
touch src/data/validation.py

# Fichiers Features
touch src/features/engineering.py

# Fichiers Modèle
touch src/model/train.py
touch src/model/evaluation.py

# Fichiers Monitoring
touch src/monitoring/drift_detector.py

# Fichiers Utilitaires
touch src/utils.py

# Création du répertoire Tests (tests/)
echo "-> Création du dossier tests (tests)"
mkdir -p tests/{unit,integration,e2e}
touch tests/__init__.py
touch tests/unit/test_data_quality.py
touch tests/unit/test_features.py
touch tests/integration/test_pipeline.py
touch tests/e2e/test_api_e2e.py

# Création du répertoire Infrastructure (infra/)
echo "-> Création du dossier infra (infra)"
mkdir -p infra/data/{raw,processed}
mkdir -p infra/mlflow
mkdir -p infra/dags
mkdir -p infra/helm/credit-scoring-chart/templates
mkdir -p infra/monitoring/grafana/dashboards

# Fichiers Infrastructure spécifiques
touch infra/mlflow/Dockerfile.mlflow
touch infra/mlflow/entrypoint.sh
touch infra/dags/ml_pipeline_dag.py
touch infra/dags/drift_monitoring_dag.py
touch infra/helm/credit-scoring-chart/Chart.yaml
touch infra/helm/credit-scoring-chart/values.yaml
touch infra/helm/credit-scoring-chart/values-staging.yaml
touch infra/helm/credit-scoring-chart/values-prod.yaml
touch infra/monitoring/prometheus.yml
touch infra/monitoring/alertmanager.yml

# Création du répertoire Documentation (docs/)
echo "-> Création du dossier docs (docs)"
mkdir -p docs
touch docs/ARCHITECTURE.md
touch docs/DEPLOYMENT.md
touch docs/API.md
touch docs/MONITORING.md
touch docs/ML_MODEL.md

# Création du répertoire Reports (reports/)
echo "-> Création du dossier reports (reports)"
mkdir -p reports/drift
touch reports/data_quality_report.html
touch reports/model_comparison.csv
touch reports/feature_importance.csv
touch reports/shap_summary_plot.png

# Fichiers à la racine
echo "-> Création des fichiers racines"
touch README.md
touch Dockerfile
touch docker-compose.yml
touch requirements.txt

echo "✅ Structure de projet MLOps créée avec succès dans /$PROJECT_NAME"