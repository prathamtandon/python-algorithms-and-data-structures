from palindromicSubstrings import palindromeSubStr
import pytest

def test_palindromeSubStr():
    string = 'abaaa'
    res = palindromeSubStr(string)

    assert(len(res) == 5)
    assert('a' in res)
    assert('aa' in res)
    assert('aaa' in res)
    assert('aba' in res)
    assert('b' in res)
