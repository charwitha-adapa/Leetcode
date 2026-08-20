class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        c=-1
        for s in word:
            c = c+1
            if s == ch:
                break
        word = list(word)
        ss = []
        for i in range(c,-1,-1):
            ss.append(word[i])
        for i in range(c+1,len(word)):
            ss.append(word[i])
        return ''.join(ss)



