class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Step 1: Compute the frequencies of string p
        d2 = {}
        for i in p:
            d2[i] = d2.get(i, 0) + 1
        #Step 2: Do a k-length sliding window on s
        #Count the frequencies of charchters in substring into d1
        k = len(p)
        d1 = {}
        left = 0
        ans=[]
        #Count frequency of substring k
        for right in range(len(s)):
            d1[s[right]] = d1.get(s[right],0)+1
            #Checking Validity of window
            if right >= k-1:
                if d1==d2:
                    ans.append(left)
                #remove outgoing element i.e left
                d1[s[left]] = d1[s[left]] - 1
                if d1[s[left]]==0:
                    d1.pop(s[left])
                left = left + 1
        return ans

        