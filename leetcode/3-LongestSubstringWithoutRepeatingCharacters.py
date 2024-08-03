class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setA = list()
        leng = 0
        j = 0
        for ind, i in enumerate(s):
            if i in setA:
                if leng < ind - j:
                    leng = ind - j
                while i in setA:
                    del setA[0]
                    j+=1
            setA.append(i)
            
        return leng if leng > len(setA) else len(setA)                
        
        
    
s = "abcabcbb"  
s = "bbbbb"
s = "pwwkew"
s = "b"
print(Solution().lengthOfLongestSubstring(s))    
    