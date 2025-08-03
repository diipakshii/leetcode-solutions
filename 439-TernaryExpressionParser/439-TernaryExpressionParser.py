# Last updated: 8/3/2025, 4:35:46 PM
class Solution(object):
    def confusingNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # dictionary of valid rotated numbers
        flip = {0:0, 1:1, 6:9, 8:8, 9:6}

        flip = {0:0, 1:1, 6:9, 8:8, 9:6}

        original = n
        rotated = 0

        while n > 0:
            digit = n % 10
            if digit not in flip:
                return False
            rotated = rotated * 10 + flip[digit]
            n //= 10

        return rotated != original