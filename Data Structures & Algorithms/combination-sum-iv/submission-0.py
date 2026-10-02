class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res=[0]
        def bt(s):
            if s==target:
                res[0]+=1
                return
            if s>target:
                return
            for i in range(len(nums)):
                s+=nums[i]
                bt(s)
                s-=nums[i]
        bt(0)
        return res[0]