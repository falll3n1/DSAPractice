class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 : return n

        cur, pre = 2 , 1

        for _ in range (3 , n + 1):
            pre, cur = cur, pre+ cur

        return cur