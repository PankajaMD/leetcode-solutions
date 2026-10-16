class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freqMap = Counter(tasks)

        # Step 2: Build a max heap based on the frequency
        # heapq is a min-heap, so store negated values
        maxHeap = [-freq for freq in freqMap.values()]
        heapq.heapify(maxHeap)

        # Step 3: Process tasks
        time = 0
        while maxHeap:
            temp = []
            for i in range(n + 1):
                if maxHeap:
                    temp.append(-heapq.heappop(maxHeap))

            for freq in temp:
                freq -= 1
                if freq > 0:
                    heapq.heappush(maxHeap, -freq)

            # Step 4: Update time
            time += len(temp) if not maxHeap else n + 1

        return time
