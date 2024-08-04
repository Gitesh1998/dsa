def didWeFound(i, j, board):
    countRow = 0
    countColumn = 0

    for k in range(9):
        countRow += 1 if board[i][j] == board[i][k] else 0
    for l in range(9):
        countColumn += 1 if board[i][j] == board[l][j] else 0
    return countColumn == countRow


def foundInBlock(i, j, board):
    seen = set()
    for k in range(i, i + 3):
        for l in range(j, j + 3):
            if board[k][l] == ".":
                continue
            if (board[k][l] in seen) or (not didWeFound(k, l, board)):
                return False
            if board[k][l] != ".":
                seen.add(board[k][l])
    return True


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                if not foundInBlock(i * 3, j * 3, board):
                    return False
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(Solution().isValidSudoku(board))
