# Last updated: 6/18/2025, 10:37:56 PM
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash = {}

        for char in magazine:
            if char not in hash:
                hash[char] = 1
            else:
                hash[char] += 1
        
        for c in ransomNote:
            if c in hash:
                hash[c] -= 1

                if hash[c] == 0:
                    del hash[c]
            else:
                return False
        
        return True
        