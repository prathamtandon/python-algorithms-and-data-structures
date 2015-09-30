# Implement a function to check if a binary tree is balanced.
# Heights of the two subtrees at any node never differ by more than 1.

def getHeight(node):
    if node is None:
        return 0
    return max(getHeight(node.left), getHeight(node.right)) + 1

def isBalanced(node):
    if node is None:
        return True
    return isBalanced(node.right) and isBalanced(node.left) and abs(getHeight(node.right) - getHeight(node.left)) <= 1

def checkHeight(node):
    if node is None:
        return 0

    leftHeight = checkHeight(node.left)
    if leftHeight == -1:
        return -1

    rightHeight = checkHeight(node.right)
    if rightHeight == -1:
        return -1

    if abs(leftHeight - rightHeight) > 1:
        return -1

    return max(leftHeight, rightHeight) + 1

def isBalanced_better(root):
    return not (checkHeight(root) == -1)


