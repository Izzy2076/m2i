## Exercice : Création de tables pour une base de données de bibliothèque

Supposons que vous devez créer une base de données pour une bibliothèque. Vous
devez concevoir deux tables : une pour les livres et une pour les membres. Voici les détails des tables requises :

- Table "Livres" :
   - Nom de la table : livres
   - Colonnes :
      - id_livre (clé primaire)
      - titre (texte)
      - auteur (texte)
      - année_publication (entier)
      - genre (texte)
      - exemplaires_disponibles (entier)
      
- Table "Membres" :
   - Nom de la table : membres
   - Colonnes :
      - id_membre (clé primaire)
      - nom (texte)
      - prénom (texte)
      - date_naissance (date)
      - adresse (texte)
      - email (texte)
      - téléphone (texte)

Votre tâche consiste à écrire les instructions SQL nécessaires pour créer ces deux tables dans une base de données. Assurez-vous de définir les types de données appropriés et de spécifier les clés primaires.

---

```sql
-- Creation de la base de données:
CREATE DATABASE IF NOT EXISTS bibliotheque;
USE bibliotheque;

-- Creation de la table Livres:
CREATE TABLE livres (
    id_livre INT PRIMARY KEY,
    titre TEXT,
    auteur TEXT,
    annee_publication INT,
    genre TEXT,
    exemplaires_disponibles INT
);

-- Creation de la table Membres:
CREATE TABLE membres (
    id_membre INT PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    date_naissance DATE,
    adresse TEXT,
    email TEXT,
    telephone TEXT
);

```