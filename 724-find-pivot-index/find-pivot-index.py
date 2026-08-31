class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p = [0]
        n = len(nums)
        s = 0
        for i in range(n):
            s = s+nums[i]
            p.append(s)
        print(p)
        r = 0
        l = 0
        for i in range(len(p)-1):
            l = p[i]
            r = p[n]-p[i+1]
            if l==r:
                return i
        return -1        