class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        currStr = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if len(currStr):
                    return len(currStr)
            else:
                currStr += s[i]
        return len(currStr)



s = "Hello World"
# s = "   fly me   to   the moon  "
# s = "luffy is still joyboy"
print(Solution().lengthOfLastWord(s))