# Last updated: 8/3/2025, 5:11:21 PM
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # O(n) time
        
        elements = {}
        count = 0

        for num in arr:
            if num not in elements:
                elements[num] = 1
            else:
                elements[num] += 1
        
        for element in elements:
            x = element + 1
            if x in elements:
                count += elements[element]
        
        return count
        