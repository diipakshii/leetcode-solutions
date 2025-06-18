# Last updated: 6/17/2025, 9:45:12 PM
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0

        for i in range(len(nums)):
            if nums[i] != val:
                counter += 1
                nums[counter - 1] = nums[i]
        
        return counter