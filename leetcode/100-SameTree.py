from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p = TreeNode(10)
p.left = TreeNode(5)
p.right = TreeNode(15)

q = TreeNode(10)
q.left = TreeNode(5)
q.left.right = TreeNode(15)



class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        print(p.val, q.val)
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)    


print(Solution().isSameTree(p, q))