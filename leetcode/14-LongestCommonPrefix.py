class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        char = [i for i in strs[0]]
        count = [1 for _ in strs[0]]
        totalLen = len(char)
        for i in strs:
            for j in range(len(i)):
                if j >= totalLen:
                    break
                if i[j] == char[j]:
                    count[j] += 1
                else:
                    break
        result = ""
        totalStr = len(strs)
        for i in range(len(count)):
            if count[i] == (totalStr+1):
                result += char[i] 
        return result
    
   
strs = ["flower","flow","flight"] 
strs = ["dog","racecar","car"]
print(Solution().longestCommonPrefix(strs))