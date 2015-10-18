from printLongestWord import getLongestWord
import pytest

def test_printLongestWord():
    dictionary = ["abcd","ab","cd"]
    assert(getLongestWord(dictionary) == "abcd")
