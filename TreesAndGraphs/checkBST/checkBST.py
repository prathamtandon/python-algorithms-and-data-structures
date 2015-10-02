# Implement a function to check if a binary tree is a BST

# One way is to implement an inorder traversel and check if its in
# sorted order.

def checkBST(node):
    return checkBST_helper(node, -float('Inf'), float('Inf'))

def checkBST_helper(node, minimum, maximum):
    if node is None:
        return True
    if not (minimum <= node.key <= maximum):
        return False
    return checkBST_helper(node.left, minimum, node.key) and checkBST_helper(node.right, node.key, maximum)
