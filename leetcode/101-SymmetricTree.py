from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p = TreeNode(4)
p.left = TreeNode(2)
p.right = TreeNode(2)

p.left.left = TreeNode(3)
p.left.right = TreeNode(4)

p.right.left = TreeNode(4)
# p.right.right = TreeNode(3)


def isSym(p, q):
    if p == None and q == None:
        return True
    if p == None or q == None or p.val != q.val:
        return False
    return isSym(p.left, q.right) and isSym(p.right, q.left)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return isSym(root.left, root.right)


print(Solution().isSymmetric(p))
