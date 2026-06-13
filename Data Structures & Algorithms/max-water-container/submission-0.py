class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        res = 0

        for height in heights:
            res = max(res, min(heights[i], heights[j]) * (j - i))
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                j -= 1

        return res
