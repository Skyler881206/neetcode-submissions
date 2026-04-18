class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = [] # Init the 2D prefix sum
        
        for i in matrix:
            inner_prefix_sum = [] # Init the 1D prefix sum
            sum_value = 0 # Init Left side value
            for j in range(len(i)):
                sum_value += i[j]
                inner_prefix_sum.append(sum_value) # Calculate the prefix sum
            self.prefix_sum.append(inner_prefix_sum) # Save to 2D prefix sum array

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        target_sum = 0
        for i in range(row1, row2 + 1):
            right_side = self.prefix_sum[i][col2]
            left_side = self.prefix_sum[i][col1 - 1] if col1 > 0 else 0

            target_sum += right_side - left_side
        return target_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)