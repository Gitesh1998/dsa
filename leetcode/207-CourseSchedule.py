

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        dict = {}
        for i in prerequisites:
            if i[0] in dict:
                i[0].append(i[1])
            else:
                dict[i[0]] = [i[1]]
                
        print(dict)
        
        return True
    
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(Solution().canFinish(numCourses, prerequisites))