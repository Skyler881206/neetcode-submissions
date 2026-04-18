class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sub_array_sum = 0
        count = 0
        L = 0

        for R in range(len(arr)):
            if (R - L + 1) > k: # Over the window size
                sub_array_sum -= arr[L]
                L += 1

            sub_array_sum += arr[R]
            if ((sub_array_sum / k) >= threshold) and ((R - L + 1) == k):
                count += 1
        return count