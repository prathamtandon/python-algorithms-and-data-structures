from sortAnagrams import sortAnagrams
from sortAnagrams import sortAnagrams2
import pytest


def test_sortAnagrams():
    array = ["dot", "acre", "prat", "race", "trap", "tod"]
    cloned = list(array)
    '''
    array = sortAnagrams(array)
    print array
    assert(array == ["acre","race","dot","tod","prat","trap"])
    '''
    cloned = sortAnagrams2(cloned)
    assert(cloned == ["acre","race","dot","tod","prat","trap"])

