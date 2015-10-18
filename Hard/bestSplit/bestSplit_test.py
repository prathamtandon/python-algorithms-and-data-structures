from bestSplit import bestSplit
import pytest

def test_bestSplit():
    dictionary = ['hi','my','name','is','pratham']
    sentence = 'himynameispratham'

    assert(bestSplit(dictionary,sentence) == 'hi my name is pratham')
