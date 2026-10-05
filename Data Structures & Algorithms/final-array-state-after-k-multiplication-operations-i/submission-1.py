class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def findmin(a):
            mi=0
            m=a[0]
            for i in range(len(a)):
                if a[i]<m:
                    m=a[i]
                    mi=i
            return mi
        for _ in range(k):
            i=findmin(nums)
            nums[i]*=multiplier
        return nums