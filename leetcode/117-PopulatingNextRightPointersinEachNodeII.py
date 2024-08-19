from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


p = TreeNode(4)
p.left = TreeNode(2)
p.right = TreeNode(7)

p.left.left = TreeNode(1)
p.left.right = TreeNode(3)

p.right.left = TreeNode(6)
p.right.right = TreeNode(9)


def levelOrder(p):
    if p == None:
        print(False)
    
    stack = [p]
    while len(stack) > 0:
        temp = stack.pop(0)
        if temp == None:
            continue
        print(temp.val, end = " ")
        stack.append(temp.left)    
        stack.append(temp.right)
    print()


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        stack = [root]
        
        while stack:
            tempS = []
            for i in stack:
                if i.left:
                    tempS.append(i.left)
                if i.right:
                    tempS.append(i.right)
            for i in range(len(tempS)-1):
                tempS[i].next = tempS[i+1]
            stack = tempS
    
        return root

levelOrder(Solution().connect(p))


