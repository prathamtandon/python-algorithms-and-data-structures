# Given a directed, weighted graph, and a source vertex 'u' and
# target vertex 'v', find the shortest path between u and v with
# exactly k edges.

def shortestPathKEdges (graph, u, v, k):
    V = len(graph)
    
    # let memo[i][j][k] denote the shortest path length from
    # i to j of length exactly k
    memo = [[[0 for i in range(k+1)] for i in range(V)] for i in range(V)]
    
    for num_edges in range(k+1):
        for src in range(V):
            for dest in range(V):
                memo[src][dest][num_edges] = float('inf')
                
                if num_edges == 0 and src == dest:
                    memo[src][dest][num_edges] = 0
                if num_edges == 1 and graph[src][dest] != float('inf'):
                    memo[src][dest][num_edges] = graph[src][dest]
                
                if num_edges > 1:
                    for adjacent in range(V):
                        if graph[src][adjacent] != float('inf') and adjacent not in [src,dest] and memo[adjacent][dest][num_edges-1] != float('inf'):
                            memo[src][dest][num_edges] = min(memo[src][dest][num_edges], graph[src][adjacent] + memo[adjacent][dest][num_edges-1])
    
    
    
    return memo[u][v][k]
                
                
                
                
