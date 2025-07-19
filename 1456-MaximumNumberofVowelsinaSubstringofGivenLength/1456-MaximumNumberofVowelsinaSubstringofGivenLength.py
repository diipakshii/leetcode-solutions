# Last updated: 7/19/2025, 12:26:32 AM
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = {'a', 'e', 'i', 'o', 'u'}

        maxVowels = 0
        curr = 0

        left = 0
        right = 0

        while right < k:
            if s[right] in vowels:
                curr += 1
            right += 1
        
        maxVowels = curr
        
        while right < len(s):
            if s[left] in vowels:
                curr -= 1
            if s[right] in vowels:
                curr += 1
            
            maxVowels = max(maxVowels, curr)
            if maxVowels == k:
                return maxVowels
                break
            
                        
            left += 1
            right += 1
        
        return maxVowels

