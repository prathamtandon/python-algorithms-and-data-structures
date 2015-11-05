from zSearch import search
import pytest

def test_zSearch():
    string = 'baabaa'
    pattern = 'aab'

    assert(search(string, pattern) == 1)
