from RouteBetweenNodes import RouteBetweenNodes
from RouteBetweenNodes import Node
from RouteBetweenNodes import Graph
import pytest

def test_route_exists():
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	
	a.set_adjacency([b, c])
	c.set_adjacency([b, d, e])
	
	G = Graph([a, b, c, d, e])
	
	assert(RouteBetweenNodes(G, a, d) == True)

def test_no_route_exists():
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	
	a.set_adjacency([b, c])
	c.set_adjacency([b, d, e])
	
	G = Graph([a, b, c, d, e])
	
	assert(RouteBetweenNodes(G, b, c) == False)
	
