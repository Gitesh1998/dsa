def getDir(stack, current):
    if len(current) > 0:
        if current != ".." and current != ".":
            stack.append(current)
        elif len(stack) > 0 and current == "..":
            stack.pop()
            


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current = ""
        for i in path:
            if i == "/":
                getDir(stack, current)
                current = ""        
            else:
                current += i
        getDir(stack, current)
                     
        return "/"+"/".join(stack)
    
path = "/home/"
path = "/home//foo"
path = "/home/user/Documents/../Pictures"
path = "/../"
path = "/.../a/../b/c/../d/./"
path = "/a//b////c/d//././/.."
print(Solution().simplifyPath(path))