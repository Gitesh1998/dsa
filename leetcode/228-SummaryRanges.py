class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        i = 1
        
        result = []
        start = nums[0]
        end = nums[0]
        while i < len(nums):
            if end+1 == nums[i]:
                end += 1
            elif end == start:
                result.append(f"{end}")
                start, end = nums[i], nums[i]
            else:
                result.append(f"{start}->{end}")
                start, end = nums[i], nums[i]
            i+=1
            
        if start == end:
            result.append(f"{end}")
        else:
            result.append(f"{start}->{end}")
            
        return result

        
nums = [0,1,2,4,5,7]
# nums = [0,2,3,4,6,8,9]
print(Solution().summaryRanges(nums))