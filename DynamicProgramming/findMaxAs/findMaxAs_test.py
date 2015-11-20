from findMaxAs import findMaxAs
import pytest

def test_findMaxAs():
    n = 6
    output = 6
    assert(findMaxAs(n) == output)
    
    n = 7
    output = 9
    assert(findMaxAs(n) == output)
    
    n = 11
    output = 27
    assert(findMaxAs(n) == output)
    
    
    n = 20
    output = 324
    assert(findMaxAs(n) == output)
