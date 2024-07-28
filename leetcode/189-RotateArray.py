class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        rotateNum = k%len(nums)
        newNum = nums[:len(nums)-rotateNum]
        for i in range(rotateNum):
            nums[i] = nums[i+len(newNum)]
        for i in range(rotateNum, len(nums)):
            nums[i] = newNum[i-rotateNum]

nums = [1,2,3,4,5,6,7]
k = 6  
print(Solution().rotate(nums, k))
print(nums)