### Exercice - Subqueries avec la table "Users"

**Instructions :** Utilisez des subqueries pour répondre aux questions suivantes.

1. Affichez les utilisateurs nés dans le même lieu que celui du plus jeune utilisateur.

2. Sélectionnez les utilisateurs dont le salaire est inférieur à la moyenne des salaires des "Developers".

3. Affichez les utilisateurs dont le salaire est supérieur à la moyenne des salaires des utilisateurs nés dans la même ville que "John Doe".

---

### CORRECTION : Subqueries avec la table "Users"

```sql
SELECT *
FROM Users
WHERE lieu_naissance = (
    SELECT lieu_naissance
    FROM Users
    ORDER BY date_naissance DESC
    LIMIT 1
);

SELECT *
FROM Users
WHERE salaire < (
    SELECT AVG(salaire)
    FROM Users
    WHERE profession = 'Developer'
);

SELECT *
FROM Users
WHERE salaire > (
    SELECT AVG(salaire)
    FROM Users
    WHERE lieu_naissance = (
        SELECT lieu_naissance
        FROM Users
        WHERE nom = 'John Doe'
        LIMIT 1
    )
);
```
