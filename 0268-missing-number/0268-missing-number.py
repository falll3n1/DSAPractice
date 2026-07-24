class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # use a set add elements to it remove elements preent in the input array ,
        # only one element will remain , pop it into a variable and return it
        # s = set()
        # n = len(nums) + 1 
        # for i in range(n):
            # s.add(i)
        # for num in nums:
            # s.discard(num)
        # ans = s.pop()
        # return ans

        # n = len(nums)
        # win_sum = n * (n+1) //2
        # ar_sum = 0
        # for num in nums :
        #     ar_sum += num
        # return (win_sum - ar_sum)
        
        # return len(nums) * (len(nums)+1) //2 - sum(nums)

        # ans = len(nums)
        # for i , v in enumerate(nums):
        #     ans ^= i ^ v 
        # return ans

        nums.sort()
        hi , lo = len(nums) , 0
        while lo < hi :
            mid = (lo + hi) // 2

            if nums[mid] == mid :
                lo = mid +1
            else :
                hi = mid

        return lo 




        

        