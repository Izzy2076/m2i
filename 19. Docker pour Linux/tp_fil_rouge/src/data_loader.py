import pandas as pd
from pathlib import Path


def load_csv(filepath: str, encoding: str = 'utf-8') -> pd.DataFrame:
    path = Path(filepath)
    
    if not path.exists():
        raise FileNotFoundError(f"Le fichier {filepath} n'existe pas")

    try:
        df = pd.read_csv(filepath, encoding=encoding)
        
        if df.empty:
            raise ValueError("Le fichier CSV est vide")
        
        return df
        
    except pd.errors.EmptyDataError:
        raise ValueError("Le fichier CSV ne contient aucune donnée")