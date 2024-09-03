class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        bag = set()
        bag.add(s)
        dict = {}
        for i in wordDict:
            dict[i] = len(i)
                
        while bag:
            print(bag)
            newBag = set()
            for i in bag:
                for j in dict:
                   if j == i[:dict[j]] and (i[dict[j]:] not in bag):
                       if not i[dict[j]:]:
                           return True
                       newBag.add(i[dict[j]:])
            bag = newBag
            
        return False
    
s = "leetcode"
wordDict = ["leet","code"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(Solution().wordBreak(s, wordDict))