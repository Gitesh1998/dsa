class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for ind in range(1, len(nums)):
            if nums[ind] != nums[i]:
                nums[i + 1] = nums[ind]
                i += 1
        return i+1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1,1]

print(Solution().removeDuplicates(nums))
