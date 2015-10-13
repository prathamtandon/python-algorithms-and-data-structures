from hashtable import HashTable
import pytest

def test_put():
    ht = HashTable()

    # test with integer keys
    ht.put(9, 100)
    ht.put(20, 110)

    # test with string keys
    ht.put('cat', 125)
    ht.put('meow', 'blah!')

def test_get():
    ht = HashTable()

    # test with integer keys
    ht.put(9, 100)
    ht.put(20, 110)

    # test with string keys
    ht.put('cat', 125)
    ht.put('meow', 'blah!')

    assert(ht.get(9) == 100)
    assert(ht.get(20) == 110)
    assert(ht.get('cat') == 125)
    assert(ht.get('meow') == 'blah!')

def test_remove():
    ht = HashTable()

    # test with integer keys
    ht.put(9, 100)
    ht.put(20, 110)

    # test with string keys
    ht.put('cat', 125)
    ht.put('meow', 'blah!')

    ht.remove(9)
    ht.remove('cat')

    assert(ht.get(9) is None)
    assert(ht.get('cat') is None)
    assert(ht.get(20) == 110)
    assert(ht.get('meow') == 'blah!')

def test_size():
    ht = HashTable()

    # test with integer keys
    ht.put(9, 100)
    ht.put(20, 110)

    # test with string keys
    ht.put('cat', 125)
    ht.put('meow', 'blah!')

    assert(ht.size() == 4)

    ht.remove(9)
    ht.remove('cat')

    assert(ht.size() == 2)

