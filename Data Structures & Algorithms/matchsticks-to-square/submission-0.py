class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sm=sum(matchsticks)

        if sm%4!=0:
            return False
        side=sm//4
        matchsticks.sort(reverse=True)

        sides=[0,0,0,0]

        def bt(i):
            if i==len(matchsticks):
                return True
            v=matchsticks[i]
            for j in range(4):
                if sides[j]+v<=side:
                    sides[j]+=v

                    if bt(i+1):
                        return True
                    sides[j]-=v
            return False
        return bt(0)
            
