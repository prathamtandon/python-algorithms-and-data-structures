from allSequences import allSequences
import pytest

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def allSequences_test():
    node1 = Node(2)
    node2 = Node(1)
    node3 = Node(3)

    node1.left = node2
    node1.right = node3

    sequences = allSequences(node1)

    assert(sequences[0] == [2, 1, 3])
    assert(sequences[1] == [2, 3, 1])

    node1 = Node(20)
    node2 = Node(10)
    node3 = Node(25)
    node4 = Node(5)
    node5 = Node(15)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    '''
            20
           / \
          10  25
         / \
        5  15
    '''

    sequences = allSequences(node1)
    assert(len(sequences) == 8)
    assert([20,25,10,5,15] in sequences)
    assert([20,25,5,10,15] in sequences)
    assert([20,25,5,15,10] in sequences)
    assert([20,10,25,5,15] in sequences)
    assert([20,25,10,15,5] in sequences)
    assert([20,25,15,10,5] in sequences)
    assert([20,25,15,5,10] in sequences)
    assert([20,10,25,15,5] in sequences)

