
# SELECT BETWEEN IN 

#### Exercice: Manipulation de données dans la table "Users"

Dans notre table **Users**, en utilisant au moins pour une requête IN et pour une autre BETWEEN:
1) Sélectionnez tous les enregistrements où le métier est "Engineer"
2) Sélectionnez les prénoms et les noms de famille des utilisateurs nés à Londres, Paris ou Berlin
3) Sélectionnez les utilisateurs dont l'âge est compris entre 25 et 35 ans
4) Sélectionnez les utilisateurs qui sont à la fois des développeurs et dont le salaire est supérieur à 2500€

---
### Correction : 



```sql
SELECT * FROM Users
WHERE job = 'Engineer';

SELECT first_name, last_name FROM Users
WHERE birth_location IN ('London', 'Paris', 'Berlin');

SELECT * FROM Users
WHERE age BETWEEN 25 AND 35;

SELECT * FROM Users
WHERE job = 'Developer' AND salary > 2500;
```
