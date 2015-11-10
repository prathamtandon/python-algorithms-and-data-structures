from linearEquation import countSolnOptimized
import pytest

def test_linearEquation():
        coefficient = [2,2,5]
        rhs = 4
        output = 3
        
        assert(countSolnOptimized(coefficient, len(coefficient), rhs) == output)
