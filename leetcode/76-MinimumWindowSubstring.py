class Solution:
    def minWindow(self, s: str, t: str) -> str:

        result = ""

        if len(s) < len(t):
            return result

        charDict = {}
        j = 0
        totalLeng = len(t)

        for i in t:
            if i not in charDict:
                charDict[i] = 1
            else:
                charDict[i] += 1

        for i, val in enumerate(s):
            if (totalLeng == 0) and ((len(result) == 0) or (len(result) > (i - j))):
                result = s[j:i]

            if val in charDict:
                if charDict[val] > 0:
                    charDict[val] -= 1
                    totalLeng -= 1
                else:
                    while charDict[val] < 1:
                        if s[j] in charDict:
                            charDict[s[j]] += 1
                            totalLeng += 1
                        j+=1
                    while s[j] not in charDict:
                        j += 1
                    charDict[val] -= 1
                    totalLeng -= 1

            if totalLeng == len(t):
                j += 1
             
            print(j, i, s[j:i+1], totalLeng)
             
              
        print("final")
        print(j, i, s[j:i+1], totalLeng)

        if (totalLeng == 0) and ((len(result) == 0) or (len(result) > (i+1 - j))):
                result = s[j:i+1]
        return result            
            

s = "ADOBECODEBANC"
t = "ABC"
s = "a"
t = "a"
# s = "a"
# t = "aa"
s = "ab"
t = "b"
print(Solution().minWindow(s, t))
