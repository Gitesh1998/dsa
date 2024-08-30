class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        currentSum = [0 for _ in nums]
        maxSum = [0 for _ in nums]
        currentSum[0] = nums[0]
        maxSum[0] = nums[0]
        for i in range(1, len(nums)):
            print(maxSum, currentSum)
            if (currentSum[i-1] + nums[i]) < nums[i]:
                currentSum[i] = nums[i]
            else:
                currentSum[i] = currentSum[i-1] + nums[i]
            
            if currentSum[i] > maxSum[i-1]:
                maxSum[i] = currentSum[i]
            else:
                maxSum[i] = maxSum[i-1]
        
        return maxSum[-1]
    
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))