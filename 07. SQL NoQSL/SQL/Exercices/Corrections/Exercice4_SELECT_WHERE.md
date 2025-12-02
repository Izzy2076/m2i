
# SELECT WHERE


#### Exercice : filtrer les données de notre table avec WHERE

Essayons maintenant nous-même de filtrer les données de la table **Users** de notre base de données.
1) Dans une première requête, récupérez tous les utilisateurs dont le métier n'est pas développeur
2) Dans une seconde requête, récupérez tous les utilisateurs dont le prénom est John.
3) Dans une dernière requête, récupérez tous les utilisateurs dont le salaire est supérieur ou égal à 3000.

---
#### CORRECTION : filtrer les données avec WHERE


```sql
SELECT first_name, last_name, job
FROM Users
WHERE job != 'Developer';

SELECT first_name, last_name
FROM Users
WHERE first_name = 'John';

SELECT first_name, last_name, salary
FROM Users
WHERE salary >= 3000
```