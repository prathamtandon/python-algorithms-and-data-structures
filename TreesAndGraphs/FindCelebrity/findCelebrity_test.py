from findCelebrity import celebrity
import pytest

def test_celebrity():
    relationships = [[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]]
    size = 4
    assert(celebrity(relationships, size) == 3)
