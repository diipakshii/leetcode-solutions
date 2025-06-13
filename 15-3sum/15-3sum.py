# Last updated: 6/13/2025, 11:40:33 AM
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        nums.sort()  

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                threesum = a + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    ans.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return ans