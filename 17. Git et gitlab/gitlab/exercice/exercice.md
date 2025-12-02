# Exercice Gitlab CI/CD

## Partie 0 : Préparation de l'application

1. Créer `calculatrice.py` (addition, soustraction, division...)
2. Créer `test_calculatrice.py`
3. Créer un `Dockerfile`
4. Créer `requirements.txt`

```txt
pytest==7.4.3
pytest-cov==4.1.0
```

5. Tester localement

## Partie 1

- Créer un job "run_tests" qui :
    - utilise l'image python:3.11
    - Installer les dépendances
    - lancer les tests avec pytest
    - Afficher un message de succès

## Partie 2

- Ajouter des variables dans les settings :
    - `APP_NAME` = `Calculatrice`
    - `APP_VERSION` = `1.0.0`
    - `DEV_NAME` = `Toto`

Ajouter un nouveau job "show_info":
    - Afficher le contenu des variables

## Partie 3

ajouter un job "build_app"
    - compile calculatrice
    - sauvegarde l'artifact
        - expire dans 1 jour

ajouter au job "run_test"
    - sauvegarde un rapport avec pytest :
        - pytest -v --junitxml=report.xml
        - artifact: report.xml

ajouter un job "show_report"
    - utilise l'artifact de run test
    - Affiche le contenu du rapport avec cat report.xml

# Partie 4:

Ajouter la variable : PIP_CACHE_DIR

Modifier build pour ajouter un cache
Modifier test pour utiliser le cache

# Partie 5

blocquer la pipeline si les tests échoues

# Partie 6

build => toutes les branches
test => branche dev et main
Créer un job deploy => main uniquement
