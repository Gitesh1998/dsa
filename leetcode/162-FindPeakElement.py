class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        start, end = 0, len(nums) - 1
        mid = (start + end) // 2
        while True:
            if start + 1 == end:
                if nums[start] < nums[end]:
                    return end
                else:
                    return start
                
            if nums[start] < nums[mid]:
                if nums[mid] > nums[mid+1]:
                    end = mid
                else:
                    start = mid
            else:
                end = mid
            mid = (start + end) // 2

nums = [1,2,3,4,6,7,1]
print(Solution().findPeakElement(nums))
