class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        maxArr = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    maxArr[i] = max(maxArr[i], maxArr[j]+1)
        return max(maxArr)
 
 
nums = [10,9,2,5,3,7,101,18]  
nums = [0,1,0,3,2,3]
# nums = [7,7,7,7,7,7,7] 
print(Solution().lengthOfLIS(nums))