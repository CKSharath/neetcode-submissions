class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        p=[False]*len(nums)
        def bt(s,ts):
            if s==ts:
                return True
            
            for i in range(len(nums)):
                if p[i]==False:
                    p[i]=True
                    s+=nums[i]
                    ts-=nums[i]
                    if bt(s,ts):
                        return True
                    s-=nums[i]
                    ts+=nums[i]
                    p[i]=False
            return False
        return bt(0,sum(nums))