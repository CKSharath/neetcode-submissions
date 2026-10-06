class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sm=sum(nums)
        l=0
        s=0
        while l<len(nums):
            if s==(sm-s-nums[l]):
                return l
            s+=nums[l]
            l+=1
        return -1