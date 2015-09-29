from queue import Queue
import pytest

def test_enqueue():
    queue = Queue(2)
    queue.enqueue(12)
    queue.enqueue(5)
    assert(queue.contains(12))
    assert(queue.contains(5))

def test_dequeue():
    queue = Queue(2)
    queue.enqueue(12)
    queue.enqueue(5)
    assert(queue.dequeue() == 12)
    assert(queue.dequeue() == 5)
