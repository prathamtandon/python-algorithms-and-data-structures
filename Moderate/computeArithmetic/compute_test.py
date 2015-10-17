from compute import compute
import pytest

def test_compute():
    sequence = '3+6*2'
    result = 15

    assert(compute(sequence) == result)

    sequence = '2*3+5/6*3+15'
    result = 23.5

    assert(compute(sequence) == result)
