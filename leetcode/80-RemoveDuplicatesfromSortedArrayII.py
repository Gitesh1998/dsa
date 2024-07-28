class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = 1
        for ind in range(2, len(nums)):
            if (nums[i] != nums[ind]) or (nums[i] != nums[i-1]):
                nums[i + 1] = nums[ind]
                i += 1
        return i+1


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# nums = [1,1,1,2,2,3]
print(Solution().removeDuplicates(nums))
