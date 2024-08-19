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


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root == None:
            return None
        p = []
        temp = [root]
        reverse = False
        while temp:
            if reverse:
                p.append([i.val for i in temp][::-1])
                reverse = False
            else:
                p.append([i.val for i in temp])
                reverse = True
            tempS = []
            for i in temp:
                if i.left:
                    tempS.append(i.left)
                if i.right:
                    tempS.append(i.right)
            temp = tempS
        return p

print(Solution().zigzagLevelOrder(p))


