# Last updated: 6/13/2025, 11:40:18 AM
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)

        dictionary = {}

        for index, value in enumerate(sorted_nums):
            if value not in dictionary:
                dictionary[value] = index
        
        result = []

        for i in nums:
            result.append(dictionary[i])
        
        return result




        
        