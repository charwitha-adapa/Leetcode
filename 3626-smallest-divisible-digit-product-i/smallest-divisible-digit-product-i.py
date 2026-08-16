def dgp(n):
    p = 1
    while n>0:
        d = n%10
        p = p*d
        n = n//10
    return p
class Solution:
    def smallestNumber(self, a: int, t: int) -> int:
        if dgp(a)%t == 0:
            print(a)
        lst = list(x for x in range(a,a+11))
        for i in lst:
            if dgp(i)%t==0:
                return i
        