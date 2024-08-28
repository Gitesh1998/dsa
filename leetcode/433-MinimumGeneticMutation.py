def isSingleMutation(f, s):
    count = 0
    for ind, val in enumerate(f):
        if val != s[ind]:
            count += 1
    if count == 1:
        return True
    return False


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if not bank:
            return -1
        count = 0
        visited = set()
        currentBank = [startGene]

        tempBank = []
        while currentBank:
            for i in currentBank:
                for j in bank:
                    if j in visited:
                        continue
                    if isSingleMutation(i, j):
                        if j == endGene:
                            return count + 1
                        visited.add(j)
                        tempBank.append(j)
            currentBank = tempBank
            tempBank = []
            count += 1
        return -1


startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
print(Solution().minMutation(startGene, endGene, bank))
