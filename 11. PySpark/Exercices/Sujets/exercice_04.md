## Dataset

- Source : [MovieLens Small sur Kaggle](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset)
- Schéma :
  - `movies.csv` : `movieId:int`, `title:string`, `genres:string`
  - `ratings.csv` : `userId:int`, `movieId:int`, `rating:float`, `timestamp:long`

## Étapes du TP

1. Charger les données
2. Jointure de base

- Faire un **inner join** entre `ratings` et `movies` sur `movieId`
- Afficher quelques exemples de notes enrichies avec le titre du film

3. Statistiques globales

- Calculer le nombre de notes et la moyenne des notes par film
- Trier par nombre de notes décroissant

4. Variantes de jointures

- **LEFT SEMI** : films qui ont au moins une note
- **LEFT ANTI** : films sans aucune note
- **LEFT OUTER** : liste complète des films avec stats si disponibles
- **FULL OUTER** : diagnostic des clés présentes uniquement dans l’un des deux fichiers

5. Exercices pratiques

A. **Top 5 global** : films les mieux notés
B. **Top 10 par genre** : films les mieux notés par genre
C. **Moyenne annuelle** : moyenne des notes par année de sortie  
D. **Profil utilisateur** : genre préféré de chaque utilisateur
E. **Films sans note** : lister 20 films sans aucune note  
F. **Validation** : vérifier qu’aucun `movieId` n’est dupliqué dans `movies`
