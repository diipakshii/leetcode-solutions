# Last updated: 7/5/2025, 12:06:22 AM
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashmap = set()

        while n != 1:
            curr = n

            str_sum = 0

            while curr > 0:
                digit = curr % 10
                str_sum += digit * digit
                curr //= 10
            
            if str_sum in hashmap:
                return False
            
            hashmap.add(str_sum)

            n = str_sum
        
        return True
