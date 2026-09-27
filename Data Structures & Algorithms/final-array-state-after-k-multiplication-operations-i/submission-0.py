class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def findMin(arr):
            mi=0
            m=arr[0]
            for i in range(len(arr)):
                if arr[i]<m:
                    m=arr[i]
                    mi=i
            return mi
        for i in range(k):
            v=findMin(nums)
            nums[v]*=multiplier
        return nums