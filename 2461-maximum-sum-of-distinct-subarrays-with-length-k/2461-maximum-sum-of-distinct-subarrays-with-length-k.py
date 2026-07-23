class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # if not k == 0 or len(nums) == 0 : return 0

        res = 0 
        count = defaultdict(int)

        cur = 0
        l = 0

        for r in range(len(nums)):
            count[nums[r]] += 1
            cur += nums[r]

            if r - l + 1 > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])
                cur -= nums[l]
                l += 1

            if len(count) == r - l + 1 == k:
                res = max(res , cur)

        return res 