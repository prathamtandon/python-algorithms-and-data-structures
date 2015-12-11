from rodCutting import ropeCutting
import pytest

def test_ropeCutting ():
    n = 10
    output = 36
    
    assert (ropeCutting (n) == output)
