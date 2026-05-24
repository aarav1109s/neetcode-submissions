class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = float('-inf')
        maxSum = float('-inf')
        for i in range(len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(currSum, maxSum)
        
        return maxSum

