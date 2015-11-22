# A vertex cover of an undirected graph is a subset of its vertices
# such that for every edge (u,v) of the graph, either u or v is inta
# vertex cover. Although the name is vertex cover, the set covers all
# edges of given graph.
# The problem to find minimum size vertex cover for a graph is NP
# complete. But it can be solved in polynomial time for trees.

# The idea is to recursively consider following two points for the 
# root and then all nodes downwards:
# 1. Root is part of vertex cover - We recursively compute the sizes
# of vertex cover for left and right subtrees and then add 1 for the
# root.
# 2. Root is not part of vertex cover - We recursively compute the sizes
# of vertex cover for grandchildren of root and then add 2 for the left
# and right child nodes of root.

# In following implementation, we have an additional field 'vc'. 'vc' is
# set to 0 for all nodes initially. The value of 'vc' is computed
# only if it is zero.

def vCover (root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 0
    
    if root.vc != 0:
        return root.vc
    
    # size including root
    size_incl = 1 + vCover (root.left) + vCover (root.right)
    
    size_excl = 0
    if root.left is not None:
        size_excl += 1 + vCover (root.left.left) + vCover (root.left.right)
    
    if root.right is not None:
        size_excl += 1 + vCover (root.right.left) + vCover (root.right.right)
    
    
    root.vc = min(size_incl, size_excl)

    return root.vc
