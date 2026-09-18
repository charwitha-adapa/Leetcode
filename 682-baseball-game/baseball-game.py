class Solution:
    def calPoints(self, ops: list[str]) -> int:
        l = []
        for i in ops:
            x = len(l)
            if i=="+":
                l.append(l[x-1]+l[x-2])
            elif i=="C":
                l.remove(l[x-1])
            elif i== "D":
                l.append((l[x-1])*2)
            else:
                l.append(int(i))
        return sum(l)