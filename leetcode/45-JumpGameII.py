class Solution:
    def jump(self, nums: list[int]) -> int:
        canWe = [float("inf") for _ in nums]
        canWe[0] = 0
        for i in range(len(nums)):
            if canWe[-1] != float("inf"):
                return canWe[-1]
            for j in range(i+1,min(len(nums), i+nums[i]+1)):
                canWe[j] = min(canWe[j], canWe[i]+1)
        return canWe[-1]
    
nums = [2,3,1,1,4]
nums = [2,3,0,1,4]
print(Solution().jump(nums))