from checkBST import checkBST
import pytest

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def test_checkBST():
    node1 = Node(24)
    node2 = Node(18)
    node3 = Node(29)
    node1.left = node2
    node1.right = node3

    assert(checkBST(node1) == True)
