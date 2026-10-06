class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n=len(nums)
        for r in range(n+1):
            g=0
            for i in nums:
                if i>=r:
                    g+=1
            if g==r:
                return r
        return -1