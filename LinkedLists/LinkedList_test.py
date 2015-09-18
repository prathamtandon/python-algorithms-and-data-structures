from LinkedList import LinkedList
import pytest

def test_insert():
	l_list = LinkedList()
	l_list.insert("Batman")
	assert l_list.head.get_key() == "Batman"
	assert l_list.head.get_prev() is None
	
def test_insert_multi():
	l_list = LinkedList()
	l_list.insert("Batman")
	l_list.insert("Superman")
	assert l_list.head.get_key() == "Superman"
	second = l_list.head.get_next()
	assert second.get_key() == "Batman"

def test_positive_search():
	l_list = LinkedList()
	l_list.insert("Batman")
	l_list.insert("Superman")
	found = l_list.search("Batman")
	assert found.get_key() == "Batman"
	found = l_list.search("Superman")
	assert found.get_key() == "Superman"
	
def test_negative_search():
	l_list = LinkedList()
	l_list.insert("Batman")
	not_found = l_list.search("Bruce Wayne")
	assert not_found is None
	
def test_delete():
	l_list = LinkedList()
	l_list.insert("Batman")
	l_list.insert("Superman")
	l_list.insert("Wonder Woman")
	l_list.delete("Superman")
	assert l_list.head.get_next().get_key() == "Batman"
	l_list.delete("Batman")
	assert l_list.head.get_key() == "Wonder Woman"
	
def test_delete_value_not_in_list():
	l_list = LinkedList()
	l_list.insert("Batman")
	l_list.insert("Superman")
	with pytest.raises(ValueError):
		l_list.delete("Flash")

def test_delete_empty_list():
	l_list = LinkedList()
	with pytest.raises(ValueError):
		l_list.delete("Hawkgirl")

def test_delete_head():
	l_list = LinkedList()
	l_list.insert("Batman")
	l_list.insert("Superman")
	assert l_list.head.get_key() == "Superman"
	l_list.delete("Superman")
	assert l_list.head.get_key() == "Batman"
	
def test_size(): 
	l_list = LinkedList()
	assert l_list.size() == 0
	l_list.insert("Batman")
	l_list.insert("Superman")
	assert l_list.size() == 2
	l_list.delete("Superman")
	assert l_list.size() == 1
