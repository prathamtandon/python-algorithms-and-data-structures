# The triangulation of a polygon is defined as dividing the polygon
# into smaller triangles such that no two diagonals of the polygon
# intersect. 
# The cost of traingulation is the total cost of all traingles formed
# after the triangulation. The cost of a traingle is just its perimeter.
# We need to find the min cost of triangulation.

# We can define this problem recursively as dividing the polygon into
# a triangle, the sub-polygon to left of triangle and the sub-polygon
# to right of triangle. The cost of triangulation is then sum
# of cost of left and right sub-polygons and cost of triangle.
from math import sqrt

def distance(p1,p2):
    return sqrt(pow(p1.x-p2.x,2) + pow(p1.y-p2.y,2))

def cost_triangle(points, i, j, k):
    p1 = points[i]
    p2 = points[j]
    p3 = points[k]
    
    return distance(p1,p2) + distance(p2,p3) + distance(p1,p3)
    
def minCostTriangulation (points, n):
    if n < 3:
        return 0.0
    
    # memo stores the results of subproblems. memo[i][j] stores
    # the cost of triangulation of points from i to j. We need
    # to return memo[0][n-1]
    memo = [[0 for i in range(n)] for i in range(n)]
    
    # fill the memo diagonally
    for gap in range(n):
        i = 0
        j = gap
        while j < n:
            if j < i + 2:
                memo[i][j] = 0
            else:
                memo[i][j] = float('inf')
                for k in range(i+1,j):
                    memo[i][j] = min(memo[i][j], memo[i][k] + memo[k][j] + cost_triangle(points,i,k,j))
            
            j += 1
            i += 1
    
    return memo[0][n-1]
