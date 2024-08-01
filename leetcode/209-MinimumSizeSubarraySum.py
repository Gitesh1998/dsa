class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i, j = 0, 0
        sumVal = 0
        leng = len(nums) + 1
        while j < len(nums):
            
            sumVal += nums[j]
            
            if sumVal >= target and leng > (j - i + 1):
                leng = j - i + 1
                
            while sumVal >= target:
                sumVal -= nums[i]
                i += 1
                if sumVal >= target and leng > (j - i + 1):
                    leng = j - i + 1
            j += 1
        if leng == len(nums) +1 :
            return 0
        return leng


target = 7
nums = [2, 3, 1, 2, 4, 3]
# target = 4
# nums = [1,4,4]
target = 11
nums = [1,1,1,1,1,1,1,1]
print(Solution().minSubArrayLen(target, nums))
