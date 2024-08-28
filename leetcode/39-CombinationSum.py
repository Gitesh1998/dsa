def temp(result, current, cand, sum, target):
    if sum == target:
        result.append(current)
        return
    if sum > target:
        return

    for ind, i in enumerate(cand):
        tempV = [*current, i]
        tempSum = sum + i
        temp(result, tempV, cand[ind:], tempSum, target)


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        temp(result, [], candidates, 0, target)
        return result


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
