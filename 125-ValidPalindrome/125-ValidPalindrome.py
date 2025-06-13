# Last updated: 6/13/2025, 11:40:29 AM
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # lowercase all characters in str and get rid of anything that is not alphabetical
        string = ''.join(c.lower() for c in s if c.isalnum())

        l = 0
        r = len(string) - 1

        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        
        return True