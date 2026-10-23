class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo_table = {}

        for i in range(len(nums)):
            if nums[i] not in memo_table.keys():
                memo_table[target - nums[i]] = i
            else:
                return [memo_table[nums[i]], i]