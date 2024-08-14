class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        if len(intervals) == 0:
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            return [newInterval, *intervals]

        if newInterval[0] > intervals[-1][1]:
            return [*intervals, newInterval]

        result = []
        i = 0
        while i < len(intervals):
            if (intervals[i][0] <= newInterval[0] <= intervals[i][1]) or (intervals[i][0] <= newInterval[1] <= intervals[i][1]) or (newInterval[0] <= intervals[i][0] <= newInterval[1]): 
                start = intervals[i][0] if intervals[i][0] < newInterval[0] else newInterval[0]
                end = intervals[i][1] if intervals[i][1] > newInterval[1] else newInterval[1]
                i+=1
                while i < len(intervals) and intervals[i][0] <= end:
                    end = intervals[i][1] if intervals[i][1] > end else end
                    i+=1
                result.append([start, end])
                return [*result, *intervals[i:]]
            elif newInterval[1] < intervals[i][0]:
                return [*result, newInterval, *intervals[i:]]
            
            result.append(intervals[i])
            i+=1
            
            
        return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

intervals = [[1,5]]
newInterval = [0,6]

print(Solution().insert(intervals, newInterval))
