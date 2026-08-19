class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}

        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        res = list(d.values())
        return len(res) == len(set(res))        