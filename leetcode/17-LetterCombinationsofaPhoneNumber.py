# def getWord(numDict, digits, words):
#     if not digits:
#         return
#     newWord
#     for i in words


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        numDict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        if not digits:
            return []
        
        words = numDict[digits[0]]
        
        for i in digits[1:]:
            tempWord = []
            for j in words:
                for k in numDict[i]:
                    tempWord.append(j+k)
            words = tempWord
        
        return words
        


digits = "234"
print(Solution().letterCombinations(digits))
