class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0 # Init the count value

        prefix_sum = 0 # Init the prefix sum array
        hash_sum = {0: 1}
        temp_sum = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in hash_sum:
                count += hash_sum[prefix_sum - k]

            hash_sum[prefix_sum] = hash_sum.get(prefix_sum, 0) + 1

        return count

            