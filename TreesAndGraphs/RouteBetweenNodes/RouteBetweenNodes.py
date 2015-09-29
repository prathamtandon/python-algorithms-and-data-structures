# Given a directed graph, find whether there is a route between two
# nodes.
from Queue import Queue
from enum import Enum

class State(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3

class Node:
    counter = 0
    def __init__(self, key):
        self.identifier = ++Node.counter
        self.key = key
        self.adjacency = []
        self.state = State.WHITE
    def set_adjacency(self, adjacency):
		self.adjacency = adjacency


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

def RouteBetweenNodes(graph, node1, node2):
    src = filter(lambda node: node is node1, graph.nodes)
    if len(src) == 0:
        raise ValueError("source not found in graph")
    else:
		src = src[0]

    dest = filter(lambda node: node is node2, graph.nodes)
    if len(dest) == 0:
        raise ValueError("destination not found in graph")
    else:
		dest = dest[0]


    Q = Queue()
    Q.put(src)
    src.state = State.GRAY

    while not Q.empty():
        u = Q.get()
        for v in u.adjacency:
            if v is dest:
                return True
            if v.state == State.WHITE:
                v.state = State.GRAY
                Q.put(v)
        u.state = State.BLACK
    return False



