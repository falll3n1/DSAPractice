class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == 0 or k == 0 : return 0

        if k == 1 : return max(nums)

        window_sum = sum(nums[:k])

        max_sum = window_sum
         
        for i in range(k , n):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum , window_sum)

        return max_sum/k
        