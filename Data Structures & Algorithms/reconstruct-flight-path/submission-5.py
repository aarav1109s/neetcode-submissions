import collections
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. Build the adjacency list and sort destinations in reverse order
        # Reverse sorting allows us to pop from the end of the list in O(1) time
        adj = collections.defaultdict(list)
        
        # Sort tickets backwards so lexically smaller destinations end up at the end
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
            
        res = []
        
        # 2. Post-order DFS (Hierholzer's Algorithm)
        def dfs(airport):
            while adj[airport]:
                next_dest = adj[airport].pop()
                dfs(next_dest)
            # Append to result only when an airport has no more outgoing flights
            res.append(airport)
            
        dfs("JFK")
        
        # 3. Reverse the path because it was built from the destination backwards
        return res[::-1]
