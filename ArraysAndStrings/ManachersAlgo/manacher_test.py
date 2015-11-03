from manacher2 import longest_palindrome
import pytest

def test_findLongestPalindrome():
    string = 'bananas'
    output = 'anana'

    assert(longest_palindrome(string) == output)
