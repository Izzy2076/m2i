import pytest
from src.classes.Utilisateur import Utilisateur

@pytest.fixture()
def utilisateur_majeur():
    return Utilisateur("Toto", "Tata", 19)

@pytest.fixture()
def utilisateur_mineur():
    return Utilisateur("Toto", "Tata", 17)

def test_nom_complet(utilisateur_majeur):
    assert utilisateur_majeur.nom_complet() == "Tata Toto"

def test_est_majeur_true(utilisateur_majeur):
    assert utilisateur_majeur.est_majeur() == True


def test_est_majeur_false(utilisateur_mineur):
    assert utilisateur_mineur.est_majeur() == False