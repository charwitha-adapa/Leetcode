class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c = 1
        m = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c = c+1
            else:
                m = max(m,c)
                c = 1
        return max(c,m)
        