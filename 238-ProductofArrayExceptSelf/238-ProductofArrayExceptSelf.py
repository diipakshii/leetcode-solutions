# Last updated: 7/3/2025, 9:01:23 PM
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # calculate products from left to right and then right to left

        n = len(nums)
        products = [1] * n

        for i in range(1, n):
            products[i] = products[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(n-2, -1, -1):
            products[i] *= right
            right *= nums[i]

        return products

        