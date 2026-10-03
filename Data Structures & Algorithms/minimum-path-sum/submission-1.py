class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=[float('inf')]
        r=len(grid)
        c=len(grid[0])
        dp={}
        def dfs(i,j,sm):
            if (i,j) in dp:
                return dp[(i,j)] 
            if i>=r or j>=c:
                return float('inf')

            if i==r-1 and j==c-1:
                return grid[i][j]

            right=dfs(i+1,j,sm)
            down=dfs(i,j+1,sm)
            dp[(i,j)]=grid[i][j]+min(right,down)
            return dp[(i,j)]
        return dfs(0,0,0)
