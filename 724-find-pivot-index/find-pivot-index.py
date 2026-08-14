import itertools
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = list(itertools.accumulate(nums,initial=0))
        for i in range(len(nums)):
            l_sum = prefix_sum[i]
            r_sum = prefix_sum[n] - prefix_sum[i+1]
            if l_sum==r_sum:
                return i
                break      
        else:
            return -1 
        