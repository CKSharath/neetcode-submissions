class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        ms=-1
        for r in range(len(nums)):
            k-=(1 if nums[r]==0 else 0)
            while k<0:
                k+=(1 if nums[l]==0 else 0)
                l+=1
            ms=max(ms,r-l+1)
        return ms