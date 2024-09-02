class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        if n == 1:
            return a
        for _ in range(2, n + 1):
            a, b = b, b + a
        return b


n = 1
print(Solution().climbStairs(n))
