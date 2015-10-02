from containsTree import containsTree
import pytest

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def test_containsTree_match():
    node11 = Node(10)
    node12 = Node(5)
    node13 = Node(15)
    node14 = Node(3)
    node15 = Node(7)
    node16 = Node(17)

    node11.left = node12
    node11.right = node13
    node12.left = node14
    node12.right = node15
    node13.right = node16


    node21 = Node(15)
    node22 = Node(17)

    node21.right = node22

    '''
        T1:     10
               /  \
              5    15
             /\      \
            3  7      17

        T2:     15
                 \
                 17
    '''

    assert(containsTree(node11, node21) == True)

def test_containsTree_no_match():
    node11 = Node(10)
    node12 = Node(5)
    node13 = Node(15)
    node14 = Node(3)
    node15 = Node(7)
    node16 = Node(17)

    node11.left = node12
    node11.right = node13
    node12.left = node14
    node12.right = node15
    node13.right = node16


    node21 = Node(15)
    node22 = Node(17)

    node21.left = node22

    '''
        T1:     10
               /  \
              5    15
             /\      \
            3  7      17

        T2:     15
                /
               17
    '''
    assert(containsTree(node11, node21) == False)
