from Tries import Trie
import pytest

def test_insert():
	 t_trie = Trie()
	 t_trie.insert_key("to", 7)
	 t_trie.insert_key("tea", 3)
	 assert t_trie.retrieve_val("to") == 7
	 assert t_trie.retrieve_val("tea") == 3
