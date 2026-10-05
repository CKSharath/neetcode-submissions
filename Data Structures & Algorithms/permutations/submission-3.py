class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        pick=[False]*n
        res=[]
        def perm(a,pick):
            if len(a)==len(nums):
                res.append(a[:])

            for i in range(len(nums)):
                if pick[i]==False:
                    pick[i]=True
                    a.append(nums[i])
                    perm(a,pick)
                    pick[i]=False
                    a.pop()
        perm([],pick)
        return res