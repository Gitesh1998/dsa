class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        postfix = [1]
        
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]*nums[i-1])
        for i in range(len(nums)-2, -1, -1):
            postfix.append(postfix[-1]*nums[i+1])

        postfix.reverse()
        for i in range(len(prefix)):
            prefix[i] *= postfix[i]
        return prefix
nums = [-1,1,0,-3,3]
# nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))