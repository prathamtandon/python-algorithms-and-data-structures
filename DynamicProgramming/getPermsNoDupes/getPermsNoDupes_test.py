from getPermsNoDupes import getPerms
from getPermsNoDupes import getPerms2
import pytest

def test_getPerms():
	assert(getPerms("") == [""])
	assert(getPerms("a") == ["a"])
	perms = getPerms("abc")
	assert(len(perms) == 6)
	assert("abc" in perms)
	assert("acb" in perms)
	assert("bac" in perms)
	assert("bca" in perms)
	assert("cab" in perms)
	assert("cba" in perms)
	
def test_getPerms2():
	assert(getPerms2("") == [""])
	assert(getPerms2("a") == ["a"])
	perms = getPerms2("abc")
	assert(len(perms) == 6)
	assert("abc" in perms)
	assert("acb" in perms)
	assert("bac" in perms)
	assert("bca" in perms)
	assert("cab" in perms)
	assert("cba" in perms)
