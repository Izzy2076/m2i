# Exercice pratique MongoDB : Collection Films pt3 

## **Préparation**
Dans une base de données nommée `cinéma`, importer les documents du fichier json dans la collection `films`

### Aggregation

1. Afficher les titres en majuscule avec leur annee de production ($project)


2. Lister les films avec un âge limite >= 12, puis projeter leurs `titre` et un nouveau champs `nb_genres` qui donne le nombre de genre qu'il posséde. ($match + $project)


3. Compter le nombre de films par âge limite ($group)


4. Compter le nombre de films par genre et trier par ordre décroissant


5. Ajouter un champs `nb_genres` qui compte le nombre de genre par films. 
Récupérer les films avec plus de 1 genres, regrouper par `nb_genres` et trier par ordre croissant. 

- BONUS: Compter le nombre de films par décennie puis trier par ordre croissant. 

*Petit calcul nécessaire: 
1999/10 => 199.9 ($divide)
199.9 => 199 ($floor)
199 => 1990 ($multiply)
