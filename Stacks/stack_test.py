from stack import Stack
import pytest

def test_push():
    stack = Stack()
    stack.push(15)
    stack.push(6)
    stack.push(2)
    stack.push(9)
    assert(stack.empty() == False)
    assert(stack.peek() == 9)

def test_pop():
    stack = Stack()
    stack.push(15)
    stack.push(6)
    assert(stack.pop() == 6)
    assert(stack.pop() == 15)
    with pytest.raises(Exception):
        stack.pop()
