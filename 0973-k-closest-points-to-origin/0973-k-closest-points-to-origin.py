import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x , y  in points:
            dis = x * x + y * y
            heapq.heappush(heap, (-dis, [x, y]))
            while len(heap) > k :
                heapq.heappop(heap)
        res = []
        while k > 0 :
            dis , x = heapq.heappop(heap)
            res.append(x)
            k -= 1

        return res

        
        

