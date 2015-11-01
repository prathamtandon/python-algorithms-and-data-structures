from longestPalindrome import longestPalSubstr
import pytest

def test_longestPalSubstr():
    string = 'forgeeksskeegfor'
    output = 'geeksskeeg'

    res = longestPalSubstr(string)
    start = res[0]
    length = res[1]
    assert(string[start:start+length] == output)
