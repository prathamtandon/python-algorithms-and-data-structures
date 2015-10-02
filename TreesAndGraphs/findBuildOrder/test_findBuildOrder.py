from findBuildOrder import findBuildOrder
import pytest

def test_findBuildOrder():
    projects = ["a", "b", "c" ,"d", "e", "f", "g"]
    dependencies = { "f": ["a", "c", "b"], "c": ["a"], "b": ["a", "e"], "a": ["e"], "d": ["g"] }

    order = findBuildOrder(projects, dependencies)

    assert(map(lambda x: x.get_name(), order) == ["d", "f", "g", "c", "b", "a", "e"])
