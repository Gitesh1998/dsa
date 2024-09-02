def findPeakElement(nums: list[int]) -> int:
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
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid
        else:
            end = mid
        mid = (start + end) // 2


def binarySearch(nums, start, end, target):
    if start == end and nums[start] == target:
        return start
    if start + 1 == end:
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    while start <= end:
        print(start, end)
        if (start+1) == end or start == end:
            if nums[start] == target:        
                return start
            if nums[end] == target:
                return end
            return -1
        mid = (start + end) // 2
        if start == mid and (nums[end] == target):
            return end
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            start = mid
        else:
            end = mid
    return -1


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        high = findPeakElement(nums)
        arrSize = len(nums)
        if nums[high] == target:
            return high
        if high == (len(nums) - 1):
            return binarySearch(nums, 0, arrSize - 2, target)

        if high == 0:
            return binarySearch(nums, 1, arrSize - 1, target)

        if nums[0] <= target:
            return binarySearch(nums, 0, high - 1, target)

        return binarySearch(nums, high + 1, arrSize - 1, target)


nums = [4, 5, 6, 7, 0, 1, 2]
nums= [3,5,1]
target = 1
print(Solution().search(nums, target))
