class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        res , sol = [],[]

        def back():
            if len(sol) == n :
                res.append(sol[:])
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    back()
                    sol.pop()

        back()

        return res

        # Time = n!
        # space = n