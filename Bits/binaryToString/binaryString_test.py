from binaryString import printBinary
import pytest

def test_printBinary():
    num = 0.625
    assert(printBinary(num) == '.101')

