class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        amo = [amount for _ in range(amount+1)]
        amo[0] = 0

        for i in coins:
            if i > amount:
                continue
            amo[i] = 1

        print(amo)

        for i in range(1, amount+1):
            for j in coins:
                if j <= i:
                    amo[i] = min(amo[i-j]+1, amo[i])              
                    
        if amo[-1] == amount and 1 not in coins:
            return -1
        return amo[-1]

coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))
