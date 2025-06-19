# Last updated: 6/18/2025, 9:55:15 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        x_str = str(x)

        left = 0
        right = len(x_str) - 1

        while left < right:
            if x_str[left] == x_str[right]:
                left += 1
                right -= 1
            else:
                return False

        return True