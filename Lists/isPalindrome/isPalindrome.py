# Returns if a Linked List is a palindrome
from LinkedList import LinkedList

def reverse(lst):
    reverse_lst = LinkedList()
    cur = lst.head
    while cur is not None:
        reverse_lst.insert(cur.get_key())
        cur = cur.get_next()
    return reverse_lst

def is_equal_list(list1, list2):
    cur1 = list1.head
    cur2 = list2.head
    while cur1 is not None and cur2 is not None:
        if cur1.get_key() != cur2.get_key():
            return False
        cur1 = cur1.get_next()
        cur2 = cur2.get_next()

    return cur1 is None and cur2 is None

def isPalindrome(lst):
    reverse_lst = reverse(lst)
    return is_equal_list(lst, reverse_lst)
