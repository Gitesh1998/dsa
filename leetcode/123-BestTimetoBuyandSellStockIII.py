class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        minVals = []
        maxVals = []

        minVal = prices[0]
        minProfit = 0
        for i in prices:
            if i < minVal:
                minVal = i
            if (i - minVal) > minProfit:
                minProfit = i - minVal
            minVals.append(minProfit)

        maxVal = prices[-1]
        maxProfit = 0
        for i in prices[::-1]:
            if i > maxVal:
                maxVal = i
            if (maxVal - i) > maxProfit:
                maxProfit = maxVal - i
            maxVals.append(maxProfit)
        maxVals = maxVals[::-1]
        result = 0
        for i in range(1, len(prices)):
            if (minVals[i - 1] + maxVals[i]) > result:
                result = minVals[i - 1] + maxVals[i]
        return max(result, maxVals[0])


prices = [3, 3, 5, 0, 0, 3, 1, 4]
prices = [1, 2, 3, 4, 5]
prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
print(Solution().maxProfit(prices))
