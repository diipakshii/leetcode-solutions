# Last updated: 7/4/2025, 8:50:34 PM
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # converts binary strings to int to calculate sum
        sum = int(a, 2) + int(b, 2)

        # converts sum back to binary and removes 0b from beginning
        return bin(sum)[2:]