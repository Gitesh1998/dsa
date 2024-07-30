class Solution:
    def reverseWords(self, s: str) -> str:
        bagOfWords = []
        currStr = ""
        for i in range(len(s)):
            if s[i] == " ":
                if len(currStr):
                    bagOfWords.append(currStr)
                currStr = ""
            else:
                currStr += s[i]
        if len(currStr):
            bagOfWords.append(currStr)
        return " ".join(bagOfWords[::-1])
        
    
    
s = "the sky is blue"
# s = "a good   example"
# s = "  hello world  "
print(Solution().reverseWords(s))