from simple_math import SimpleMath


def test_square_positive():
    assert SimpleMath().square(2) == 4


def test_square_negative():
    assert SimpleMath().square(-3) == 9


def test_square_zero():
    assert SimpleMath().square(0) == 0


def test_cube_positive():
    assert SimpleMath().cube(2) == 8


def test_cube_negative():
    assert SimpleMath().cube(-3) == -27


def test_cube_zero():
    assert SimpleMath().cube(0) == 0