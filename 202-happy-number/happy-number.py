class Solution:
    def isHappy(self, n: int) -> bool:
        t = n
        sum = 0
        while(t>0):
            d = t%10
            sum = sum + (d*d)
            t = t//10
        if sum > 9:
            return self.isHappy(sum)
        elif sum==1 or sum==7:
            return True
        else:
            return False
        