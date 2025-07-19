# Last updated: 7/18/2025, 11:24:26 PM
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        # O(n) time

        curr_alt = 0
        highest_pt = curr_alt

        for val in gain:
            curr_alt += val
            highest_pt = max(curr_alt, highest_pt)
        
        return highest_pt