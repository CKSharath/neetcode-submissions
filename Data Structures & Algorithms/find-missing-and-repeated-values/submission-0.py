class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        v=[0]*(n**2+1)
        v[0]=1
        for i in range(n):
            for j in range(n):
                v[grid[i][j]]+=1
        res=[]
        res.append(v.index(max(v)))
        res.append(v.index(min(v)))
        return res