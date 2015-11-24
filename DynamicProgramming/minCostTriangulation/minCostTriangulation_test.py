from minCostTriangulation import minCostTriangulation
import pytest

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def test_minCostTriangulation ():
    points = [Point(0.0,0.0),Point(1.0,0.0),Point(2.0,1.0),Point(1.0,2.0),Point(0.0,2.0)]
    expected = 15.3006
    actual = minCostTriangulation (points, len(points))
    epsilon = 0.001
    
    assert(abs(actual-expected) < epsilon)
    
    
