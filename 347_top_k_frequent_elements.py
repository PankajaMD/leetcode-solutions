class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(set(nums)):
            return list(set(nums))
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # Min-heap based on frequency
        heap = []
        for n in count.keys():
            heapq.heappush(heap, (count[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract the k most frequent elements
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans
