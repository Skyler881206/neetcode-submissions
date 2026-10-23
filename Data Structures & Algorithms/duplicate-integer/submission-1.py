class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy_board = {}

        for num in nums:
            if num not in copy_board.keys():
                copy_board[num] = 1
            else:
                return True
        return False