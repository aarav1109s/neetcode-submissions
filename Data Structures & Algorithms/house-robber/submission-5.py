class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        

        rob_prev = 0
        rob_cur = 0

        for num in nums:
            new_max = max(rob_cur, rob_prev + num)

            rob_prev = rob_cur
            rob_cur = new_max
        
        return rob_cur