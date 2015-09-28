from priority_queue import PriorityQueue
import pytest

def test_insert_key():
    pq = PriorityQueue()
    pq.insert_key(24)
    pq.insert_key(12)
    pq.insert_key(1)
    pq.insert_key(35)

    assert(pq.contains(24) == True)
    assert(pq.contains(12) == True)
    assert(pq.contains(1) == True)
    assert(pq.contains(35) == True)
    assert(pq.contains(10) == False)

def test_get_max():
    pq = PriorityQueue()
    pq.insert_key(24)
    pq.insert_key(12)
    pq.insert_key(1)
    pq.insert_key(35)

    assert(pq.get_max() == 35)

def test_extract_max():
    pq = PriorityQueue()
    pq.insert_key(24)
    pq.insert_key(12)
    pq.insert_key(1)
    pq.insert_key(35)

    assert(pq.extract_max() == 35)
    assert(pq.extract_max() == 24)
