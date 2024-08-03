import copy

def didWeGet(s, diction, lenoFWorld):
    if len(s) == 0:
        return True
    if s[:lenoFWorld] in diction.keys() and (diction[s[:lenoFWorld]] > 0):
        diction[s[:lenoFWorld]] -= 1
        return didWeGet(s[lenoFWorld:], diction, lenoFWorld)
    return False


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        result = []
        word_count = {}
        wordLength = len(words[0])
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        lengthOfS = len(words) * len(words[0])
        for ind, val in enumerate(s):
            newWordCount = copy.deepcopy(word_count)
            if ind + lengthOfS > len(s): 
                break
            if s[ind:ind+wordLength] in newWordCount.keys() and (
                newWordCount[s[ind:ind+wordLength]] > 0
            ):
                newWordCount[s[ind:ind+wordLength]] -= 1
                if didWeGet(s[ind+wordLength:ind+lengthOfS], newWordCount, wordLength):
                    result.append(ind)
                          
        return result


# s = "barfoothefoobarman"
# words = ["foo", "bar"]
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
# s = "wordgoodgoodgoodbestword"
# words = ["word", "good", "best", "good"]

s = "a"
words = ["a"]

s = "bcabbcaabbccacacbabccacaababcbb"
words = ["c", "b", "a", "c", "a", "a", "a", "b", "c"]
print(Solution().findSubstring(s, words))
