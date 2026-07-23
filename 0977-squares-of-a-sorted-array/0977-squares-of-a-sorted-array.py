class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l , r = 0 , len(nums) - 1
        res = [0] * len(nums)
        last = len(nums) - 1
        while l <= r :
            if pow(nums[r],2) > pow(nums[l],2) :
                res[last] = nums[r]**2
                r -= 1
                last -=1
            else:
                res[last] = nums[l]**2
                l += 1
                last -= 1
        return res