def getJustifiedString(strData, maxWidth):
    strings = strData.split(" ")
    totalString = len(strings)
    totalSpaces = (maxWidth - len(strData)) + (totalString - 1)
    if totalString == 1:
        return strData + (" " * totalSpaces)
    if totalString == 2:
        return strings[0] + (" " * totalSpaces) + strings[1]

    spaces = ["" for _ in range(totalString - 1)]
    space = totalSpaces // (totalString - 1)
    for i in range(len(spaces)):
        spaces[i] = " " * space

    i = 0
    space = totalSpaces % (totalString - 1)
    while space > 0:
        spaces[i] = spaces[i] + " "
        space -= 1
        i += 1
    result = ""
    for i in range(len(spaces)):
        result += strings[i] + spaces[i]
    return result + strings[-1]


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        curLineStr = ""
        result = []
        for i in words:
            if len(curLineStr + " " + i) > maxWidth:
                if len(curLineStr) == 0 and len(i) == maxWidth:
                    result.append(i)
                else:
                    result.append(getJustifiedString(curLineStr, maxWidth))
                    curLineStr = i
            else:
                if len(curLineStr):
                    curLineStr += " " + i
                else:
                    curLineStr = i
                    
        if len(curLineStr):
            result.append(curLineStr + (" " * (maxWidth - len(curLineStr))))
        return result


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
words = ["What", "must", "be", "acknowledgment", "shall", "be"]
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
words = ["Listen", "to", "many,", "speak", "to", "a", "few."]
maxWidth = 6
print(Solution().fullJustify(words, maxWidth))
