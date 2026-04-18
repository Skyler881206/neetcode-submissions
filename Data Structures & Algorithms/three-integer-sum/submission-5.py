class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # Avoid count again

            target = -nums[i]
            seen = {}
            
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
                if complement in seen:
                    result.append([nums[i], complement, nums[j]])
                    while (j + 1 < len(nums)) and (nums[j] == nums[j + 1]):
                        j += 1
                seen[nums[j]] = nums[j]

        return [x for x in set(tuple(y) for y in result)]