class NumArray:

    def __init__(self, nums: List[int]):
        self.num_array = nums

        self.sum_array = [0] * len(nums) # Build sum array space
        for i in range(len(nums)):
            self.sum_array[i] = self.num_array[i] + self.sum_array[i - 1]
        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.sum_array[right] - self.sum_array[left - 1]
        return self.sum_array[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)