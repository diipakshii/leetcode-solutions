# Last updated: 6/15/2025, 8:52:58 PM
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sorting -> O(nlogn)
        
        n = len(nums)
        
        nums.sort()

        return nums[n/2]

