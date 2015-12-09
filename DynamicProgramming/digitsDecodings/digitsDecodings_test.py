from digitsDecodings import countDecodings
import pytest

def test_countDecodings ():
    digits = "1234"
    # The possible decodings are "ABCD", "LCD", "AWD"
    output = 3
    
    assert(countDecodings(digits) == output)

    digits = "121"
    output = 3

    assert(countDecodings(digits) == output)

