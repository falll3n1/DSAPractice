class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        r = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i , v in enumerate(row):
                r[i] = v + min(r[i], r[i+1])

        return r[0]