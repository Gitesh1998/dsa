class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1


haystack = "thissadbutsad"
needle = "sad"
# haystack = "leetcode"
# needle = "leeto"

haystack = "a"
needle = "a"
print(Solution().strStr(haystack, needle))