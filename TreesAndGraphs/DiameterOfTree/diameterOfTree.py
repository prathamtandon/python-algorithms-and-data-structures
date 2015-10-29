# Diameter of binary tree is defined as number of nodes on the longest path
# between two leaves of a tree.

# Diameter of tree is largest of following quantities:
# 1. Diameter of T's left subtree
# 2. Diameter of T's right subtree
# 3. The longest path between leaves that goes through the root of T.

def diameter(root):
    if root is None:
        return { 'height': 0, 'diameter': 0 }

    l_result = diameter(root.left)
    r_result = diameter(root.right)

    res = {}
    res['height'] = max(l_result['height'], r_result['height']) + 1
    res['diameter'] = max(l_result['height'] + r_result['height'] + 1, l_result['diameter'], r_result['diameter'])

    return res

