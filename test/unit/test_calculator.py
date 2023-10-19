from calculator.calculator import add, subtract, multiply, divide
import pytest


def test_add():
    assert add(5, 3) == 8
    assert add(-2, 2) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(2, 5) == -3
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(2, -5) == -10
    assert multiply(0, 10) == 0


def test_divide():
    assert divide(8, 2) == 4
    assert divide(10, 2) == 5
    assert divide(7, 3) == 2.3333333333333335  # Approximate result

    # Testing division by zero with a context manager
    with pytest.raises(ValueError):
        divide(5, 0)
