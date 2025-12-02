# TP supplémentaire 1

## **Contexte Data Engineering**
Vous développez un pipeline de données pour une startup qui analyse les performances de sites e-commerce. Le système doit traiter des logs d'API, des données de sessions utilisateurs, et des métriques business en utilisant uniquement Bash (orchestration) et Python (traitement) sur Linux.

## **Problématique Data**
Le pipeline traite quotidiennement :
- **Logs d'API** : 200+ fichiers JSON (1-5GB chacun) avec requêtes utilisateurs
- **Sessions web** : CSV avec parcours clients, durées, conversions
- **Métriques business** : Ventes, abandons panier, taux de rebond
- **Données produits** : Catalogues, prix, stock (Excel/CSV)
- **Log serveurs** : Nginx access logs avec géolocalisation

**Défi Data** : Traiter 50+ GB/jour avec parallélisation intelligente, transformations complexes, et génération de rapports business.

---

## **CONSIGNES TECHNIQUES PRÉCISES**

### **📋 MISSION DATA ENGINEERING**
Créer un pipeline de données production-ready qui ingère, transforme, et analyse automatiquement les données e-commerce avec Bash + Python.

### **MODULES OBLIGATOIRES**

#### **Module 1 : Data Orchestrator (Bash)** ⭐ **(Priorité Critique)**
```bash
#!/bin/bash
# CONSIGNE : Orchestrateur principal qui gère le pipeline de données

# Architecture obligatoire :
data_pipeline_master.sh
├── initialize_data_pipeline()   # Configuration environnement data
├── scan_data_sources()          # Découverte automatique des sources
├── distribute_processing()      # Répartition par type/taille de données  
├── monitor_data_quality()       # Surveillance qualité en temps réel
├── aggregate_data_results()     # Consolidation multi-sources
├── generate_data_reports()      # Rapports automatiques
└── archive_processed_data()     # Archivage avec compression

# Variables data obligatoires :
DATA_WORKERS=6               # Workers spécialisés par type de données
CHUNK_SIZE_MB=500           # Taille des chunks de traitement
QUALITY_THRESHOLD=95        # Seuil minimal de qualité (%)
PROCESSING_TIMEOUT=3600     # Timeout par fichier (1h)
```

**Fonctionnalités Bash data-specific :**
- 📁 **Data discovery** : Auto-détection de formats (CSV, JSON, logs)
- 🔄 **Pipeline restart** : Reprise automatique après crash
- 💾 **Data partitioning** : Organisation par date/source/format

#### **Module 2 : Data Processor (Python)** ⭐ **(Priorité Critique)**
```python
#!/usr/bin/env python3
# CONSIGNE : Moteur de traitement de données multi-format


```

**Transformations data obligatoires :**
- 🧹 **Data cleaning** : Déduplication, gestion des nulls, normalisation
- 🔗 **Data joining** : Jointures complexes entre sources hétérogènes
- 📈 **Data aggregation** : GroupBy, pivots, window functions
- 🎯 **Data enrichment** : Géocodage, catégorisation, scoring
- ⚡ **Data validation** : Règles métier, contraintes d'intégrité

#### **Module 3 : Data Quality Manager (Bash + Python)** ⭐ **(Priorité Haute)**
```bash
#!/bin/bash
# CONSIGNE : Gestionnaire de qualité des données

data_quality_monitor.sh() {
    # OBLIGATOIRE : Validation de schémas (colonnes attendues/reçues)
    # OBLIGATOIRE : Contrôles de cohérence inter-fichiers
    # OBLIGATOIRE : Détection d'anomalies statistiques
    # OBLIGATOIRE : Alertes automatiques si qualité < seuil
    
    
}
```

**Contrôles qualité data obligatoires :**
- 📋 **Schema validation** : Vérification structure attendue
- 🚨 **Anomaly detection** : Valeurs aberrantes, pics suspects
- 🎯 **Business rules** : Validation des règles métier

### **🔧 ARCHITECTURE DATA**

#### **Structure data pipeline obligatoire :**


```

### **📊 EXIGENCES DATA ENGINEERING**

#### **Performance data obligatoire :**
- 🔄 **Parallelism** : 6 workers Python simultanés
- 💾 **Memory efficiency** : Traitement par chunks de 100K lignes

#### **Fonctionnalités data avancées :**
```python
# EXEMPLES D'IMPLÉMENTATIONS OBLIGATOIRES

def incremental_processing(data_dir, last_processed_timestamp):
    """Traitement incrémental - ne traite que les nouvelles données"""
    # Delta processing pour éviter de retraiter tout l'historique
    pass

def data_lineage_tracker(input_files, transformations, output_files):
    """Traçabilité complète des transformations de données"""
    # Tracking de chaque étape pour audit et debug
    pass

def adaptive_chunking(file_size, available_memory):
    """Calcul automatique de la taille des chunks selon les ressources"""
    # Optimisation dynamique selon la mémoire disponible
    pass

def data_quality_scoring(dataframe, quality_rules):
    """Calcul de score de qualité multi-dimensionnel"""
    # Score composite : complétude, exactitude, cohérence, fraîcheur
    pass
```

### **🎯 LIVRABLES DATA ENGINEERING**

#### **1. Pipeline Data Fonctionnel** 

#### **2. Code Data Production** 

#### **3. Documentation Data** 
---

