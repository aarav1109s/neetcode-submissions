class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        boo = [False] * len(nums)
        def dfs(cur):
            if len(cur) == len(nums):
                    res.append(cur.copy())
                    return

            for i in range(len(nums)):
                if boo[i] == True:
                    continue
                boo[i] = True
                cur.append(nums[i])
                dfs(cur)
                cur.pop()
                boo[i] = False

            
        dfs([])

        return res