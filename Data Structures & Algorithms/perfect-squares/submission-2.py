class Solution:
    def numSquares(self, n: int) -> int:
        dp={}
        def bt(target):
            if target==0:
                return 0
            if target in dp:
                return dp[target]
            res=target
            for i in range(1,target+1):
                if i*i>target:
                    break
                res=min(res,1+bt(target-i*i))
            dp[target]=res
            return res
        return bt(n)