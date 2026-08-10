class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c =[]
        word1 = list(word1)
        word2 = list(word2)
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                c.append(word1[i])
            if i < len(word2):
                c.append(word2[i])
        return ''.join(c)
