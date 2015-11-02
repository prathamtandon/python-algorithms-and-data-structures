from manacher import findLongestPalindrome
import pytest

def test_findLongestPalindrome():
    string = 'bananas'
    output = 'anana'

    assert(findLongestPalindrome(string) == output)
