from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p = TreeNode(2)
p.left = TreeNode(1)
p.right = TreeNode(6)

# p.left.left = TreeNode(1)
# p.left.right = TreeNode(2)

# p.right.left = TreeNode(3)
# p.right.right = TreeNode(7)


def preOrder(root, min):
    if not root: return
    preOrder(root.left, min)
    min.append(root.val)
    preOrder(root.right, min)
    
    
    
    
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min = []
        preOrder(root, min)
        minNum = float('inf')
        for i in range(1, len(min)):
            if minNum > (min[i] - min[i-1]):
                minNum = min[i] - min[i-1]
        return minNum


print(Solution().getMinimumDifference(p))
