# Documentation du Modèle : Entraînement et Interprétabilité

Ce document détaille le processus de développement du modèle, de l'évaluation des algorithmes à l'optimisation du seuil de décision en fonction de la contrainte métier.

## 1. Contexte et Stratégie de Modélisation

### A. Objectif de Prédiction

L'objectif est de prédire la variable **TARGET** (1 : le client a fait défaut, 0 : le client a remboursé). Le modèle doit fournir une **probabilité de défaut** ($\text{p}$) qui est ensuite utilisée pour la prise de décision.

### B. Défi Principal : Déséquilibre des Classes

Le jeu de données présente un fort déséquilibre de classes (environ **92% de classe 0** contre **8% de classe 1**).

* **Stratégie d'Atténuation :** Utilisation de l'outil **`imbalanced-learn`** (SMOTE) ou ajustement des poids de classes dans l'algorithme LightGBM pour donner plus d'importance aux défauts (classe 1).

## 2. Métrique d'Évaluation Critique

Dans un contexte bancaire, la métrique standard **AUC-ROC** est utilisée pour comparer la performance des modèles. Cependant, la décision finale doit être prise en minimisant un **coût métier** spécifique.

### A. Fonction de Coût Métier

L'objectif est de minimiser le coût total $C$, basé sur les faux négatifs ($\text{FN}$) et les faux positifs ($\text{FP}$) :

$$C = (C_{FN} \times \text{FN}) + (C_{FP} \times \text{FP})$$

Où :
*$C_{FN}$ (Coût du Faux Négatif) : Coût d'accorder un prêt à un client qui fera défaut. **Pénalité forte (Exemple : 10 €)**.
*$C_{FP}$ (Coût du Faux Positif) : Coût de refuser un prêt à un client qui aurait remboursé. **Pénalité faible (Exemple : 1 €)**.

> **Contrainte du TP :** $C = (10 \times \text{FN}) + (1 \times \text{FP})$. Le Faux Négatif est 10 fois plus coûteux que le Faux Positif.

### B. Optimisation du Seuil de Décision

Le script d'entraînement (`src/model/evaluation.py`) doit itérer sur différents seuils de probabilité (ex: $0.05$ à $0.20$) et sélectionner le seuil $\theta^*$ qui **minimise la fonction de coût $C$** sur l'ensemble de validation.

## 3. Comparaison et Choix de l'Algorithme

Nous comparons plusieurs modèles pour trouver le meilleur compromis entre performance, vitesse d'entraînement et interprétabilité.

### A. Résultats des Modèles (Exemple)

Le modèle final sélectionné est **LightGBM** pour sa rapidité et son efficacité sur les données tabulaires. Le tracking de ces résultats est effectué dans **MLflow**.

| Modèle | AUC-ROC Validation | Coût Métier Min. ($C$) | Seuil Optimal ($\theta^*$) | Temps d'Entraînement | Statut MLflow |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **LightGBM** (Optuna) | **0.785** | **12 500 €** | **0.125** | 120s | **Production** |
| XGBoost (GridSearch) | 0.778 | 13 800 € | 0.130 | 350s | Archive |
| Logistic Regression | 0.721 | 22 100 € | 0.150 | 5s | Archive |

### B. Optimisation des Hyperparamètres (Optuna)

L'outil **Optuna** est utilisé pour optimiser les hyperparamètres (nombre d'estimateurs, profondeur maximale, learning rate, etc.) de LightGBM afin de maximiser l'AUC-ROC tout en minimisant le Coût Métier.

## 4. Interprétabilité du Modèle (SHAP)

L'interprétabilité est fondamentale pour la confiance métier, la justification des refus de crédit, et le débogage.

### A. Interprétabilité Globale (Feature Importance)

La méthode **SHAP (SHapley Additive exPlanations)** est utilisée pour déterminer l'importance globale des features.

* **Résultat :** Le graphique SHAP Summary Plot (`reports/shap_summary_plot.png`) visualise les 20 features ayant le plus grand impact sur la prédiction (valeur moyenne absolue SHAP).

* **Top 3 des Features (Exemple) :**
1.`EXT_SOURCE_3` : Score de source de données externe (Impact Négatif).
2.`BUREAU_CREDIT_COUNT` : Nombre total de prêts passés (Impact Positif).
3.`DAYS_EMPLOYED` : Nombre de jours travaillés (Impact Positif).

### B. Interprétabilité Locale (Justification)

La plateforme est capable de fournir une explication par client (justification du score).

* **Rôle :** Pour chaque requête de prédiction dans l'API, les 3 à 5 features qui ont le plus fortement contribué à la probabilité de défaut (valeurs SHAP locales) sont retournées.
* **Utilisation :** Cette information est cruciale pour générer une lettre de refus de crédit conforme aux réglementations (ex: "Votre score est bas en raison d'un ratio Dette/Revenu élevé et d'un historique de prêts actifs courts").
