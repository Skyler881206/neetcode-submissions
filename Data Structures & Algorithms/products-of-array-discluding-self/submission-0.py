class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result_container = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    result_container[i] *= nums[j]

        return result_container