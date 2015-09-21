from IsPermutation import IsPermutationWithLetterCount, IsPermutationWithSort
import pytest

def test_IsPermutation():
	src = 'blah'
	target = ''
	assert(IsPermutationWithLetterCount(src, target) is False)
	assert(IsPermutationWithSort(src, target) is False)
	target = 'bl'
	assert(IsPermutationWithLetterCount(src, target) is False)
	assert(IsPermutationWithSort(src, target) is False)
	target = 'blah'
	assert(IsPermutationWithLetterCount(src, target) is True)
	assert(IsPermutationWithSort(src, target) is True)
	target = 'blahzz'
	assert(IsPermutationWithLetterCount(src, target) is False)
	assert(IsPermutationWithSort(src, target) is False)
	target = 'lbha'
	assert(IsPermutationWithLetterCount(src, target) is True)
	assert(IsPermutationWithSort(src, target) is True)
	target = 'lbhaa'
	assert(IsPermutationWithLetterCount(src, target) is False)
	assert(IsPermutationWithSort(src, target) is False)
	
