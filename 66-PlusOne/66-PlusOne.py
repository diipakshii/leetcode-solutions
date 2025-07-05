# Last updated: 7/5/2025, 12:19:37 AM
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        int_sum = 0

        for digit in digits:
            val = (10 ** n) * digit
            int_sum += val
            n -= 1
        
        int_sum += 1

        string = str(int_sum)

        digit_list = [int(dig) for dig in str(int_sum)]

        return digit_list
        