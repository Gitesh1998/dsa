class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for i in s:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] = 1
                
        for i in t:
            if i not in dict:
                return False
            elif dict[i] < 1:
                return False
            dict[i] -= 1
            
        for i in dict:
            if dict[i] != 0:
                return False
        
        return True
    
s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))