## **Exercice pratique : Création et validation d'une collection**

### **Enoncé**

1. Créez une collection appelée `employees` dans une bdd `exercice` avec les règles suivantes :
    - Les documents doivent contenir :
        - Un champ `name` (chaîne de caractères, obligatoire).
        - Un champ `age` (nombre entier, minimum : 18).
        - Un champ `department` (chaîne de caractères).
    - Validez strictement les documents.
    - Rejetez les documents non conformes.
2. Insérez deux documents valides et un document non valide pour tester la validation :
    - Document valide : `{ name: "Alice", age: 25, department: "HR" }`.
    - Document valide : `{ name: "Bob", age: 30, department: "IT" }`.
    - Document non valide : `{ name: "Charlie", age: 17 }`.