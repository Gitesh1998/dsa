class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        ele = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == ele:
                count += 1
            elif nums[i] != ele:
                if count == 0:
                    ele = nums[i]
                else:
                    count -= 1
        return ele


nums = [2, 2, 1, 1, 1, 2, 2]
# nums = [3, 2, 3]
print(Solution().majorityElement(nums))
    