from sparseSimilarity import computeSimilarities, Document, DocPair
import pytest

def test_sparseSimilarity():
    doc1 = Document(13,[14,15,100,9,3])
    doc2 = Document(16,[32,1,9,3,5])
    doc3 = Document(19,[15,29,2,6,8,7])
    doc4 = Document(24,[7,10])

    hashmap = { 13: doc1, 16: doc2, 19: doc3, 24: doc4 }

    res = computeSimilarities(hashmap)
    assert(len(res) == 3)
    assert(DocPair(13,19) in res)
    assert(DocPair(13,16) in res)
    assert(DocPair(19,24) in res)
    assert(res[DocPair(13,19)] == 0.1)
    assert(res[DocPair(13,16)] == 0.25)
