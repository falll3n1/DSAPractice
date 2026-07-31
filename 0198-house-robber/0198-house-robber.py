class Solution:
    def rob(self, nums: List[int]) -> int:
        pre , cur = 0 , 0 

        for num in nums:
            pre , cur = cur , max(cur ,pre + num)
        return cur


# prev, curr = 0, 0: curr is the best up to the previous house (dp[i-1]), prev is the best up to two houses back (dp[i-2]). Both start at 0 since with no houses considered, the max is 0. This framing lets the first iteration work without special-casing.
# for num in nums:: Walks each house's value. We don't need the index, only the value and the two rolling maxima.
# prev, curr = curr, max(curr, prev + num): The core step. New curr is the better of skipping this house (old curr) or robbing it (prev + num). Then prev slides up to the old curr. Both happen simultaneously via tuple assignment, so no temp needed.
# return curr: After all houses, curr holds the overall max.