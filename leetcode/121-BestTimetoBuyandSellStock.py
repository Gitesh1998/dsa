class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min,max=prices[0],0
        for i in (prices):
            print(min, max, i)
            if i < min :
                min = i
            elif i-min > max:
                max = i-min
        return max


prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
