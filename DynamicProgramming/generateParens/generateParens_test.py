from generateParens import generateParens
import pytest

def test_generateParens():
	parens = generateParens(2)
	assert(len(parens) == 2)
	assert("(())" in parens)
	assert("()()" in parens)
	parens = generateParens(3)
	assert(len(parens) == 5)
	assert("(()())" in parens)
	assert("((()))" in parens)
	assert("()(())" in parens)
	assert("(())()" in parens)
	assert("()()()" in parens)
