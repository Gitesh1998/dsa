class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        
        result = []
        for i in range(1, len(intervals)):
            if end < intervals[i][0]:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            elif intervals[i][0] <= end < intervals[i][1]:
                end = intervals[i][1]
                
        result.append([start, end])
        return result
    
    

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
intervals = [[1,4],[0,4]]
print(Solution().merge(intervals))