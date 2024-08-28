class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        param = ["()" for _ in range(n)]
        print(param)
        s = set()
        result = ["()"]
        for i in param[1:]:
            temp = []
            for j in result:
                for ind, val in enumerate(j):
                    tempString = f"{j[:ind]}{i}{j[ind:]}"
                    if tempString in s:
                        continue
                    temp.append(f"{j[:ind]}{i}{j[ind:]}")
                    s.add(f"{j[:ind]}{i}{j[ind:]}")
            result = temp
        return result
    
n = 3
print(Solution().generateParenthesis(n))