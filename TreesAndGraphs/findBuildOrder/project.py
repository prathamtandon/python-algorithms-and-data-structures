class Project:

    def __init__(self, name):
        self.name = name
        self.children = []
        self.project_map = {}
        self.dependency_count = 0

    def add_neighbour(self, project):
        if not project.get_name() in self.project_map:
            self.children.append(project)
            project.increment_dependencies()

    def increment_dependencies(self):
        self.dependency_count += 1

    def decrement_dependencies(self):
        self.dependency_count -= 1

    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

    def get_dependency_count(self):
        return self.dependency_count
