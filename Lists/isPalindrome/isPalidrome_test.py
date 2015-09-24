from LinkedList import LinkedList
from isPalindrome import isPalindrome, isPalidrome_iterative

def test_isPalindrome():
    lst1 = LinkedList()
    lst1.insert(3)
    lst1.insert(5)
    lst1.insert(2)
    # 2 -> 5 -> 3 -> None
    assert(isPalindrome(lst1) is False)
    assert(isPalidrome_iterative(lst1) is False)

    lst2 = LinkedList()
    lst2.insert(3)
    lst2.insert(3)
    lst2.insert(5)
    lst2.insert(5)
    lst2.insert(3)
    lst2.insert(3)
    # 3 -> 3 -> 5 -> 5 -> 3 -> 3 -> None
    assert(isPalindrome(lst2) is True)
    assert(isPalidrome_iterative(lst2) is True)
