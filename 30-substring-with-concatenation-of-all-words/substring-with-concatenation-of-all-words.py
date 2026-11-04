from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        target = Counter(words)
        result = []

        for i in range(len(s) - total_len + 1):

            substring = s[i:i + total_len]

            extracted = []

            for j in range(0, total_len, word_len):
                chunk = substring[j:j + word_len]
                extracted.append(chunk)

            if Counter(extracted) == target:
                result.append(i)

        return result