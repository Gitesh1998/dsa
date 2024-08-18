from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p = TreeNode(4)
p.left = TreeNode(2)
p.right = TreeNode(7)

p.left.left = TreeNode(1)
p.left.right = TreeNode(3)

p.right.left = TreeNode(6)
p.right.right = TreeNode(9)


p.left.left.left = TreeNode(10)

def left(root):
    if not root:
        return 0
    return 1 + left(root.left)


def right(root):
    if not root:
        return 0
    return 1 + right(root.right)


def temp(root, l, r):
    if not root:
        return 0
    if r == -1:
        r = right(root)
    if l == -1:
        l = left(root)
    if r == l:
        return (2**r) - 1
    return temp(root.left, l - 1, -1) + temp(root.right, -1, r - 1) + 1


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = left(root)
        r = right(root)
        return temp(root, l, r)


print(Solution().countNodes(p))
