from findSquare import findSquare
import pytest

def test_findSquare():
    matrix = [[1,0,1],[0,0,1],[0,0,1]]
    result = findSquare(matrix)

    assert(result is not None)
    assert(result.size == 2)
    assert(result.row == 1)
    assert(result.col == 0)
