class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.minHeap = []
        # Add initial elements to the heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heappop(self.minHeap)  # Remove the smallest element
            heapq.heappush(self.minHeap, val)  # Add the new value
        
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
