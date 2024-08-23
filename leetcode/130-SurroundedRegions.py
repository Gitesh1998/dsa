import copy


def search(grid, visited, x, y):
    if (
        x < 0
        or y < 0
        or x >= len(grid)
        or y >= len(grid[0])
        or grid[x][y] == "X"
        or visited[x][y] == 1
    ):
        return
    visited[x][y] = 1
    grid[x][y] = 1

    search(grid, visited, x - 1, y)
    search(grid, visited, x, y - 1)
    search(grid, visited, x + 1, y)
    search(grid, visited, x, y + 1)


class Solution:
    def solve(self, board: list[list[str]]) -> None:

        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board[0])):
            if board[0][i] == "O":
                visi = copy.deepcopy(visited)
                search(board, visi, 0, i)
            if board[len(board) - 1][i] == "O":
                visi = copy.deepcopy(visited)
                search(board, visi, len(board) - 1, i)

        for i in range(1, len(board) - 1):
            if board[i][0] == "O":
                visi = copy.deepcopy(visited)
                search(board, visi, i, 0)
            if board[i][len(board[0])-1] == "O":
                visi = copy.deepcopy(visited)
                search(board, visi, i, len(board[0])-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == 1:
                    board[i][j] = "O"
        print(board)

board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]

board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
]
print(Solution().solve(board))
