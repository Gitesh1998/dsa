class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
                continue
            if len(stack) == 0:
                return False
            if (i == ")" and stack[-1] != "(") or (i == "}" and stack[-1] != "{") or (i == "]" and stack[-1] != "["):
                return False
            stack.pop()
        
        
        if len(stack) > 0:
            return False
        return True
        
        
    
s = "()[]{}"
print(Solution().isValid(s))