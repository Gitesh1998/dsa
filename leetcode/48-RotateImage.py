class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        for i in range(len(matrix)//2):
            matrix[i], matrix[len(matrix)-1-i] = matrix[len(matrix)-1-i], matrix[i]
        
        for i in range(0, len(matrix)-1):
            for j in range(i+1, len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            
        return matrix
    
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().rotate(matrix))
        