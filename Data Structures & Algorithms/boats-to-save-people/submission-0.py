class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        l=0
        r=n-1
        res=0
        people.sort()
        while l<=r:
            v=limit-people[r]
            r-=1
            res+=1
            if l<=r and v-people[l]>=0:
                l+=1
        return res