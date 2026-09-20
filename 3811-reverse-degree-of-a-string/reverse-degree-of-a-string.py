class Solution:
    def reverseDegree(self, q: str) -> int:
        s = 0
        q = list(q)
        z = 1
        for i in range(len(q)):
            a = (26 - (ord(q[i]) - ord('a'))) * z
            s = s+a
            z = z+1
        return s
        