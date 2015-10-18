from continuousMedian import addNewNumber, getMedian
import pytest

def test_continuousMedian():
    addNewNumber(10)
    addNewNumber(9)
    addNewNumber(15)
    addNewNumber(25)

    assert(getMedian() == 12.5)
