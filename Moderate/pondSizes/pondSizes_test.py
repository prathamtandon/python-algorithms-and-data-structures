from pondSizes import computePondSizes
import pytest

def test_computePondSizes():
    land = [[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]

    sizes = computePondSizes(land)

    assert(len(sizes) == 3)
    assert(2 in sizes)
    assert(1 in sizes)
    assert(4 in sizes)
