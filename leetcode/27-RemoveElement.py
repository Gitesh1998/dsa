class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for _, num in enumerate(nums):
            if num != val:
                nums[k] = num
                k += 1
        return k


nums = [3, 2, 2, 3]
val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2

print(Solution().removeElement(nums, val))
