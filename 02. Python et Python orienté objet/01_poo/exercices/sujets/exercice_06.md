# Exercice : Gestion des employés dans une entreprise

## Instructions

### 1. Créer une classe `Employe`

- **Attributs** :
  - `nom` (str) : le nom de l'employé.
  - `salaire` (float) : le salaire de l'employé.
  - `id_employe` (int) : un identifiant unique généré automatiquement pour chaque employé.
- **Méthodes** :
  - `__init__` : initialise les attributs (l'`id_employe` est généré à partir d'un compteur de classe).
  - `presentation` : affiche une phrase décrivant l'employé, par exemple :  
    _"Je suis [nom], mon ID est [id_employe], et mon salaire est de [salaire] €."_
  - `augmenter_salaire(pourcentage)` : augmente le salaire de l'employé d'un pourcentage donné.

---

### 2. Créer deux sous-classes `Manager` et `Technicien`

#### Classe `Manager`

- **Attributs supplémentaires** :
  - `equipe` (list) : une liste contenant les objets des employés sous sa supervision.
- **Méthodes supplémentaires** :
  - `ajouter_employe(employe)` : ajoute un objet `Employe` (ou ses sous-classes) à l'équipe.
  - `presentation` : affiche une description du manager et le nombre de personnes dans son équipe, par exemple :  
    _"Je suis [nom], manager. Mon ID est [id_employe]. Je supervise une équipe de [nombre] personnes et mon salaire est de [salaire] €."_  
    **Bonus** : Inclure les noms des employés supervisés dans la présentation.

#### Classe `Technicien`

- **Attribut supplémentaire** :
  - `specialite` (str) : la spécialité technique de l'employé.
- **Méthodes supplémentaires** :
  - `changer_specialite(nouvelle_specialite)` : change la spécialité du technicien.
  - `presentation` : affiche une description du technicien avec sa spécialité, par exemple :  
    _"Je suis [nom], technicien spécialisé en [specialite]. Mon ID est [id_employe] et mon salaire est de [salaire] €."_

---

### 3. Ajouter des fonctionnalités avancées

- **Gestion des salaires** :
  - Créer une méthode de classe dans `Employe` appelée `total_salaire(liste_employes)` qui calcule et retourne la somme des salaires d'une liste d'employés.
- **Filtrage par rôle** :
  - Ajouter une méthode `filtrer_par_role(liste_employes, role)` (hors des classes) pour retourner une liste d'employés appartenant à un rôle donné (par exemple, `Manager` ou `Technicien`).
