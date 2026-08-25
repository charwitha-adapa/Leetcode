class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        l = len(nums)
        lst = []
        for i in range(1,l+10):
            lst.append(k*i)
        for i in lst:
            if i not in nums:
                return i
                break

        