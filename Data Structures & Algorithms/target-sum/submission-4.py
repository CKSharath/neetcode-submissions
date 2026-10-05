class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def bt(i,s):
            if i==len(nums):
                return s==target
            return bt(i+1,s+nums[i])+bt(i+1,s-nums[i])
        return bt(0,0)