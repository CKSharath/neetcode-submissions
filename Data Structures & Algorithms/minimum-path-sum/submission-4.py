class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        dp={}
        def bt(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==r-1 and j==c-1:
                return grid[i][j]
            if i>=r or j>=c:
                return float('inf')
            res= grid[i][j]+min(bt(i+1,j),bt(i,j+1))
            dp[(i,j)]=res
            return dp[(i,j)]
        return bt(0,0)