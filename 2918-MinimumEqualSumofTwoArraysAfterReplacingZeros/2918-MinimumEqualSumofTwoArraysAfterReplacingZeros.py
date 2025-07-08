# Last updated: 7/7/2025, 10:49:44 PM
class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # using count 
        
        sum1 = 0
        sum2 = 0

        count1 = nums1.count(0)
        count2 = nums2.count(0)

        for num in nums1:
            sum1 += num 

        sum1 += count1
        
        for num in nums2:
            sum2 += num

        sum2 += count2
        
        if (count1 == 0 and sum2 > sum1) or (count2 == 0 and sum1 > sum2):
            return -1
        
        return max(sum1, sum2)