class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxavg = -10000000
        left = 0
        currentsum = 0
        for right in range(len(nums)):
            currentsum += nums[right]
            if right >= k-1:
                avg = currentsum/k
                maxavg = max(avg, maxavg)
                currentsum -= nums[left]
                left += 1
        return maxavg