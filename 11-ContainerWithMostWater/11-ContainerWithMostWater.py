# Last updated: 9/12/2025, 8:21:59 PM
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1

        maximum = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            water = h * w
            
            maximum = max(maximum, water)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return maximum






        