class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1

        result = (height[i] if height[i] < height[j] else height[j]) * (j - i)

        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            if result < ((height[i] if height[i] < height[j] else height[j]) * (j - i)):
                result = (height[i] if height[i] < height[j] else height[j]) * (j - i)

        return result


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1,1]
print(Solution().maxArea(height))
