class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def LinkedListPerLevel(root):
    if root is None:
        return []
    l_lists = []
    cur_list = [root]
    while len(cur_list) > 0:
        l_lists.append(cur_list)
        parent_list = list(cur_list)
        cur_list = []
        for parent in parent_list:
            if parent.left is not None:
                cur_list.append(parent.left)
            if parent.right is not None:
                cur_list.append(parent.right)

    return l_lists

def LinkedListPerLevel_r(node, level, lists):
    if node is None:
        return
    cur_depth_list = []
    if len(lists) == level:
        lists.append(cur_depth_list)
    else:
        cur_depth_lists = lists[level]

    cur_depth_list.append(node)
    LinkedListPerLevel_r(node.left, level + 1, lists)
    LinkedListPerLevel_r(node.right, level + 1, lists)
