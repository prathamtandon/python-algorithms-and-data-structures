from searchRotated import searchRotated
import pytest

def test_searchRotated():
    arr = [29,45,64,10,20]
    x = 45
    assert(searchRotated(arr,0,len(arr)-1,x) == 1)

    arr = [45,64,10,20,29]
    x = 20
    assert(searchRotated(arr,0,len(arr)-1,x) == 3)

    arr = [2,2,2,3,4,2]
    x = 4
    assert(searchRotated(arr,0,len(arr)-1,x) == 4)

    assert(searchRotated(arr,0,len(arr)-1,100) == -1)

