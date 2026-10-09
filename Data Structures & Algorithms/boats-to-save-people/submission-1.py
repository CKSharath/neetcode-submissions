class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        res=0
        r=len(people)-1
        while l<=r:
            rem=limit-people[r]
            res+=1
            if rem>=people[l]:
                l+=1
            r-=1
        return res