import pytest
from src.main import additionner, diviser

def test_additionner_nombres_positifs():
    # Arrange

    a, b = 3, 5

    # Act 
    result = additionner(a, b)

    # Assert
    assert result == 8

def test_additionner_nombres_negatifs():
    # Arrange
    a, b = -2, -3

    # Act 
    result = additionner(a, b)

    # Assert
    assert result == -5

def test_diviser_nombres_valides():
    # Arrange
    a, b = 10, 2

    # Act 
    result = diviser(a, b)

    # Assert
    assert result == 5

def test_diviser_par_zero():
    a, b = 10, 0
    with pytest.raises(ValueError, match="Division par zéro impossible"):
        diviser(a,b)