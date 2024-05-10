import pytest
from my_math import *

def test_add():
    calculator = MathOperations(2,3)
    assert calculator.add() == 5

def test_sub():
    calculator = MathOperations(7,3)
    assert calculator.sub() == 4

def test_mult():
    calculator = MathOperations(7,3)
    assert calculator.sub() == 21

def test_div():
    calculator = MathOperations(8,2)
    assert calculator.div() == 4