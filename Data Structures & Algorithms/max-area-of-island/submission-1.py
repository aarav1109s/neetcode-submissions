class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])

        res = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            area = 0

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                r, c = q.popleft()
                area += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 0
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))
        
        return res

        