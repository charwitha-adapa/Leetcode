class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if ord(s[i])>64 and ord(s[i])<91:
                z = (ord(s[i]))+32
                s[i] = chr(z)
        return "".join(s)
        