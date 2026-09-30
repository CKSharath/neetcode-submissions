class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[0]
        def bt(a,i):
            if i==len(nums):
                res[0]=max(res[0],len(a))
                return
            
            #pick
            if not a or a[-1]<nums[i]:
                a.append(nums[i])
                bt(a,i+1)
                a.pop()
            bt(a,i+1)
        bt([],0)
        return res[0]