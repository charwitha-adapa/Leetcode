class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        chars = sorted(count, key=count.get, reverse=True)

        ans = ""

        for ch in chars:
            ans += ch * count[ch]

        return ans