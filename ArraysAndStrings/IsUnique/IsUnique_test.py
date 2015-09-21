from IsUnique import isUniqueChars
import pytest

def test_isUniqueChars():
	str = ''
	assert(isUniqueChars(str) is True)
	str = 'xypkq'
	assert(isUniqueChars(str) is True)
	str = 'xyypky'
	assert(isUniqueChars(str) is False)
