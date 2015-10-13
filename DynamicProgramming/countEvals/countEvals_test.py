from countEvals import countEvals
import pytest

def test_countEvals():
    expr = '1^0|0|1'
    result = False
    hashmap = {}

    assert(countEvals(expr, result, hashmap) == 2)

    expr = '0&0&0&1^1|0'
    result = True
    hashmap = {}

    assert(countEvals(expr, result, hashmap) == 10)
