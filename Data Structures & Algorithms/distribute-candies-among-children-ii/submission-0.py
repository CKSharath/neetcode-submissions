class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res=0
        for a in range(min(n,limit)+1):
            for b in range(min(n-a,limit)+1):
                if n-a-b<=limit:
                    res+=1
        return res