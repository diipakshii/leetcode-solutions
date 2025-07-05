# Last updated: 7/5/2025, 12:23:03 AM
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # recursion
        if not digits:
            return [1]
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]