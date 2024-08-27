def search(grid, visited, x, y):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == "0" or visited[x][y]:
        return
    visited[x][y] = 1
    search(grid, visited, x - 1, y)
    search(grid, visited, x, y - 1)
    search(grid, visited, x + 1, y)
    search(grid, visited, x, y + 1)


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == '1') and not visited[i][j]:
                    count += 1
                    search(grid, visited, i, j)
        return count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))
