from placeQueens import placeQueens

def test_placeQueens():
    results = []
    placeQueens(0, [None]*8, results)
    assert(len(results) == 92)
