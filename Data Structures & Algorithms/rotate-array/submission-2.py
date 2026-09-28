class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        l=0
        r=len(nums)-1
        k=k%(r+1)
        rev(0,r)
        rev(0,k-1)
        rev(k,r)
        