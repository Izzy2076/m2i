# Exercice pratique MongoDB : Collection Films

## **Préparation**
Dans une base de données nommée `cinéma`, importer les documents du fichier json dans la collection `films`

---

## Partie 1 : Requêtes de base

### 1.1 Lecture simple

1. Affichez tous les films

2. Affichez uniquement le premier film

3. Convertissez tous les résultats en tableau

### 1.2 Filtres simples

4. Trouvez tous les films sortis en 1994 => 4
 
5. Trouvez le film "Inception" => 1

6. Trouvez tous les films avec un âge limite de 18 ans => 4

---

## Partie 2 : Opérateurs de comparaison

### 2.1 Comparaisons numériques

7. Trouvez les films produits après 2000 => 10

8. Trouvez les films avec un âge limite inférieur ou égal à 6 ans => 8

9. Trouvez les films qui ne sont PAS sortis en 1994 => 26

---

## Partie 3 : Opérateurs logiques

### 3.1 Combinaisons de conditions

10. Trouvez les films produits entre 1990 et 2000 (inclus) => 14

11. Trouvez les films d'Action ET produits après 2010 => 1

12. Trouvez les films avec âge limite 3 ans OU 6 ans => 8

13. Trouvez les films qui ne sont PAS des drames => 11

---

## Partie 4 : Opérateurs sur les tableaux

### 4.1 Recherche dans les genres

14. Trouvez les films contenant exactement les genres ["Action", "Science-Fiction"] => 1

15. Trouvez les films qui sont soit "Comédie" soit "Romance" => 6

16. Trouvez les films qui ne sont ni "Horreur" ni "Thriller" => 25

17. Trouvez les films qui sont à la fois "Action" ET "Aventure" => 4

18. Trouvez les films ayant exactement 3 genres => 19

---

## Partie 5 : Tri, limitation et pagination

### 5.1 Organisation des résultats

19. Triez les films par année croissante => Casablanca

20. Triez les films par titre décroissant => Titanic

21. Affichez les 5 films les plus récents => Parasite

22. Affichez les films 11 à 15 (pagination) => Star Wars: Episode IV

23. Affichez les 3 films les plus anciens avec âge limite 12+ => The Godfather

---

## Partie 6 : Projection

### 6.1 Sélection de champs

24. Affichez uniquement le titre et l'année (sans _id)

25. Affichez tout sauf les genres

26. Affichez le titre et l'âge limite des films d'animation

---

## Partie 7 : Requêtes complexes combinées

### 7.1 Défis avancés

27. Affichez le top 3 des films d'action les plus récents (titre et année uniquement) => Avengers

28. Trouvez les films des années 90 tout public (âge ≤ 6) triés par titre => 2

29. Trouvez les films sci-fi ou fantastique, après 2000, âge 12+ maximum => 6 

30. Parcourez tous les films et affichez les titres en majuscules

---

## Partie 8 : Opérateurs d'éléments et vérifications

### 8.1 Structure des documents

31. Vérifiez quels films ont le champ 'genres'

32. Trouvez les films où 'age_limite' est un nombre

33. Comptez les films par décennie

---

## Défis bonus

34. Trouvez les films avec un titre contenant un chiffre => 1 

35. Trouvez les films de plus de 2 genres, triés par nombre de genres décroissant => 19

36. Affichez la page 2 des films d'action (5 par page)

37. Effectuez une recherche multi-critères avec projection complète : films de genre "Drame" ou "Crime", produits après 1990, avec âge limite 16+, triés par année décroissante, limités à 10 résultats => 6