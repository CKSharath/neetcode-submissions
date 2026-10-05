class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def bt(i,s):
            if i==len(nums):
                return s==target
            if i in dp:
                return dp[i]
            res= bt(i+1,s+nums[i])+bt(i+1,s-nums[i])
            dp[i]=res
            return dp[i]
        return bt(0,0)