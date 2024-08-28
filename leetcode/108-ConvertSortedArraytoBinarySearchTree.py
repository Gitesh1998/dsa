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


def divide(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return TreeNode(nums[0])
    
    mid = len(nums)//2
    temp = TreeNode(nums[mid])
    temp.left = divide(nums[:mid])
    temp.right = divide( nums[mid+1:])
    return temp

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        return divide(nums)
    
    
nums = [-10,-3,0,5,9]
levelOrder(Solution().sortedArrayToBST(nums))