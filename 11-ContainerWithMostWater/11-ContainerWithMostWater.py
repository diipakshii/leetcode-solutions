# Last updated: 8/1/2025, 9:35:56 PM
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        right = 0

        max_count = 0

        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            
            while k < 0:
                if nums[left] == 0:
                    k += 1
                
                left += 1
            
            curr = right - left + 1
            max_count = max(max_count, curr)
            
            right += 1
        
        return max_count

                
        