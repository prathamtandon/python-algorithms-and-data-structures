from minProduct import minProduct
import pytest

def test_minProduct():
	assert(minProduct(1,0) == 0)
	assert(minProduct(1,2) == 2)
	assert(minProduct(2,5) == 10)
	assert(minProduct(5,4) == 20)
