from LinkedListPerLevel import LinkedListPerLevel
from LinkedListPerLevel import LinkedListPerLevel_r
from LinkedListPerLevel import Node
import pytest

def test_LinkedListPerLevel():
    node1 = Node(24)
    node2 = Node(15)
    node3 = Node(35)
    node4 = Node(20)
    node5 = Node(32)
    node6 = Node(40)

    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.left = node5
    node3.right = node6

    '''
        24
       /  \
      15  35
       \  / \
       20 32 40
    '''

    result = LinkedListPerLevel(node1)
    assert(len(result) == 3)
    assert(map(lambda x: x.key, result[0]) == [24])
    assert(map(lambda x: x.key, result[1]) == [15, 35])
    assert(map(lambda x: x.key, result[2]) == [20, 32, 40])


def test_LinkedListPerLevel_r():
    node1 = Node(24)
    node2 = Node(15)
    node3 = Node(35)
    node4 = Node(20)
    node5 = Node(32)
    node6 = Node(40)

    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.left = node5
    node3.right = node6

    result = []
    LinkedListPerLevel_r(node1, 0, result)
    assert(len(result) == 3)
    #assert(map(lambda x: x.key, result[0]) == [24])
    assert(map(lambda x: x.key, result[1]) == [15, 35])
    assert(map(lambda x: x.key, result[2]) == [20, 32, 40])

