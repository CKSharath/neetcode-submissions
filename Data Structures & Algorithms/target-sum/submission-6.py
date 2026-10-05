class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def bt(i,s):
            if i==len(nums):
                return s==target
            if (i,s) in dp:
                return dp[(i,s)]
            res= bt(i+1,s+nums[i])+bt(i+1,s-nums[i])
            dp[(i,s)]=res
            return dp[(i,s)]
        return bt(0,0)