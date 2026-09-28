class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        l=0
        r=len(nums)-1
        v=r
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                res[v]=nums[l]**2
                l+=1
            else:
                res[v]=nums[r]**2
                r-=1
            v-=1
        return res