from mastermind import Result,estimate
import pytest

def test_estimate():
    guess = 'GGRR'
    solution = 'RGBY'

    res = estimate(guess, solution)

    assert(res.hits == 1)
    assert(res.pseudo_hits == 1)

