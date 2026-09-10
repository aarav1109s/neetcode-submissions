class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        valid = set()

        def dfs(r, c):
            if 0 > r or r == rows or 0 > c or c == cols or (r, c) in valid or board[r][c] == "X":
                return

            valid.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in valid and board[r][c] == "O":
                    board[r][c] = "X"
