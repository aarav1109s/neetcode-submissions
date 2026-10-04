class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, cur):
            if i == len(nums) and cur == target:
                return 1
            if i >= len(nums):
                return 0
            if (i, cur) in dp:
                return dp[i, cur]


            neg = dfs(i + 1, cur - nums[i])
            pos = dfs(i + 1, cur + nums[i])

            dp[(i, cur)] = neg + pos
            return dp[(i, cur)]
        
        return dfs(0, 0)
        
