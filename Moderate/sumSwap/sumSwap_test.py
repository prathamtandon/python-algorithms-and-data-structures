from sumSwap import findSwapValues
import pytest

def test_findSwapValues():
    array1 = [4,1,2,1,1,2]
    array2 = [3,6,3,3]

    pair = findSwapValues(array1,array2)

    assert(pair == (3,1))


