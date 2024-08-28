class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        hash = {}
        
        for i in range(len(beginWord)):
            newWord = beginWord[:i] + "*" + beginWord[i+1:]
            if newWord in hash.keys():
                hash[newWord].add(beginWord)
            else:
                # hash[newWord] = [beginWord]
                hash[newWord] = set()
                hash[newWord].add(beginWord)
        
        
        for i in wordList:
            for j in range(len(i)):
                newWord = i[:j] + "*" + i[j+1:]
                if newWord in hash.keys():
                    hash[newWord].add(i)
                else:
                    hash[newWord] = set()
                    hash[newWord].add(i)
                    
        data = set()
        visited = set()
        data.add(beginWord)
        count = 1
        while count <= len(wordList):
            print(data, visited)
            count += 1
            newData = set()
            for i in data:
                visited.add(i)
                for j in range(len(i)):
                    newWord = i[:j] + "*" + i[j+1:] 
                    newData = newData | set(hash[newWord])
                    newData.difference_update(visited)
            data = newData
            # print(data)
            if endWord in newData:
                return count
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))