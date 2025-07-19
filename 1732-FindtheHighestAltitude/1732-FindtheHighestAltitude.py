# Last updated: 7/18/2025, 11:47:53 PM
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dictionary = {}

        for val in arr:
            if val in dictionary:
                dictionary[val] += 1
            else:
                dictionary[val] = 1
        
        values = set()

        for key, value in dictionary.items():
            if value in values:
                return False
            else:
                values.add(value)
        
        return True