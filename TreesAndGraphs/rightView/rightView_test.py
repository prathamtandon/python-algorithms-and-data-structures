from rightView import rightView
import pytest

class Node:
        def __init__(self,key):
                self.key = key
                self.left = None
                self.right = None

def test_rightView():
        root = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        node8 = Node(8)
        
        root.left = node2
        root.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node6.left = node7
        node7.right = node8
        
        output = [1,3,6,7,8]
        
        assert(rightView(root) == output)
