# Instructions

### 1. Créer une classe `Book`

- Attributs :
  - `title` (titre du livre)
  - `author` (auteur du livre)
  - `year` (année de publication)
- Méthodes :
  - `to_dict` : Convertit un objet `Book` en dictionnaire.
  - `from_dict` : Recrée un objet `Book` à partir d'un dictionnaire.

---

### 2. Implémenter les fonctionnalités suivantes

#### Afficher tous les livres

- Affiche chaque livre sous la forme :
  ```
  Titre - Auteur (Année)
  ```

#### Ajouter un livre

- Permet à l'utilisateur d'ajouter un nouveau livre :
  - Entrer le titre.
  - Entrer l'auteur.
  - Entrer l'année de publication.

#### Sauvegarder les livres

- Enregistre la liste mise à jour dans un fichier JSON.

#### Charger les livres

- Charge la liste depuis un fichier JSON.
