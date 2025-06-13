# Last updated: 6/13/2025, 11:40:25 AM
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two pointer 
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum_point = numbers[left] + numbers[right]

            if sum_point == target:
                return [left + 1, right + 1]
            elif sum_point > target:
                right -= 1
            elif sum_point < target:
                left += 1
        
        return []