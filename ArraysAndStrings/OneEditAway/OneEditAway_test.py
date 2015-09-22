from OneEditAway import OneAway
import pytest

def test_OneAway():
	str1 = "pale"
	str2 = "ple"
	assert(OneAway(str1, str2) == True)
	str1 = "pales"
	str2 = "pale"
	assert(OneAway(str1, str2) == True)
	str1 = "pale"
	str2 = "bale"
	assert(OneAway(str1, str2) == True)
	str1 = "pale"
	str2 = "bake"
	assert(OneAway(str1, str2) == False)
	str1 = "p"
	str2 = ""
	assert(OneAway(str1, str2) == True)
	str1 = "pa"
	str2 = ""
	assert(OneAway(str1, str2) == False)
	str1 = "pal"
	str2 = "paler"
	assert(OneAway(str1, str2) == False)
	str1 = "potassium"
	str2 = "potassium"
	assert(OneAway(str1, str2) == True)
