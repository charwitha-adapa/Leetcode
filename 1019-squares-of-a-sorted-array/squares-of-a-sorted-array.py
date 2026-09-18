class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        x = [i*i for i in nums]
        x.sort()
        return x