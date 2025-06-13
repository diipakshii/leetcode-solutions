# Last updated: 6/13/2025, 11:40:34 AM
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # two pointer

        maxAmt = 0

        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left

            amt = h * w

            if amt > maxAmt:
                maxAmt = amt
            
            if min(height[left], height[right]) == height[left]:
                left += 1
            else:
                right -= 1
            
        return maxAmt