class Solution:
    def trap(self, height: list[int]) -> int:
        leftMax = [height[0]]
        
        for i in range(1, len(height)):
            if height[i] > leftMax[-1]:
                leftMax.append(height[i])
            else:
                leftMax.append(leftMax[-1])
        
        totalWater = 0
        lastMax = height[-1]
        for i in range(len(height)-2, -1, -1):
            if height[i] > lastMax:
                lastMax = height[i]
            totalWater += (min(lastMax, leftMax[i]) - height[i])
        return totalWater
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))