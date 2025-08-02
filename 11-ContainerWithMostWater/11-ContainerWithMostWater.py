# Last updated: 8/1/2025, 9:35:41 PM
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        right = 0

        curr = 0
        max_count = 0

        while right < len(nums):
            if nums[right] == 1:
                curr += 1
                right += 1
            else: 
                if k > 0:
                    k -= 1
                    curr += 1
                    right += 1
                else:
                    if nums[left] == 0:
                        k += 1
                    curr -= 1
                    left += 1
            
            max_count = max(curr, max_count)

        return max_count