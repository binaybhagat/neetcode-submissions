class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            m = (l+r)//2            
            minRate=sum([math.ceil(float(c) / m) for c in piles])
            if minRate <= h:
                res=m
                r=m-1
            else:
                l=m+1
        return res
            