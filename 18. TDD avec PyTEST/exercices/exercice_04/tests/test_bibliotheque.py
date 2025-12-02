import pytest
from src.classes.Bibliotheque import Bibliotheque
from src.classes.Livre import Livre
from src.classes.Membre import Membre


def test_creation_bibliotheque():
    """Test la création d'une bibliothèque"""
    biblio = Bibliotheque("Bibliothèque Municipale")
    assert biblio.nom == "Bibliothèque Municipale"


def test_listes_vides_au_debut():
    """Test que les listes de livres et membres sont vides au début"""
    biblio = Bibliotheque("Bibliothèque Municipale")
    assert biblio.livres == []
    assert biblio.membres == []


def test_ajout_livres():
    """Test l'ajout de livres"""
    biblio = Bibliotheque("Bibliothèque Municipale")
    livre1 = Livre("1984", "George Orwell", "978-0451524935")
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "978-2070408504")
    
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    
    assert len(biblio.livres) == 2
    assert livre1 in biblio.livres
    assert livre2 in biblio.livres


def test_ajout_membres():
    """Test l'ajout de membres"""
    biblio = Bibliotheque("Bibliothèque Municipale")
    membre1 = Membre("Dupont", "Jean", "M001")
    membre2 = Membre("Martin", "Marie", "M002")
    
    biblio.ajouter_membre(membre1)
    biblio.ajouter_membre(membre2)
    
    assert len(biblio.membres) == 2
    assert membre1 in biblio.membres
    assert membre2 in biblio.membres


def test_recherche_livre_par_isbn():
    """Test la recherche de livre par ISBN"""
    biblio = Bibliotheque("Bibliothèque Municipale")
    livre1 = Livre("1984", "George Orwell", "978-0451524935")
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "978-2070408504")
    
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    
    livre_trouve = biblio.trouver_livre_par_isbn("978-2070408504")
    assert livre_trouve == livre2
    assert livre_trouve.titre == "Le Petit Prince"


def test_recherche_livre_inexistant():
    """Test la recherche d'un livre inexistant"""
    biblio = Bibliotheque("Bibliothèque Municipale")
    livre = Livre("1984", "George Orwell", "978-0451524935")
    biblio.ajouter_livre(livre)
    
    livre_trouve = biblio.trouver_livre_par_isbn("999-9999999999")
    assert livre_trouve is None


def test_recherche_membre_par_numero():
    """Test la recherche de membre par numéro"""
    biblio = Bibliotheque("Bibliothèque Municipale")
    membre1 = Membre("Dupont", "Jean", "M001")
    membre2 = Membre("Martin", "Marie", "M002")
    
    biblio.ajouter_membre(membre1)
    biblio.ajouter_membre(membre2)
    
    membre_trouve = biblio.trouver_membre_par_numero("M002")
    assert membre_trouve == membre2
    assert membre_trouve.get_nom_complet() == "Marie Martin"


def test_recherche_membre_inexistant():
    """Test la recherche d'un membre inexistant"""
    biblio = Bibliotheque("Bibliothèque Municipale")
    membre = Membre("Dupont", "Jean", "M001")
    biblio.ajouter_membre(membre)
    
    membre_trouve = biblio.trouver_membre_par_numero("M999")
    assert membre_trouve is None


def test_liste_livres_disponibles():
    """Test que la liste des livres disponibles est correcte"""
    biblio = Bibliotheque("Bibliothèque Municipale")
    livre1 = Livre("1984", "George Orwell", "978-0451524935")
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "978-2070408504")
    livre3 = Livre("Harry Potter", "J.K. Rowling", "978-0747532699")
    
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    biblio.ajouter_livre(livre3)
    
    # Tous les livres sont disponibles
    livres_disponibles = biblio.get_livres_disponibles()
    assert len(livres_disponibles) == 3
    
    # On emprunte un livre
    livre2.emprunter()
    livres_disponibles = biblio.get_livres_disponibles()
    assert len(livres_disponibles) == 2
    assert livre2 not in livres_disponibles
    assert livre1 in livres_disponibles
    assert livre3 in livres_disponibles