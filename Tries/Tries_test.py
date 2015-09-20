from Tries import Trie
import pytest

def test_insert():
	 t_trie = Trie()
	 t_trie.insert_key("to", 7)
	 t_trie.insert_key("tea", 3)
	 assert t_trie.retrieve_val("to") == 7
	 assert t_trie.retrieve_val("tea") == 3

def test_has_key():
	t_trie = Trie()
	assert t_trie.has_key("t") == False
	t_trie.insert_key("in", 5)
	t_trie.insert_key("to", 7)
	assert t_trie.has_key("in") == True
	assert t_trie.has_key("to") == True
	assert t_trie.has_key("t") == True
	assert t_trie.has_key("inn") == False

def test_retrieve_val():
	t_trie = Trie()
	t_trie.insert_key("A", 15)
	t_trie.insert_key("ten", 12)
	assert t_trie.retrieve_val("ten") == 12
	assert t_trie.retrieve_val("A") == 15
	assert t_trie.retrieve_val("A") is not 20
	assert t_trie.retrieve_val("te") is None
	
def test_starts_with_prefix():
	t_trie = Trie()
	t_trie.insert_key("to", 7)
	t_trie.insert_key("tea", 3)
	t_trie.insert_key("ted", 4)
	t_trie.insert_key("ten", 12)
	t_trie.insert_key("A", 15)
	t_trie.insert_key("in", 5)
	t_trie.insert_key("inn", 9)
	assert t_trie.starts_with_prefix("t") == ["to", "tea", "ted", "ten"]
	assert t_trie.starts_with_prefix("in") == ["in", "inn"]
	assert t_trie.starts_with_prefix("AB") == []

def test_lexicographic_sort():
	t_trie = Trie()
	t_trie.insert_key("to", 7)
	t_trie.insert_key("tea", 3)
	t_trie.insert_key("ted", 4)
	t_trie.insert_key("ten", 12)
	t_trie.insert_key("A", 15)
	t_trie.insert_key("in", 5)
	t_trie.insert_key("inn", 9)
	t_trie.insert_key("inn", 9)
	assert t_trie.lexicographic_sort() == ['A', 'in', 'inn', 'tea', 'ted', 'ten', 'to']
