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


def preOrder(root, l):
    if not root: return
    l.append(root)
    preOrder(root.left, l)
    preOrder(root.right, l) 

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return root
        l = []
        preOrder(root, l)
        for i in range(len(l)-1):
            l[i].left = None
            l[i].right = l[i+1]
            
        

Solution().invertTree(p)


