from mobileKeypad import mobileKeypad
import pytest

def test_mobileKeypad ():
    n = 2
    output = 36
    
    assert (mobileKeypad (n) == output)
    
    n = 4
    output = 532
    
    assert (mobileKeypad (n) == output)
    
    n = 5
    output = 2062
    
    assert (mobileKeypad (n) == output)
