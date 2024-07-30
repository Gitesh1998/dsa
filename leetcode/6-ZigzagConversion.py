class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (len(s) < numRows) or (numRows == 1):
            return s

        zigZag = ["" for _ in range(numRows)]
        isDown = True
        currInd = 0
        for i in s:
            zigZag[currInd]+=i
            if isDown:
                currInd += 1
            else:
                currInd -= 1

            if currInd == (len(zigZag) - 1):
                isDown = False
            elif currInd == 0:
                isDown = True

        return "".join(zigZag) 


s = "PAYPALISHIRING"
numRows = 3
print(Solution().convert(s, numRows))
