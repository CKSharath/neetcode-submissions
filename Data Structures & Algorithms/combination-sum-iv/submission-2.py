class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp={0:1}
        def bt(t):
            if t in dp:
                return dp[t]
            res=0
            for i in nums:
                if t<i:
                    break
                res+=bt(t-i)
            dp[t]=res
            return dp[t]
        return bt(target)