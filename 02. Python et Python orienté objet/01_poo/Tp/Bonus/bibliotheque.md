# **Exercice : Gestion d’une bibliothèque**

### **1. Classe de base : `Media`**

- **Attributs** :
  - `titre` (str)
  - `auteur` (str)
  - `année` (int)
  - `disponible` (bool, par défaut `True`)
- **Méthodes** :
  - `afficher_informations()` : Affiche les informations du média.
  - `changer_disponibilite()` : Met à jour la disponibilité (True/False).

---

### **2. Sous-classes de `Media`**

- **Livre** :
  - **Attributs supplémentaires** : `nombre_de_pages` (int)
- **DVD** :
  - **Attributs supplémentaires** : `durée` (int, en minutes)
- **Magazine** :
  - **Attributs supplémentaires** : `édition` (str)

Chaque sous-classe doit redéfinir la méthode `afficher_informations()` pour inclure ses attributs spécifiques.

---

### **3. Classe `Membre`**

- **Attributs** :
  - `nom` (str)
  - `identifiant` (int)
  - `medias_empruntes` (list)
- **Méthodes** :
  - `emprunter_media(media)` : Ajoute un média à la liste des emprunts et met à jour la disponibilité du média.
    - Si le média n’est pas disponible, lever une exception personnalisée `MediaIndisponibleException`.
  - `rendre_media(media)` : Retire un média de la liste des emprunts et met à jour sa disponibilité.
  - `afficher_emprunts()` : Liste tous les médias empruntés par le membre.

---

### **4. Classe `Bibliothèque`**

- **Attributs** :
  - `catalogue` (list de médias)
  - `membres` (list de membres)
- **Méthodes** :
  1. **Gestion des médias** :
     - `ajouter_media(media)` : Ajoute un média au catalogue.
     - `afficher_catalogue()` : Affiche tous les médias (disponibles et indisponibles).
  2. **Gestion des membres** :
     - `ajouter_membre(membre)` : Ajoute un nouveau membre à la bibliothèque.
     - `trouver_membre(identifiant)` : Recherche un membre par son identifiant.
  3. **Gestion des emprunts** :
     - `emprunter_media(identifiant_membre, titre_media)` : Gère l'emprunt d’un média par un membre.
     - `rendre_media(identifiant_membre, titre_media)` : Gère le retour d’un média emprunté.

### **5. Exceptions personnalisées**

- **`MediaIndisponibleException`** : Levée lorsque l’emprunt d’un média indisponible est tenté.
- **`MembreInexistantException`** : Levée lorsque l’identifiant d’un membre n’est pas trouvé.
- **`MediaNonEmprunteException`** : Levée lorsqu’un membre tente de retourner un média qu’il n’a pas emprunté.

## Bonus

1. **Interface utilisateur** :
   - Créez une interface en ligne de commande pour interagir avec la bibliothèque. Par exemple :
     ```
     [1] Ajouter un média
     [2] Ajouter un membre
     [3] Emprunter un média
     [4] Rendre un média
     [5] Afficher le catalogue
     ```
