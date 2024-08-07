class Solution:
    def isHappy(self, n: int) -> bool:
        dict = {}
        while True:
            strs = str(n)
            sums = 0
            for i in strs:
                sums += (int(i)*int(i))    
            if sums == 1:
                return True
            if sums in dict:
                return False
            n = sums
            dict[sums] = True

n = 19
print(Solution().isHappy(n))