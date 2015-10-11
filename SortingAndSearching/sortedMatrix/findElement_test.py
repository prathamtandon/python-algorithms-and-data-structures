from findElement import findElement
import pytest

def test_findElement():
    matrix = [[15,20,40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]]
    x = 55

    assert(findElement(matrix, x) == True)

    x = 110
    assert(findElement(matrix, x) == False)
