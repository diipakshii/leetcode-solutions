# Last updated: 6/13/2025, 11:40:19 AM
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashset = set(nums)

        result = []

        for i in range(1, len(nums) + 1):
            if i not in hashset:
                result.append(i)
        
        return result

        # O(n)
                