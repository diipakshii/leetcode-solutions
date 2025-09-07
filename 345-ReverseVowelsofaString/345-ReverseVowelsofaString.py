# Last updated: 9/7/2025, 2:28:10 AM
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # two pointer 

        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        left = 0
        right = len(s) - 1

        # turn string to list
        s = list(s)

        while left < right: 
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                # swap
                s[left], s[right] = s[right], s[left]
                left += 1
                right -=1
        
        return "".join(s)
            


        