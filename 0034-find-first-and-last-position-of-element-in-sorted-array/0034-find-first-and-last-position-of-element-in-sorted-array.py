class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(left):
            l , r = 0 , len(nums) -1 
            bound = -1
            while l <= r :
                m = (l+r)//2
                if nums[m] == target:
                    bound = m 
                    if left: r = m - 1
                    else: l = m + 1
                elif (nums[m] < target):l = m + 1
                else:r = m - 1
            return bound
        return [find(True), find(False)]


