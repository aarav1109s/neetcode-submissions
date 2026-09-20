class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cur = 0
        prev = 0

        for i in range(len(nums) - 1):
            new_max = max(cur, prev + nums[i])

            prev = cur
            cur = new_max
        cur2, prev2 = 0, 0
        for i in range(1, len(nums)):
            new_max = max(cur2, prev2 + nums[i])

            prev2 = cur2
            cur2 = new_max
        return max(cur2, cur)