class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            if (numbers[i] + numbers[j]) > target:
                j -= 1
            elif (numbers[i] + numbers[j]) == target:
                break
            else:
                i+=1

        return [i+1, j+1]


numbers = [2, 7, 11, 15]
target = 9
numbers = [2,3,4]
target = 6
numbers = [-1,0]
target = -1
print(Solution().twoSum(numbers, target))
