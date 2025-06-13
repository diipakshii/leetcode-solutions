# Last updated: 6/13/2025, 12:09:49 PM
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = rows * columns - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            row = mid // columns
            column = mid % columns

            if target > matrix[row][column]:
                left = mid + 1
            elif target < matrix[row][column]:
                right = mid - 1
            else:
                return True
        
        return False

        # O(log(m * n))
        