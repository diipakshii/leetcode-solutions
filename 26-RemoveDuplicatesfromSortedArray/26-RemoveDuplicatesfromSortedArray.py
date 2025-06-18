# Last updated: 6/17/2025, 10:13:48 PM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointer -> O(n)
        
        i = 0
        j = 1

        while i < j and j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i + 1
        