from findBestLine import Point,Line,findBestLine
import pytest

def test_findBestLine():
    points = [Point(1,3),Point(2,4),Point(4,6),Point(5,3),Point(-2,3)]
    bestLine = findBestLine(points)

    assert(bestLine.slope == 0)
    assert(bestLine.intercept == 3)
    assert(bestLine.infinite_slope == False)

