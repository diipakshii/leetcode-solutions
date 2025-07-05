# Last updated: 7/5/2025, 3:05:11 AM
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = set()
        length = 0

        for char in s:
            if char in hashmap:
                hashmap.remove(char)
                length += 2
            else:
                hashmap.add(char)

        if len(hashmap) > 0:
            length += 1

        return length

         
        

        