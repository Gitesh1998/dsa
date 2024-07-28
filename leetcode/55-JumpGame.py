class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reachEle = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if reachEle - i <= nums[i]:
                reachEle = i
        return reachEle == 0

# nums = [2,3,1,1,4]
nums = [3,2,2,0,1,2,4]
print(Solution().canJump(nums))