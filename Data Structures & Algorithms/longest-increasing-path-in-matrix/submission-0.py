class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            max_path = 1
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if nr >= 0 and nr < len(matrix) and nc >= 0 and nc < len(matrix[0]) and matrix[nr][nc] > matrix[i][j]:
                    max_path = max(max_path, dfs(nr, nc) + 1)
            
            dp[(i, j)] = max_path
            return max_path
        
        return max(dfs(r, c) for r in range(len(matrix)) for c in range(len(matrix[0])))