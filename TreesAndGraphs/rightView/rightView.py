# Given a binary tree, print its Right view. Right view is set of 
# nodes visible when tree is visited from Right side.

def rightView(root):
        cur = root
        res = []
        while cur is not None:
                res.append(cur.key)
                while cur.right is not None:
                        cur = cur.right
                        res.append(cur.key)
                cur = cur.left

        return res
