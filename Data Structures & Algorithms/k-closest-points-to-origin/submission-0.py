class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            subset = []
            subset.append(points[i][0] * points[i][0] + points[i][1] * points[i][1])
            subset.append(points[i][0])
            subset.append(points[i][1])
            minHeap.append(subset.copy())
        
        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            smallest = heapq.heappop(minHeap) 
            res.append([smallest[1], smallest[2]])

        return res

