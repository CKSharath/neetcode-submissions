class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res=0
        n=len(customers)
        for i in range(n):
            if grumpy[i]==0:
                res+=customers[i]
        curr=res
        for r in range(n-minutes+1):
            res2=0
            for j in range(r,r+minutes):
                if grumpy[j]==1:
                    res2+=customers[j]
            res=max(res2+curr,res)
        return res
