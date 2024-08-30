class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        print(left)

        if left == len(matrix):
            if target > matrix[len(matrix)-1][len(matrix[0])-1]:
                return False
            
        if not left and matrix[0][0] > target:
            return False

        
        temp = matrix[left - 1]
        start, end = 0, len(temp) - 1
        while start <= end:
            if start == end:
                if temp[start] == target:

                    return True
                return False
            mid = (start+end)//2
            if temp[mid] == target:
                return True
            if temp[mid] < target:
                start = mid+1
            else:
                end = mid

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 30
# matrix = [[1,3]]
# target = 3
print(Solution().searchMatrix(matrix, target))
