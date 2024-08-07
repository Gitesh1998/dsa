class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordBag = s.split(" ")
        if len(pattern) != len(wordBag):
            return False
        
        dict = {}
        setData = set()
        for i in range(len(pattern)):
            if pattern[i] in dict:
                if dict[pattern[i]] != wordBag[i]:
                    return False
            else:
                if wordBag[i] in setData:
                    return False
                dict[pattern[i]] = wordBag[i]
                setData.add(wordBag[i])
        return True
        
    
pattern = "abba"
s = "dog cat cat dog"
pattern = "abba"
s = "dog cat cat fish"
pattern = "aaaa"
s = "dog cat cat dog"
print(Solution().wordPattern(pattern, s))