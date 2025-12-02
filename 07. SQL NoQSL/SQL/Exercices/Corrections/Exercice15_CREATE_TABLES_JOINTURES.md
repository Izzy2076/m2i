
### Exercice: Création de tables

**Instructions :** Vous utiliserez les 

1. Créez une base de données nommée `music_stream.

2. Créez une table `utilisateurs` contenant les infos suivantes :
  - Un identifiant unique pour chaque utilisateur (id_utilisateur)
  - Le nom d’utilisateur (nom_utilisateur) – requis
  - Une adresse email – unique
  - La date d’inscription – par défaut à la date/heure actuelle
  - Le pays d’origine de l’utilisateur

3. Créez une table `chansons` contenant les informations suivantes :
  - Un identifiant unique pour chaque chanson (id_chanson)
  - Le titre de la chanson
  - Le nom de l’artiste
  - Le nom de l’album
  - La durée de la chanson
  - Le genre musical
  - L’année de sortie

4. Créez une table `playlists` contenant les informations suivantes :

- Un identifiant unique pour chaque playlist (id_playlist)
- Le nom de la playlist
- L’identifiant de l’utilisateur qui a créé la playlist (id_utilisateur) – clé étrangère vers la table utilisateurs
- L'identifiant de la chansons intégrée dans la playlist (id_chanson) – clé étrangère vers la table chansons
- La date de création – par défaut à la date/heure actuelle

---

```sql
-- Creation de la base de données:
CREATE DATABASE IF NOT EXISTS music_stream;
USE music_stream;

-- Création de la table "Utilisateurs"
CREATE TABLE utilisateurs (
    id_utilisateur INT PRIMARY KEY,
    nom_utilisateur VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pays VARCHAR(255)
);

-- Création de la table "Chansons"
CREATE TABLE chansons (
    id_chanson INT PRIMARY KEY,
    titre VARCHAR(255),
    artiste VARCHAR(255),
    album VARCHAR(255),
    duree TIME,
    genre VARCHAR(255),
    annee_sortie YEAR
);

-- Création de la table "Playlists"
CREATE TABLE playlists (
    id_playlist INT PRIMARY KEY,
    nom_playlist VARCHAR(255),
    id_utilisateur INT,
    id_chanson INT,
    date_creation TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id_utilisateur)
    FOREIGN KEY (id_chanson) REFERENCES chansons(id_chanson)
);

-- Pour effectuer la jointure sur la table intermédiaire
SELECT u.nom_utilisateur, c.titre, p.nom_playlist
FROM Playlists AS p
INNER JOIN Chansons AS c ON p.id_chanson = c.id_chanson
INNER JOIN Utilisateurs AS u ON p.id_utilisateur = u.id_utilisateur; 
```