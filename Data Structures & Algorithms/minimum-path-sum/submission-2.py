class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        def bt(i,j):
            if i==r-1 and j==c-1:
                return grid[i][j]
            if i>=r or j>=c:
                return float('inf')
            return grid[i][j]+min(bt(i+1,j),bt(i,j+1))
        return bt(0,0)