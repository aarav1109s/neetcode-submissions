class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        res = []

        for num in nums:
            count[num] += 1

        val = len(nums) // 3

        for i in count.keys():
            if count[i] > val:
                res.append(i)
        
        return res