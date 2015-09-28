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
