from getPermsDupes import getPermsDupes
import pytest

def test_getPermsDupes():
	perms = getPermsDupes("aba")
	assert(len(perms) == 3)
	assert("aab" in perms)
	assert("aba" in perms)
	assert("baa" in perms)
