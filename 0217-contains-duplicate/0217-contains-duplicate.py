class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # freq = Counter(nums)

        # for num in nums:
        #     if freq[num] > 1:
        #         return True
        # return False

        a=len(nums)
        b=len(set(nums))
        return  a!=b

