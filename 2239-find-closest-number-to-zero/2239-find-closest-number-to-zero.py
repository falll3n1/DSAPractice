class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mini = nums[0]

        for num in nums:
            if abs(num) < abs(mini):
                mini = num
        if mini < 0 and abs(mini) in nums:
            return abs(mini)
        else:
            return mini