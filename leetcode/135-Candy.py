class Solution:
    def candy(self, ratings: list[int]) -> int:
        leftSide = [1]
        rightSide = [1]
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                leftSide.append(leftSide[-1]+1)
            else:
                leftSide.append(1)
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rightSide.append(rightSide[-1]+1)
            else:
                rightSide.append(1)
        
        rightSide = rightSide[::-1]
        
        sumEle = 0
        for i in range(len(ratings)):
            sumEle += max(leftSide[i], rightSide[i])
        return sumEle
        
ratings = [1,0,2]
# ratings = [1,3,2,2,1]
print(Solution().candy(ratings))