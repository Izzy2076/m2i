
## Exercice : Création de tables pour une base de données de streaming musical

Imaginez que vous devez concevoir une base de données pour un service de streaming musical. Vous devez créer trois tables : une pour les utilisateurs, une pour les chansons et une pour les playlists. Voici les détails des tables requises :

- Table "Utilisateurs" :
    - Nom de la table : utilisateurs
    - Colonnes :
        - -id_utilisateur (clé primaire)
        - nom_utilisateur (texte)
        - email (texte)
        - date_inscription (date)
        - pays (texte)

- Table "Chansons" :
    - Nom de la table : chansons
    - Colonnes :
        - id_chanson (clé primaire)
        - titre (texte)
        - artiste (texte)
        - album (texte)
        - durée (intervalle de temps)
        - genre (texte)
        - année_sortie (année)

- Table "Playlists" :
    - Nom de la table : playlists
    - Colonnes :
        - id_playlist (clé primaire)
        - nom_playlist (texte)
        - id_utilisateur (clé étrangère faisant référence à la table "Utilisateurs")
        - id_chansons (clé étrangère faisant référence à la table "Chansons")
        - date_creation (date)

Votre tâche consiste à écrire les instructions SQL nécessaires pour créer ces trois tables dans une base de données. Assurez-vous de définir les types de données
appropriés, de spécifier les clés primaires et étrangères, et de gérer les relations
entre les tables.