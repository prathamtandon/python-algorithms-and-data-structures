from doesMatch import doesMatch
import pytest

def test_doesMatch():
    pattern = 'aabab'
    value = 'catcatgocatgo'

    assert(doesMatch(pattern,value) == True)

    value = 'cat'
    assert(doesMatch(pattern,value) == False)
