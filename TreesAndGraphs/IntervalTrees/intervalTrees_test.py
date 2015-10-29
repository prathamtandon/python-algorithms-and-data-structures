from intervalTrees import Interval, IntervalTreeNode
import pytest

def test_intervalTrees():
    node1 = IntervalTreeNode(Interval(16,21))

    node1.insert(Interval(8,9))
    node1.insert(Interval(25,30))
    node1.insert(Interval(8,9))
    node1.insert(Interval(5,8))
    node1.insert(Interval(15,23))
    node1.insert(Interval(17,19))
    node1.insert(Interval(26,26))
    node1.insert(Interval(0,3))
    node1.insert(Interval(6,10))
    node1.insert(Interval(19,20))

    assert(node1.search(Interval(23,25)) is None)
    assert(node1.search(Interval(2,4)).interval == Interval(0,3))
