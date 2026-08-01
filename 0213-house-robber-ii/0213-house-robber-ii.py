class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def abc(nums):
            pre , cur = 0 , 0
            
            for n in nums:
                pre , cur = cur , max (cur , pre + n )
                
            return cur

        return max (nums[0],abc(nums[:n-1:]), abc(nums[1:]))