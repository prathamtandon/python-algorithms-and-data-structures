from wordTransformer import transform
import pytest

def test_wordTransformer():
    dictionary = ['DAMP','DICE','DUKE','LIKE','LAMP','LIME','DIME','LIMP']
    start = 'DAMP'
    stop = 'LIKE'

    path = transform(start,stop,dictionary)

    assert(path == ['DAMP','LAMP','LIMP','LIME','LIKE'])
