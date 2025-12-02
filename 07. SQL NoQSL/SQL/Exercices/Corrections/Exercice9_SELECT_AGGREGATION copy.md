# SELECT MIN, MAX, AVG, SUM (aggregation)

### Exercice: Utilisation des fonctions d'agrégation


Dans ma table Users, trouvez les requêtes suivantes **en utilisant à chaque fois des alias**:

1) Quel est le salaire minimum parmi tous les utilisateurs ?
2) Quel est l'âge maximum parmi les utilisateurs ayant le métier "Engineer" ?
3) Trouvez le salaire moyen des utilisateurs dont le métier est "Teacher".
4) Trouvez le montant total des salaires de tous les utilisateurs.

---

#### CORRECTION: Utilisation des fonctions d'agrégation


```sql
SELECT MIN(salary) AS MinSalary
FROM Users;

SELECT MAX(age) AS MaxAgeEngineer
FROM Users
WHERE job = 'Engineer';

SELECT AVG(salary) AS AvgSalaryTeacher
FROM Users
WHERE job = 'Teacher';

SELECT SUM(salary) AS TotalSalaries
FROM Users;
```
