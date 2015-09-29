# Given a sorted array with unique integer elements, create a BST
# with minimal height

class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def createMinimalBST(items):
    return createMinimalBST_helper(items, 0, len(items) - 1)

def createMinimalBST_helper(items, start, end):
    if start > end:
        return None

    mid = (start + end) / 2
    root = Node(items[mid])
    root.left = createMinimalBST_helper(items, start, mid - 1)
    root.right = createMinimalBST_helper(items, mid + 1, end)
    return root
