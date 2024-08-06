class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        current = False
        i, j, k, depth = 0, 0, len(matrix[0]) - 1, 0

        while True:

            for data in range(j, k + 1):
                current = True
                result.append(matrix[i][data])

            if not current:
                break

            current = False

            j = i + 1
            i = k
            k = len(matrix) - 1 - depth

            # print(i, j, k)
            # print(result)

            for data in range(j, k + 1):
                current = True
                result.append(matrix[data][i])

            if not current:
                break

            current = False

            j = i - 1
            i = k
            k = 0 + depth

            # print(i, j, k)
            # print(result)

            for data in range(j, k - 1, -1):
                current = True
                result.append(matrix[i][data])

            if not current:
                break

            current = False
            depth += 1
            j = i - 1
            i = k
            k = 0 + depth

            # print(i, j, k)
            # print(result)

            for data in range(j, k - 1, -1):
                current = True
                result.append(matrix[data][i])

            if not current:
                break

            current = False
            j = i + 1
            i = k
            k = len(matrix[0]) - 1 - depth

            # print(i, j, k)
            # print(result)

        return result


matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1,2,3,4],[12,13,14,5]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(Solution().spiralOrder(matrix))


# class Solution:
#     def spiralOrder(self, matrix: list[list[int]]) -> list[int]:            
#             res = []
#             while matrix:
#                 res.extend(matrix.pop(0))
#                 matrix = [*zip(*matrix)][::-1]
#             return res
