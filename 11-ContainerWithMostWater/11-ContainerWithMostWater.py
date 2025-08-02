# Last updated: 8/1/2025, 8:54:31 PM
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0

        nums.sort()

        left = 0
        right = len(nums) - 1

        while left < right:
            curr = nums[left] + nums[right] 

            if curr == k:
                left += 1
                right -= 1
                count += 1
            elif curr > k:
                right -= 1
            else:
                left += 1
        
        return count


        