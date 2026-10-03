class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=[float('inf')]
        r=len(grid)
        c=len(grid[0])
        dp={}
        def dfs(i,j,sm):
            if i>=r or j>=c:
                return
            sm+=grid[i][j]
            if i==r-1 and j==c-1:
                m[0]=min(m[0],sm)
            dfs(i+1,j,sm)
            dfs(i,j+1,sm)
        dfs(0,0,0)
        return m[0]