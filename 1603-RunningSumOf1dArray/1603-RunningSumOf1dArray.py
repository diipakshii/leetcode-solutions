# Last updated: 6/13/2025, 11:40:15 AM
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        
        return nums
        