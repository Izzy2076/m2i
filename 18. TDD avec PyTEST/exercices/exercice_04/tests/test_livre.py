import pytest
from src.classes.Livre import Livre


def test_creation_livre():
    """Test la création d'un livre avec tous ses attributs"""
    livre = Livre("1984", "George Orwell", "978-0451524935")
    assert livre.titre == "1984"
    assert livre.auteur == "George Orwell"
    assert livre.isbn == "978-0451524935"


def test_livre_disponible_par_defaut():
    """Test qu'un livre est disponible par défaut"""
    livre = Livre("1984", "George Orwell", "978-0451524935")
    assert livre.disponible is True


def test_emprunt_livre_disponible():
    """Test l'emprunt d'un livre disponible"""
    livre = Livre("1984", "George Orwell", "978-0451524935")
    resultat = livre.emprunter()
    assert resultat is True
    assert livre.disponible is False


def test_emprunt_livre_deja_emprunte():
    """Test l'impossibilité d'emprunter un livre déjà emprunté"""
    livre = Livre("1984", "George Orwell", "978-0451524935")
    livre.emprunter()
    resultat = livre.emprunter()
    assert resultat is False
    assert livre.disponible is False


def test_retour_livre_emprunte():
    """Test le retour d'un livre emprunté"""
    livre = Livre("1984", "George Orwell", "978-0451524935")
    livre.emprunter()
    resultat = livre.retourner()
    assert resultat is True
    assert livre.disponible is True


def test_retour_livre_deja_disponible():
    """Test l'impossibilité de retourner un livre déjà disponible"""
    livre = Livre("1984", "George Orwell", "978-0451524935")
    resultat = livre.retourner()
    assert resultat is False
    assert livre.disponible is True


def test_get_info():
    """Test que get_info() retourne le bon format"""
    livre = Livre("1984", "George Orwell", "978-0451524935")
    info = livre.get_info()
    assert info == "1984 par George Orwell (ISBN: 978-0451524935)"