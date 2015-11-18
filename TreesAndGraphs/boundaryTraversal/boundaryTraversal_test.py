from boundaryTraversal import boundaryTraversal
import pytest

class Node:
        def __init__(self, key):
                self.key = key
                self.left = None
                self.right = None

def test_boundaryTraversal():
        root = Node(20)
        node8 = Node(18)
        node22 = Node(21)
        node4 = Node(4)
        node12 = Node(12)
        node25 = Node(25)
        node10 = Node(10)
        node14 = Node(14)
        
        root.left = node8
        root.right = node22
        node8.left = node4
        node8.right = node12
        node22.right = node25
        node12.left = node10
        node12.right = node14
        
        output  = [20,18,4,10,14,25,21]
        
        assert(boundaryTraversal(root) == output)
