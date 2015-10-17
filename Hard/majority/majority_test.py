from majority import findMajorityElement
import pytest

def test_majority_exists():
    arr = [1,2,5,9,5,9,5,5,5]
    assert(findMajorityElement(arr) == 5)

def test_majority_does_not_exist():
    arr = [3,1,7,1]
    assert(findMajorityElement(arr) == -1)
