class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<=r:
            m=(l+r)//2

            reqDay=1
            cap=0
            for w in weights:
                if cap+w>m:
                    reqDay+=1
                    cap=0
                cap+=w
            if reqDay<=days:
                r=m-1
            else:
                l=m+1
        return l
