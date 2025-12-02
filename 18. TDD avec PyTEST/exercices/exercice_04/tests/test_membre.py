import pytest
from src.classes.Membre import Membre
from src.classes.Livre import Livre


def test_creation_membre():
    """Test la création d'un membre avec tous ses attributs"""
    membre = Membre("Dupont", "Jean", "M001")
    assert membre.nom == "Dupont"
    assert membre.prenom == "Jean"
    assert membre.numero_membre == "M001"


def test_liste_emprunts_vide_par_defaut():
    """Test que la liste de livres empruntés est vide par défaut"""
    membre = Membre("Dupont", "Jean", "M001")
    assert membre.livres_empruntes == []


def test_limite_emprunts_par_defaut():
    """Test que la limite d'emprunts est de 3 par défaut"""
    membre = Membre("Dupont", "Jean", "M001")
    assert membre.limite_emprunts == 3


def test_membre_peut_emprunter_livre():
    """Test qu'un membre peut emprunter un livre"""
    membre = Membre("Dupont", "Jean", "M001")
    livre = Livre("1984", "George Orwell", "978-0451524935")
    resultat = membre.emprunter_livre(livre)
    assert resultat is True
    assert livre in membre.livres_empruntes


def test_nombre_emprunts_augmente():
    """Test que le nombre d'emprunts augmente"""
    membre = Membre("Dupont", "Jean", "M001")
    livre1 = Livre("1984", "George Orwell", "978-0451524935")
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "978-2070408504")
    
    membre.emprunter_livre(livre1)
    assert membre.get_nombre_emprunts() == 1
    
    membre.emprunter_livre(livre2)
    assert membre.get_nombre_emprunts() == 2


def test_membre_ne_peut_pas_depasser_limite():
    """Test qu'un membre ne peut pas emprunter plus de 3 livres"""
    membre = Membre("Dupont", "Jean", "M001")
    livre1 = Livre("1984", "George Orwell", "978-0451524935")
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "978-2070408504")
    livre3 = Livre("Harry Potter", "J.K. Rowling", "978-0747532699")
    livre4 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", "978-0618640157")
    
    membre.emprunter_livre(livre1)
    membre.emprunter_livre(livre2)
    membre.emprunter_livre(livre3)
    resultat = membre.emprunter_livre(livre4)
    
    assert resultat is False
    assert membre.get_nombre_emprunts() == 3


def test_peut_emprunter_retourne_false_a_la_limite():
    """Test que peut_emprunter() retourne False quand la limite est atteinte"""
    membre = Membre("Dupont", "Jean", "M001")
    livre1 = Livre("1984", "George Orwell", "978-0451524935")
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "978-2070408504")
    livre3 = Livre("Harry Potter", "J.K. Rowling", "978-0747532699")
    
    assert membre.peut_emprunter() is True
    
    membre.emprunter_livre(livre1)
    membre.emprunter_livre(livre2)
    membre.emprunter_livre(livre3)
    
    assert membre.peut_emprunter() is False


def test_membre_peut_retourner_livre():
    """Test qu'un membre peut retourner un livre emprunté"""
    membre = Membre("Dupont", "Jean", "M001")
    livre = Livre("1984", "George Orwell", "978-0451524935")
    
    membre.emprunter_livre(livre)
    resultat = membre.retourner_livre(livre)
    
    assert resultat is True
    assert livre not in membre.livres_empruntes


def test_nombre_emprunts_diminue_apres_retour():
    """Test que le nombre d'emprunts diminue après un retour"""
    membre = Membre("Dupont", "Jean", "M001")
    livre1 = Livre("1984", "George Orwell", "978-0451524935")
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "978-2070408504")
    
    membre.emprunter_livre(livre1)
    membre.emprunter_livre(livre2)
    assert membre.get_nombre_emprunts() == 2
    
    membre.retourner_livre(livre1)
    assert membre.get_nombre_emprunts() == 1


def test_ne_peut_pas_retourner_livre_non_emprunte():
    """Test qu'on ne peut pas retourner un livre non emprunté"""
    membre = Membre("Dupont", "Jean", "M001")
    livre = Livre("1984", "George Orwell", "978-0451524935")
    
    resultat = membre.retourner_livre(livre)
    assert resultat is False


def test_get_nom_complet():
    """Test que get_nom_complet() retourne le bon format"""
    membre = Membre("Dupont", "Jean", "M001")
    assert membre.get_nom_complet() == "Jean Dupont"