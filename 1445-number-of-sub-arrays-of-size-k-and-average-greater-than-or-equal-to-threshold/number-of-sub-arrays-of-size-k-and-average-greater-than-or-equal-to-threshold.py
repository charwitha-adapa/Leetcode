class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        c = 0
        currsum = 0
        left = 0
        for right in range(len(arr)):
            currsum = currsum + arr[right]
            if right>=k-1:
                avg = currsum/k
                if avg>=threshold:
                    c = c+1
                currsum = currsum - arr[left]
                left = left + 1

        return c

        