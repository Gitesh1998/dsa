class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = {}

        for i in magazine:
            if i in magDict:
                magDict[i] += 1
            else:
                magDict[i] = 1

        for j in ransomNote:
            if j not in magDict:
                return False
            if j in magDict and magDict[j] < 1:
                return False
            magDict[j] -= 1
            

        return True


ransomNote = "a"
magazine = "b"
ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine))
