from URLify import URLify
import pytest

def test_URLify():
	ipt = "   "
	opt = "%20"
	assert(URLify(ipt, 1) == opt)
	ipt = "Mr John Smith    "
	opt = "Mr%20John%20Smith"
	assert(URLify(ipt, 13) == opt)
