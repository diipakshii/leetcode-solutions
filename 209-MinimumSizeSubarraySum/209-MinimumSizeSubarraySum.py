# Last updated: 7/14/2025, 10:20:29 PM
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = float('inf')
        wind_sum = 0

        left = 0
        right = 0

        for right in range(len(nums)):
            wind_sum += nums[right]

            while wind_sum >= target:
                min_len = min(min_len, right - left + 1)
                wind_sum -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0
        