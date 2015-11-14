from verticalTraversal import printVerticalOrder
import pytest

class Node:
        def __init__(self,key):
                self.key = key
                self.left = None
                self.right = None

def test_printVerticalOrder():
        root = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        node8 = Node(8)
        node9 = Node(9)
        
        root.left = node2
        root.right = node3
        
        node2.left = node4
        node2.right = node5
        
        node3.left = node6
        node3.right = node7
        node6.right = node8
        node7.right = node9
        
        output = [[4],[2],[1,5,6],[3,8],[7],[9]]
        assert(sorted(printVerticalOrder(root)) == sorted(output)) 
        
