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
        if (start + 1) == end or start == end:
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


def findLast(nums, start, end, target, result):
    if start > end:
        return result
    if start == end:
        if nums[start] == target:
            return start
        else:
            return result
    val = binarySearch(nums, start, end, target)
    if val == -1:
        return result
    return findLast(nums, start + 1, end, target, val)


def findFirst(nums, start, end, target, result):
    if start > end:
        return result
    if start == end:
        if nums[start] == target:
            return start
        else:
            return result
    val = binarySearch(nums, start, end, target)
    if val == -1:
        return result
    return findFirst(nums, start, end - 1, target, val)

nums = [1, 2, 3, 3, 3, 3]


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        arrSize = len(nums)
        if arrSize == 0:
            return [-1, -1]
        if arrSize == 1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]

        pos = binarySearch(nums, 0, len(nums) - 1, target)
        print(pos, findFirst(nums, 0, pos, target, pos), findLast(nums, pos, arrSize - 1, target, pos))
        if pos == -1:
            return [-1, -1]

        return [
            findFirst(nums, 0, pos, target, pos),
            findLast(nums, pos, arrSize - 1, target, pos),
        ]


nums = [5, 7, 7, 8, 8, 10]
nums = [1, 2, 3, 3, 3, 3, 4, 5, 9]
target = 3
print(Solution().searchRange(nums, target))
