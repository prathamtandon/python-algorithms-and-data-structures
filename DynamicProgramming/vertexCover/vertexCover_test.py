from vertexCover import vCover
import pytest

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.vc = 0

def test_vCover():
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    
    output = 3
    
    assert (vCover(root) == output)
