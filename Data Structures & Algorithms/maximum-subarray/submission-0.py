class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms,cs=nums[0],0
        for n in nums:
            if cs<0:
                cs=0
            cs+=n
            ms=max(ms,cs)
        return ms