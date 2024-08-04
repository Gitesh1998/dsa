class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = len(words) * word_len
        word_freq = {}
        res = []

        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        if len(s) < total_len:
            return res

        for i in range(word_len):
            window_freq = {}
            left = i
            right = i
            count = 0

            while right + word_len <= len(s):
                chunk = s[right:right + word_len]
                right += word_len
                if chunk in word_freq:
                    if chunk in window_freq:
                        window_freq[chunk] += 1
                    else:
                        window_freq[chunk] = 1
                    count += 1

                    while window_freq[chunk] > word_freq[chunk]:
                        left_chunk = s[left:left + word_len]
                        window_freq[left_chunk] -= 1
                        left += word_len
                        count -= 1

                    if count == len(words):
                        res.append(left)
                else:
                    window_freq = {}
                    left = right
                    count = 0

        return res

# Example usage
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(Solution().findSubstring(s, words))  # Output: [0, 9]
