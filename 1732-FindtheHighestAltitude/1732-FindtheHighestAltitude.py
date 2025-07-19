# Last updated: 7/18/2025, 11:39:01 PM
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        hash1 = set(nums1)
        hash2 = set(nums2)

        l = set()
        m = set()

        for i in nums1:
            if i not in hash2:
                l.add(i)
        
        for i in nums2:
            if i not in hash1:
                m.add(i)
        
        return [list(l), list(m)]
        