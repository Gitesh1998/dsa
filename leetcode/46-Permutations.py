def data(result, current, last):
    if not last:
        result.append(current)
        return

    for ind, val in enumerate(last):
        temp = [*last[: ind], *last[ind + 1 :]]
        temp1 = [*current, val]
        data(result, temp1, temp)


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        data(result, [], nums)        
        return result


nums = [1, 2, 3]
nums = [1]
print(Solution().permute(nums))
