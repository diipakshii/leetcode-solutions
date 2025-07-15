# Last updated: 7/14/2025, 8:46:29 PM
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        nums.sort()

        max_len = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    curr += 1
                else: 
                    max_len = max(max_len, curr)
                    curr = 1
        
        return max(max_len, curr)
            
        