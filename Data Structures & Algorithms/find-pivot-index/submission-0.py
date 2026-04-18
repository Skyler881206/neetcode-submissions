class Solution:
    def pivotIndex(self, nums: List[int]) -> int:        
        prefix_sum = []
        
        sum_value = 0
        for i in nums: # Make prefix sum array
            sum_value += i
            prefix_sum.append(sum_value)

        for i in range(len(prefix_sum)):
            left_sum = prefix_sum[i] - nums[i]
            if prefix_sum[-1] - prefix_sum[i] == left_sum:
                return i
        return -1