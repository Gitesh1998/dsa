from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p = TreeNode(3)
p.left = TreeNode(1)
p.right = TreeNode(4)

# p.left.left = TreeNode(1)
p.left.right = TreeNode(2)

# p.right.left = TreeNode(3)
# p.right.right = TreeNode(7)

def small(root, data):
    if not root or not data[0]: return
    small(root.left, data)
    if data[0] == 1:
        data[1] = root.val
    data[0] -= 1
    small(root.right, data)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        data = [k, False]
        small(root, data)
        return data[1]
    
print(Solution().kthSmallest(p, 3))        