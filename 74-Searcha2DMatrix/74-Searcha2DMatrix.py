# Last updated: 6/13/2025, 12:04:30 PM
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        num_rows = len(matrix)
        num_columns = len(matrix[0])

        row = 0
        column = num_columns - 1

        while row < len(matrix) and column >= 0:
            if matrix[row][column] > target:
                column -= 1
            elif matrix[row][column] < target:
                row += 1
            else:
                return True
        
        return False

        # O(m + n)
        