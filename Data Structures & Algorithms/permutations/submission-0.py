class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bt(perm,nums,pick):
            if len(perm)==len(nums):
                res.append(perm[:])
            for i in range(len(nums)):
                if pick[i]==False:
                    perm.append(nums[i])
                    pick[i]=True
                    bt(perm,nums,pick)
                    pick[i]=False
                    perm.pop()
        bt([],nums,[False]*len(nums))
        return res
