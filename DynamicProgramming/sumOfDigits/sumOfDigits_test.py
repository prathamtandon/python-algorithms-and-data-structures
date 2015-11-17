from sumOfDigits import sumOfDigitsFrom1ToN
import pytest

def test_sumOfDigitsFrom1ToN():
    n = 328
    output = 3241
    
    assert(sumOfDigitsFrom1ToN(n) == output)
    
    n = 5
    output = 15
    
    assert(sumOfDigitsFrom1ToN(n) == output)
