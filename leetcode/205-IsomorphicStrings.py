class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        setData = set()
        for i in range(len(s)):
            if s[i] in dict:
                if dict[s[i]] != t[i]:
                    return False
            else:
                if t[i] in setData:
                    return False
                dict[s[i]] = t[i]
                setData.add(t[i])
        return True
    
s = "egg"
t = "add"
s = "foo"
t = "bar"
s = "paper"
t = "title"
s = "badc"
t = "baba"
print(Solution().isIsomorphic(s, t))