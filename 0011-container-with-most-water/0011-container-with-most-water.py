class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r , res = 0 , len(height) - 1, 0 

        while l < r :
            area = (r - l ) * min(height[l] , height[r])
            res = max (res , area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res