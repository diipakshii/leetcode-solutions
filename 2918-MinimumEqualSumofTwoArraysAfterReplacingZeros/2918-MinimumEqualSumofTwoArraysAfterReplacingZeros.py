# Last updated: 7/7/2025, 10:46:51 PM
class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        sum1 = 0
        sum2 = 0

        count1 = 0
        count2 = 0

        for num in nums1:
            sum1 += num
            
            if num == 0:
                count1 += 1
                sum1 += 1
        
        for num in nums2:
            sum2 += num

            if num == 0:
                count2 += 1
                sum2 += 1
        
        if (count1 == 0 and sum2 > sum1) or (count2 == 0 and sum1 > sum2):
            return -1
        
        return max(sum1, sum2)