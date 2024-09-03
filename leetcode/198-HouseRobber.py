class Solution:
    def rob(self, nums: list[int]) -> int:
        arrSize = len(nums)
        if arrSize == 1:
            return nums[0]
        a = nums[0]
        b = max(nums[0], nums[1])

        for i in range(2, arrSize):
            print(i, a, b , max(b, a+nums[i]))
            a, b = b, max(b, a+nums[i])       
        return b


nums = [1, 2, 3, 3]
nums = [2,7,9,3,1]
nums = [2,1]    
print(Solution().rob(nums))
