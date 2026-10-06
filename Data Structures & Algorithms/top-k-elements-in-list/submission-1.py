class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        arr=[]
        for i,c in d.items():
            arr.append([i,c])
        arr.sort(key=lambda i:i[1])
        while k:
            res.append(arr[-1][0])
            arr.pop()
            k-=1
        return res
