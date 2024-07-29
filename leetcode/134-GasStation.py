class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        # diff = []
        sumVal = 0
        ind = 0
        for i in range(len(gas)):
            if sumVal + (gas[i]-cost[i]) < 0:
                ind = i+1
                sumVal = 0
            else:
                sumVal+=(gas[i]-cost[i])
        return ind
    
    
    
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]

# gas = [2,3,4]
# cost = [3,4,3]
print(Solution().canCompleteCircuit(gas, cost))