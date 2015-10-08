from towerOfHanoi import Tower
import pytest

def test_towerOfHanoi():
    n = 3
    towers = [None] * n
    for i in range(0, n):
        towers[i] = Tower(i)

    for i in reversed(range(1, n+1)):
        towers[0].add(i)

    towers[0].moveDisks(n, towers[2], towers[1])

    assert(towers[0].disks == [])
    assert(towers[1].disks == [])
    assert(towers[2].disks == [3,2,1])
