from project import Project

class Graph:

    def __init__(self):
        self.nodes = []
        self.project_map = {}

    def get_or_create(self, name):
        if not name in self.project_map:
            node = Project(name)
            self.nodes.append(node)
            self.project_map[name] = node

        return self.project_map[name]

    def add_edge(self, src, dest):
        src = self.get_or_create(src)
        dest = self.get_or_create(dest)
        src.add_neighbour(dest)

    def get_nodes(self):
        return self.nodes
