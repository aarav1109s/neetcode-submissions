class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = 0
        count = 0
        for num in nums:
            if maj != num:
                if count == 0:
                    count = 1
                    maj = num
                else:
                    count -= 1
            else:
                count += 1
        return maj