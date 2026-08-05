class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        mx = 0
        c = 0
        for i in range(len(nums)):
            if nums[i]==1:
                c = c+1
            if nums[i]==0:
                mx = max(c,mx)
                c = 0
        return max(mx,c)


        