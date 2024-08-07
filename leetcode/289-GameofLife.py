def count1s(i, j, right, bottom, board):
    con = 0
    if (
        (0 <= (i - 1) < bottom)
        and (0 <= (j - 1) < right)
        and (board[i - 1][j - 1] == 1 or board[i - 1][j - 1] == "-x")
    ):
        con += 1

    if (
        (0 <= (i - 1) < bottom)
        and (0 <= (j) < right)
        and (board[i - 1][j] == 1 or board[i - 1][j] == "-x")
    ):
        con += 1

    if (
        (0 <= (i - 1) < bottom)
        and (0 <= (j + 1) < right)
        and (board[i - 1][j + 1] == 1 or board[i - 1][j + 1] == "-x")
    ):
        con += 1

    if (
        (0 <= (i) < bottom)
        and (0 <= (j - 1) < right)
        and (board[i][j - 1] == 1 or board[i][j - 1] == "-x")
    ):
        con += 1

    if (
        (0 <= (i) < bottom)
        and (0 <= (j + 1) < right)
        and (board[i][j + 1] == 1 or board[i][j + 1] == "-x")
    ):
        con += 1

    if (
        (0 <= (i + 1) < bottom)
        and (0 <= (j - 1) < right)
        and (board[i + 1][j - 1] == 1 or board[i + 1][j - 1] == "-x")
    ):
        con += 1

    if (
        (0 <= (i + 1) < bottom)
        and (0 <= (j) < right)
        and (board[i + 1][j] == 1 or board[i + 1][j] == "-x")
    ):
        con += 1

    if (
        (0 <= (i + 1) < bottom)
        and (0 <= (j + 1) < right)
        and (board[i + 1][j + 1] == 1 or board[i + 1][j + 1] == "-x")
    ):
        con += 1

    return con


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        right = len(board[0])
        bottom = len(board)
        for i in range(bottom):
            for j in range(right):
                total1s = count1s(i, j, right, bottom, board)
                if (total1s < 2 or total1s > 3) and (board[i][j] == 1):
                    board[i][j] = "-x"
                if (total1s == 3) and (board[i][j] == 0):
                    board[i][j] = "x"


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "-x":
                    board[i][j] = 0
                elif board[i][j] == "x":
                    board[i][j] = 1

        return board


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
board = [[1,1],[1,0]]

print(Solution().gameOfLife(board))
