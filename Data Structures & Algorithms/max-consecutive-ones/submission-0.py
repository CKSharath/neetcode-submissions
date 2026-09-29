class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        r=0
        res=0
        while r<len(nums):
            if nums[r]==0:
                l=r+1
            res=max(res,r-l+1)
            r+=1
        return res