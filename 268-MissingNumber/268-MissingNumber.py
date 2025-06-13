# Last updated: 6/13/2025, 11:40:20 AM
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return sum(range(len(nums)+1)) - sum(nums)

        # O(n) solution