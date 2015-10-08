from getPath import Point
from getPath import getPath

def test_getPath():
    maze = [[True, True, True], [True, False, False], [True, False, True], [False, True, True]]
    assert(getPath(maze) is None)
    maze = [[True, True, True], [True, False, False], [True, True, True], [False, True, True]]
    path = getPath(maze)
    assert(len(path) == 6)
    assert(Point(0,0) in path)
    assert(Point(1,0) in path)
    assert(Point(2,0) in path)
    assert(Point(2,1) in path)
    assert(Point(2,2) in path or Point(3,1) in path)
    assert(Point(3,2) in path)
