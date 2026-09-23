class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        res=[]
        l=0
        r=n-1
        while l<r:
            ss=numbers[l]+numbers[r]
            if ss==target:
                return [l+1,r+1]
            elif ss>target:
                r-=1
            else:
                l+=1