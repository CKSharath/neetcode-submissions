class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def perm(arr,pick):
            if len(arr)==len(nums):
                res.append(arr[:])
            for i in range(len(nums)):
                if pick[i]==False:
                    pick[i]=True
                    arr.append(nums[i])
                    perm(arr,pick)
                    arr.pop()
                    pick[i]=False
        p=[False]*len(nums)
        perm([],p)
        return res