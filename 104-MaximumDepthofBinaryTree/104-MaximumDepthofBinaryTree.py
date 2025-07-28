# Last updated: 7/28/2025, 12:27:48 AM
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        minimum = 1
        maximum = n 

        while minimum <= maximum:
            mid = minimum + (maximum - minimum) // 2
            num = guess(mid)

            if num == 0:
                return mid
            elif num == -1:
                maximum = mid - 1
            else:
                minimum = mid + 1
            
        