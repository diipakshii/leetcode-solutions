# Last updated: 6/18/2025, 10:10:43 PM
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # binary search -> O(logn)
        
        left = 0
        right = x

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == x:
                return mid
            if square < x:
                left = mid + 1
            if square > x:
                right = mid - 1
        
        return right
        