class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set()
        n = len(nums) + 1 

        for i in range(n):
            s.add(i)


        for num in nums:
            s.discard(num)

        ans = s.pop()

        return ans

        