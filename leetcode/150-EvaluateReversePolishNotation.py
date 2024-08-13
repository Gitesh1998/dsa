class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for i in tokens:
            print(stack)
            if i == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second+first))
            elif i == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second-first))
            elif i == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second*first))
            elif i == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second/first))
            else:
                stack.append(int(i))
        
        return stack.pop()
    
    
tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["4","13","5","/","+"]
print(Solution().evalRPN(tokens))