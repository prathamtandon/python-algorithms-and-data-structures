from countNonDecreasing import countNonDecreasing
import pytest

def test_countNonDecreasing():
        n = 3
        output = 220
        
        assert(countNonDecreasing(n) == output)
