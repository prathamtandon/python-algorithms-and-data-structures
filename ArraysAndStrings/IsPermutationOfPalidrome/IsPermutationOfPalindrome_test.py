from IsPermutationOfPalindrome import IsPermutationOfPalindrome
import pytest

def test_IsPermutationOfPalindrome():
	str = 'Tact Coa'
	assert(IsPermutationOfPalindrome(str) is True)
	str = 'abc'
	assert(IsPermutationOfPalindrome(str) is False)
