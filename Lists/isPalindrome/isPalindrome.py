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


# Approach 2: Use fast and slow pointers where fast moves at
# twice the speed of slow. So, when fast reaches end of list,
# slow should be at the middle.
# Now if we know the reverse of first half of list, we could
# compare it with remaining half and if they are equal, then
# given list is palindrome. This approach is slightly more space
# efficient as it would still use a Stack to get the reverse of first
# half.

def isPalidrome_iterative(lst):
    slow = lst.head
    fast = lst.head

    stack = []

    while fast is not None and fast.get_next() is not None:
        stack.append(slow.get_key())
        slow = slow.get_next()
        fast = fast.get_next().get_next()

    # When there are odd number of nodes, skip the middle.
    if fast is not None:
        slow = slow.get_next()

    while slow is not None:
        if slow.get_key() != stack.pop():
            return False
        slow = slow.get_next()

    return True
