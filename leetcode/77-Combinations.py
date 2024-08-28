def back(result, current, last, k):
    print(result, current, last, k)
    if len(current) == k:
        result.append(current)
        return

    for ind, val in enumerate(last):
        newCurrent = [*current, val]
        back(result, newCurrent, last[ind + 1 :], k)


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        currNum = [i for i in range(1, n + 1)]
        result = []
        for ind, val in enumerate(currNum):
            back(result, [val], currNum[ind + 1 :], k)
        return result


n = 4
k = 3
print(Solution().combine(n, k))
