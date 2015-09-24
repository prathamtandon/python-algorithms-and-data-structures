from LinkedList import LinkedList
from kthToLast import kthToLast
import pytest

def test_kthToLast():
    lst = LinkedList()
    lst.insert("Batman")
    lst.insert("Superman")
    lst.insert("Flash")
    lst.insert("Green Lantern")
    lst.insert("Wonder Woman")
    lst.insert("Hawkgirl")
    # Hawkgirl -> Wonder Woman -> ... -> Batman -> None
    _2nd_last = kthToLast(lst, 2)
    _6th_last = kthToLast(lst, 6)
    _1st_last = kthToLast(lst, 1)
    _overflow = kthToLast(lst, 10)
    _underflow = kthToLast(lst, -1)
    assert(_2nd_last.get_key() == "Superman")
    assert(_6th_last.get_key() == "Hawkgirl")
    assert(_1st_last.get_key() == "Batman")
    assert(_overflow is None)
    assert(_underflow is None)


