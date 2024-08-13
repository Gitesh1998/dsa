class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        dict = {}
        for i in nums:
            dict[i] = 1
        
        for i in nums:
            if i-1 in dict:
                continue
            count = 1
            start = i
            while True:
                if start+1 in dict:
                    count += 1
                    start += 1
                else:
                    break
            dict[i] = count
        
        result = 1
        for i in dict:
            result = dict[i] if dict[i] > result else result
        return result


    
nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums))