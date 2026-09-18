class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = 0
        cache = [0] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if cache[i] != 0:
                return cache[i]
            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return cache[i]
        return min(dfs(1), dfs(0))
