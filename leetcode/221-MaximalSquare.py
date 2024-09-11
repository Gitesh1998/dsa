class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        box = [[0 for _ in (matrix[0])] for _ in matrix]
        maxNum = 0
        for i in range(len(matrix[0])):
            if matrix[0][i] == "1":
                box[0][i] = 1
                maxNum = 1

        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                box[i][0] = 1
                maxNum = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "1":
                    if box[i - 1][j - 1] and box[i - 1][j] and box[i][j - 1]:
                        box[i][j] = (
                            min(box[i - 1][j - 1], box[i - 1][j], box[i][j - 1]) + 1
                        )
                    else:
                        box[i][j] = 1
                maxNum = max(maxNum, box[i][j])

        return maxNum**2


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
matrix = [["0", "1"], ["1", "0"]]
matrix = [["0"]]
# matrix = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"],
#     ["0", "0", "1", "1", "1"],
# ]
print(Solution().maximalSquare(matrix))
