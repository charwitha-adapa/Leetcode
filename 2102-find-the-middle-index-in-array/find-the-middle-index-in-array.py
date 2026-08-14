class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = list(itertools.accumulate(nums, initial=0))
        for i in range(len(nums)):
            l_sum = prefix_sum[i]
            print(l_sum)
            r_sum = prefix_sum[len(nums)]-prefix_sum[i+1]
            print(r_sum)
            if l_sum == r_sum:
                return i
       
        return -1
        