class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        res=0
        r=0
        while r<len(nums):
            while l<=r and nums[l]==0:
                l+=1
            if nums[r]==0:
                l=r
            res=max(res,r-l+1)
            r+=1
        return res