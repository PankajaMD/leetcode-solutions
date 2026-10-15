class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        for point in points:
            dist = -(point[0] * point[0] + point[1] * point[1])
            heapq.heappush(max_heap, (dist, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        result = [point for (dist, point) in max_heap]

        return result
