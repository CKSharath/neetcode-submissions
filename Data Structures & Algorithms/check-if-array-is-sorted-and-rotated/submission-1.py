class Solution:
    def check(self, nums: List[int]) -> bool:
        k=0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                k+=1

        if nums[-1] > nums[0]:
            k += 1
        return k<=1