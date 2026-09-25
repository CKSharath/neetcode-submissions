class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        p=[False]*len(nums)
        def bt(ans,pick):
            if len(ans)==len(nums):
                res.append(ans[:])
                return
            for i in range(len(nums)):
                if pick[i]==False:
                    ans.append(nums[i])
                    pick[i]=True
                    bt(ans,pick)
                    pick[i]=False
                    ans.pop()
        bt([],p)
        return res