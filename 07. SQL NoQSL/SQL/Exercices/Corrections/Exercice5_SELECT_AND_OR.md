
# SELECT OR AND 

#### Exercice : utiliser les opérateurs OR et AND


Dans notre table **Users**, essayez de filtrer de cette manière:
1) Dans un première requête, récupérez tous les utilisateurs dont l'âge est inférieur à 30ans ou supérieur et égal à 35ans.
2) Récupérez ensuite tous les utilisateurs dont le métier est professeur et le salaire est supérieur à 2600.

---
#### CORRECTION : Filtrer les données avec WHERE


```sql
SELECT first_name, last_name, age
FROM Users
WHERE  age < 30 OR age >= 35;

SELECT first_name, last_name, age, salary
FROM Users
WHERE  job = 'Teacher' AND salary > 2600;
```
