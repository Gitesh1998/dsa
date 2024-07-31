class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) == 0:
            return True
        ind = 0
        for i in t:
            if ind == len(s):
                return True
            if i == s[ind]:
                ind += 1
        if ind == len(s):
            return True
        else:
            return False
        
    

s = "abc"
t = "ahbgdc"
s = "axc"
t = "ahbgdc"
print(Solution().isSubsequence(s,t))