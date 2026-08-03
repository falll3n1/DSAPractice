import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            heavy = heapq.heappop(heap)
            light = heapq.heappop(heap)

            if heavy != light :
                heapq.heappush(heap, heavy - light)

        return -heap[0] if heap else 0