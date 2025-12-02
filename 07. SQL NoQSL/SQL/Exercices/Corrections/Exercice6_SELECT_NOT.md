# SELECT ALL 

#### Exercice: récapitulatif


Créez une requête qui permet de récupérer toutes les personnes qui sont nées à New York, dont le salaire est compris entre 3000 et 3500 (compris) et qui ne sont ni docteur ni avocat.

- Toutes les conditions doivent tenir en une seule requête
- Les trois opérateurs logiques : AND, OR et NOT doivent être utilisés.

---
#### Correction: récapitulatif



```sql
SELECT 
  * 
FROM 
  Users 
WHERE 
  birth_location = 'New York' 
  AND (salary >= 3000 AND salary <= 3500) 
  AND NOT (job = 'Doctor' OR job = 'Lawyer');

```