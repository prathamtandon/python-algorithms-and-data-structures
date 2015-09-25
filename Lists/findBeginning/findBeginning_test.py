from findBeginning import findBeginning
from Node import Node
import pytest

def test_findBeginning():
	first = Node('A')
	second = Node('B')
	third = Node('C')
	fourth = Node('D')
	fifth = Node('E')
	
	first.set_next(second)
	second.set_next(third)
	third.set_next(fourth)
	fourth.set_next(fifth)
	fifth.set_next(third)
	
	beginning = findBeginning(first)
	
	assert(beginning is not None)
	assert(beginning.get_key() == 'C')
