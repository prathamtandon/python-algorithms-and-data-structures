from add import add
import pytest

def test_add():
    assert(add(0,0) == 0)
    assert(add(12,2) == 14)
