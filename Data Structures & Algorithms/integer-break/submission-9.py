class Solution:
    def integerBreak(self, n: int) -> int:
        dp={1:1}
        def bt(num):
            if num in dp:
                return dp[num]
            if num==1:
                return 1
            res=0 if n==num else num
            for i in range(1,num):
                v=bt(i)*bt(num-i)
                res=max(res,v)
            dp[num]=res
            return dp[num]
        return bt(n)
        