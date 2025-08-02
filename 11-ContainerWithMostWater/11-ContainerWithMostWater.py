# Last updated: 8/1/2025, 9:48:02 PM
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = 0

        max_count = 0
        zero = 0

        while right < len(nums):
            if nums[right] == 0:
                zero += 1
            
            if zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1

            max_count = max(max_count, right - left)

            right += 1

        return max_count

        