# Given a binary tree, print boundary nodes of tree in anti-clockwise
# starting from root.
# The basic idea is:
# 1. Print the left boundary in top-down manner
# 2. Print all leaf nodes from left to right
#   2.1 Print all leaf nodes in left subtree from left to right
#   2.2 Print all leaf nodes in right subtree from left to right
# 3. Print the right boundary in bottom-up manner


def rightBoundaryTraversal(node, res):
        temp = []
        while node is not None:
                if node.left is None and node.right is None:
                        break
                temp.append(node.key)
                node = node.right
        temp = reversed(temp)
        res += temp

def leavesTraversal(node, res):
        if node is None:
                return
        if node.left is None and node.right is None:
                res.append(node.key)
        leavesTraversal(node.left, res)
        leavesTraversal(node.right, res)
                

def leftBoundaryTraversal(node, res):
        while node is not None:
                if node.left is None and node.right is None:
                        break
                res.append(node.key)
                node = node.left

def boundaryTraversal(root):
        res = []
        if root is not None:
                res.append(root.key)
                leftBoundaryTraversal(root.left, res)
                leavesTraversal(root.left, res)
                leavesTraversal(root.right, res)
                rightBoundaryTraversal(root.right, res)
        
        return res
                
