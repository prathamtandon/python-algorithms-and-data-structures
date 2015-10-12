from rankNode import Rank
import pytest

def test_rankNode():
	store = Rank()
	store.track(20)
	store.track(15)
	store.track(25)
	store.track(23)
	store.track(10)
	store.track(5)
	store.track(13)
	store.track(24)
	
	assert(store.getRank(20) == 4)
	assert(store.getRank(25) == 7)
	assert(store.getRank(24) == 6)
