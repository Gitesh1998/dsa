from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p = TreeNode(5)
p.left = TreeNode(4)
p.right = TreeNode(6)

# p.left.left = TreeNode(1)
# p.left.right = TreeNode(3)

p.right.left = TreeNode(3)
p.right.right = TreeNode(7)

def preOrder(root):
    if not root: return
    preOrder(root.left)
    print(root.val, end=" ")
    preOrder(root.right)

def valid(root, min, max):
    if not root: return True
    if min < root.val < max:
        return valid(root.left, min, root.val) and valid(root.right, root.val, max)
    return False

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min, max = float('-inf'), float('inf')
        return valid(root, min, max)
    
# preOrder(Solution().isValidBST(p))
print(Solution().isValidBST(p))