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

def divide(inorder, preorder):
    if not inorder: return None
    temp = preorder[0]
    preorder.pop(0)
    if len(inorder) == 1:
        return TreeNode(temp)
    i = 0
    while i< len(inorder):
        if inorder[i] == temp:
            break
        i+=1
    tempNode = TreeNode(temp)
    tempNode.right = divide(inorder[i+1:], preorder)
    tempNode.left = divide(inorder[:i], preorder)
    return tempNode


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        temp = divide(inorder, postorder[::-1])
        
        return temp

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

levelOrder(Solution().buildTree(inorder, postorder))


