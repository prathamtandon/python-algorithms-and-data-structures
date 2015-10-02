# Given a list of projects and a list of dependencies, return a
# build order of the projects. If no build order is possible,
# return an error.

# The idea is to represent the projects and dependencies as a graph
# and do a topological sort on the graph. No build order is possible
# if there is a cycle in the graph.
from graph import Graph

def findBuildOrder(projects, dependencies):
    graph = build_graph(projects, dependencies)
    return order_projects(graph.get_nodes())

def build_graph(projects, dependencies):
    graph = Graph()

    for project in projects:
        graph.get_or_create(project)

    for node in dependencies:
        dependecy_list = dependencies[node]
        for dep in dependecy_list:
            graph.add_edge(node, dep)

    return graph

def order_projects(projects):
    order = [None] * len(projects)
    end_of_list = add_non_dependent(order, projects, 0)
    to_be_processed = 0
    while to_be_processed < len(order):
        current = order[to_be_processed]
        if current is None:
            # We have found a circular dependency!
            return None

        children = current.get_children()
        for child in children:
            child.decrement_dependencies()

        end_of_list = add_non_dependent(order, children, end_of_list)
        to_be_processed += 1

    return order

def add_non_dependent(order, projects, offset):
    for project in projects:
        if project.get_dependency_count() == 0:
            order[offset] = project
            offset += 1
    return offset


