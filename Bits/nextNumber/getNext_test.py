from getNext import getNext
import pytest

def test_getNext():
    n = 13948
    assert(getNext(n) == 13967)
