from arithmetic import minus, multiply, divide
import pytest

def test_minus():

    assert(minus(0,0) == 0)
    assert(minus(10,0) == 10)
    assert(minus(0,10) == -10)
    assert(minus(14,7) == 7)
    assert(minus(25,28) == -3)

def test_multiply():

    assert(multiply(0,10) == 0)
    assert(multiply(10,0) == 0)
    assert(multiply(2,2) == 4)
    assert(multiply(5,10) == 50)
    assert(multiply(12,-2) == -24)
    assert(multiply(-3,4) == -12)
    assert(multiply(-2,-8) == 16)


def test_divide():

    assert(divide(0,5) == 0)
    assert(divide(-5,2) == -2)
    assert(divide(12,-2) == -6)
    assert(divide(-40,-6) == 6)
    assert(divide(12,22) == 0)
    assert(divide(24,12) == 2)


