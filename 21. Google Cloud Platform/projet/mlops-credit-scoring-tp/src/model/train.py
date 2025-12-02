# src/model/train.py

import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
# Importez vos modules pour l'ETL et les Features
from src.data.ingestion import load_and_clean_data # À créer
from src.features.engineering import get_all_features # Les fonctions que nous venons d'écrire
from src.model.evaluation import evaluate_and_select_threshold # À créer

def train_pipeline(tracking_uri: str, model_name: str):
    # 1. Configuration MLflow
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment("Credit_Scoring_TP")

    with mlflow.start_run():
        # 2. Chargement et Feature Engineering
        print("Étape 1: Chargement et Préparation des données...")
        
        # NOTE: Cette fonction appellera vos fonctions get_bureau_features, get_pos_cash_features, etc.
        # et joindra le résultat au dataframe principal (application_train/test).
        df_final = get_all_features(train_path="infra/data/raw/application_train.csv") 

        # 3. Séparation et Préprocessing (simplifié)
        X = df_final.drop(columns=['SK_ID_CURR', 'TARGET'])
        y = df_final['TARGET']
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        
        # 4. Entraînement du Modèle
        print("Étape 2: Entraînement du modèle LightGBM...")
        params = {'n_estimators': 1000, 'learning_rate': 0.05, 'random_state': 42}
        lgbm = LGBMClassifier(**params, n_jobs=-1, class_weight='balanced') # Utilisation du class_weight pour l'imbalance
        lgbm.fit(X_train, y_train)
        
        # 5. Évaluation et Optimisation du Seuil (selon Coût Métier C)
        auc_roc, optimal_threshold, cost_min = evaluate_and_select_threshold(lgbm, X_val, y_val)
        
        # 6. Logging MLflow
        mlflow.log_params(params)
        mlflow.log_metric("AUC_ROC_VAL", auc_roc)
        mlflow.log_metric("COST_MINIMIZED", cost_min)
        mlflow.log_metric("OPTIMAL_THRESHOLD", optimal_threshold)

        # 7. Enregistrement du Modèle (avec le seuil intégré)
        mlflow.sklearn.log_model(
            sk_model=lgbm,
            artifact_path="model",
            registered_model_name=model_name,
            # Vous pourriez logguer le seuil dans les tags du modèle
            metadata={"optimal_threshold": optimal_threshold} 
        )
        print(f"Modèle enregistré dans MLflow Registry: {model_name}")

if __name__ == "__main__":
    # Définir l'URI du serveur de tracking (celui de docker-compose)
    TRACKING_URI = "http://mlflow-server:5000" # Sera accessible dans Docker
    MODEL_REGISTRY_NAME = "CreditScoringLGBM"
    
    # En local, si vous n'êtes pas dans Docker, utilisez l'URI locale:
    # TRACKING_URI = "http://localhost:5000"
    
    try:
        train_pipeline(TRACKING_URI, MODEL_REGISTRY_NAME)
    except Exception as e:
        print(f"Erreur lors de l'exécution du pipeline: {e}")