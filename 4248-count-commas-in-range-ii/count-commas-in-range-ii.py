class Solution:
    def countCommas(self, n: int) -> int:
        t = n
        s = 0
        while(n>0):
            d = n%10
            s = s+1
            n = n//10
        n = t
        if s<4:
            return 0
        elif s>=4 and s<7:
            return (n-999)
        elif s>=7 and s<10:
            return (n-999)+(n-999999)
        elif s>=10 and s<13:
            return (n-999)+(n-999999)+(n-999999999)
        elif s>=13 and s<16:
            return (n-999)+(n-999999)+(n-999999999)+(n-999999999999)
        elif s>=16 and s<19:
            return (n-999)+(n-999999)+(n-999999999)+(n-999999999999)+(n-999999999999999)
        else:
            return 0
