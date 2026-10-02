class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        v=[0]*len(heights)
        mv=heights[-1]
        for i in range(len(heights)-1,-1,-1):
            mv=max(mv,heights[i])
            v[i-1]=mv
        res=[]
        for j in range(len(heights)-1):
            if heights[j]>v[j]:
                res.append(j)
        res.append(len(heights)-1)
        return res