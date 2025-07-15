# Last updated: 7/14/2025, 8:22:56 PM
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])

        return False
            


            
        