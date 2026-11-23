class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        val = 0
        hashM = {0 : 1}

        for i in range(len(nums)):
            val += nums[i]
            diff = val - k
            
            res += hashM.get(diff, 0)
            hashM[val] = 1 + hashM.get(val, 0)
        return res