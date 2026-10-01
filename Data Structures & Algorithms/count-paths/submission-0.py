class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n

        grid = [[1] * n for c in range(m)] 

        for c in range(cols):
            grid[rows - 1][c] = 1


        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        
        return grid[m-1][n-1]

