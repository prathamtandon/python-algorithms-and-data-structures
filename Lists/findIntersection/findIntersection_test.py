from Node import Node
from findIntersection import findIntersection

def test_findIntersection():
    ## Create first list
    first1 = Node(3)
    second1 = Node(1)
    third1 = Node(5)
    fourth1 = Node(9)
    common = Node(7)
    sixth1 = Node(2)
    seventh1 = Node(1)

    first1.set_next(second1)
    second1.set_next(third1)
    third1.set_next(fourth1)
    fourth1.set_next(common)
    common.set_next(sixth1)
    sixth1.set_next(seventh1)

    ## Create second list
    first2 = Node(4)
    second2 = Node(6)

    first2.set_next(second2)
    second2.set_next(common)

    ## Check for intersection
    intersection = findIntersection(first1, first2)

    assert(intersection is not None)
    assert(intersection.get_key() == 7)





