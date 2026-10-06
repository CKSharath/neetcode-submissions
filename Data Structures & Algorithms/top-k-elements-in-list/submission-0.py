class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        r=len(nums)-1
        while r>0:
            if len(res)==k:
                break
            while r-1>=0 and nums[r-1]==nums[r]:
                r-=1
            res.append(nums[r])
            r-=1
        return res