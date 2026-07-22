class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0 

        w_sum = sum(arr[:k])

        if w_sum/k >= threshold:
            ans += 1

        for i in range(k , len(arr)):
            w_sum += arr[i]
            w_sum -= arr[i-k]

            if w_sum/k >= threshold:
                ans += 1

        return ans