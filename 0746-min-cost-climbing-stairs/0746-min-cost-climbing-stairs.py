class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        pre , cur = 0 , 0 

        for i in range(2 , n + 1):
            pre , cur = cur , min(cur + cost[i - 1 ] , pre + cost[i - 2])

        return cur