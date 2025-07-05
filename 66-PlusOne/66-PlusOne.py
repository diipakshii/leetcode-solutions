# Last updated: 7/5/2025, 3:00:36 AM
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1

        # count number of character in s
        hashmap = {}
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1

        max_length = 0
        odd = 0
        
        # add even counts of letters
        for key in hashmap.keys():
            count = hashmap[key]
            if count % 2 == 0:
                max_length += count
            else: 
                max_length += count - 1 
                odd = 1
        
        return max_length + odd

         
        

        