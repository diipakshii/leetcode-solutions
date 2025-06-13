# Last updated: 6/13/2025, 11:40:21 AM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        # O(1)

        dict = {}

        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        # O(n) where n = len(s) = len(t)
        
        for char in t:
            if char in dict:
                dict[char] -= 1
                if dict[char] == 0:
                    del dict[char]
            else:
                return False
        # O(n) where n = len(t) = len(s)
        
        return True

        # O(1) + O(n) + O(n) = O(n) time
        