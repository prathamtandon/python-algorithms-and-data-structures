from LinkedList import LinkedList
from deleteDupes import deleteDupes
import pytest

def test_deleteDupes():
	lst = LinkedList()
	lst.insert("Batman")
	lst.insert("Superman")
	lst.insert("Batman")
	lst.insert("Batman")
	deleteDupes(lst)
	assert(lst.head.get_key() == "Batman")
	assert(lst.head.get_next().get_key() == "Superman")
	assert(lst.head.get_next().get_next() is None)
	lst = LinkedList()
	lst.insert("Batman")
	lst.insert("Superman")
	deleteDupes(lst)
	assert(lst.head.get_key() == "Superman")
	assert(lst.head.get_next().get_key() == "Batman")
	assert(lst.head.get_next().get_next() is None)
	lst = LinkedList()
	lst.insert("Batman")
	lst.insert("Batman")
	lst.insert("Batman")
	deleteDupes(lst)
	assert(lst.head.get_key() == "Batman")
	assert(lst.head.get_next() is None)
