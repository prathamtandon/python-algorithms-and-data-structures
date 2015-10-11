from sparseSearch import sparseSearch
import pytest

def test_sparseSearch():
    strings = ["at","","","","ball","","","car","","","dad","",""]
    x = "ball"

    assert(sparseSearch(strings, x) == 4)

    x = "cat"
    assert(sparseSearch(strings, x) == -1)
