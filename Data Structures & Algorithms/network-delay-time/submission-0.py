class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, i, t in times:
            adj[u].append((t, i))
        

        seen = set()
        minHeap = [(0, k)]
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in seen:
                continue
            
            seen.add(n1)
            t = max(t, w1)
            for w2, n2 in adj[n1]:
                if n2 not in seen:
                    heapq.heappush(minHeap, (w2 + w1, n2))
        
        return t if len(seen) == n else -1

