from compress import compress
import pytest

def test_compress():
    original = "aabcccccaaa"
    compressed = "a2b1c5a3"
    assert(compress(original) == compressed)
    original = "aab"
    assert(compress(original) == original)
