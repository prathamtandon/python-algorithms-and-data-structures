from substrEqualSum import substrEqualSum
import pytest

def test_substrEqualSum ():
    string = '1538023'
    output = 4
    
    assert(substrEqualSum (string) == output)
    
    string = '220112'
    output = 6
    
    assert(substrEqualSum (string) == output)
