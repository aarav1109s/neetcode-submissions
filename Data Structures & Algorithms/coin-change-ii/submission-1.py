class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, total):
            if i >= len(coins):
                return 0
            if (i, total) in dp:
                return dp[(i, total)]
            if amount == total:
                return 1
            if amount < total:
                return 0
            
            stay = dfs(i, total + coins[i])
            move = dfs(i + 1, total)

            dp[(i, total)] = move + stay

            return dp[(i, total)]
        
        return dfs(0, 0)