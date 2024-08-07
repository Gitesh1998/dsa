class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        listN = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in listN:
                listN[key].append(i)
            else:
                listN[key] = [i]
        result = []
        for i in listN.keys():
            result.append(listN[i])
        return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
