from diameterOfTree import diameter
import pytest

class Node:
    def __init__(self,left=None,right=None):
        self.left = left
        self.right = right

def test_diameter():
    nodes = []
    for i in range(13):
        nodes.append(Node())

    nodes[0].left = nodes[1]
    nodes[0].right = nodes[6]
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]
    nodes[3].left = nodes[4]
    nodes[3].right = nodes[5]
    nodes[6].right = nodes[7]
    nodes[7].right = nodes[8]
    nodes[8].left = nodes[9]
    nodes[8].right = nodes[10]
    nodes[9].left = nodes[11]
    nodes[9].right = nodes[12]

    res = diameter(nodes[0])

    assert(res['diameter'] == 9)
