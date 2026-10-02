class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res=0
        n=len(customers)
        for i in range(n):
            if not grumpy[i]:
                res+=customers[i]
        ans=res
        for i in range(n-minutes+1):
            res2=0
            for j in range(i,i+minutes):
                if grumpy[j]:
                    res2+=customers[j]
                res=max(res,res2+ans)
        return res
