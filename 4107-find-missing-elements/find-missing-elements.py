class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mx = max(nums)
        mn = min(nums)
        lst = list(x for x in range(mn, mx+1))
        ans = []
        for i in lst:
            if i not in nums:
                ans.append(i)
        return ans
        