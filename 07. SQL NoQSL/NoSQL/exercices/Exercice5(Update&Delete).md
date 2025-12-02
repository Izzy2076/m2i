# Exercice pratique MongoDB : Collection Films pt2 

## **Préparation**
Dans une base de données nommée `cinéma`, importer les documents du fichier json dans la collection `films`

### Update

1. Via update, changer le titre du film `The Shawshank Redemption` par `Les évadés`. 

2. Via un update, ajouter un champs `nbUpdate` (entier initialisé à 0) à tout les documents de la collection et incrémenter le de 1 : en une seule requête. 

3. Via update, supprimer le champs `nbUpdate` pour les films produit avant l'année 2000. 

4. Via update, ajouter au tableau `genres` du film intitulé `Fight Club`, le genre 'Romance'. 

### Delete

5. Supprimer le film dont le titre est `Parasite`.

6. Supprimer tout les documents qui sont du genre `Thriller` OU `Guerre`.

