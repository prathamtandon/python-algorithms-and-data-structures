from shortestPathKEdges import shortestPathKEdges
import pytest

def test_shortestPathKEdges():
    INF = float('inf')
    graph = [[0,10,3,2],[INF,0,INF,7],[INF,INF,0,6],[INF,INF,INF,0]]
    
    u = 0
    v = 3
    k = 2
    
    output = 9
    
    assert (shortestPathKEdges(graph,u,v,k) == output)
