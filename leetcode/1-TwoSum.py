class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for ind, val in enumerate(nums):
            if target - val in dict:
                return [dict[target - val], ind]
            dict[val] = ind
        
        return True
    
nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))