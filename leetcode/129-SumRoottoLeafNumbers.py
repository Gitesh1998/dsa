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


def getNum(root, num):
    if not root:
        return 0
    val = (num * 10) + root.val
    if not root.left and not root.right:
        return val
    return getNum(root.left, val) + getNum(root.right, val)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return getNum(root, 0)


print(Solution().sumNumbers(p))
