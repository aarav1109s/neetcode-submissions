class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parentMap = {i : [] for i in range(n)}

        for par, chi in edges:
            parentMap[par].append(chi)
            parentMap[chi].append(par)
        
        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False
            if i == prev:
                return
            
            visit.add(i)

            for child in parentMap[i]:
                if child == prev:
                    continue
                if not dfs(child, i):
                    return False

            return True
        
        return dfs(0, None) and len(visit) == n