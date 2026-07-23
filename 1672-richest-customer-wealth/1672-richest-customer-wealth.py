class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0

        for m in range(len(accounts)):
            total = 0
            for n in range(len(accounts[0])):
                total += accounts[m][n]
            maxi = max(maxi , total)


        return maxi