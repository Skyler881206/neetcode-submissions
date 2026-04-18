class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result_container = [1] * len(nums)
        
        left_product = [1]
        right_product = [1]
        for i in range(len(nums)):
            left_product.append(left_product[i] * nums[i])
            right_product.append(right_product[i] * nums[len(nums) - 1 - i])
        
        for i in range(len(nums)):
            result_container[i] = left_product[i] * right_product[len(nums) - 1 - i]
        return result_container