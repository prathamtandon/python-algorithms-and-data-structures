from MinimalTree import createMinimalBST

def test_minimal_tree_even_array():
    root = createMinimalBST([23, 46, 55, 78])
    assert(root.key == 46)
    assert(root.left.key == 23)
    assert(root.right.key == 55)
    assert(root.right.right.key == 78)

def test_minimal_tree_even_array():
    root = createMinimalBST([15, 23, 46, 55, 78, 92, 99])
    assert(root.key == 55)
    assert(root.left.key == 23)
    assert(root.left.left.key == 15)
    assert(root.left.right.key == 46)
    assert(root.right.key == 92)
    assert(root.right.left.key == 78)
    assert(root.right.right.key == 99)
