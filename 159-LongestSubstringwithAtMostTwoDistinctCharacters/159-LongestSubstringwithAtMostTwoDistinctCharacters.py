# Last updated: 8/3/2025, 12:56:26 AM
class Solution(object):
    def anagramMappings(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dictionary = {}
        
        for i, val in enumerate(nums2):
            dictionary[val] = i

        result = []

        for num in nums1:
            result.append(dictionary[num])

        return result   