from calculatrice import *

def test_addition():
    assert addition(5, 3) == 8
    assert addition(-1, 1) == 0

def test_multiplication():
    assert multiplication(5, 3) == 15
    assert multiplication(5, 0) == 0

def test_soustraction():
    assert soustraction(10, 4) == 6
    assert soustraction(5, 5) == 0

def test_division():
    assert division(20, 4) == 5
    assert division(10, 2) == 5