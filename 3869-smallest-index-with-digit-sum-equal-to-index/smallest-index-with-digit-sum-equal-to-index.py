class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            t = nums[i]
            c = 0
            while(t>0):
                d = t%10
                c = c+d
                t = t//10
            if i == c:
                return i
                break
        return -1
        