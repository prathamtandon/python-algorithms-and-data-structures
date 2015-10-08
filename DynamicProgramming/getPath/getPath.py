# Given a robot starting at top-left corner of a maze with r rows and
# c columns, find a path for the robot to bottom-right corner of the
# maze, given that certain cells in the maze are "off-limits".

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y
    def __hash__(self):
		return hash((self.x, self.y))

def getPath(maze):
    if maze is None or len(maze) == 0:
        return None
    r = len(maze)
    c = len(maze[0])
    path = []
    cache = {}
    if getPath_helper(Point(r-1,c-1), maze, path, cache):
        return path
    else:
        return None

def getPath_helper(location, maze, path, cache):
    x = location.x
    y = location.y
    if x < 0 or y < 0 or not maze[x][y]:
        return False
    if location in cache:
        return cache[location]
    if location == Point(0,0) or getPath_helper(Point(x-1,y), maze, path, cache) or getPath_helper(Point(x, y-1), maze, path, cache):
        cache[location] = True
        path.insert(0, location)
        return True
    cache[location] = False
    return False


