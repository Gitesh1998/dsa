def makeZero(i, j, right, bottom, matrix):
    for k in range(0, right):
        if matrix[i][k] != 0:
            matrix[i][k] = 'x'
    
    for k in range(0, bottom):
        if matrix[k][j] != 0:
            matrix[k][j] = 'x'
            
            
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    makeZero(i, j, len(matrix[0]), len(matrix), matrix)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0
        return matrix
    
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().setZeroes(matrix))
        
        
        