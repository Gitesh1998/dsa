class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        hIndex = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                hIndex = i+1
        return hIndex

citations = [3,0,6,1,5]
# citations = [1,3,1]
print(Solution().hIndex(citations))