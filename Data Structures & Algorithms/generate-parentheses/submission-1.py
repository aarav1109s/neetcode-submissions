class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = []

        def dfs(closedN, openN):
            if closedN == openN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                dfs(closedN, openN + 1)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                dfs(closedN + 1, openN)
                stack.pop()
        
        dfs(0, 0)
        return res