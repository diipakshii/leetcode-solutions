# Last updated: 6/13/2025, 11:40:22 AM
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = set()

        for num in nums:
            if num not in hash:
                hash.add(num)
            else:
                return True
        
        return False

        # O(n) time