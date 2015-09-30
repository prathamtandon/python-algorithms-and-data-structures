from isBalanced import isBalanced
from isBalanced import isBalanced_better
import pytest

class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def test_isBalanced():
        node1 = Node(24)
        node2 = Node(15)
        node3 = Node(36)
        node4 = Node(11)
        node5 = Node(17)

        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5

        assert(isBalanced(node1) == True)
        assert(isBalanced_better(node1) == True)

    def test_isnotBalanced():
        node1 = Node(24)
        node2 = Node(15)
        node3 = Node(36)
        node4 = Node(48)
        node5 = Node(54)
        node6 = Node(77)

        node1.left = node2
        node1.right = node3
        node3.right = node4
        node4.right = node5
        node5.right = node6

        assert(isBalanced(node1) == False)
        assert(isBalanced_better(node1) == False)
