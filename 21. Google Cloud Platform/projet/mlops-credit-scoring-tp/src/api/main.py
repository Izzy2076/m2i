# src/api/main.py

from fastapi import FastAPI, HTTPException
import mlflow
import uvicorn
import pandas as pd
# Importez vos schémas (validation d'entrée/sortie)
from src.api.schemas import CreditApplicationInput, PredictionOutput
# Importez votre code de Feature Engineering (pour transformer les entrées API)
# from src.features.engineering import preprocess_api_input 
# Importez vos métriques pour Prometheus
from src.api.prometheus_metrics import metrics_app

# --- Configuration et Chargement du Modèle ---

MLFLOW_TRACKING_URI = "http://mlflow-server:5000" # ou l'adresse de votre serveur K8s
MODEL_NAME = "CreditScoringLGBM"
MODEL_STAGE = "Production" # Charge le modèle le plus récent taggué "Production"

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

try:
    # Charger le modèle à partir du Registry MLflow
    MODEL_URI = f"models:/{MODEL_NAME}/{MODEL_STAGE}"
    model = mlflow.sklearn.load_model(MODEL_URI)
    print(f"Modèle chargé: {MODEL_URI}")
    
    # Récupérer le seuil optimal loggué dans les metadata du modèle
    # NOTE: Ceci suppose que vous avez stocké cette info lors de l'enregistrement dans train.py
    model_version = mlflow.tracking.MlflowClient().get_latest_versions(MODEL_NAME, stages=[MODEL_STAGE])[0]
    OPTIMAL_THRESHOLD = float(model_version.tags.get("optimal_threshold", 0.125)) # Valeur par défaut si non trouvé
    
except Exception as e:
    print(f"Erreur fatale au chargement du modèle: {e}")
    model = None
    OPTIMAL_THRESHOLD = 0.125 # Utiliser une valeur par défaut pour l'initialisation

# --- Initialisation de l'API ---
app = FastAPI(title="Credit Scoring MLOps API", version="1.0.0")

# Ajouter l'application de métriques Prometheus
app.mount("/metrics", metrics_app)

@app.get("/health")
def health_check():
    """Vérification de la santé du service et du modèle."""
    if model:
        return {"status": "ok", "model_version": model_version.version if 'model_version' in locals() else "N/A", "model_stage": MODEL_STAGE}
    else:
        # 503 Service Unavailable si le modèle n'a pas pu être chargé
        raise HTTPException(status_code=503, detail="Model not loaded. Service Unavailable.")

@app.post("/predict", response_model=PredictionOutput)
def predict(data: CreditApplicationInput):
    """Calcule le score de risque de défaut (probabilité) et la décision."""
    if not model:
        raise HTTPException(status_code=503, detail="Model service not ready.")

    # 1. Transformer les données d'entrée Pydantic en DataFrame
    df_input = pd.DataFrame([data.model_dump()]) # Ou data.dict() pour les versions antérieures
    
    # 2. Exécuter le Feature Engineering nécessaire sur les entrées API
    # NOTE: En production, ceci doit être rapide et léger, car les features complexes devraient être dans un Feature Store.
    # df_processed = preprocess_api_input(df_input) # Appel de votre fonction de préprocessing
    df_processed = df_input # Simplification pour l'exemple

    # 3. Prédiction
    prob_default = model.predict_proba(df_processed)[:, 1][0]
    
    # 4. Décision basée sur le seuil optimal
    decision = "REJECTED" if prob_default >= OPTIMAL_THRESHOLD else "ACCEPTED"
    
    # NOTE: L'explication SHAP (justification) serait calculée ici

    return PredictionOutput(
        SK_ID_CURR=data.SK_ID_CURR,
        risk_score=prob_default,
        decision=decision,
        decision_threshold=OPTIMAL_THRESHOLD,
        justification=[] # Remplir avec les résultats SHAP
    )

if __name__ == "__main__":
    # Pour l'exécution locale
    uvicorn.run(app, host="0.0.0.0", port=8000)