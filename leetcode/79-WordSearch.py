def dfs(board, visited, result, i, j):
    if not result:
        return True
    temp = f"{i}{j}"
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (temp in visited):
        return False
    
    if board[i][j] != result[0]:
        return False
    s = set(visited)
    s.add(temp)
    return (
        dfs(board, s, result[1:], i + 1, j)
        or dfs(board, s, result[1:], i, j + 1)
        or dfs(board, s, result[1:], i - 1, j)
        or dfs(board, s, result[1:], i, j - 1)
    )


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    s = set()
                    if dfs(board, s, word, i, j):
                        return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
board = [["A"]]
word = "A"
print(Solution().exist(board, word))
