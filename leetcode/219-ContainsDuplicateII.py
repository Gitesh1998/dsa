class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dict = {}
        
        for ind, val in enumerate(nums):
            if val in dict:
                if (ind - dict[val]) <= k:
                    return True
            dict[val] = ind        
        return False
    
nums = [1,2,3,1]
k = 3
nums = [1,0,1,1]
k = 1
nums = [1,2,3,1,2,3]
k = 2
print(Solution().containsNearbyDuplicate(nums, k))