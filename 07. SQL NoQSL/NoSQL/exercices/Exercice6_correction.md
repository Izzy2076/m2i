# Exercice pratique MongoDB : Collection Films pt3 

## **Préparation**
Dans une base de données nommée `cinéma`, importer les documents du fichier json dans la collection `films`

### Aggregation

1. Afficher les titres en majuscule avec leur annee de production ($project)

```js
db.films.aggregate([
  {
    $project: {
        _id: 0,  
        titre: { $toUpper: "$titre" },
        annee_production: 1
    }
  }
])
```

2. Lister les films avec un âge limite >= 12, puis projeter leurs `titre` et un nouveau champs `nb_genres` qui donne le nombre de genre qu'il posséde. ($match + $project)

```js
db.films.aggregate([
  { $match: { age_limite: { $gte: 12 } } },
  {
    $project: {
      titre: 1,
      age_limite: 1,
      nb_genres: { $size: "$genres" }
    }
  }
])
```

3. Compter le nombre de films par âge limite ($group)

```js
db.films.aggregate([
  {
    $group: {
      _id: "$age_limite",
      count: { $sum: 1 }
    }
  }
])
```

4. Compter le nombre de films par genre et trier par ordre décroissant

```js
db.films.aggregate([
  { $unwind: "$genres" },
  {
    $group: {
      _id: "$genres",
      count: { $sum: 1 }
    }
  },
  { $sort: { count: -1 } }
])
```

5. Ajouter un champs `nb_genres` qui compte le nombre de genre par films. 
Récupérer les films avec plus de 1 genres, regrouper par `nb_genres` et trier par ordre croissant. 

```js
db.films.aggregate([
  {
    $addFields: { nb_genres: { $size: "$genres" } }
  },
  {
    $match: { nb_genres: { $gte: 2 } }
  },
  {
    $group: {
      _id: "$nb_genres",
      count: { $sum: 1 }
    }
  },
  {
    $sort: { _id: 1 }
  }
])
```

- BONUS: Compter le nombre de films par décennie puis trier par ordre croissant. 

*Petit calcul nécessaire: 
1999/10 => 199.9 ($divide)
199.9 => 199 ($floor)
199 => 1990 ($multiply)

```js
db.films.aggregate([
  {
    $project: {
      decennie: {
        $multiply: [
          { $floor: { $divide: ["$annee_production", 10] } },
          10
        ]
      }
    }
  },
  {
    $group: {
      _id: "$decennie",
      count: { $sum: 1 }
    }
  },
  { $sort: { _id: 1 } }
])
```