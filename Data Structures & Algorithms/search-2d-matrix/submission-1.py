class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_L = 0
        row_R = len(matrix) - 1

        while row_L <= row_R:
            mid = (row_R + row_L) // 2

            if matrix[mid][0] > target:
                row_R = mid - 1

            if matrix[mid][0] < target:
                row_L = mid + 1

            if matrix[mid][0] == target:
                return True

        L = 0
        R = len(matrix[0]) - 1
        while L <= R:
            mid = (L + R) // 2

            if matrix[row_R][mid] > target:
                R = mid - 1
            
            if matrix[row_R][mid] < target:
                L = mid + 1
            
            if matrix[row_R][mid] == target:
                return True
        return False