from LinkedList import LinkedList
from partition import partition_list
import pytest

def verify_partition_output(head, x):
    assert(head is not None)
    cur = head
    less_than_x = True
    while cur is not None:
        if cur.get_key() < x:
            assert(less_than_x is True)
        else:
            less_than_x = False
        cur = cur.get_next()

def test_partition_list():
    lst = LinkedList()
    lst.insert(1)
    lst.insert(2)
    lst.insert(10)
    lst.insert(5)
    lst.insert(8)
    lst.insert(5)
    lst.insert(3)
    # 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
    verify_partition_output(partition_list(lst, 5), 5)
    verify_partition_output(partition_list(lst, 3), 3)


