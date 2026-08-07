class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount = 0
        maxlength = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount = zeroCount +1
            #Find invalid state, until valid shrink()
            while zeroCount > k:
                #shrink
                if nums[left] == 0:
                    zeroCount = zeroCount - 1
                left = left+1
            #Update max length
            maxlength = max(maxlength, right-left+1)
        return maxlength