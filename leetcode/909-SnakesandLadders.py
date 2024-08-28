class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        newBo = []
        dir = True
        for v in board[::-1]:
            if dir:
                newBo = newBo + v
                dir = False
            else:
                dir = True
                newBo = newBo + v[::-1]
        for i in range(len(newBo)):
            if newBo[i] != -1:
                newBo[i] -= 1
        visited = set()
        visited.add(0)
        count = 0
        boardLen = len(newBo) - 1
        while boardLen > count:
            print(visited)
            newVisited = set()
            for i in visited:
                if i >= boardLen:
                    return count
                for j in range(1, 7):
                    if i + j <= boardLen:
                        if newBo[i + j] != -1:
                            if newBo[i + j] not in visited and newBo[i + j] not in newVisited:
                                newVisited.add(newBo[i + j])
                        elif (i + j) not in visited and (i + j) not in newVisited:
                            newVisited.add(i + j)
            visited = newVisited
            count += 1
        return -1

board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1],
]
print(Solution().snakesAndLadders(board))