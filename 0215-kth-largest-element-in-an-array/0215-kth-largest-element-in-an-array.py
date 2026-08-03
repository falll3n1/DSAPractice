import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = [-i for i in nums]
        # heapq.heapify(heap)
        # while k != 0 :
        #     res = heapq.heappop(heap)
        #     k -= 1
        # return -res
        
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]