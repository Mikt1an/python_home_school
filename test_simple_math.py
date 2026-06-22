import pytest
from simple_math import SimpleMath


@pytest.fixture
def math():
    return SimpleMath()

def test_square_positive(math):
    assert math.square(2) == 4


def test_square_negative(math):
    assert math.square(-3) == 9


def test_square_zero(math):
    assert math.square(0) == 0


def test_cube_positive(math):
    assert math.cube(2) == 8


def test_cube_negative(math):
    assert math.cube(-3) == -27


def test_cube_zero(math):
    assert math.cube(0) == 0
