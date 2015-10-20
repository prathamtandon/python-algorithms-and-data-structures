from fillWithXandO import fillWithXandO
import pytest

def test_fillWithXandO():
    arr = ['a','b','c','d','e','f','g','h']
    width = 4
    height = 2
    fillWithXandO(arr,width,height+1,0,'o')
    assert(arr == ['o','o','o','o','x','x','x','x'])
    arr = ['a','b','c','d','e','f']
    width = 4
    height = len(arr)/width
    fillWithXandO(arr,width,height+1,0,'o')
    assert(arr == ['o','o','o','o','x','x'])
