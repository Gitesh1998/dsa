class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    
        if newInterval[1] < intervals[0][0]:
            return [newInterval, *intervals]
    
        if newInterval[0] > intervals[-1][1]:
            return [*intervals, newInterval]
    
    
        start = newInterval[0] if newInterval[0] < intervals[0][0] else intervals[0][0]
        print(start)
    
        return True
    
    
intervals = [[1,3],[6,9]]
newInterval = [2, 5]
print(Solution().insert(intervals, newInterval))